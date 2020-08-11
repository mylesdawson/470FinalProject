FROM python:3.7
WORKDIR /code
ENV PYTHONUNBUFFERED=1
COPY backend/wait.sh /wait.sh
RUN chmod +x /wait.sh
COPY backend/requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
ADD ./ /code
CMD /wait.sh db 5432 \
  && python backend/skedge/manage.py collectstatic --noinput \
  && python backend/skedge/manage.py makemigrations booking \
  && python backend/skedge/manage.py migrate booking \
  && python backend/skedge/manage.py migrate authtoken \
  && python backend/skedge/manage.py showmigrations booking \
  && echo "from django.contrib.auth.models import User; user = User.objects.create_user('customer1', password='secret', last_login='2020-08-09'); user.save()" | python backend/skedge/manage.py shell \
  && echo "from django.contrib.auth.models import User; user = User.objects.create_user('business1', password='secret', last_login='2020-08-09'); user.save()" | python backend/skedge/manage.py shell \
  && echo "from django.contrib.auth.models import User; user = User.objects.create_user('business2', password='secret', last_login='2020-08-09'); user.save()" | python backend/skedge/manage.py shell \
  && echo "from django.contrib.auth.models import User; user = User.objects.create_user('business3', password='secret', last_login='2020-08-09'); user.save()" | python backend/skedge/manage.py shell \
  && echo "from django.contrib.auth.models import User; user = User.objects.create_user('business4', password='secret', last_login='2020-08-09'); user.save()" | python backend/skedge/manage.py shell \
  && echo "from django.contrib.auth.models import User; user = User.objects.create_user('business5', password='secret', last_login='2020-08-09'); user.save()" | python backend/skedge/manage.py shell \
  && echo "from django.contrib.auth.models import User; user = User.objects.create_user('business6', password='secret', last_login='2020-08-09'); user.save()" | python backend/skedge/manage.py shell \
  && echo "from django.contrib.auth.models import User; user = User.objects.create_user('customer2', password='secret', last_login='2020-08-09'); user.save()" | python backend/skedge/manage.py shell \
  && python backend/skedge/manage.py loaddata backend/data.json \
  && /usr/local/bin/uwsgi --ini /code/backend/skedge/skedge/uwsgi.ini
