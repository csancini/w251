### Facedetector

Docker image used in ```dockerfiles/facedetector```
```
xhost +

sudo docker run --name face_detector --network hw03 -it --rm --runtime nvidia -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix -v /data/hw3/dockerdata:/root --device=/dev/video1 csancini/hw3

cd ~
python3 facedetector.py
```

### Local Broker

Docker image used in ```dockerfiles/mosquitto```
```
sudo docker run --name mosquitto --network hw03 -p 1883:1883 -ti --rm -v /data/hw3/dockerdata:/root csancini/hw3-mosquitto sh
/usr/sbin/mosquitto
```

### Local Forwarder

Docker image used in ```dockerfiles/mosquitto```
```
sudo docker run --name forwarder --network hw03 -dti --rm -v /data/hw3/dockerdata:/root csancini/hw3-mosquitto sh
sudo docker network connect bridge forwarder
sudo docker attach forwarder

cd ~
python3 forwarder.py
```

### Remote Broker

Docker image used in ```dockerfiles/mosquitto```
```
sudo docker run --name remote-broker --network hw03 -p 1883:1883 -dti --rm -v /root/dockerdata:/root csancini/hw3-mosquitto sh
sudo docker network connect bridge remote-broker
sudo docker exec -it remote-broker /usr/sbin/mosquitto
```

### Image Processor

Docker image used in ```dockerfiles/image-processor```
```
sudo docker run --name image-processor --network hw03 -ti --rm -v /root/dockerdata:/root -v /mnt/mybucket:/mnt/mybucket csancini/hw3-image-processor sh

cd ~
python3 image-processor.py
```

