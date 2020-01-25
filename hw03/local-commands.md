### Facedetector

xhost +

sudo docker run --name face_detector --network hw03 -it --rm --runtime nvidia -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix -v /data/hw3/dockerdata:/root --device=/dev/video1 csancini/hw3

cd ~

python3 facedetector.py

### Local Broker

sudo docker run --name mosquitto --network hw03 -p 1883:1883 -ti --rm -v /data/hw3/dockerdata:/root csancini/hw3-broker sh

/usr/sbin/mosquitto

### Local Forwarder

sudo docker run --name forwarder --network hw03 -dti --rm -v /data/hw3/dockerdata:/root csancini/hw3-broker sh

sudo docker network connect bridge forwarder

sudo docker attach forwarder

cd ~

python3 forwarder.py
