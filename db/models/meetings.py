from sqlmodel import Field, SQLModel

class Meetings(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    meeting_room_id: int
    start: int
    end: int