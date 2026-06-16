# 05. The Docker Engine

Docker Engine is a jargon for the server-side components of Docker that run and manage containers.
The Docker Engine is modular and built from many small specialized components pulled from projects such as the OCI, the CNCF, and the Moby project.
The Docker engine is made from many specialized tools that work together to create and run containers - the API, image builder, high-level runtime, low-level runtime, etc


## The Docker Engine

* When Docker was first released, the Docker Engine had two major components
    * The Docker Daemon: a monolithic binary containing all the code for the API, image builders, container execution, volumes, networking, and more.
    * LXC: it interacted with the Linux kernel and constructed the required namespaces and cgroups to build and start containers

* Relying on LXC posed several problems for the Docker projects
    * LXC is Linux-specific, and docker had aspirations of being multi-platform
    * Docker was evolving fast, and there was no way of ensuring LXC evolved in the ways Docker needed
    * To improve the experience and help the project evolved more quickly, Docker replaced LXC with its own tool, `libontainer`, whose goal was to be a platform-agnostic tool that gave Docker access to the fundamental container building block in the host kernel

* The Docker engine was a monolithic, with almost all funcionality coded into the daemon. However, as time passed, this became more and more problematic.
* The project began a long-running program to break apart and refactor the Engine so that every feature became its own small specialized tool

