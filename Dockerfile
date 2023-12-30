FROM python:3.11-slim-bookworm

RUN apt-get update -y
RUN apt-get install gunicorn3 -y

COPY requirements.txt requirements.txt
COPY . /opt/

RUN pip3 install -r requirements.txt
WORKDIR /opt/

CMD ["gunicorn3", "-b", "0.0.0.0:8000", "app:app", "--workers=5"]




