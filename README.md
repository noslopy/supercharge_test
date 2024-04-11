# Test assignment for Supercharge ⚡


# Meeting room booking system
### Stack: Python3+, FastAPI, SQLite

* **GET /meeting-rooms/available**
    * List all the meeting rooms that are available for a given time period.
* **GET /meeting-rooms/{meetingRoomId}/upcoming-meetings**
    * List upcoming meetings for a meeting room.
* **POST /meeting-rooms/{meetingRoomId}/book**
    * A user should be able to book a meeting room for a given timeframe.
* **DELETE /meetings/{meetingId}**
    * Cancel booked event.

# Table of contents

* [Setup](#setup)
    * [Setup pyenv](#setup-pyenv)
    * [Setup pipenv](#setup-pipenv)
* [Testing](#testing)

# Setup
## Setup pyenv

Pyenv handles python versions (kudos to ruby devs)

```bash
pyenv install 3.12.3
pyenv global 3.12.3
```

## Setup pipenv

Pipenv handles local project dependencies

```bash
pip install --user pipenv
```

Add user bin to PATH for pipenv!

## Dependencies

 Install pipenv deps

```bash
pipenv install
```

## Testing

Run service locally

```bash
pipenv run uvicorn main:app --reload
```

Run tests

```bash
pipenv run pytest # -v -s
```