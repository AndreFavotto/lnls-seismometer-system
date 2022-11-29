FROM public.ecr.aws/debian/debian:10-slim

ENV TZ="America/Sao_Paulo"

USER root
#Basic tools
RUN set -e; set -x;\
    apt update -y;\
    apt install -y\
    build-essential\
    libreadline-dev\
    wget\
    swig\
    python3\
    python3-pip

# EPICS environment variables
ENV EPICS_VERSION 3.16.2
ENV EPICS_HOST_ARCH linux-x86_64
ENV EPICS_BASE /opt/epics-${EPICS_VERSION}/base
ENV PATH ${EPICS_BASE}/bin/${EPICS_HOST_ARCH}:${PATH}

# EPICS install
RUN set -e; set -x;\
    mkdir -p /opt/epics-${EPICS_VERSION};\
    cd /opt/epics-${EPICS_VERSION};\
    wget https://epics.anl.gov/download/base/base-${EPICS_VERSION}.tar.gz;\
    tar -zxf base-${EPICS_VERSION}.tar.gz;\
    rm -v base-${EPICS_VERSION}.tar.gz;\
    mv base-${EPICS_VERSION} base;\
    cd base;\
    make -j$(nproc)

WORKDIR /home/ioc

COPY . .

RUN pip3 install --upgrade setuptools;\
    pip3 install pcaspy;\
    chmod 777 /home/ioc
    #Chmod was necessary to allow reftek application to write files.

ARG DAS_PATH
ARG PV_PREFIX
ARG DAS_UNIT_ID
ARG DAS_DATA_STREAM

ENV DAS_PATH ${DAS_PATH}
ENV PV_PREFIX ${PV_PREFIX}
ENV DAS_UNIT_ID ${DAS_UNIT_ID}
ENV DAS_DATA_STREAM ${DAS_DATA_STREAM}

CMD python3 ./scripts/main.py -p ${DAS_PATH} -P ${PV_PREFIX} -i ${DAS_UNIT_ID} -s ${DAS_DATA_STREAM} 