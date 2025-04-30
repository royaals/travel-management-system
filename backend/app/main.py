from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from . import crud, models, schemas
from .database import engine, get_db, Base
from .mcp.server import mcp_server
from .seed import seed_database


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Travel Itinerary Management System",
    description="API for managing travel itineraries in Thailand's Phuket and Krabi regions",
    version="1.0.0"
)

@app.on_event("startup")
def startup_event():
    db = next(get_db())
    
    if db.query(models.Location).count() == 0:
        seed_database(db)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Travel Itinerary Management System API"}


@app.post("/itineraries/", response_model=schemas.Itinerary, tags=["Itineraries"])
def create_itinerary(itinerary: schemas.ItineraryCreate, db: Session = Depends(get_db)):
    """
    Create a new itinerary with accommodations, excursions, and transfers.
    """
    return crud.create_itinerary(db=db, itinerary=itinerary)

@app.get("/itineraries/", response_model=List[schemas.Itinerary], tags=["Itineraries"])
def read_itineraries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve all itineraries.
    """
    itineraries = crud.get_itineraries(db, skip=skip, limit=limit)
    return itineraries

@app.get("/itineraries/{itinerary_id}", response_model=schemas.ItineraryDetail, tags=["Itineraries"])
def read_itinerary(itinerary_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific itinerary by ID with detailed information.
    """
    try:
        itinerary = crud.get_itinerary(db, itinerary_id=itinerary_id)
        if itinerary is None:
            raise HTTPException(status_code=404, detail="Itinerary not found")
        
        
        valid_excursions = [exc for exc in itinerary.excursions if exc.activity is not None]
        valid_accommodations = [acc for acc in itinerary.accommodations if acc.hotel is not None]
        valid_transfers = [trans for trans in itinerary.transfers if trans.transfer is not None]
        
        
        itinerary.excursions = valid_excursions
        itinerary.accommodations = valid_accommodations
        itinerary.transfers = valid_transfers
        
        return itinerary
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while retrieving the itinerary: {str(e)}"
        )


@app.get("/recommended-itineraries/", response_model=List[schemas.Itinerary], tags=["Recommendations"])
def get_recommended_itineraries(duration_nights: int = Query(..., description="Number of nights for the trip")):
    """
    Get recommended itineraries for a specific duration in nights.
    """
    itineraries = mcp_server.get_recommended_itineraries(duration_nights)
    if not itineraries:
        raise HTTPException(status_code=404, detail=f"No recommended itineraries found for {duration_nights} nights")
    return itineraries


@app.get("/hotels/", response_model=List[schemas.Hotel], tags=["Reference Data"])
def read_hotels(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve all hotels.
    """
    return crud.get_hotels(db, skip=skip, limit=limit)

@app.get("/activities/", response_model=List[schemas.Activity], tags=["Reference Data"])
def read_activities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve all activities.
    """
    return crud.get_activities(db, skip=skip, limit=limit)

@app.get("/transfers/", response_model=List[schemas.Transfer], tags=["Reference Data"])
def read_transfers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve all transfers.
    """
    return crud.get_transfers(db, skip=skip, limit=limit)

@app.get("/locations/", response_model=List[schemas.Location], tags=["Reference Data"])
def read_locations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve all locations.
    """
    return crud.get_locations(db, skip=skip, limit=limit)