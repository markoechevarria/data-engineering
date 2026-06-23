# 2. Creating and Running containers

* Kubernetes is a platform for creating, deploying and managing distributed applications
* Application programs are tiplically comprised of a language runtime, libraries and source code
* The traditional methods of running multiple programs on a single machine require that all of these programs share the same versions of shared libraries on the system
* Docker, the default tool most people use for containers, makes it easy to package an executable and push it to remote registry where it can later be pulled by others
* Container images bundle a program and its dependencies into a single artifact under a root filesystem

## Container images

* A container image is a binary package that encapsulates all of the files necessary to run a program inside of an OS container

### The Docker Image format

* The most popular and widespread container image format is the Docker image format, which was developed by the Docker open  source Project for packaging, distributing, and running containers using the `docker` command
* The Docker image format continues to be the facto standard, and is made up of a series of filesystem layers. Each layer adds, removes, or modifies files from the preceding layer in the filesystem
* Container images are typically combined with a container configuration, which provides instructions on how to set up the container environment and execute an application entry point
* Containers fall into two main categories:
* System containers: seek to mimic vms and often run a full boot process
* Application containers: They commonly run a single program

## Building applications with Docker

* In general, container orchestration systems like Kubernetes, are focused on building and deploying distributed systems made up of application containers

### Dockerfiles

* A Dockerfile can be used to automate the creation of a Docker container image
* The `Dockerfile` is a recipe for how to build the container image, while `.dockerignore` defines the set of files that should be ignored when copying files into the image
* `docker build -t app-name .`: to créate the app-name Docker image
* `docker run --rm -p 3000:3000 app-name`: to run an image

### Optmizing Image Sizes

* Files that are removed by subsequent layers in the system are actually still present in the images; they're just inaccesibles
* Every time a layer is changed, it changes every layer that comes after it. It means that they need to be rebuilt, repushed and repulled to deploy the image to development

### Image Security

* Don't build containers with passwords baked in - and this includes not just in the final layer, but any layers in the image
* Deleting a file in one layer doesn't delete that file from preceding layers. Is still takes up space, and it can be accessed by anyone with the right tools
* Secret and images should never be mixed
* Because container images are narrowly focused on running individual applications, a best practice for container images is to minimize the files withing the container image

## Multistage Image Builds

* Compiling code as part of the image leaves all of the unnecesary development tools lying around inside of our image and slowing down the deployments
* Docker introduced `multistage builds`, with them, rather than producing a single image, a Docker file can actually produce multiple image. Each image is considered a stage. Artifacts can be copied from preceding stages to the current stage

## Storing Images in a Remote Registry

* The standard within the Docker community is to store Docker images in a remote registry
* Public registries allow anyone to download images stored in the registry
* Private registries require authentication to download images
* To push an image, we need to authenticate to the registry using the `docker login` command
* Once we are logged in, we can tag our image by prepending the target Docker registry. We can also append another identifier that is usually used fo the versión of variant of that image, separated by a colon `docker tag image-name docker-registrie:version`, then we can push the image `docker push docker-registrie:version`

## The container Runtime Interface

* Kubernetes provides an API for describing an application deployment, but relies on a container runtime to set up an application container using the container-specific APIs native to the target OS

### Running Containers with Docker

* `Docker run -d --name alias-container -p host-port:container-port name-image`: to deploy a container using the `name-image` image

### Limiting Resource Usage

* Docker provides the ability to limit the amount of resources used by applications
* One of the benefits to running applications within a container is the ability to restrict resource utilization. This allows multiple applications to coexist on the same hardware and ensures fair usage
* `docker run -d ... --memory 200m --memory-swap 1G ...`: to limit to 200MB and 1GB of swap space

### Limiting CPU resources

* `docker run -d … --cpe-shares 1024 ...`: Restrict CPU utilization

## Cleanup

* `docker rmi <tag-name` and `docker rmi <image-id>`: delete an image
* Unless we explicitly delete an image it will live on our system forever, even if we build a new image with an identical name
* `docker images`: to see the images currently on our machine
* `docker system prune`: for general cleanup. It Will remove all stopped containers, all untagged images, and all unused image layers cached as part of the build process
