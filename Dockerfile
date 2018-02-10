FROM python:3
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y \
    cron

RUN mkdir /code

WORKDIR /code
ADD requirements.txt /code/
ADD . /code/
RUN chmod 777 /code/start.sh
CMD ["/code/start.sh"]