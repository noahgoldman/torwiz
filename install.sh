#Throw everything in here needed to install stuff

sudo apt-get install -y python-libtorrent python-libtorrent-dbg libtorrent-rasterbar-dev libtorrent-rasterbar7 python-pip python-dev mongodb
sudo pip install -r requirements.txt

mongo mongoinstallscript.js
