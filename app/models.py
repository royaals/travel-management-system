from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Time, Text, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    region = Column(String, index=True)  
    description = Column(Text)
    
    hotels = relationship("Hotel", back_populates="location")
    activities = relationship("Activity", back_populates="location")

class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    price_per_night = Column(Float)
    star_rating = Column(Integer)
    location_id = Column(Integer, ForeignKey("locations.id"))
    
    location = relationship("Location", back_populates="hotels")
    accommodations = relationship("Accommodation", back_populates="hotel")

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    duration_hours = Column(Float)
    price = Column(Float)
    location_id = Column(Integer, ForeignKey("locations.id"))
    
    location = relationship("Location", back_populates="activities")
    excursions = relationship("Excursion", back_populates="activity")

class Transfer(Base):
    __tablename__ = "transfers"
    
    id = Column(Integer, primary_key=True, index=True)
    from_location_id = Column(Integer, ForeignKey("locations.id"))
    to_location_id = Column(Integer, ForeignKey("locations.id"))
    mode = Column(String)  
    duration_hours = Column(Float)
    price = Column(Float)
    
    from_location = relationship("Location", foreign_keys=[from_location_id])
    to_location = relationship("Location", foreign_keys=[to_location_id])
    itinerary_transfers = relationship("ItineraryTransfer", back_populates="transfer")

class Itinerary(Base):
    __tablename__ = "itineraries"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    duration_nights = Column(Integer, index=True)
    is_recommended = Column(Boolean, default=False)
    total_price = Column(Float)
    
    accommodations = relationship("Accommodation", back_populates="itinerary")
    excursions = relationship("Excursion", back_populates="itinerary")
    transfers = relationship("ItineraryTransfer", back_populates="itinerary")

class Accommodation(Base):
    __tablename__ = "accommodations"
    
    id = Column(Integer, primary_key=True, index=True)
    itinerary_id = Column(Integer, ForeignKey("itineraries.id"))
    hotel_id = Column(Integer, ForeignKey("hotels.id"))
    day = Column(Integer)  
    
    itinerary = relationship("Itinerary", back_populates="accommodations")
    hotel = relationship("Hotel", back_populates="accommodations")

class Excursion(Base):
    __tablename__ = "excursions"
    
    id = Column(Integer, primary_key=True, index=True)
    itinerary_id = Column(Integer, ForeignKey("itineraries.id"))
    activity_id = Column(Integer, ForeignKey("activities.id"))
    day = Column(Integer)
    start_time = Column(Time)
    
    itinerary = relationship("Itinerary", back_populates="excursions")
    activity = relationship("Activity", back_populates="excursions")

class ItineraryTransfer(Base):
    __tablename__ = "itinerary_transfers"
    
    id = Column(Integer, primary_key=True, index=True)
    itinerary_id = Column(Integer, ForeignKey("itineraries.id"))
    transfer_id = Column(Integer, ForeignKey("transfers.id"))
    day = Column(Integer)
    time = Column(Time)
    
    itinerary = relationship("Itinerary", back_populates="transfers")
    transfer = relationship("Transfer", back_populates="itinerary_transfers")