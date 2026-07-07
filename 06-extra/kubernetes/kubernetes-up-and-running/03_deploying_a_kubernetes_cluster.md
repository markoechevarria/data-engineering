# 03. Deploying a Kubernetes Cluster

* Cloud-based Kubernetes services make it easy to create a cluster with a few commands
* `minikube` tool provides an easy-to-use way to get a local Kubernetes cluster up running in a VM on a local laptop or desktop
* A more recent alternative is to run a Docker-in-Docker cluster, which can spin up a multinode cluster on a single machine

## Installing Kubernetes on a Public Cloud Provider

* Google Kubernetes Engine: To get started with GKE, a Google Cloud Platform should be enabled and the `gcloud tool` installed
* Azure Kubernetes Service: The easiest way is to use the built-in Azure Cloud Shell. The shell has the `az` tool automatically installed and configured to work
* Elastic Kubernetes Service: The easiest way to create an EKS cluster is via the open source `eksctl` command-line tool

## Installing Kubernetes Locally Using minikube

* `minikube` is a good simulation of a Kubernetes cluster

## Installing Kubernetes in Docker

* `kind`: uses Docker containers to simulate multiple Kubernetes nodes instead of running everything on a virtual machine

## The Kubernetes Client

* The official Kubernetes client is `kubectl`: a command-line tool for interacting with the Kubernetes API

### Checking cluster status

* `kubectl version`: check the version of the cluster we are running
* `kubectl get componentstatuses`: check if the cluster is generally healthy
* the `controller-manager` is responsible for running various controllers that regulate behavior in the cluster
* the `scheduler` is responsible for placing different Pods onto different nodes in the cluster
* the  `etcd` server is the storage for the cluster where all of the API objects are stored

## Listing Kubernetes Worker Nodes

* `kubectl get nodes`: list out all of the nodes in the cluster
* In Kubernetes, nodes are separated into `control-plane` nodes that contain containers like the API server, scheduler, etc, which manage the cluster, and `worker` nodes where our containers will run
* `kubectl describe nodes <name-node>`: get more information about a specific node. It display:
  * Basic information about the node
  * Information about the operation, it shows disk and memory space
  * Capacity of the machine
  * Information about the software on the node, including the version of Docker that is running, the versions of K8s and the Linux kernel
  * Information about the Pods that are curerntly running on this node

## Cluster Components

* Many of the components that make up the Kubernetes cluster are actually deployed using Kubernetes itself. All of these components run in the `kube-system` namespaces

### Kubernetes Proxy

* Is responsable for routing network traffic to load-balanced services in the Kubernetes cluster. The proxy must be present on every node in the cluster
* Kubernetes has an API object named DaemonSet, that is used in many clusters to accomplish the presence of proxy on every node
* `kubectl get daemonSets --namespace=<name-space> kube-proxy`: to show the proxies

### Kubernetes DNS

* Kubernetes runs a DNS server, which provides naming and Discovery for the services that are defined in the cluster
* The DNS server also runs as a replicated service on the cluster
* The DNS server is run as a Kubernetes deployment, which manages these replicas
* There is also a Kubernetes service that performs load balancing for the DNS server, it can be seen with `kubectl get deployments --namespace=<name-namespace> core-dns`

### Kubernetes UI

* Most of the cloud providers integrate such a visualization into the GUI for their cloud
