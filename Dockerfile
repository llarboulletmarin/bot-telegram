FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y python3.12 python3-pip python3-wheel build-essential && \
	apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . /app
WORKDIR /app

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]