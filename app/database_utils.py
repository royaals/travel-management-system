from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from . import models
from .database import engine, Base, SessionLocal

def clear_database(db: Session = None):
    """
    Clear all data from the database but keep the tables intact.
    
    Args:
        db: SQLAlchemy session. If not provided, a new one will be created.
        
    Returns:
        bool: True if successful, False otherwise
    """
    close_db = False
    if db is None:
        db = SessionLocal()
        close_db = True
    
    try:
        print("Clearing database...")
        
        
        try:
            
            db.execute(text("SET CONSTRAINTS ALL DEFERRED"))
        except Exception as e:
            print(f"Note: Could not defer constraints (might be SQLite): {e}")
        
        
        print("Clearing itinerary transfers...")
        db.query(models.ItineraryTransfer).delete()
        
        print("Clearing excursions...")
        db.query(models.Excursion).delete()
        
        print("Clearing accommodations...")
        db.query(models.Accommodation).delete()
        
        print("Clearing itineraries...")
        db.query(models.Itinerary).delete()
        
        print("Clearing transfers...")
        db.query(models.Transfer).delete()
        
        print("Clearing activities...")
        db.query(models.Activity).delete()
        
        print("Clearing hotels...")
        db.query(models.Hotel).delete()
        
        print("Clearing locations...")
        db.query(models.Location).delete()
        
        
        db.commit()
        print("Database cleared successfully!")
        return True
    
    except Exception as e:
        db.rollback()
        print(f"Error clearing database: {str(e)}")
        return False
    
    finally:
        if close_db:
            db.close()