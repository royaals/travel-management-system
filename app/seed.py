from sqlalchemy.orm import Session
from . import models
from datetime import time
import random


def seed_database(db: Session):
    print("Starting database seeding process...")

    try:
        # Clear existing data first to avoid conflicts
        print("Clearing existing data...")
        db.execute("SET CONSTRAINTS ALL DEFERRED")
        db.query(models.ItineraryTransfer).delete()
        db.query(models.Excursion).delete()
        db.query(models.Accommodation).delete()
        db.query(models.Itinerary).delete()
        db.query(models.Transfer).delete()
        db.query(models.Activity).delete()
        db.query(models.Hotel).delete()
        db.query(models.Location).delete()
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Warning when clearing data: {str(e)}")

    print("Creating locations...")
    # Create Locations
    phuket = models.Location(
        name="Phuket",
        region="Phuket",
        description="Thailand's largest island known for beautiful beaches and vibrant nightlife.",
    )
    db.add(phuket)
    db.flush()  # Flush to get the ID without committing

    patong = models.Location(
        name="Patong",
        region="Phuket",
        description="Famous beach town in Phuket with lively atmosphere.",
    )
    db.add(patong)
    db.flush()

    kata = models.Location(
        name="Kata",
        region="Phuket",
        description="Family-friendly beach area in Phuket.",
    )
    db.add(kata)
    db.flush()

    karon = models.Location(
        name="Karon",
        region="Phuket",
        description="Quieter beach area in Phuket with great sunset views.",
    )
    db.add(karon)
    db.flush()

    krabi = models.Location(
        name="Krabi",
        region="Krabi",
        description="Province known for limestone cliffs and stunning islands.",
    )
    db.add(krabi)
    db.flush()

    ao_nang = models.Location(
        name="Ao Nang",
        region="Krabi",
        description="Main tourist hub in Krabi with beaches and boat tours.",
    )
    db.add(ao_nang)
    db.flush()

    railay = models.Location(
        name="Railay",
        region="Krabi",
        description="Peninsula between Krabi and Ao Nang known for rock climbing.",
    )
    db.add(railay)
    db.flush()

    koh_phi_phi = models.Location(
        name="Koh Phi Phi",
        region="Krabi",
        description="Famous island in Krabi with beautiful beaches and marine life.",
    )
    db.add(koh_phi_phi)
    db.flush()

    # Store all locations in a list
    locations = [phuket, patong, kata, karon, krabi, ao_nang, railay, koh_phi_phi]
    db.commit()
    print(f"Created {len(locations)} locations")

    print("Creating hotels...")
    # Create Hotels
    # Phuket hotels
    hotel1 = models.Hotel(
        name="Phuket Marriott Resort",
        description="Luxury beachfront resort",
        price_per_night=250.0,
        star_rating=5,
        location_id=phuket.id,
    )
    db.add(hotel1)
    db.flush()

    hotel2 = models.Hotel(
        name="Amari Phuket",
        description="Elegant hotel with ocean views",
        price_per_night=180.0,
        star_rating=4,
        location_id=phuket.id,
    )
    db.add(hotel2)
    db.flush()

    hotel3 = models.Hotel(
        name="Holiday Inn Resort Phuket",
        description="Family-friendly resort",
        price_per_night=120.0,
        star_rating=4,
        location_id=phuket.id,
    )
    db.add(hotel3)
    db.flush()

    # Patong hotels
    hotel4 = models.Hotel(
        name="Patong Beach Hotel",
        description="Central hotel near nightlife",
        price_per_night=100.0,
        star_rating=3,
        location_id=patong.id,
    )
    db.add(hotel4)
    db.flush()

    hotel5 = models.Hotel(
        name="The Charm Resort Phuket",
        description="Modern hotel near Patong Beach",
        price_per_night=150.0,
        star_rating=4,
        location_id=patong.id,
    )
    db.add(hotel5)
    db.flush()

    # Kata hotels
    hotel6 = models.Hotel(
        name="Kata Beach Resort & Spa",
        description="Beachfront resort with large pool",
        price_per_night=170.0,
        star_rating=4,
        location_id=kata.id,
    )
    db.add(hotel6)
    db.flush()

    hotel7 = models.Hotel(
        name="Kata Sea Breeze Resort",
        description="Family resort with multiple pools",
        price_per_night=130.0,
        star_rating=3,
        location_id=kata.id,
    )
    db.add(hotel7)
    db.flush()

    # Karon hotels
    hotel8 = models.Hotel(
        name="Karon Sea Sands Resort",
        description="Resort near Karon Beach",
        price_per_night=140.0,
        star_rating=4,
        location_id=karon.id,
    )
    db.add(hotel8)
    db.flush()

    hotel9 = models.Hotel(
        name="Centara Grand Beach Resort Phuket",
        description="Luxury beachfront resort",
        price_per_night=280.0,
        star_rating=5,
        location_id=karon.id,
    )
    db.add(hotel9)
    db.flush()

    # Krabi hotels
    hotel10 = models.Hotel(
        name="Dusit Thani Krabi Beach Resort",
        description="Elegant beachfront resort",
        price_per_night=220.0,
        star_rating=5,
        location_id=krabi.id,
    )
    db.add(hotel10)
    db.flush()

    hotel11 = models.Hotel(
        name="Krabi Thai Village Resort",
        description="Traditional Thai-style resort",
        price_per_night=120.0,
        star_rating=4,
        location_id=krabi.id,
    )
    db.add(hotel11)
    db.flush()

    # Ao Nang hotels
    hotel12 = models.Hotel(
        name="Ao Nang Cliff Beach Resort",
        description="Hillside resort with stunning views",
        price_per_night=160.0,
        star_rating=4,
        location_id=ao_nang.id,
    )
    db.add(hotel12)
    db.flush()

    hotel13 = models.Hotel(
        name="Holiday Inn Resort Krabi Ao Nang Beach",
        description="Family-friendly resort",
        price_per_night=140.0,
        star_rating=4,
        location_id=ao_nang.id,
    )
    db.add(hotel13)
    db.flush()

    # Railay hotels
    hotel14 = models.Hotel(
        name="Railay Princess Resort & Spa",
        description="Resort surrounded by limestone cliffs",
        price_per_night=190.0,
        star_rating=4,
        location_id=railay.id,
    )
    db.add(hotel14)
    db.flush()

    hotel15 = models.Hotel(
        name="Rayavadee",
        description="Luxury resort with private beaches",
        price_per_night=450.0,
        star_rating=5,
        location_id=railay.id,
    )
    db.add(hotel15)
    db.flush()

    # Koh Phi Phi hotels
    hotel16 = models.Hotel(
        name="Phi Phi Island Village Beach Resort",
        description="Beachfront bungalows",
        price_per_night=230.0,
        star_rating=4,
        location_id=koh_phi_phi.id,
    )
    db.add(hotel16)
    db.flush()

    hotel17 = models.Hotel(
        name="Zeavola Resort",
        description="Luxury barefoot resort",
        price_per_night=320.0,
        star_rating=5,
        location_id=koh_phi_phi.id,
    )
    db.add(hotel17)
    db.flush()

    # Store all hotels in a list
    hotels = [
        hotel1,
        hotel2,
        hotel3,
        hotel4,
        hotel5,
        hotel6,
        hotel7,
        hotel8,
        hotel9,
        hotel10,
        hotel11,
        hotel12,
        hotel13,
        hotel14,
        hotel15,
        hotel16,
        hotel17,
    ]
    db.commit()
    print(f"Created {len(hotels)} hotels")

    print("Creating activities...")
    # Create Activities
    # Phuket activities
    activity1 = models.Activity(
        name="Big Buddha Visit",
        description="Visit the famous 45m tall marble statue",
        duration_hours=3.0,
        price=30.0,
        location_id=phuket.id,
    )
    db.add(activity1)
    db.flush()

    activity2 = models.Activity(
        name="Old Phuket Town Tour",
        description="Explore the historic Sino-Portuguese architecture",
        duration_hours=4.0,
        price=40.0,
        location_id=phuket.id,
    )
    db.add(activity2)
    db.flush()

    activity3 = models.Activity(
        name="Phuket Fantasea Show",
        description="Cultural theme park with shows",
        duration_hours=4.0,
        price=60.0,
        location_id=phuket.id,
    )
    db.add(activity3)
    db.flush()

    # Patong activities
    activity4 = models.Activity(
        name="Patong Beach Day",
        description="Relax at the famous beach",
        duration_hours=6.0,
        price=0.0,
        location_id=patong.id,
    )
    db.add(activity4)
    db.flush()

    activity5 = models.Activity(
        name="Bangla Road Nightlife",
        description="Experience the vibrant nightlife",
        duration_hours=4.0,
        price=0.0,
        location_id=patong.id,
    )
    db.add(activity5)
    db.flush()

    # Kata/Karon activities
    activity6 = models.Activity(
        name="Surf Lessons",
        description="Learn to surf at Kata Beach",
        duration_hours=2.0,
        price=50.0,
        location_id=kata.id,
    )
    db.add(activity6)
    db.flush()

    activity7 = models.Activity(
        name="Karon Viewpoint Visit",
        description="Stunning views of three beaches",
        duration_hours=2.0,
        price=0.0,
        location_id=karon.id,
    )
    db.add(activity7)
    db.flush()

    # Krabi activities
    activity8 = models.Activity(
        name="Four Islands Tour",
        description="Visit four beautiful islands by boat",
        duration_hours=8.0,
        price=80.0,
        location_id=krabi.id,
    )
    db.add(activity8)
    db.flush()

    activity9 = models.Activity(
        name="Emerald Pool & Hot Springs",
        description="Natural attractions in Krabi",
        duration_hours=6.0,
        price=70.0,
        location_id=krabi.id,
    )
    db.add(activity9)
    db.flush()

    activity10 = models.Activity(
        name="Tiger Cave Temple",
        description="Buddhist temple with 1,260 steps to the top",
        duration_hours=3.0,
        price=0.0,
        location_id=krabi.id,
    )
    db.add(activity10)
    db.flush()

    # Ao Nang activities
    activity11 = models.Activity(
        name="Island Hopping Tour",
        description="Visit nearby islands by longtail boat",
        duration_hours=7.0,
        price=60.0,
        location_id=ao_nang.id,
    )
    db.add(activity11)
    db.flush()

    # Railay activities
    activity12 = models.Activity(
        name="Rock Climbing",
        description="World-class climbing on limestone cliffs",
        duration_hours=5.0,
        price=90.0,
        location_id=railay.id,
    )
    db.add(activity12)
    db.flush()

    activity13 = models.Activity(
        name="Phra Nang Cave Beach",
        description="Visit the beautiful beach and princess cave",
        duration_hours=3.0,
        price=0.0,
        location_id=railay.id,
    )
    db.add(activity13)
    db.flush()

    # Koh Phi Phi activities
    activity14 = models.Activity(
        name="Maya Bay Tour",
        description="Visit the famous beach from 'The Beach' movie",
        duration_hours=4.0,
        price=50.0,
        location_id=koh_phi_phi.id,
    )
    db.add(activity14)
    db.flush()

    activity15 = models.Activity(
        name="Phi Phi Viewpoint Hike",
        description="Hike to the viewpoint for stunning views",
        duration_hours=2.0,
        price=0.0,
        location_id=koh_phi_phi.id,
    )
    db.add(activity15)
    db.flush()

    activity16 = models.Activity(
        name="Snorkeling Trip",
        description="Explore the underwater world around Phi Phi",
        duration_hours=5.0,
        price=40.0,
        location_id=koh_phi_phi.id,
    )
    db.add(activity16)
    db.flush()

    # Store all activities in a list
    activities = [
        activity1,
        activity2,
        activity3,
        activity4,
        activity5,
        activity6,
        activity7,
        activity8,
        activity9,
        activity10,
        activity11,
        activity12,
        activity13,
        activity14,
        activity15,
        activity16,
    ]
    db.commit()
    print(f"Created {len(activities)} activities")

    print("Creating transfers...")
    # Create Transfers
    transfer_map = {}  # To store transfers between locations

    for from_loc in locations:
        for to_loc in locations:
            if from_loc.id != to_loc.id:
                # Determine mode based on locations
                if (
                    "Koh" in to_loc.name
                    or "Railay" in to_loc.name
                    or "Koh" in from_loc.name
                    or "Railay" in from_loc.name
                ):
                    mode = "Ferry"
                    duration = round(random.uniform(1.0, 3.0), 1)
                    price = round(40.0 + random.uniform(0, 30.0), 2)
                elif from_loc.region != to_loc.region:
                    mode = "Van/Bus"
                    duration = round(random.uniform(2.0, 5.0), 1)
                    price = round(30.0 + random.uniform(0, 40.0), 2)
                else:
                    mode = "Car/Taxi"
                    duration = round(random.uniform(0.5, 1.5), 1)
                    price = round(20.0 + random.uniform(0, 20.0), 2)

                transfer = models.Transfer(
                    from_location_id=from_loc.id,
                    to_location_id=to_loc.id,
                    mode=mode,
                    duration_hours=duration,
                    price=price,
                )
                db.add(transfer)
                db.flush()

                # Store in map for easy lookup
                key = f"{from_loc.id}-{to_loc.id}"
                transfer_map[key] = transfer

    db.commit()
    print(f"Created {len(transfer_map)} transfers")

    print("Creating recommended itineraries...")
    # Create 2-night Phuket itinerary
    phuket_2n = models.Itinerary(
        name="Quick Phuket Getaway",
        description="A short but sweet 2-night trip to experience the best of Phuket",
        duration_nights=2,
        is_recommended=True,
        total_price=450.0,
    )
    db.add(phuket_2n)
    db.flush()

    # Add accommodations, activities for 2-night Phuket
    db.add(models.Accommodation(itinerary_id=phuket_2n.id, hotel_id=hotel1.id, day=1))
    db.add(models.Accommodation(itinerary_id=phuket_2n.id, hotel_id=hotel1.id, day=2))
    db.add(
        models.Excursion(
            itinerary_id=phuket_2n.id,
            activity_id=activity1.id,
            day=1,
            start_time=time(10, 0),
        )
    )
    db.add(
        models.Excursion(
            itinerary_id=phuket_2n.id,
            activity_id=activity4.id,
            day=1,
            start_time=time(14, 0),
        )
    )
    db.add(
        models.Excursion(
            itinerary_id=phuket_2n.id,
            activity_id=activity2.id,
            day=2,
            start_time=time(10, 0),
        )
    )
    db.add(
        models.Excursion(
            itinerary_id=phuket_2n.id,
            activity_id=activity5.id,
            day=2,
            start_time=time(19, 0),
        )
    )
    db.flush()

    # Create 4-night Phuket & Krabi
    phuket_krabi_4n = models.Itinerary(
        name="Phuket & Krabi Explorer",
        description="Experience the best of both Phuket and Krabi in this 4-night adventure",
        duration_nights=4,
        is_recommended=True,
        total_price=950.0,
    )
    db.add(phuket_krabi_4n)
    db.flush()

    # Get phuket to krabi transfer
    phuket_to_krabi_key = f"{phuket.id}-{krabi.id}"
    phuket_to_krabi_transfer = transfer_map[phuket_to_krabi_key]

    # Add accommodations, activities and transfers for 4-night Phuket & Krabi
    db.add(
        models.Accommodation(itinerary_id=phuket_krabi_4n.id, hotel_id=hotel2.id, day=1)
    )
    db.add(
        models.Accommodation(itinerary_id=phuket_krabi_4n.id, hotel_id=hotel2.id, day=2)
    )
    db.add(
        models.Accommodation(
            itinerary_id=phuket_krabi_4n.id, hotel_id=hotel10.id, day=3
        )
    )
    db.add(
        models.Accommodation(
            itinerary_id=phuket_krabi_4n.id, hotel_id=hotel10.id, day=4
        )
    )

    db.add(
        models.Excursion(
            itinerary_id=phuket_krabi_4n.id,
            activity_id=activity1.id,
            day=1,
            start_time=time(10, 0),
        )
    )
    db.add(
        models.Excursion(
            itinerary_id=phuket_krabi_4n.id,
            activity_id=activity5.id,
            day=1,
            start_time=time(19, 0),
        )
    )
    db.add(
        models.Excursion(
            itinerary_id=phuket_krabi_4n.id,
            activity_id=activity2.id,
            day=2,
            start_time=time(9, 0),
        )
    )
    db.add(
        models.Excursion(
            itinerary_id=phuket_krabi_4n.id,
            activity_id=activity3.id,
            day=2,
            start_time=time(19, 0),
        )
    )

    db.add(
        models.ItineraryTransfer(
            itinerary_id=phuket_krabi_4n.id,
            transfer_id=phuket_to_krabi_transfer.id,
            day=3,
            time=time(9, 0),
        )
    )

    db.add(
        models.Excursion(
            itinerary_id=phuket_krabi_4n.id,
            activity_id=activity9.id,
            day=3,
            start_time=time(14, 0),
        )
    )
    db.add(
        models.Excursion(
            itinerary_id=phuket_krabi_4n.id,
            activity_id=activity8.id,
            day=4,
            start_time=time(9, 0),
        )
    )
    db.flush()

    # Create 6-night Full Experience
    full_exp_6n = models.Itinerary(
        name="Thailand Island Experience",
        description="A comprehensive 6-night journey through Phuket, Krabi and Phi Phi Islands",
        duration_nights=6,
        is_recommended=True,
        total_price=1450.0,
    )
    db.add(full_exp_6n)
    db.flush()

    # Get transfers
    krabi_to_phiphi_key = f"{krabi.id}-{koh_phi_phi.id}"
    krabi_to_phiphi_transfer = transfer_map[krabi_to_phiphi_key]

    phiphi_to_phuket_key = f"{koh_phi_phi.id}-{phuket.id}"
    phiphi_to_phuket_transfer = transfer_map[phiphi_to_phuket_key]

    # Add accommodations
    db.add(models.Accommodation(itinerary_id=full_exp_6n.id, hotel_id=hotel1.id, day=1))
    db.add(models.Accommodation(itinerary_id=full_exp_6n.id, hotel_id=hotel1.id, day=2))
    db.add(
        models.Accommodation(itinerary_id=full_exp_6n.id, hotel_id=hotel10.id, day=3)
    )
    db.add(
        models.Accommodation(itinerary_id=full_exp_6n.id, hotel_id=hotel10.id, day=4)
    )
    db.add(
        models.Accommodation(itinerary_id=full_exp_6n.id, hotel_id=hotel16.id, day=5)
    )
    db.add(
        models.Accommodation(itinerary_id=full_exp_6n.id, hotel_id=hotel16.id, day=6)
    )

    # Add excursions
    db.add(
        models.Excursion(
            itinerary_id=full_exp_6n.id,
            activity_id=activity1.id,
            day=1,
            start_time=time(10, 0),
        )
    )
    db.add(
        models.Excursion(
            itinerary_id=full_exp_6n.id,
            activity_id=activity4.id,
            day=1,
            start_time=time(15, 0),
        )
    )
    db.add(
        models.Excursion(
            itinerary_id=full_exp_6n.id,
            activity_id=activity2.id,
            day=2,
            start_time=time(9, 0),
        )
    )
    db.add(
        models.Excursion(
            itinerary_id=full_exp_6n.id,
            activity_id=activity3.id,
            day=2,
            start_time=time(19, 0),
        )
    )

    # Add transfers
    db.add(
        models.ItineraryTransfer(
            itinerary_id=full_exp_6n.id,
            transfer_id=phuket_to_krabi_transfer.id,
            day=3,
            time=time(9, 0),
        )
    )

    db.add(
        models.Excursion(
            itinerary_id=full_exp_6n.id,
            activity_id=activity9.id,
            day=3,
            start_time=time(14, 0),
        )
    )
    db.add(
        models.Excursion(
            itinerary_id=full_exp_6n.id,
            activity_id=activity8.id,
            day=4,
            start_time=time(9, 0),
        )
    )

    db.add(
        models.ItineraryTransfer(
            itinerary_id=full_exp_6n.id,
            transfer_id=krabi_to_phiphi_transfer.id,
            day=5,
            time=time(9, 0),
        )
    )

    db.add(
        models.Excursion(
            itinerary_id=full_exp_6n.id,
            activity_id=activity14.id,
            day=5,
            start_time=time(14, 0),
        )
    )
    db.add(
        models.Excursion(
            itinerary_id=full_exp_6n.id,
            activity_id=activity15.id,
            day=6,
            start_time=time(9, 0),
        )
    )
    db.add(
        models.Excursion(
            itinerary_id=full_exp_6n.id,
            activity_id=activity16.id,
            day=6,
            start_time=time(14, 0),
        )
    )

    db.add(
        models.ItineraryTransfer(
            itinerary_id=full_exp_6n.id,
            transfer_id=phiphi_to_phuket_transfer.id,
            day=6,
            time=time(18, 0),
        )
    )
    db.flush()

    # Create 8-night Ultimate Thailand
    ultimate_8n = models.Itinerary(
        name="Ultimate Thailand Islands",
        description="The most comprehensive 8-night journey exploring all the highlights of Phuket, Krabi, Railay and Phi Phi",
        duration_nights=8,
        is_recommended=True,
        total_price=1950.0,
    )
    db.add(ultimate_8n)
    db.flush()

    # Get additional transfers
    krabi_to_railay_key = f"{krabi.id}-{railay.id}"
    krabi_to_railay_transfer = transfer_map[krabi_to_railay_key]

    railay_to_phiphi_key = f"{railay.id}-{koh_phi_phi.id}"
    railay_to_phiphi_transfer = transfer_map[railay_to_phiphi_key]

    phuket_to_karon_key = f"{phuket.id}-{karon.id}"
    phuket_to_karon_transfer = transfer_map[phuket_to_karon_key]

    karon_to_krabi_key = f"{karon.id}-{krabi.id}"
    karon_to_krabi_transfer = transfer_map[karon_to_krabi_key]

    # Add accommodations
    db.add(models.Accommodation(itinerary_id=ultimate_8n.id, hotel_id=hotel1.id, day=1))
    db.add(models.Accommodation(itinerary_id=ultimate_8n.id, hotel_id=hotel1.id, day=2))
    db.add(models.Accommodation(itinerary_id=ultimate_8n.id, hotel_id=hotel8.id, day=3))
    db.add(
        models.Accommodation(itinerary_id=ultimate_8n.id, hotel_id=hotel10.id, day=4)
    )
    db.add(
        models.Accommodation(itinerary_id=ultimate_8n.id, hotel_id=hotel10.id, day=5)
    )
    db.add(
        models.Accommodation(itinerary_id=ultimate_8n.id, hotel_id=hotel14.id, day=6)
    )
    db.add(
        models.Accommodation(itinerary_id=ultimate_8n.id, hotel_id=hotel16.id, day=7)
    )
    db.add(
        models.Accommodation(itinerary_id=ultimate_8n.id, hotel_id=hotel16.id, day=8)
    )

    # Day 1-2: Phuket
    db.add(
        models.Excursion(
            itinerary_id=ultimate_8n.id,
            activity_id=activity1.id,
            day=1,
            start_time=time(10, 0),
        )
    )
    db.add(
        models.Excursion(
            itinerary_id=ultimate_8n.id,
            activity_id=activity4.id,
            day=1,
            start_time=time(15, 0),
        )
    )
    db.add(
        models.Excursion(
            itinerary_id=ultimate_8n.id,
            activity_id=activity2.id,
            day=2,
            start_time=time(9, 0),
        )
    )
    db.add(
        models.Excursion(
            itinerary_id=ultimate_8n.id,
            activity_id=activity3.id,
            day=2,
            start_time=time(19, 0),
        )
    )

    # Day 3: Karon
    db.add(
        models.ItineraryTransfer(
            itinerary_id=ultimate_8n.id,
            transfer_id=phuket_to_karon_transfer.id,
            day=3,
            time=time(9, 0),
        )
    )
    db.add(
        models.Excursion(
            itinerary_id=ultimate_8n.id,
            activity_id=activity7.id,
            day=3,
            start_time=time(14, 0),
        )
    )

    # Day 4-5: Krabi
    db.add(
        models.ItineraryTransfer(
            itinerary_id=ultimate_8n.id,
            transfer_id=karon_to_krabi_transfer.id,
            day=4,
            time=time(9, 0),
        )
    )
    db.add(
        models.Excursion(
            itinerary_id=ultimate_8n.id,
            activity_id=activity9.id,
            day=4,
            start_time=time(14, 0),
        )
    )
    db.add(
        models.Excursion(
            itinerary_id=ultimate_8n.id,
            activity_id=activity8.id,
            day=5,
            start_time=time(9, 0),
        )
    )

    # Day 6: Railay
    db.add(
        models.ItineraryTransfer(
            itinerary_id=ultimate_8n.id,
            transfer_id=krabi_to_railay_transfer.id,
            day=6,
            time=time(9, 0),
        )
    )
    db.add(
        models.Excursion(
            itinerary_id=ultimate_8n.id,
            activity_id=activity12.id,
            day=6,
            start_time=time(11, 0),
        )
    )
    db.add(
        models.Excursion(
            itinerary_id=ultimate_8n.id,
            activity_id=activity13.id,
            day=6,
            start_time=time(16, 0),
        )
    )

    # Day 7-8: Phi Phi
    db.add(
        models.ItineraryTransfer(
            itinerary_id=ultimate_8n.id,
            transfer_id=railay_to_phiphi_transfer.id,
            day=7,
            time=time(9, 0),
        )
    )
    db.add(
        models.Excursion(
            itinerary_id=ultimate_8n.id,
            activity_id=activity14.id,
            day=7,
            start_time=time(14, 0),
        )
    )
    db.add(
        models.Excursion(
            itinerary_id=ultimate_8n.id,
            activity_id=activity15.id,
            day=8,
            start_time=time(9, 0),
        )
    )
    db.add(
        models.Excursion(
            itinerary_id=ultimate_8n.id,
            activity_id=activity16.id,
            day=8,
            start_time=time(14, 0),
        )
    )

    db.add(
        models.ItineraryTransfer(
            itinerary_id=ultimate_8n.id,
            transfer_id=phiphi_to_phuket_transfer.id,
            day=8,
            time=time(18, 0),
        )
    )

    
    db.commit()
    print("All recommended itineraries created successfully")

    print("Database seeded successfully!")
    return True
