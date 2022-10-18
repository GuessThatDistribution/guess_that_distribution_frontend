FROM python:3.10.5-slim

COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

WORKDIR /app
COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
