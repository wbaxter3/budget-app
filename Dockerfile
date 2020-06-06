FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /budgeter
WORKDIR /budgeter
ADD . /budgeter/
RUN pip3 install -r requirements.txt
