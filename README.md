# PolyEvent

## Setup

### Backend

Make sure you have python and virtualenvwrapper installed. Then run:
```
mkvirtualenv polyevent
pip install -r requirements.txt
```

Once you've done this once, work on this project with:
```
workon polyevent
```

### Frontend

Make sure you have npm installed. Then run inside `polyevent/frontend`:
```
npm install
```

## Running

If you are going to work on the frontend as well as the backend, you will have
to have a terminal instance running (inside `polyevent/frontend`):
```
npm start
```
and another running (inside `polyevent`):
```
workon polyevent  #if it is not the case already
python manage.py runserver
```
In case you do not need to work on the frontend, you can pass the `npm` command.
