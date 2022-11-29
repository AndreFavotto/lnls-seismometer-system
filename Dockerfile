FROM public.ecr.aws/debian/debian:10-slim

ENV TZ="America/Sao_Paulo"
USER root

RUN set -e; set -x;\
    apt update -y;\
    apt install -y\
    build-essential\
    apt-utils\
    libreadline-dev\
    gettext-base\
    procps\
    sudo

# ---------------------------- Reftek system ---------------------------#

RUN useradd -ms /bin/bash reftek; \
    adduser reftek sudo;\
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER reftek
WORKDIR /home/reftek/
COPY . .
WORKDIR /home/reftek/reftek-system-files/

ARG DAS_IP
ARG SERVER_IP
ARG DAS_UNIT_ID

ENV DAS_IP ${DAS_IP}
ENV SERVER_IP ${SERVER_IP}
ENV DAS_UNIT_ID ${DAS_UNIT_ID}

RUN sudo chown reftek ./**;\
    sudo cp ./rtcc.ini ./rtccaux.ini;\
    envsubst < ./rtccaux.ini > ./rtcc.ini;\
    sudo rm -rf ./rtccaux.ini;\ 
    sudo cp ./rtpd.ini ./rtpdaux.ini;\
    envsubst < ./rtpdaux.ini > ./rtpd.ini;\
    sudo rm -rf ./rtpdaux.ini;\ 
    sudo ./install

ENV PATH ${PATH}:/home/reftek/bin

WORKDIR /home/reftek/bin

RUN arccreate archive "Online Archive"

CMD ./rtp start && ./rtcc >/dev/null