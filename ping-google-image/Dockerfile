FROM ubuntu:latest

RUN apt-get update && apt-get install -y iputils-ping && apt-get clean

CMD ["ping", "-w", "5", "google.com"]