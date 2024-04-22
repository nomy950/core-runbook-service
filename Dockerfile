FROM tiangolo/uwsgi-nginx-flask:python3.10
ENV UWSGI_INI /app/uwsgi.ini
COPY ./app/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY ./app /app