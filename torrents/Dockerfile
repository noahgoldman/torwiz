FROM ubuntu:trusty
WORKDIR /src
RUN apt-get update 
RUN apt-get install -y python-libtorrent python-libtorrent-dbg libtorrent-rasterbar-dev libtorrent-rasterbar7 python-pip python-dev
RUN pip install -r requirements.txt
CMD python client.py
