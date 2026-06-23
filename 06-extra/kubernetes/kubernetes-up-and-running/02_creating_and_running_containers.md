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
* The `Dockerfile` is a récipe for how to build the container image, while `.dockerignore` defines the set of files that should be ignored when copying files into the image


