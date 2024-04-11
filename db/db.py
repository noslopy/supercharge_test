import os
from sqlmodel import SQLModel, create_engine

class DB:
    def __init__(self):
        self.sqlite_file_name = "testdb.sqlite" # read from ENV
        sqlite_url = f"sqlite:///{self.sqlite_file_name}"
        self.engine = create_engine(sqlite_url, echo=True)

    def create_db(self):
        SQLModel.metadata.create_all(self.engine)

    def drop_db(self):
        os.remove(self.sqlite_file_name)