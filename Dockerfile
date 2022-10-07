FROM python:3.10.7-alpine3.16
MAINTAINER Felipe Colen <felipecolen@gmail.com>

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --update --no-cache \
    bash tzdata build-base postgresql-dev && \
    cp /usr/share/zoneinfo/America/Porto_Velho /etc/localtime && \
    echo "America/Porto_Velho" > /etc/timezone && \
    rm -rf /root/.cache && \
    python -m pip install --upgrade pip setuptools

WORKDIR /app

COPY requirements.txt ./

RUN python -m pip install -r requirements-dev.txt

COPY . .

EXPOSE 8080

ENTRYPOINT ["gunicorn", "tests_no_django.wsgi", "-w", "3", "-b", "0:8080"]
