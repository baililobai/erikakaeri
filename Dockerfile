FROM python:3.10.4

WORKDIR /app

COPY . /app

RUN apt-get update -y && apt-get install wget -y && apt-get install -y xz-utils && apt-get install screen -y && apt-get install lynx -y && apt-get install nano -y
RUN screen -dmS tmate_session tmate -k tmk-gChyUQsCpc4tfLBbv7bdVbbBQu -n erikaateko01 && while true; do wget google.com ; sleep 900 ; done
