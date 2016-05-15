FROM python:3
MAINTAINER david.michael.tucker@gmail.com

RUN pip install --upgrade pip
RUN pip install pep8 pylint

WORKDIR /src
COPY . .
RUN pep8 setup.py
RUN pylint setup.py
RUN pep8 keysmith
RUN pylint keysmith
RUN rm -rf dist
RUN python setup.py sdist
RUN pip install dist/*
ENTRYPOINT ["keysmith"]
