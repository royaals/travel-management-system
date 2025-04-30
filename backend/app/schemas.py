from typing import List, Optional
from datetime import time
from pydantic import BaseModel


class LocationBase(BaseModel):
    name: str
    region: str
    description: str

class LocationCreate(LocationBase):
    pass

class Location(LocationBase):
    id: int
    
    class Config:
        orm_mode = True


class HotelBase(BaseModel):
    name: str
    description: str
    price_per_night: float
    star_rating: int
    location_id: int

class HotelCreate(HotelBase):
    pass

class Hotel(HotelBase):
    id: int
    
    class Config:
        orm_mode = True


class ActivityBase(BaseModel):
    name: str
    description: str
    duration_hours: float
    price: float
    location_id: int

class ActivityCreate(ActivityBase):
    pass

class Activity(ActivityBase):
    id: int
    
    class Config:
        orm_mode = True


class TransferBase(BaseModel):
    from_location_id: int
    to_location_id: int
    mode: str
    duration_hours: float
    price: float

class TransferCreate(TransferBase):
    pass

class Transfer(TransferBase):
    id: int
    
    class Config:
        orm_mode = True


class AccommodationBase(BaseModel):
    hotel_id: int
    day: int

class AccommodationCreate(AccommodationBase):
    pass

class Accommodation(AccommodationBase):
    id: int
    
    class Config:
        orm_mode = True


class ExcursionBase(BaseModel):
    activity_id: int
    day: int
    start_time: time

class ExcursionCreate(ExcursionBase):
    pass

class Excursion(ExcursionBase):
    id: int
    
    class Config:
        orm_mode = True




class ItineraryTransferBase(BaseModel):
    transfer_id: int
    day: int
    time: time

class ItineraryTransferCreate(ItineraryTransferBase):
    pass

class ItineraryTransfer(ItineraryTransferBase):
    id: int
    
    class Config:
        orm_mode = True


class ItineraryBase(BaseModel):
    name: str
    description: str
    duration_nights: int
    is_recommended: bool = False
    total_price: float

class ItineraryCreate(ItineraryBase):
    accommodations: List[AccommodationCreate]
    excursions: List[ExcursionCreate]
    transfers: List[ItineraryTransferCreate]

class Itinerary(ItineraryBase):
    id: int
    accommodations: List[Accommodation] = []
    excursions: List[Excursion] = []
    transfers: List[ItineraryTransfer] = []
    
    class Config:
        orm_mode = True


class AccommodationDetail(Accommodation):
    hotel: Hotel

class ExcursionDetail(Excursion):
    activity: Optional[Activity] = None 

class ItineraryTransferDetail(ItineraryTransfer):
    transfer: Transfer

class ItineraryDetail(Itinerary):
    accommodations: List[AccommodationDetail] = []
    excursions: List[ExcursionDetail] = []
    transfers: List[ItineraryTransferDetail] = []