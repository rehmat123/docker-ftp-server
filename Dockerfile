<<<<<<< HEAD
FROM python:2.7.11-slim


COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt


EXPOSE 20 21

CMD python ftpd.py
=======
FROM python:2.7.11-slim


COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

RUN mkdir /files
RUN mkdir /files/nobody
RUN mkdir /files/user

EXPOSE 20 21

CMD python app.py
>>>>>>> 842ef57b977d6cc192cdbd8d572b6216c277d36d
