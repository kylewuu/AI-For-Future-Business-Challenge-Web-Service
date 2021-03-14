FROM ubuntu:16.04

FROM python:3.7
RUN pip install --upgrade pip

EXPOSE 5000

ENV VAR1=10

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt

COPY ./resources/apple_dataset/json/detection_config.json /app/detection_config.json
COPY ./resources/temp_db/data.json /app/data.json
COPY ./resources/temp_db/temp_image.jpg /app/temp_image.jpg
COPY ./resources/apple_dataset/models/detection_model-ex-036--loss-0017.781.h5 /app/detection_model-ex-036--loss-0017.781.h5

RUN apt install libgl1-mesa-glx -y
RUN apt-get install 'ffmpeg'\
    'libsm6'\
    'libxext6' -y

WORKDIR /app

RUN pip install -r requirements.txt


COPY . /app

# ENTRYPOINT [ "python" ]

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]