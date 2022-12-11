FROM python:3.9.16-slim-buster
RUN apt-get update
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD [ "python", "app.py"]
