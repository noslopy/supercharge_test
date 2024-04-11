from fastapi import FastAPI
from .db.db import DB

app = FastAPI()
db = DB()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/meeting-rooms/available")
async def meeting_rooms_available(start: int = None, end: int = None):
    return db.available_meeting_rooms(start, end)

@app.get("/meeting-rooms/{meetingRoomId}/upcoming-meeting")
async def meeting_rooms_upcoming_meeting(meetingRoomId: int = None):
    return db.upcoming_meetings(meetingRoomId)

@app.post("/meeting-rooms/{meetingRoomId}/book")
async def meeting_rooms_book(meetingRoomId: int = None, start: int = None, end: int = None):
    return db.add_meeting(meetingRoomId, start, end)

@app.delete("/meetings/{meetingId}")
async def meetings_delete(meetingId: int = None):
    return db.drop_meeting(meetingId)