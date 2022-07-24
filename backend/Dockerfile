FROM nginx/unit:1.25.0-python3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /usr/src/constricon

WORKDIR /usr/src/constricon

COPY requirements.txt /usr/src/constricon/

RUN apt update && apt install -y python3-pip                                  \
    && pip3 install -r requirements.txt                                       \
    && apt remove -y python3-pip                                              \
    && apt autoremove --purge -y                                              \
    && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/*.list

COPY . /usr/src/constricon/

RUN python manage.py collectstatic --noinput

EXPOSE 80

RUN chmod +x /usr/src/constricon/entrypoint.sh
