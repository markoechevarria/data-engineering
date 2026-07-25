# 08. Containerizing an app

* Docker aims to make it easy to build, share, and run applications
* Containerization process:
    * Write an application and create a list of dependencies
    * Create a Dockerfile that tells Docker how to build and run the app
    * Build the app into an image
    * Push the image to a registry (optional)
    * Run a container from the image

## Containerize a single-container app

### 1. Get the application code

* It can be downloaded from Github
* The directory where it is is the `build context` because it contains the application source code and the files listing dependencies

### 2. Create a Dockerfile

```
ARG NODE_VERSION=20.8.0             # Set the node version
FROM node:${NODE_VERSION}-alpine    # tell Docker to pull the exact image and use it as the base for the new image
ENV NODE_ENV production             # tells Node to un in production mode
WORKDIR /usr/src/app                # sets the working directory for the remaining steps
RUN --mount=type=bind,source=package.json,target=pakcage.json \
    --mount=type=bind,source=package-lock.json,target=package-lock.json \
    --mount=type=cache,target=/root/.npm \
    npm ci --omit=dev               # bind mounts the dependency file
USER node                           # ensures Node.js runs the app as a non-root user
COPY . .                            # copies the application's source code from the build context into the WORKDIR directory inside the image
EXPOSE 8080                         # docuemnts the application's network port
CMD node app.js                     # the command Docker will execute whenever it starts a container from the image
```

### 3. Containerize the app

* `docker build -t <image-name> .`: to buld a new image called <image-name>. The trailing period (.) tells docker to use the current working directory as the build context
* `docker inspect <image-name>`: to verify the image and see the settings from Dockerfile

### 4. Push the image to Docker Hub (optional)

* `docker login`: log in to Docker Hub
* `docker tag <current-tag> <new-tag>`: to re-tag the image to include an Docker ID
* `docker push <tag>`: to push the image to Docker Hub
* `docker.io / markoen / ddd-book : ch8.node` => `default registry / repository / image-tag`

### 5. Run the app

* `docker run -d --name <container-name> -p <host-port>:<container-port> <image-name>`: runs the container and assign it the name <container-name>, maps port <host-port> on the Docker host to port <container-port> inside the container

### Looking a bit closer

* The `docker build` comamnds parses the Dockerifle one line at a time, starting from the top
* Comments can be inserted by starting a line with the `#` character
* All non-comments lines are called instructions or steps and take the format <INSTRUCTION> <arguments>. Instructions names are not case-sensitive, but it's common to write them in UPPERCASE to amke the file easier to read
* Instructions that add content (FROM, RUN, COPY and WORKDIR), such as files and programs, create new layers
* Instructions that don't add content (EXPOSE, ENV, CMD, and ENTRYPOINT) don't add layers and only crate metadata
* It's generally considered a good practice to use Docker Official Images and Verified Publisher images as the base layers for new images

## Moving to production with multi-stage builds

* Container images should only contain the stuff needed to run the applications in production
* Multi-stage builds use a single Dockerfile with multiple FROM instructions - each FROM instruction represents a new build stage. This allows to have a stage where the heavy lifting of building the app inside a large image with compilers and other build tools is done, but another stage where the compiled app is copied into a slim image for production

```

FROM golang:1.23.4-alpine AS base
WORKDIR /src
COPY go.mod go.sum .
RUN go mod download
COPY . .

FROM base AS build-client
RUN go build -o /bin/client ./cmd/client

FROM base AS build-server
RUN go build -o /bin/server ./cmd/server

FROM scratch AS prod
COPY --from=build-client /bin/client /bin/
COPY --from=build-server /bin/server /bin/
ENTRYPOINT [ "/bin/server" ]

```

* Stage 0 is called base and builds an image with compilation tools, etc
* Stage 1 is called build-client and compiles the client executable
* Stage 2 is called build-server and compiles the server executable
* Stage 3 is called prod and copies the client and server executables into a slim image
* Each stage outputs an intermediate iamge that later stages can use. However, Docker deletes them when the final stage completes
* Docker will always attempt to run stages in parallel, but it can only when no dependencies exits

## Buildx, BuildKit, drivers and Build Cloud

* Docker's build system has a client and server:
    * Client: Buildx
    * Server: BuildKit
* Buildx can be configured to talk to multiple BuildKit instances, and each instance of BuildKit is called a builder. Builders can run on a local machine, in a cloud or dataenter, or Docker's Build Cloud
* When a `docker build` command is run, buildx interprets the command and sends the build request to the selected builder. This includes the Dockerfile, command line arguments, caching options, export options and the build context (app and dependency). The builder performs the build and exports the image. The Buildx client monitors the build and reports on progress

## Multi-architecture builds

* The `docker build` command can be useed to build images for multiple platforms and CPU architectures, including ones different from the local machine
* `docker buildx build --builder=container --platform=linux/amd64,linux/arm64 -t markoen/ddd-book:ch8.1 --push .`: to build an app into AMD and ARM images and export them to Docker Hub

## A few good practices

### Leverage the build cache

* BuildKit uses a cache to speed up builds
* Cache can be shared on Docker Build cloud
* For each build, the builder iterates through the Dockerfile one line at a time, starting from the top. For each line, it checks if it already has the layer in its cache
* `docker build --no-cache` to ignore the cache 

### Only install essential packages

* Some packages managers provide a way to only download and install essential packages instead of the entire internet

## The commands

* `docker build` containerized applications. it reads a Dockerfile and follows the instructions to create an OCI image
* The Dockerfile `FROM` instructio specifies the base image. It’s usually the first instruction in a Dockerfile, and it’s considered a good practice to build from Docker Official Images or images from Verified Publishers
* The Dockerfile RUN instruction lets you run commands during a build. It’s commonly used to update packages and install dependencies. Every RUN instruction creates a new image layer
* The Dockerfile COPY instruction adds files to images, and you’ll regularly use it to copy your application code into a new image. Every COPY instruction creates an image layer
* The Dockerfile EXPOSE instruction documents an application’s network port
* The Dockerfile ENTRYPOINT and CMD instructions tell Docker how to run the app when starting a new container
* Some other Dockerfile instructions include LABEL, ENV, ONBUILD, HEALTHCHECK and more
