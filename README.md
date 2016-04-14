# polyevent

## Setup

Make sure you have python and virtualenvwrapper installed. Then run:
```
mkvirtualenv polyevent
pip install -r requirements.txt
```

Once you've done this once, work on this project with:
```
workon polyevent
```
To work on the frontend side of things, install `npm`, then install `ionic` with:
```
npm install -g cordova ionic
```
## Running
In the `polyevent` directory, you can run the django backend with:
```
python manage.py migrate
python manage.py runserver
```
It will then be available at [localhost:8000]().

To run the frontend app, you should go run the following command in the `frontend` directory:
```
ionic serve
```
The app will then open in you browser, at [localhost:8100]().
