# 04. The Big picture

* The Ops perspective: focuses in starting, stopping, deleting containers and executing commands inside them
* The Devs perspective: focuses more on the application side of things and runs through taking application source code, building it into a container image, and running it as a container.

## The Ops perspective

* A typical docker installation installs the client and the engine on the same machine and configures them to talk to each other.
* `docker version`: to ensure both the client and the engine are installed and running.

### Donwload an Image

* Images are objects that contain everything an app needs to run ( OS, filesystem, the application and all dependencies).
* `docker images`: list images in the machine
* `docker pull image-name`: copy new images onto the Docker host, it is called pulling

### Start a container from the image

* `docker run image-name`: to start a new container from a image
    * `--name container-name`: told Docker to call this container with a specific alias name.
    * `-d`: told Docker to start the container in the backgound ( detached mode).
    * `-p host-port:container-port`: told Docker to map port `container-port` on the container to `host-port` on the Docker host
* `docker ps`: list the running containers
    * It list the Container ID, Image name, Command to start the app inside the container, the time since the container was created, the status, the mapping ports, and the name of the app.

### Execute a command inside the container

* `docker exec -it container-name bash-command`: attach the shell fo a new Bash process inside the container
* `exit`: to terminate the bash process and connect the shell back to the local terminal

### Delete the container

* `docker stop container-name`: Stop the container
* `docker rm container-name`: Kill the container

## The Devs perspective

### Inspect the app's Dockerfile

* The Dockerfile is a plain-text document that tells Docker how to build the app and dependencies into an image.

### Containerize the app

* `docker build .`: to create a new image based on the insructions in the Dockerfile located in the current directory.
    `-t container-name:version`: it names the image as `container-name` and assign the version `version`

### Run the app as a container

* `docker run image-name`: start a container
    * `-d`: run in detached mode
    * `--name container-name`: container name
    * `--publish host-port:container-port`: told Docker to map port `container-port` on the container to `host-port` on the Docker host

### Clean Up

* `docker rm name-container -f`: terminate the container and delete the image