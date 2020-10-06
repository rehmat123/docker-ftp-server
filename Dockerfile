FROM python:2.7.11-slim


COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

RUN mkdir /files
RUN mkdir /files/nobody
RUN mkdir /files/user

EXPOSE 20 21

CMD python app.py