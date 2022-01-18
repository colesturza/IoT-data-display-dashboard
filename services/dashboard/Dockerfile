FROM python:3.8

ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app/
ADD . /app/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
