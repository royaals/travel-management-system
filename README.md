# Travel Management System

A robust backend system for managing travel itineraries. Built with **FastAPI** and **SQLAlchemy**, this system offers complete control over itinerary creation, management, and recommendations.

---

##  Features

###  Database Architecture
Designed using SQLAlchemy ORM:
- Day-wise **hotel accommodations**
- Inter-location **transfers**
- **Activities and excursions**
- Comprehensive entity **relationships**

###  RESTful API (FastAPI)
- Create new itineraries
- View existing itineraries
- Access reference data: hotels, activities, locations

###  MCP Recommendation Server
- Smart recommendations based on duration

###  Seed Data
- Multiple realistic locations in Phuket & Krabi
- Hotels with varying prices and ratings
- Activities & excursions
- Pre-configured recommended itineraries

---

##  Installation

###  Prerequisites
- Python 3.7+
- SQLite3

###  SQLite Installation

#### Windows (via Chocolatey)

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; `
[System.Net.ServicePointManager]::SecurityProtocol = `
[System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

choco install sqlite
```

#### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install sqlite3
```

#### macOS

```bash

sqlite3 --version  
```

###  Setting Up the Environment

```bash

git clone https://github.com/royaals/travel-management-system.git
cd travel-management-system


# Create and activate virtual environment
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

##  Running the Application

```bash
uvicorn app.main:app --reload
```



---



- API: [http://localhost:8000](http://localhost:8000)
- Swagger Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

##  Database Operations

### Accessing the SQLite DB

```bash
sqlite3 travel_itinerary.db
```

####  Example Queries

```sql
-- View all locations
SELECT * FROM locations;

-- View hotels with locations
SELECT h.name, h.price_per_night, l.name AS location 
FROM hotels h 
JOIN locations l ON h.location_id = l.id;

-- View recommended itineraries
SELECT * FROM itineraries WHERE is_recommended = 1;
```

---

##  API Examples

### Create New Itinerary

**POST** `/itineraries/`

```json
{
  "name": "Custom Phuket Adventure",
  "description": "A 3-day custom adventure in Phuket",
  "duration_nights": 3,
  "is_recommended": false,
  "total_price": 750.0,
  "accommodations": [
    { "hotel_id": 1, "day": 1 },
    { "hotel_id": 1, "day": 2 },
    { "hotel_id": 2, "day": 3 }
  ],
  "excursions": [
    { "activity_id": 1, "day": 1, "start_time": "10:00:00" },
    { "activity_id": 2, "day": 2, "start_time": "09:00:00" }
  ],
  "transfers": [
    { "transfer_id": 1, "day": 1, "time": "08:00:00" }
  ]
}
```

###  Get Specific Itinerary

**GET** `/itineraries/1`

###  Get Recommended Itineraries

**GET** `/recommended-itineraries/?duration_nights=4`

###  Get All Hotels

**GET** `/hotels/`

---


##  Error Handling

The API includes robust error handling:

- `404`: Resource not found
- `422`: Validation error
- `500`: Internal server error

**Example Response:**

```json
{
  "detail": "Itinerary not found"
}
```

---

##  Data Models

###  Location
- `name`
- `region`
- `description`

###  Hotel
- `name`
- `description`
- `price_per_night`
- `star_rating`
- `location_id`

###  Activity
- `name`
- `description`
- `duration_hours`
- `price`
- `location_id`

###  Itinerary
- `name`
- `description`
- `duration_nights`
- `is_recommended`
- `total_price`
- `accommodations`
- `excursions`
- `transfers`

---


