FROM python:2.7
ADD . /src
WORKDIR /src
RUN apt-get update && apt-get install -y python-libtorrent
RUN pip install -r requirements.txt
CMD python client.py
