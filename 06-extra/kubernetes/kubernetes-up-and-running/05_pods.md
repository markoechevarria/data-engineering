# 05. Pods

* In real-world deployments of containerized applications it is recomended to colocate multiple applications inot a single atomic unit, scheduled onto a single machine
* K8s groups multiple containers into a single atomic unit called a Pod

## Pods in kubernetes

* A Pod is a collection of application containers and volumes running in the same execution environment
* Pods, not containers, are the smallest deployable artifcat in a kubernetes Cluster
* Each container within a Pod runs in its own cgroup, but they share a number of Linux namespaces
* Applications running in the same Pod share the same IP address and port space (network namespace), have the same hostname (UTS namespace), and can commtounicate using native interprocess communication channels. 
* Applications in different Pods are isolated from each other; they have different IP addresses, hostnames, and more

## Thinking with Pods

* "Will these containers work correctly if they land on different machines?"
* If the answer is "no", a Pod is correct grouping for the containers
* If the answer is "yes, multiple Pod is probably the correct solution

## The Pod Manifest

* Pods are described in a Pod manifest., which if just a text-file representation of the Kubernetes API object
* The Kubernetes API server accepts and processes Pod manifests before storing them in persistent storage (etcd)
* The scheduler usese K8s API to find pods that haven't been scheduled to a node. It then palces the Pods onto nodes depending on the resources and other constraints expressed in the Pod manifest
* K8s scheduler tries to ensure that Pods from the same application are distributed onto different machines for reliability in the presence of failures

### Creating a Pod

* `kubectl run NAME --image=image_name [FLAGS]`: to create a Pod 
* `kubectl get pods`: to see the stateus of the Pods
* `kubectl delete pod NAME`: to delete a Pod

### Creating a Pod Manifest

* Can be written using YAML or JSON, but YAML is generally preferred
* Pod manifest include a couple of key fields and attributes: namely, a `metadata` sectionfor describing the Pod and its labels, a `spec` section for describing volumes, and list of containers what will run in the Pod

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
```

### Running Pods

* `kubectl apply -f file.yaml`: to launch the pods defined in the file.yaml
* The Pod manifest will be submited to the Kubernetes API server. The Kubernetes system will then schedule that Pod to run on healthy node in the cluster, where the `kubelet` daemon will monitor it

### Listing Pods

* `kubectl get pods`: to list all Pods

### Pod Details

* `kubectl describe pods NAME`: to find our more information about a Pod

### Deleting a Pod

* `kubectl delete pods/kuard`: delete a Pod by name
* `kubectl delete -f file.yaml`: delete a Pod by the file used to create it

### Accessing Pods

* 