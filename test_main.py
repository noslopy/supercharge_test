from fastapi.testclient import TestClient
from sqlmodel import Session, select
from .main import app
from .db.db import DB

client = TestClient(app)

db = DB()
db.drop_db()
db.create_db()

db.add_meetingroom("Lisbon")
db.add_meetingroom("Porto")
db.add_meetingroom("Aveiro")

db.add_meeting(2, 1, 3) #belongs to porto
db.add_meeting(2, 3, 4) #belongs to porto
db.add_meeting(3, 4, 6) #belongs to aveiro

# hello
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

# has one open room
def test_meeting_rooms_available():
    response = client.get("/meeting-rooms/available?start=1&end=5")
    assert response.status_code == 200
    assert response.json() == [{"name": "Lisbon", "id": "1"}]

# all rooms free
def test_meeting_rooms_available2():
    response = client.get("/meeting-rooms/available?start=7&end=9")
    assert response.status_code == 200
    assert response.json() == [{"name": "Lisbon", "id": "1"},{"name": "Porto", "id": "2"},{"name": "Aveiro", "id": "3"}]

# all meetings in porto room
def test_meeting_rooms_upcoming_meeting():
    response = client.get("/meeting-rooms/3/upcoming-meeting")
    assert response.status_code == 200
    assert response.json() == {"meetingRoomName": "Aveiro","meetings": [{"id": "3","start": 4,"end": 6,"name": "asd"}]}

# can delete a meeting by id
def test_meetings_delete():
    response = client.delete("/meetings/3")
    assert response.status_code == 200

# delete was success new free office
def test_meeting_rooms_available3():
    response = client.get("/meeting-rooms/available?start=1&end=5")
    assert response.status_code == 200
    assert response.json() == [{"name": "Lisbon", "id": "1"},{"name": "Aveiro", "id": "3"}]

# can create a meeting by room_id
def test_meeting_rooms_book():
    response = client.post("/meeting-rooms/1/book?start=1&end=5")
    assert response.status_code == 200

# free rooms are changing
def test_meeting_rooms_available4():
    response = client.get("/meeting-rooms/available?start=1&end=5")
    assert response.status_code == 200
    assert response.json() == [{"name": "Aveiro", "id": "3"}]