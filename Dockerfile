FROM ubuntu
COPY requirements.txt .

RUN apt-get update -y \
    && apt-get install -y python3-pip
RUN pip3 install --upgrade -r requirements.txt

RUN mkdir /app
RUN mkdir /app/src

COPY src/model /app/src/model
COPY src/preprocessing /app/src/preprocessing
COPY assets /app/assets
COPY app.py /app/app.py
WORKDIR /app

CMD ["python3","app.py"]
