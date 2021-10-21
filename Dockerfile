# La base de l'image
FROM python:3.9.6-alpine

# Le dossier de travail
WORKDIR /usr/src/app

# La mise de la distribution Linux + instalation des paquets PSQL
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

# Copie du script qui permet de d'automatiser l'éxecution des migrations
COPY herosite/entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# run entrypoint.sh (dernière ligne)
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]


    



