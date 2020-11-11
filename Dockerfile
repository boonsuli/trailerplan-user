FROM python:3.8.6-slim-buster
MAINTAINER "Boon SUI <boonsuli@gmail.com>"
WORKDIR /app

# copy the dependencies file
COPY ./requirements.txt /app/requirements.txt

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory
COPY src /app

# set env variable
ENV FLASK_ENV = "docker"

# run server
CMD [ "python", "./user/UserModule.py" ]
