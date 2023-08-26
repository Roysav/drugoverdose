FROM python

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY ./drugoverdose ./drugoverdose

WORKDIR /drugoverdose

ARG POSTGRES_HOST
ARG POSTGRES_PORT
ARG POSTGRES_USER
ARG POSTGRES_PASSWORD


EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

