from sqlalchemy.orm import Session
from . import models
from datetime import time
import random


def seed_database(db: Session):
    # Create Locations
    phuket = models.Location(
        name="Phuket",
        region="Phuket",
        description="Thailand's largest island known for beautiful beaches and vibrant nightlife.",
    )
    patong = models.Location(
        name="Patong",
        region="Phuket",
        description="Famous beach town in Phuket with lively atmosphere.",
    )
    kata = models.Location(
        name="Kata",
        region="Phuket",
        description="Family-friendly beach area in Phuket.",
    )
    karon = models.Location(
        name="Karon",
        region="Phuket",
        description="Quieter beach area in Phuket with great sunset views.",
    )

    krabi = models.Location(
        name="Krabi",
        region="Krabi",
        description="Province known for limestone cliffs and stunning islands.",
    )
    ao_nang = models.Location(
        name="Ao Nang",
        region="Krabi",
        description="Main tourist hub in Krabi with beaches and boat tours.",
    )
    railay = models.Location(
        name="Railay",
        region="Krabi",
        description="Peninsula between Krabi and Ao Nang known for rock climbing.",
    )
    koh_phi_phi = models.Location(
        name="Koh Phi Phi",
        region="Krabi",
        description="Famous island in Krabi with beautiful beaches and marine life.",
    )

    locations = [phuket, patong, kata, karon, krabi, ao_nang, railay, koh_phi_phi]
    db.add_all(locations)
    db.commit()

    # Create Hotels
    hotels = [
        # Phuket hotels
        models.Hotel(
            name="Phuket Marriott Resort",
            description="Luxury beachfront resort",
            price_per_night=250.0,
            star_rating=5,
            location_id=phuket.id,
        ),
        models.Hotel(
            name="Amari Phuket",
            description="Elegant hotel with ocean views",
            price_per_night=180.0,
            star_rating=4,
            location_id=phuket.id,
        ),
        models.Hotel(
            name="Holiday Inn Resort Phuket",
            description="Family-friendly resort",
            price_per_night=120.0,
            star_rating=4,
            location_id=phuket.id,
        ),
        # Patong hotels
        models.Hotel(
            name="Patong Beach Hotel",
            description="Central hotel near nightlife",
            price_per_night=100.0,
            star_rating=3,
            location_id=patong.id,
        ),
        models.Hotel(
            name="The Charm Resort Phuket",
            description="Modern hotel near Patong Beach",
            price_per_night=150.0,
            star_rating=4,
            location_id=patong.id,
        ),
        # Kata hotels
        models.Hotel(
            name="Kata Beach Resort & Spa",
            description="Beachfront resort with large pool",
            price_per_night=170.0,
            star_rating=4,
            location_id=kata.id,
        ),
        models.Hotel(
            name="Kata Sea Breeze Resort",
            description="Family resort with multiple pools",
            price_per_night=130.0,
            star_rating=3,
            location_id=kata.id,
        ),
        # Karon hotels
        models.Hotel(
            name="Karon Sea Sands Resort",
            description="Resort near Karon Beach",
            price_per_night=140.0,
            star_rating=4,
            location_id=karon.id,
        ),
        models.Hotel(
            name="Centara Grand Beach Resort Phuket",
            description="Luxury beachfront resort",
            price_per_night=280.0,
            star_rating=5,
            location_id=karon.id,
        ),
        # Krabi hotels
        models.Hotel(
            name="Dusit Thani Krabi Beach Resort",
            description="Elegant beachfront resort",
            price_per_night=220.0,
            star_rating=5,
            location_id=krabi.id,
        ),
        models.Hotel(
            name="Krabi Thai Village Resort",
            description="Traditional Thai-style resort",
            price_per_night=120.0,
            star_rating=4,
            location_id=krabi.id,
        ),
        # Ao Nang hotels
        models.Hotel(
            name="Ao Nang Cliff Beach Resort",
            description="Hillside resort with stunning views",
            price_per_night=160.0,
            star_rating=4,
            location_id=ao_nang.id,
        ),
        models.Hotel(
            name="Holiday Inn Resort Krabi Ao Nang Beach",
            description="Family-friendly resort",
            price_per_night=140.0,
            star_rating=4,
            location_id=ao_nang.id,
        ),
        # Railay hotels
        models.Hotel(
            name="Railay Princess Resort & Spa",
            description="Resort surrounded by limestone cliffs",
            price_per_night=190.0,
            star_rating=4,
            location_id=railay.id,
        ),
        models.Hotel(
            name="Rayavadee",
            description="Luxury resort with private beaches",
            price_per_night=450.0,
            star_rating=5,
            location_id=railay.id,
        ),
        # Koh Phi Phi hotels
        models.Hotel(
            name="Phi Phi Island Village Beach Resort",
            description="Beachfront bungalows",
            price_per_night=230.0,
            star_rating=4,
            location_id=koh_phi_phi.id,
        ),
        models.Hotel(
            name="Zeavola Resort",
            description="Luxury barefoot resort",
            price_per_night=320.0,
            star_rating=5,
            location_id=koh_phi_phi.id,
        ),
    ]
    db.add_all(hotels)
    db.commit()

    # Create Activities
    activities = [
        # Phuket activities
        models.Activity(
            name="Big Buddha Visit",
            description="Visit the famous 45m tall marble statue",
            duration_hours=3.0,
            price=30.0,
            location_id=phuket.id,
        ),
        models.Activity(
            name="Old Phuket Town Tour",
            description="Explore the historic Sino-Portuguese architecture",
            duration_hours=4.0,
            price=40.0,
            location_id=phuket.id,
        ),
        models.Activity(
            name="Phuket Fantasea Show",
            description="Cultural theme park with shows",
            duration_hours=4.0,
            price=60.0,
            location_id=phuket.id,
        ),
        # Patong activities
        models.Activity(
            name="Patong Beach Day",
            description="Relax at the famous beach",
            duration_hours=6.0,
            price=0.0,
            location_id=patong.id,
        ),
        models.Activity(
            name="Bangla Road Nightlife",
            description="Experience the vibrant nightlife",
            duration_hours=4.0,
            price=0.0,
            location_id=patong.id,
        ),
        # Kata/Karon activities
        models.Activity(
            name="Surf Lessons",
            description="Learn to surf at Kata Beach",
            duration_hours=2.0,
            price=50.0,
            location_id=kata.id,
        ),
        models.Activity(
            name="Karon Viewpoint Visit",
            description="Stunning views of three beaches",
            duration_hours=2.0,
            price=0.0,
            location_id=karon.id,
        ),
        # Krabi activities
        models.Activity(
            name="Four Islands Tour",
            description="Visit four beautiful islands by boat",
            duration_hours=8.0,
            price=80.0,
            location_id=krabi.id,
        ),
        models.Activity(
            name="Emerald Pool & Hot Springs",
            description="Natural attractions in Krabi",
            duration_hours=6.0,
            price=70.0,
            location_id=krabi.id,
        ),
        models.Activity(
            name="Tiger Cave Temple",
            description="Buddhist temple with 1,260 steps to the top",
            duration_hours=3.0,
            price=0.0,
            location_id=krabi.id,
        ),
        # Ao Nang activities
        models.Activity(
            name="Island Hopping Tour",
            description="Visit nearby islands by longtail boat",
            duration_hours=7.0,
            price=60.0,
            location_id=ao_nang.id,
        ),
        # Railay activities
        models.Activity(
            name="Rock Climbing",
            description="World-class climbing on limestone cliffs",
            duration_hours=5.0,
            price=90.0,
            location_id=railay.id,
        ),
        # Railay activities (continued)
        models.Activity(
            name="Phra Nang Cave Beach",
            description="Visit the beautiful beach and princess cave",
            duration_hours=3.0,
            price=0.0,
            location_id=railay.id,
        ),
        # Koh Phi Phi activities
        models.Activity(
            name="Maya Bay Tour",
            description="Visit the famous beach from 'The Beach' movie",
            duration_hours=4.0,
            price=50.0,
            location_id=koh_phi_phi.id,
        ),
        models.Activity(
            name="Phi Phi Viewpoint Hike",
            description="Hike to the viewpoint for stunning views",
            duration_hours=2.0,
            price=0.0,
            location_id=koh_phi_phi.id,
        ),
        models.Activity(
            name="Snorkeling Trip",
            description="Explore the underwater world around Phi Phi",
            duration_hours=5.0,
            price=40.0,
            location_id=koh_phi_phi.id,
        ),
    ]
    db.add_all(activities)
    db.commit()

    # Create Transfers
    transfers = []
    # Connect all locations with appropriate transfers
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
                    duration = random.uniform(1.0, 3.0)
                    price = 40.0 + random.uniform(0, 30.0)
                elif from_loc.region != to_loc.region:
                    mode = "Van/Bus"
                    duration = random.uniform(2.0, 5.0)
                    price = 30.0 + random.uniform(0, 40.0)
                else:
                    mode = "Car/Taxi"
                    duration = random.uniform(0.5, 1.5)
                    price = 20.0 + random.uniform(0, 20.0)

                transfers.append(
                    models.Transfer(
                        from_location_id=from_loc.id,
                        to_location_id=to_loc.id,
                        mode=mode,
                        duration_hours=duration,
                        price=round(price, 2),
                    )
                )

    db.add_all(transfers)
    db.commit()

    # Create Recommended Itineraries
    # 2-night Phuket itinerary
    phuket_2n = models.Itinerary(
        name="Quick Phuket Getaway",
        description="A short but sweet 2-night trip to experience the best of Phuket",
        duration_nights=2,
        is_recommended=True,
        total_price=450.0,
    )
    db.add(phuket_2n)
    db.commit()

    # Add accommodations, activities, and transfers for 2-night Phuket
    db.add_all(
        [
            models.Accommodation(itinerary_id=phuket_2n.id, hotel_id=1, day=1),
            models.Accommodation(itinerary_id=phuket_2n.id, hotel_id=1, day=2),
            models.Excursion(
                itinerary_id=phuket_2n.id, activity_id=1, day=1, start_time=time(10, 0)
            ),
            models.Excursion(
                itinerary_id=phuket_2n.id, activity_id=4, day=1, start_time=time(14, 0)
            ),
            models.Excursion(
                itinerary_id=phuket_2n.id, activity_id=2, day=2, start_time=time(10, 0)
            ),
            models.Excursion(
                itinerary_id=phuket_2n.id, activity_id=5, day=2, start_time=time(19, 0)
            ),
        ]
    )
    db.commit()

    # 4-night Phuket & Krabi
    phuket_krabi_4n = models.Itinerary(
        name="Phuket & Krabi Explorer",
        description="Experience the best of both Phuket and Krabi in this 4-night adventure",
        duration_nights=4,
        is_recommended=True,
        total_price=950.0,
    )
    db.add(phuket_krabi_4n)
    db.commit()

    # Add accommodations, activities and transfers for 4-night Phuket & Krabi
    phuket_to_krabi_transfer = (
        db.query(models.Transfer)
        .filter(
            models.Transfer.from_location_id == phuket.id,
            models.Transfer.to_location_id == krabi.id,
        )
        .first()
    )

    db.add_all(
        [
            models.Accommodation(itinerary_id=phuket_krabi_4n.id, hotel_id=2, day=1),
            models.Accommodation(itinerary_id=phuket_krabi_4n.id, hotel_id=2, day=2),
            models.Accommodation(itinerary_id=phuket_krabi_4n.id, hotel_id=10, day=3),
            models.Accommodation(itinerary_id=phuket_krabi_4n.id, hotel_id=10, day=4),
            models.Excursion(
                itinerary_id=phuket_krabi_4n.id,
                activity_id=1,
                day=1,
                start_time=time(10, 0),
            ),
            models.Excursion(
                itinerary_id=phuket_krabi_4n.id,
                activity_id=5,
                day=1,
                start_time=time(19, 0),
            ),
            models.Excursion(
                itinerary_id=phuket_krabi_4n.id,
                activity_id=2,
                day=2,
                start_time=time(9, 0),
            ),
            models.Excursion(
                itinerary_id=phuket_krabi_4n.id,
                activity_id=3,
                day=2,
                start_time=time(19, 0),
            ),
            models.ItineraryTransfer(
                itinerary_id=phuket_krabi_4n.id,
                transfer_id=phuket_to_krabi_transfer.id,
                day=3,
                time=time(9, 0),
            ),
            models.Excursion(
                itinerary_id=phuket_krabi_4n.id,
                activity_id=9,
                day=3,
                start_time=time(14, 0),
            ),
            models.Excursion(
                itinerary_id=phuket_krabi_4n.id,
                activity_id=8,
                day=4,
                start_time=time(9, 0),
            ),
        ]
    )
    db.commit()

    # 6-night Full Experience
    full_exp_6n = models.Itinerary(
        name="Thailand Island Experience",
        description="A comprehensive 6-night journey through Phuket, Krabi and Phi Phi Islands",
        duration_nights=6,
        is_recommended=True,
        total_price=1450.0,
    )
    db.add(full_exp_6n)
    db.commit()

    # Add accommodations, activities and transfers for 6-night experience
    krabi_to_phiphi_transfer = (
        db.query(models.Transfer)
        .filter(
            models.Transfer.from_location_id == krabi.id,
            models.Transfer.to_location_id == koh_phi_phi.id,
        )
        .first()
    )

    phiphi_to_phuket_transfer = (
        db.query(models.Transfer)
        .filter(
            models.Transfer.from_location_id == koh_phi_phi.id,
            models.Transfer.to_location_id == phuket.id,
        )
        .first()
    )

    db.add_all(
        [
            models.Accommodation(itinerary_id=full_exp_6n.id, hotel_id=1, day=1),
            models.Accommodation(itinerary_id=full_exp_6n.id, hotel_id=1, day=2),
            models.Accommodation(itinerary_id=full_exp_6n.id, hotel_id=10, day=3),
            models.Accommodation(itinerary_id=full_exp_6n.id, hotel_id=10, day=4),
            models.Accommodation(itinerary_id=full_exp_6n.id, hotel_id=16, day=5),
            models.Accommodation(itinerary_id=full_exp_6n.id, hotel_id=16, day=6),
            models.Excursion(
                itinerary_id=full_exp_6n.id,
                activity_id=1,
                day=1,
                start_time=time(10, 0),
            ),
            models.Excursion(
                itinerary_id=full_exp_6n.id,
                activity_id=4,
                day=1,
                start_time=time(15, 0),
            ),
            models.Excursion(
                itinerary_id=full_exp_6n.id, activity_id=2, day=2, start_time=time(9, 0)
            ),
            models.Excursion(
                itinerary_id=full_exp_6n.id,
                activity_id=3,
                day=2,
                start_time=time(19, 0),
            ),
            models.ItineraryTransfer(
                itinerary_id=full_exp_6n.id,
                transfer_id=phuket_to_krabi_transfer.id,
                day=3,
                time=time(9, 0),
            ),
            models.Excursion(
                itinerary_id=full_exp_6n.id,
                activity_id=9,
                day=3,
                start_time=time(14, 0),
            ),
            models.Excursion(
                itinerary_id=full_exp_6n.id, activity_id=8, day=4, start_time=time(9, 0)
            ),
            models.ItineraryTransfer(
                itinerary_id=full_exp_6n.id,
                transfer_id=krabi_to_phiphi_transfer.id,
                day=5,
                time=time(9, 0),
            ),
            models.Excursion(
                itinerary_id=full_exp_6n.id,
                activity_id=15,
                day=5,
                start_time=time(14, 0),
            ),
            models.Excursion(
                itinerary_id=full_exp_6n.id,
                activity_id=16,
                day=6,
                start_time=time(9, 0),
            ),
            models.Excursion(
                itinerary_id=full_exp_6n.id,
                activity_id=17,
                day=6,
                start_time=time(14, 0),
            ),
            models.ItineraryTransfer(
                itinerary_id=full_exp_6n.id,
                transfer_id=phiphi_to_phuket_transfer.id,
                day=6,
                time=time(18, 0),
            ),
        ]
    )
    db.commit()

    # 8-night Ultimate Thailand
    ultimate_8n = models.Itinerary(
        name="Ultimate Thailand Islands",
        description="The most comprehensive 8-night journey exploring all the highlights of Phuket, Krabi, Railay and Phi Phi",
        duration_nights=8,
        is_recommended=True,
        total_price=1950.0,
    )
    db.add(ultimate_8n)
    db.commit()

    # Add accommodations, activities and transfers for 8-night experience
    krabi_to_railay_transfer = (
        db.query(models.Transfer)
        .filter(
            models.Transfer.from_location_id == krabi.id,
            models.Transfer.to_location_id == railay.id,
        )
        .first()
    )

    railay_to_phiphi_transfer = (
        db.query(models.Transfer)
        .filter(
            models.Transfer.from_location_id == railay.id,
            models.Transfer.to_location_id == koh_phi_phi.id,
        )
        .first()
    )

    db.add_all(
        [
            models.Accommodation(itinerary_id=ultimate_8n.id, hotel_id=1, day=1),
            models.Accommodation(itinerary_id=ultimate_8n.id, hotel_id=1, day=2),
            models.Accommodation(itinerary_id=ultimate_8n.id, hotel_id=8, day=3),
            models.Accommodation(itinerary_id=ultimate_8n.id, hotel_id=10, day=4),
            models.Accommodation(itinerary_id=ultimate_8n.id, hotel_id=10, day=5),
            models.Accommodation(itinerary_id=ultimate_8n.id, hotel_id=14, day=6),
            models.Accommodation(itinerary_id=ultimate_8n.id, hotel_id=16, day=7),
            models.Accommodation(itinerary_id=ultimate_8n.id, hotel_id=16, day=8),
            # Day 1-2: Phuket
            models.Excursion(
                itinerary_id=ultimate_8n.id,
                activity_id=1,
                day=1,
                start_time=time(10, 0),
            ),
            models.Excursion(
                itinerary_id=ultimate_8n.id,
                activity_id=4,
                day=1,
                start_time=time(15, 0),
            ),
            models.Excursion(
                itinerary_id=ultimate_8n.id, activity_id=2, day=2, start_time=time(9, 0)
            ),
            models.Excursion(
                itinerary_id=ultimate_8n.id,
                activity_id=3,
                day=2,
                start_time=time(19, 0),
            ),
            # Day 3: Karon
            models.ItineraryTransfer(
                itinerary_id=ultimate_8n.id,
                transfer_id=db.query(models.Transfer)
                .filter(
                    models.Transfer.from_location_id == phuket.id,
                    models.Transfer.to_location_id == karon.id,
                )
                .first()
                .id,
                day=3,
                time=time(9, 0),
            ),
            models.Excursion(
                itinerary_id=ultimate_8n.id,
                activity_id=7,
                day=3,
                start_time=time(14, 0),
            ),
            # Day 4-5: Krabi
            models.ItineraryTransfer(
                itinerary_id=ultimate_8n.id,
                transfer_id=db.query(models.Transfer)
                .filter(
                    models.Transfer.from_location_id == karon.id,
                    models.Transfer.to_location_id == krabi.id,
                )
                .first()
                .id,
                day=4,
                time=time(9, 0),
            ),
            models.Excursion(
                itinerary_id=ultimate_8n.id,
                activity_id=9,
                day=4,
                start_time=time(14, 0),
            ),
            models.Excursion(
                itinerary_id=ultimate_8n.id, activity_id=8, day=5, start_time=time(9, 0)
            ),
            # Day 6: Railay
            models.ItineraryTransfer(
                itinerary_id=ultimate_8n.id,
                transfer_id=krabi_to_railay_transfer.id,
                day=6,
                time=time(9, 0),
            ),
            models.Excursion(
                itinerary_id=ultimate_8n.id,
                activity_id=12,
                day=6,
                start_time=time(11, 0),
            ),
            models.Excursion(
                itinerary_id=ultimate_8n.id,
                activity_id=13,
                day=6,
                start_time=time(16, 0),
            ),
            # Day 7-8: Phi Phi
            models.ItineraryTransfer(
                itinerary_id=ultimate_8n.id,
                transfer_id=railay_to_phiphi_transfer.id,
                day=7,
                time=time(9, 0),
            ),
            models.Excursion(
                itinerary_id=ultimate_8n.id,
                activity_id=15,
                day=7,
                start_time=time(14, 0),
            ),
            models.Excursion(
                itinerary_id=ultimate_8n.id,
                activity_id=16,
                day=8,
                start_time=time(9, 0),
            ),
            models.Excursion(
                itinerary_id=ultimate_8n.id,
                activity_id=17,
                day=8,
                start_time=time(14, 0),
            ),
            models.ItineraryTransfer(
                itinerary_id=ultimate_8n.id,
                transfer_id=phiphi_to_phuket_transfer.id,
                day=8,
                time=time(18, 0),
            ),
        ]
    )
    db.commit()

    print("Database seeded successfully!")
