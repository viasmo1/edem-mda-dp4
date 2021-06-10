# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /ingestion

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .

RUN mkdir images

# command to run on container start
CMD [ "python3", "./ingestion.py"]