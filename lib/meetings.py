import os
from sqlmodel import SQLModel, Session, select
from ..db.models.meetings import Meetings
from ..db.models.meeting_rooms import MeetingRooms

class MeetingsLib:
    def __init__(self, db):
        self.engine = db.engine

    def add_meetingroom(self, room_name):
        with Session(self.engine) as session:
            session.add(MeetingRooms(name=room_name))
            session.commit()

    def add_meeting(self, room_id, start, end, name="Meeting"):
        with Session(self.engine) as session:
            session.add(Meetings(name=name,meeting_room_id=room_id,start=start,end=end))
            session.commit()

    def available_meeting_rooms(self, start, end):
        with Session(self.engine) as session:
            if (start == None or start == None):
                return []
            statement = select(MeetingRooms)
            meeting_rooms = session.exec(statement)
            available_rooms = []
            for room in meeting_rooms:
                if self.__room_available(room.id, start, end):
                    available_rooms.append({"name": room.name, "id": f"{room.id}"})
            return available_rooms

    def upcoming_meetings(self, room_id):
        with Session(self.engine) as session:
            statement = select(MeetingRooms).where(MeetingRooms.id == room_id)
            room = session.exec(statement).first()
            statement = select(Meetings).where(Meetings.meeting_room_id == room_id)
            meetings = session.exec(statement)
            formatted_meetings = []
            for meeting in meetings:
                formatted_meetings.append({"id": f"{meeting.id}","start": meeting.start,"end":  meeting.end,"name": meeting.name})
            return {"meetingRoomName":room.name, "meetings": formatted_meetings}

    def drop_meeting(self, meetingId):
        with Session(self.engine) as session:
            statement = select(Meetings).where(Meetings.id == meetingId)
            results = session.exec(statement)
            meeting = results.one()
            session.delete(meeting)
            session.commit()

    def __room_available(self, room_id, start, end):
        with Session(self.engine) as session:
            statement = select(Meetings) \
                .where(Meetings.meeting_room_id == room_id) \
                .where(Meetings.end > start) \
                .where(Meetings.start < end)  # TODO: join table for simplicity
            overlapping_meetings = session.exec(statement)
            for meeting in overlapping_meetings:
                return False
            return True