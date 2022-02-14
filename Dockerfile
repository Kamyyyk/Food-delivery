FROM python:3

WORKDIR /portal
COPY requiments.txt /portal/
RUN pip install -r requiments.txt
COPY . /portal/