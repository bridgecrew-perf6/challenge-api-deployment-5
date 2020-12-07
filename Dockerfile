FROM python
COPY requirements.txt .
RUN pip install --upgrade -r requirements.txt


RUN mkdir /app
RUN mkdir /app/src


COPY src/model /app/src/model
COPY src/preprocessing /app/src/preprocessing
COPY app.py /app/app.py

WORKDIR /app

CMD ["python","app.py"]