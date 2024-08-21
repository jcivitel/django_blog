FROM python:3.12-alpine AS builder

RUN apk add --no-cache libgcc mariadb-connector-c pkgconf mariadb-dev \
    postgresql-dev linux-headers

WORKDIR /opt/django_blog/
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /opt/django_blog/

FROM builder AS install
WORKDIR /opt/django_blog
ENV VIRTUAL_ENV=/opt/django_blog/venv

RUN python -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --no-cache-dir -r /opt/django_blog/requirements.txt

FROM install

EXPOSE 8000
CMD ["sh", "entry.sh"]
