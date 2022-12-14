FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/django

COPY ./doc.txt /usr/src/doc.txt
RUN pip install -r /usr/src/doc.txt

COPY . /usr/src/django

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]