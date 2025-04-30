from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas
from typing import List, Optional

def get_itinerary(db: Session, itinerary_id: int):
    itinerary = db.query(models.Itinerary).filter(models.Itinerary.id == itinerary_id).first()
    if itinerary:
        
        itinerary.excursions = [
            exc for exc in itinerary.excursions 
            if exc.activity is not None
        ]
        itinerary.accommodations = [
            acc for acc in itinerary.accommodations 
            if acc.hotel is not None
        ]
        itinerary.transfers = [
            trans for trans in itinerary.transfers 
            if trans.transfer is not None
        ]
    return itinerary

def get_itineraries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Itinerary).offset(skip).limit(limit).all()

def get_recommended_itineraries(db: Session, duration_nights: int):
    return db.query(models.Itinerary).filter(
        models.Itinerary.duration_nights == duration_nights,
        models.Itinerary.is_recommended == True
    ).all()

def create_itinerary(db: Session, itinerary: schemas.ItineraryCreate):
    db_itinerary = models.Itinerary(
        name=itinerary.name,
        description=itinerary.description,
        duration_nights=itinerary.duration_nights,
        is_recommended=itinerary.is_recommended,
        total_price=itinerary.total_price
    )
    db.add(db_itinerary)
    db.commit()
    db.refresh(db_itinerary)
    
   
    for accommodation in itinerary.accommodations:
        db_accommodation = models.Accommodation(
            itinerary_id=db_itinerary.id,
            hotel_id=accommodation.hotel_id,
            day=accommodation.day
        )
        db.add(db_accommodation)
    
    
    for excursion in itinerary.excursions:
        db_excursion = models.Excursion(
            itinerary_id=db_itinerary.id,
            activity_id=excursion.activity_id,
            day=excursion.day,
            start_time=excursion.start_time
        )
        db.add(db_excursion)
    
   
    for transfer in itinerary.transfers:
        db_transfer = models.ItineraryTransfer(
            itinerary_id=db_itinerary.id,
            transfer_id=transfer.transfer_id,
            day=transfer.day,
            time=transfer.time
        )
        db.add(db_transfer)
    
    db.commit()
    db.refresh(db_itinerary)
    return db_itinerary


def get_hotels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Hotel).offset(skip).limit(limit).all()


def get_activities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Activity).offset(skip).limit(limit).all()


def get_transfers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Transfer).offset(skip).limit(limit).all()


def get_locations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Location).offset(skip).limit(limit).all()

