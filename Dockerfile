FROM python:2.7.11-slim


COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt


EXPOSE 20 21

CMD python ftpd.py
