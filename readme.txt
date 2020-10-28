before running python3 kali_install.py as root

do the following as root if tools missing however last I check they screwup the image:

apt-key adv --keyserver pool.sks-keyservers.net --recv-keys ED444FF07D8D0BF6
copy deb http://http.kali.org/kali kali-rolling main non-free contrib to /etc/apt/sources.list
apt-get update && apt-cache search kali-linux-all
