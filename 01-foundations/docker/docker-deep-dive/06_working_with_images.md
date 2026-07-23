# 06. Working with Images

* An image is a read-only package containing everything needed to run an application
* An Image includes application code, dependencies, a minimal set of OS constructs, and metadata
* Multiple containers can be started from a single image
* Docker creates images by stacking independent layers and representing them as a single unified object

## Intro to images

* Images are built-time constructs, whereas containers are run-time constructs
* The `docker run` command is the most common way to start a container from an image
* Once the container is running, the image and the container are bound, and the image cannot be deleted until the container is stopped and deleted
* Containers are designed to run a single application or microservice. They should only contain application code and dependencies
* It's increasingly common for images to ship without a shell or a package manager, these are called `slim images`

## Pulling Images

* A clean Docker installation has an empty `local repository`, which is a jargon for an area on the local machine where Docker stores images for more convenient access
* `docker images` to inspect the contents of the local repository
* `docker pull <image-name>`: to pull the <image-name> image
* Images can share layers, and Docker is clever enough only to pull the layers it doesn't already have

## Image registries

* The images are stored in centralized places called `registries`
* The most common registry is Docker Hub, but others exist
* Image registries contain one or more image repositories, and image repositories contain one or more images

* `Official repositories` are home to images vetted and curated by Docker and the application vendor. This means they should contain up-to-date high-quality code that is secure, well-documented, and follows good practices
* `Unofficial repositories`: they should always start with the assuptiom that anything from an unofficial repository is unsafe

## Image naming and tagging

* `docker.io / markoen / ddd-book : ch8.1` => ` <registry> / <user/org> <repository> : <image/tag>`
* `docker pull <repository>:<tag>`: to pull a image from an official repository
* If the image tag is not specified after the repository name, Docker assumes the image tagged as latest is wanted
* `docker pull <user/org>/<repository>:<tag>`: to pull an image from a unofficial repository
* `docker pull <registry>/<user/org>/<repository>:<tag>`: to pull an image from a different registry
* Many tags can be given to a single image as needed

## Images and Layers

* Images are collection of loosely connected read-only layers where each layer comprises one or more files
* `docker inspect <image>`:  to get detailed image information 
* `docker history <image> `: shows the build history of an image

### Base Layers

* All docker images start with a base layer
* An image is a combination of all layers stacked in the order they were built
* Layers are stored as independent objects, and the image is just metadata identifying the required layers and explaining how to stack them
* To update files and make other changes to images is needed adding new layers containing the changes

### Sharing image layers

* The 'already exists' message during the `docker pull` execution ocurred because one of the Docker containers already pulled an image that used the exact same layer
* Layers are also shared on the registry side

## Pulling images by digest

* While pulling images using names (tags) is the most common method, it has a problem - tags are arbitrary and mutable. It's possible to tag an image incorrectly or give a new image the same tag as an older one
* Docker uses a content addressabel storage model where every image gets a cryptographic content hash what is usually called as digest. It is impossible for an image change without creating a new digest

### Image hashes and layer hashes

* An image is just a manifest file with some metadata and a list of layers
* Images and layers have their own digests as follows
    * Images digests are a crypto hash of the image's mnifest file
    * Layer digests are a crypto hash of the layer's contents

## Multi-architecture images

* Docker and the registry API adapted and became clever enough to hide images from multiple architectures behind a single tag. A `docker pull` can be done on any architecture and get the correct version of the image
* The Registry API supports two important constructs:
    * Manifest lists: a list of architectures supported by an image tag. Each supported architecture then has its own manifest that lists the layers used to buld it
    * Manifests
* `docker buildx imagetools inspect <image-name>`: to see the different architectures supported behind the <image-name> tag
* `docker manifest inspect <image-name> | grep 'architecture/|os'`: to see the manifest list and manifests for an image

## Vulnerability scanning with Docker Scout

* Lots of tools and plugins exist that scan images for know vulnerabilities
* `docker scout quickview <image-name>`: to get a quickly vulnerabilitiy oveview of an image
* `docker scout cves <image-name>`: to getmore detailed information, including remediation advice

## Deleting images

* `docker rmi`: to delete an image
* Docker will prevent the delete operation if the image is being used by a container or referenced by more than one tag. However this operation can be forced with the '-f' flag
* `docker images -q`: return a list of local image IDs. It can be passed to `docker rmi` to delete all images on the system 

