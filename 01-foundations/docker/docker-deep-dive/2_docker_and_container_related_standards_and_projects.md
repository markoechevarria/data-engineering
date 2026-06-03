# 02. Docker and container-related standards and projects

## Docker

* Docker is the heart of the container ecosystem.

### The Docker Plattform

### Docker, Inc

* Is a technology company based out of Palo Alto and founded by French-born American developer and enterpreneur Solomon Hykes.
* The word Docker is a British expression short for dock worker referring to someone who loads and unloads cargo from ships.

### The Docker Technology

* The docker platform makes it easy to build, share and run containers.
* There are two major parts of the Docker platform.
    * The CLI (client): Is the familiar docker command-line tool for deploying and managing containers.
    * The engine (server): Comprises all the server-side components that run and manage containers
* The client and engine can be on the same host or connected over the network.

## Container-related standards and projects

* Several important standards and governance bodies influence container development and the container ecosystem.

### The Open Container Initiative (OCI)

* Is a governance council responsible for low-level container-related standards.
* It operates under the umbrella of the Linux Foundation and was founded in the early days of the container ecosystem.

* When the size and properties of rail tracks were standarized, it gave enterpreneurs
* Docker has changed a lot since the formation of the OCI, and all modern versions of Docker implement all three OCI spcecs.
    * The Docker bulider (BuildKit) creates OCI compliant-images.
    * Docker uses an OCI-compliant runtime to create OCI-compliant compilers.
    * Docker Hub implements the OCI distribution spec and is an OCI-compliant registry.

### The Cloud Native Computing Foundation (CNCF)

* It was founded in 2015 with the goal of "...advancing container technologies ... and making cloud native computing ubiquitous".
* Instead of creating and maintaning container-related specifications, the CNCF hosts important projects such as Kubernetes, containerd, Notary, Prometheus, Cilium and lots more.
* All CNCF projects pass through the following three phases or stages:
    * Sandbox
    * Incubating
    * Graduated

### The moby project

* Community-led place for developers to build specialized tools for building container platforms.
* Platform builders can pick the specific Moby tools they need to build their container platform.
