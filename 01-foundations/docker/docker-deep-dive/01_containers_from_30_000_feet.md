# 01. Containers from 30,000 feet

## The bad old days

* Most application run on servers, and in the past, we were limited to running one application per server.

## Hello VMware

* The Virtual Machine (VM): a technology that allowed us to run multiple business applications on a single server safely.
* Every VM needs its own dedicated operating system (OS). This has several drawbacks:
    * Every OS consumes CPU, RAM and other resources.
    * Every VM and OS needs patching.
    * Every VM and OS needs monitoring.

## Hello Containers

* Every container shares the OS of the host it is running on. A single host can run more containers than VMs.

## Linux Containers

* Containers started in the Linux world and are the product of incredible work from many people over many years.
* Technologies underpinning modern containers include kernel namespaces, control groups (cgroups) and capabilities.

## Hello Docker

* Docker was the magic that made Linux containers easy and brougth them to the masses.

## Docker and Windows

* Windows containers run Windows Apps and require a host system with a Windows Kernel.
* Windows systems also can run Linux containers via the WSL (windows Subsystem Linux) subsystem.

### Windows containers vs Linux containers

* Containers share the kernel of the host they are running on.

### Mac Containers

* There is no such thing as Mac containers.
* The most popular way of working with with containers on a Mac is Docker Desktop. It works by running Docker inside a lightweight Linux VM on Mac.

## Wasm

* Was (WebAssembly) is a modern binary instruction set that builds applications that are smaller, faster, more secure and more portable than containers
* Docker and the container ecosystem are adapting to work with Wasm apps,

## Docker and AI

* Developers and Organizations are using more AI apps.
* Exposing GPUs and other AI acceleration hardware to apps running inside containers is very hard
* Docker Model Runner has been released as a way of running local LLMs outside of containers so they have direct access to the host's hardware.

## What about Kubernetes

* Kubernetes is the industry standard platform for deploying and managing containerized apps.
* All Docker containers work in Kubernetes