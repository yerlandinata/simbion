FROM python:3.4-slim

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt

ADD . /app

CMD if [ "$PORT" = "" ]; then gunicorn -b 0.0.0.0:8000 simbion.wsgi; else gunicorn -b 0.0.0.0:$PORT simbion.wsgi; fi
