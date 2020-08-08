# FROM python:3.7
FROM python:3.8.3-alpine

# set work directory
RUN mkdir /code
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

# do something?
# COPY wait.sh /wait.sh
# RUN chmod +x /wait.sh

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev linux-headers

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt

# copy entrypoint file
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# copy project
COPY . /code/

ENTRYPOINT ["/entrypoint.sh"]

# CMD /wait.sh db 5432 \
#   && python skedge/manage.py collectstatic --noinput \
#   && python skedge/manage.py makemigrations booking \
#   && python skedge/manage.py migrate booking \
#   && python skedge/manage.py showmigrations booking \
# #  && python skedge/manage.py loaddata data.json \
#   && /usr/local/bin/uwsgi --ini /code/skedge/skedge/uwsgi.ini
