# 1. Introduction

Kubernetes is an open source orchestrator for deploying containerized applications
Kubernetes is a proven infraestructura for distributed systems that is suitable for cloud-native developer of all scales

* Because we rely on APIs (via by services are delivered over the network), these systems must be highly `reliable`
* They must maintain `availability` even during software rollouts or other maintenance events
* Because more and more of the world is coming online and using such services, they must be highly `scalable` to that they can grow their capacity to keep up with ever-increasing usage without radical redesign of the distributed system that implements the services

## Velocity

* The software industry has evolved from shipping products as boxed CDs or DVDs to software that is delivered over the network via web-based services that are updated hourly
* Velocity is not defined in terms of simply raw speed. While the users are always looking for iterative improvement, they are more interested in a highly reliable service
* Velocity is measured not in terms of the raw number of features you can ship per hour or day, but rather in terms of the number of things you can ship while maintaining a highly available service

### Immutability

* With immutable infraestructure, once an artifact is created in the system it does not change via user modifications
* With a mutable system, changes are applied as incremental updates to an existing system. The current state of the infraestructure is not represented as a single artifact, but rather an accumulation of incremental updates and changes over time
* In an immutable system, rather than a series of incremental updates and changes, and entirely new, complete image is built, where the update simply replaces the entire image with the newer image in a single operation
* The act of building a new container improve reliability, make it easy to understand exactly the differences in some new versión and, if something goes wrong, to determine what has changed and how to fix it
* Immutable container images are at the core of everything that you will build in Kubernetes. It is posible to imperatively change running containers, but this is an anti-pattern to be used only in extreme cases where there are no other options. And even then, the changes must also be recorded through a declarative configuration update at some later time.

### Declarative configuration

* Everything in Kubernetes is a declarative configuration object that represents the desired state of a system
* Declarative configuration is an alternative to imperative configuration, where the state of the world is defined by the execution of a series of instructions rather than a declaration of the desired state of the world. While imperative commands define actions, declarative configurations define state
* Since the effects of declarative configuration can be understood before they are executed, declarative configuration is far less error-prone.
* The idea of storing declarative configuration in source control is often referred to as "infraestructura as code"

### Self-Healing systems

* Kubernetes is an online, self-healing system. When it receives the desired state configuration, it does not simply take a set of actions to make the current state match the desired state a single time. It continuously takes actions to ensure that the current state matches the desired state
* A more traditional operator repair involves a manual series of mitigation steps, or human intervention performed in response to some sort of alert
* If you assert a desired state of three replicas to Kubernetes, it does not just créate three replicas - it continuously ensures that there are exactly three replicas. If you manually create a fourth replica, Kubernetes will destroy one to bring the number back to three. If you manually destroy a replica, Kubernetes will create one to again return to the desired state

## Scaling your service and your teams

* Kubernetes achieves scalability by favoriting decoupled architectures

### Decoupling

* In a decoupled architecture, each component is separated from other components by defined APIs and service load balancers. APIs and load balancers isolate each piece of the system from the others. APIs provide a buffer between implementer and consumer, and load balancers provide a buffer between running instances of each service
* Decoupling components via load balancers makes it easy to scale the programs that make up your service
* Decoupling servers via APIs makes it easier to scale the development teams because each team can focus on a single, smaller microservice with a comprehensible surface area

### Easy scaling for applications and clusters

* The immutable, declarative nature of Kubernetes makes it the service scaling trivial to implement
* Because many machines in a cluster are entirely identical to other machines in that set and the applications themselves are decoupled from the details of the machine by containers, adding additional resources to the cluster is simply a matter of imagining a new machine of the same class and joining it into the cluster

### Scaling development teams with microservices

* Kubernetes provides numerous abstractions and APIs that make it easier to build these decoupled microservice architectures:
	* Pods, or groups of containers, can group together container images developed by diferent teams into a single deployable unit
	* Kubernetes services provide load balancing, naming and Discovery to isolate one microservice from another
	* Namespaces provide isolation and Access control, so that each microservice can control the degree to which other services interact with it
	* Ingress objects provide and easy-to-use frontend that can combine multiple microservices into a single externalized API surface área

* The health-checking and rollout features of Kubernetes guarantee a consistent approach to application rollout and reliability which ensures that a proliferation of microservice teams does not also result in a proliferation of different approaches to service production lifecycle and operations

### Separation of Concerns for consistency and Scaling

* The container orchestration API becomes a crisp contract that separates the responsabilities of the application operator from the cluster orchestration operator. The application developer relies on the service-level agreement (SLA) delivered by the container orchestration API, without worrying about the details of how this SLA is achieved. Likewise, the container orchestration API realiability engineer focuses on delivering the orchestration API's SLA without worrying about the applications that are running on top of it

* There is a thriving ecosystem of companies and projects that help to install and manage Kubernetes. 

## Abstracting your infraestructure

* The move for application-oriented container APIs like Kubernetes has two concrete benefits. First it separates developers from specific machines. This makes the machine-oriented IT role easier, since machines can simple be added in aggregate to scale the cluster, and in the context of the cloud it also enables a high degree of portability since developers are consuming a higher-level API that is implemented in terms of the specific cloud infraestucture APIs
* When your developers build their applications in terms of container images and deploy them in terms of portable Kubernete APIs, transferring your application between environments, or even running in hybrid environments, is simply a matter of sending the declarative config to a new cluster.

## Efficiency

* Efficiency can be measured by the ratio of the useful work performed by a machine or process to the total amount of energy spent doing so
* When discussing efficiency it's often helpful to think of both the cost of running a server and the human cost required to manage it
* A developer's test environment can be quickly and cheaply created as a set of containers running in a personal view of a shared Kubernetes cluster (using a feature called namespaces)

## Cloud Native Ecosystem

* In the years since it was released, tools for nearly every tak, from machine learning to continuous development and serverless programming models have been built for Kubernetes
* A way to navigate the cloud native ecosystem is via integration with Kubernetes-as-a-Service. At this point, most of the KaaS offerings also have additional services via open source projects from the cloud native ecosystem
