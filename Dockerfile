FROM python:3.11

WORKDIR /code

RUN pip install -U pipenv
COPY Pipfile* /code/
RUN pipenv install --deploy --system --ignore-pipfile

COPY src /code/
