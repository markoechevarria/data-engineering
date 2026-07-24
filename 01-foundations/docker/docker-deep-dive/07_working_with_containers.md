# 07. Working with containers

* Containers are run-time instances of images and one or more of them can be started from a single image
* Containers can be started, stopped and deleted just like the VMs
* Containers are smaller, faster and more portable then VMs
* Containers are designed to be stateless and ephemeral
* Containers are designed to be inmutable. This means they shouldn't be changed after they have been deployed - if a container fails, it should be replaced with a new one instead of connecting to it and making a live fix
* Containers should only run a single process and they are used to build microservices appo

## Containers vs VMs

* VMs virtualize hardware
* Containers virtualize operating systems
* In the VM model, a server is power on and a hypervisor boots. When the hypervisor boots, it claims all hardware resources such as CPU, RAM, storage, and network adapters. To deploy an app, we ask the hypervisor to create a virtual machine
* In the container model, a server is power on and an OS boots and claims all hardware resources. To deploy an app, we ask docker to create a container
* Hypervisors perform hardware virtualization where they divide hardware resources into virtual versions and package them as VMs. Containers runtimes perform OS virtualization where they divide OS resources into virtual versions and package them as containers

### The VM tax

* Containers are smaller than VMs because they only contain application code and a minimal set of OS-related constructs such as essential filesystem objects
* VMs need a full OS, meaning they are usually hundreds or thousands of megabytes
* Containers use the host's OS which is alread booted. VMs need to go through a full OS bootstrapping process before starting the app
* Most container engines and platforms implement sensible defaults for security-related technologies such as SELinux, AppArmor, seccomp, capabilities, and more

## Images and Containers

* An image is read-only, but each container started from it is read-write. Docker accomplishes this by creating a thin read-write layer for each container and placing it on top of the shared container
* Each container has itw own thin R/W layer but shares the same image
* The containers can see and access the files and apps in their image through their own R/W layer, and if they make changes, these get written to their R/W
* When a container is stopped, Docker keeps the R/W layer and restores it when the container is restarted
* When a container is deleted, Docker delets its R/W layer

## Check docker is running

* `docker version`: to check Docker is running

## Starting a container

* The `docker run` command is the simplest and most common way to start a new container
* `docker run <image-name>`: tells docker to run a new container
    * `-d` flag tells Docker to run it in the background as a daemon process and detached from the local terminal
    * `--name` flag tells docker to name this container 'webserver'
    * `-p <host-container>:<port-container>` flag maps port <host-container> on the local system to port <port-container> inside the container
    * `<image-name>`: tells docker which iamge to use to start the container
* the Docker client converted this command into an API request and posted it to the Docker API exposed by the Docker daemon
    * The Docker Daemon searched its local image repository for a copy of the image required. If it didn't find one, so it searched Docker Hub
    * Once it had a local copy of the image, the daemon made a request to containerd asking for a new container
    * containerd instructed runc to create the container and start the app

## How containers start apps

* There are three ways to tell Docker how to start an app in a container
    * An `Entrypoint` instruction in the image
    * A `Cmd` instruction in the image
    * A CLI argument
* `Entrypoint` and `Cmd` instructions are optional image metadata where the command wanted Docker to run to start the default app is stored
* `Entrypoint` instructions cannot be overriden on the CLI, anything passed in via the CLI will be appended to the Entrypoint instruction as an argument
* `Cmd` instructions are overriden by CLI arguments
* If an image doesn't have either a `Cmd` or `Entrypoint`, an argument is needed to be passed on the CLI
* `docker run <arguments> <image-name> <command>`: command is optional, it is not needed if the image has a Cmd or Entrypoint instruction. If a <command> is specified it will override a Cmd instruction but will be appended to an Entrypoint instruction
* The `--rm` flag cleans up the exited container so it is not necessary to delete it manually

## Connecting to a running container

* The `docker exec` command is used to execute command in running containers
    * Interactive execution sessions: connect the terminal to a shell process in the container and behave like remote SSH sessions. It is actived using the `-it` flag
    * Remote execution mode: lets command to be sent to a running container and prints the output to the local terminal

## Inspecting container processes

* Most containers only run a single process. This is the container's main app process and is always PID 1
* If the container's main process (PID 1) is killed, the container is also killed. Because containers only run while their main process is executing - when that process is no longer running, there's no reason for the container to run

## The docker inspect command

* `docker inspect <container>` retrieves full details of the running container

## Writing data to a container

* In the real world, live containers shouldn't be changed. Any time a live container is needed to be changed, a new container should be created and be tested with the required changes and then replace the existing containers with the new one

## Stopping, restarting, and deleting a container

* `docker stop <container>` to gracefully stop a container
* `docker ps` to show the running containers
* `docker ps -a`: to show all containers, including stopped ones
* `docker restart <container>`: to restart a container
* `docker rm <container>` to delete the container
* `docker rm <container> -f` to delete the container without the usual 10-second grace period

## Debugging slim images and containers with Docker Debug

* Docker Debug is only included as part of Docker Desktop and requires a Pro, Team and Business subsctiption
* It's a widely accepted good practice to deploy Slim images only contain app code and dependencies. This means no shell or debugging tools
* Docker Debug allows to get shell access to images and containers that don't include a shell
* Docker Debug works by attaching a shell to a container and mounting a toolbox loaded with debugging tools

## Self-healing containers with restart policies

* Container restart policies are a simple form of self-healing that allows the local Docker Engine to automatically restart failed containers
    * `No`: Prevents the container from restarting automatically under any circumstances, even if it crashes or fails.
    * `On-failure`: Restarts the container only if it exits with a non-zero error code, applying an optional back-off delay.
    * `Always`: Forces the container to restart regardless of the exit status, even after manual daemon restarts or explicit stops.
    * `Unless-stopped`: Triggers automatic restarts for any exit status unless the user explicitly stops the container beforehand.

* Non-zero exit codes indicate a failure ocurred. Zero exit codes indicate teh container exited and normally without an error
* The policy is set up using the `--restart <policy>` flag

## Commands

• `docker run <image>` is the command to start new containers. You give it the name of an image and it starts a container from it. 
• `Ctrl-PQ` is how you detach from a container without killing the process you’re attached to. 
• `docker ps` lists all running containers, and you can add the -a flag to also see containers in the stopped (Exited) state.
• `docker exec` allows you to run commands inside containers.
• `docker stop` stops a running container and puts it in the Exited (137) state. It issues a SIGTERM to the container’s PID 1 process and allows the container 10 seconds to gracefully quit. If the process hasn’t cleaned up and stopped within 10 seconds, it sends a SIGKILL to force the container to terminate immediately.
• `docker restart` restarts a stopped container.
• `docker rm` deletes a stopped container. You can add the -f flag to delete the container without having to stop it first.
• `docker inspect` shows you detailed configuration and run-time information about a container.
• `docker debug` attaches a debug shell to a container or image and lets you run commands that aren’t available inside the container or image. It requires a Pro, Team, or Business Docker subscription.
