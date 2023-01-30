FROM python:3.10-slim

ARG PROJECT_NAME=app

ENV FLASK_ENV=development

COPY requirements.txt /
RUN apt update &&  apt install iputils-ping net-tools -y
RUN pip install -U pip && pip install -r requirements.txt

COPY ./${PROJECT_NAME} /app/
COPY run.py /
COPY setup.py /

EXPOSE 5000

WORKDIR /
CMD gunicorn -c setup.py run:app