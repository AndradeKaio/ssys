FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /ssys
WORKDIR /ssys
COPY requirements.txt /ssys/
RUN pip install -r requirements.txt
COPY . /ssys/
COPY ./startup.sh .


RUN ["chmod", "+x", "startup.sh"]

ENTRYPOINT ["sh", "startup.sh"]