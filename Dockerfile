FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04

LABEL maintainer "amajidsinar@gmail.com"

WORKDIR /App

RUN apt update &&\
    apt install -y python3 python3-pip wget htop vim &&\
    apt install -y libsm6 libxext6 libxrender-dev git


RUN \ 
    git clone https://github.com/amajidsinar/twtgen &&\
    git clone https://github.com/attardi/wikiextractor.git

ENV LANG C.UTF-8

RUN \
    cd twtgen &&\
    pip3 install -r requirements.txt &&\
    pytest tests/ -v
    
    
