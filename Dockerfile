FROM alpine:3.20.2


RUN apk  add --no-cache python3-dev \
    && pip3 install --upgrade pip

FROM python:3.8

ADD . /code
    
WORKDIR /code
    
RUN pip install -r requirements.txt
    
CMD python index.py