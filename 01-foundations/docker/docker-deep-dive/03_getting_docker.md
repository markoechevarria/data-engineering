# 03. Getting Docker

## Docker Desktop

* Is a desktop app from Docker Inc
* Support Windows and LInux containers

## Installing Docker Desktop on Windows 10 and 11

* Search the internet for "install docker desktop on windows"
* Download the installer and follow the instructions
* WSL should be installed and enabled

## Installing Docker Desktop in Mac

* Is like Docker Desktop for Windows
* Docker Desktop on Macs installs the daemon and server-side components inside a lightweight Linux VM that seamlessly expose the API to the local MAC environment
* Search the web for "install docker desktop on Mac"
* Complete the installer

## Installing Docker with Multipass

* Multipass is a free tool for creating cloud-style Linux VMs on your Linux, Mac or Windows machine
* Go to `htts://multipass.run/install` and install the right edition for the hardware and OS targeted.
```
multipass launch docker --name node1
multipass shell node1
docker --version
```

## Installing Docker in Linux

```
sudo snap install docker
sudo docker --version
sudo groupadd docker
sudo usermod -aG docker $(whoami)
sudo service docker start
```
