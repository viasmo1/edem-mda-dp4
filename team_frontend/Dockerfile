# start from base

FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3 &&\
    apt-get install -y python3-pip &&\
    apt install -y libsm6 libxext6 &&\
    apt-get install -y libxrender-dev

RUN apt-get update && \
    apt-get -y install sudo

RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo

USER docker


# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

CMD [ "python3", "./app.py" ]