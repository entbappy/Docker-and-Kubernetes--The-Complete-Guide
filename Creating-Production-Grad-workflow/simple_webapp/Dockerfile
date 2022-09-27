FROM python:3.7

WORKDIR /usr/app
COPY . /usr/app

RUN pip install -r requirements.txt
CMD gunicorn --workers=1 --bind 0.0.0.0:5000 app:app
