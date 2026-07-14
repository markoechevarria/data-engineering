# 05. Pods

* In real-world deployments of containerized applications it is recomended to colocate multiple applications into a single atomic unit, scheduled onto a single machine
* K8s groups multiple containers into a single atomic unit called a Pod

## Pods in kubernetes

* A Pod is a collection of application containers and volumes running in the same execution environment
* Pods, not containers, are the smallest deployable artifcat in a kubernetes Cluster
* Each container within a Pod runs in its own cgroup, but they share a number of Linux namespaces
* Applications running in the same Pod share the same IP address and port space (network namespace), have the same hostname (UTS namespace), and can communicate using native interprocess communication channels. 
* Applications in different Pods are isolated from each other; they have different IP addresses, hostnames, and more

## Thinking with Pods

* "Will these containers work correctly if they land on different machines?"
* If the answer is "no", a Pod is correct grouping for the containers
* If the answer is "yes, multiple Pod is probably the correct solution

## The Pod Manifest

* Pods are described in a Pod manifest, which if just a text-file representation of the Kubernetes API object
* The Kubernetes API server accepts and processes Pod manifests before storing them in persistent storage (etcd)
* The scheduler uses K8s API to find pods that haven't been scheduled to a node. It then places the Pods onto nodes depending on the resources and other constraints expressed in the Pod manifest
* K8s scheduler tries to ensure that Pods from the same application are distributed onto different machines for reliability in the presence of failures

### Creating a Pod

* `kubectl run NAME --image=image_name [FLAGS]`: to create a Pod 
* `kubectl get pods`: to list and see the status of the Pods
* `kubectl delete pod NAME`: to delete a Pod

### Creating a Pod Manifest

* Can be written using YAML or JSON, but YAML is generally preferred
* Pod manifest include a couple of key fields and attributes: namely, a `metadata` section for describing the Pod and its labels, a `spec` section for describing volumes, and list of containers what will run in the Pod

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

### Pod Details

* `kubectl describe pods NAME`: to find out more information about a Pod

### Deleting a Pod

* `kubectl delete pod NAME`: delete a Pod by name
* `kubectl delete -f file.yaml`: delete a Pod by the file used to create it

## Accessing Pods

### Using Port Forwarding

* Access easily to a specific Pod, even if it's not serving traffic on the internet
* `kubectl port-forward <pod-name> <local-port>:<remote-port>`: to create a secure tunnel from the local machine, through the Kubernetes master, to the instance of the Pod running on one of the worker nodes

### Getting more info with Logs

* `kubectl logs <pod-name>`: downloads the current logs from the running instance
* `kubectl logs -f <pod-name>`: continuously stream logs
* `kubectl logs --previous <pod-name>`: get logs from a previous instance of the container (useful when containers are continuously restarting)

### Running commands in containers with exec

* `kubectl exec <pod-name> -- <commands>`: to execute command in the context of the container
* `kubectl exec -it <pod-name> -- <commands>`: to get an interactive sesión

### Copying files to and from Containers

* `kubectl cp <pod-name>:<remote-path> <local-path>`: to copy files from the Pod into the local machine
* `kubectl cp <pod-name>:<local-path> <remote-path>`: to copy flies from the local machine into the Pod

## Health Checks

* When a application was running as a container in Kubernetes, it is automatically kept alive using a `proces health check`, which ensures that the main process of the application is always running
* Liveness health checks run application-specific logic to verify that the application is not just stil running, but is functioning properly
* They have to be defined in the Pod manifest, since they are application-specific

### Liveness Probe

* Liveness probes are defined per container, which means each container inside a Pod is healthy-checked separately

```
apiVersion: v1
kind: Pod
metadata: 
	name: …
spec:
	containers:
		- image: ...
		  name: …
		  livenessProbe:
			httpGet:
				path: /healthy
				port: 8080
			initialDelaySeconds: 5
			timeoutSeconds: 1
			periodSeconds: 10
			failureThreshold: 3
...
```

### Readiness Probe

* Liveness determines if an application is running properly, containers that fail liveness checks are restarted
* Readiness describes when a container is ready to serve user requests, containers that fail readiness checks are removed from service load balancers

### Types of Health Checks

* Kubernetes support HTTP checks and TCP socket checks through tcpSocket health checks
* Kubernetes allows `exec` probes. These execute a script or program in the context of the container
* Following typical convention, if this script returns a zero exit code, the probe sucedes, otherwise, it fails

## Resource Management

* Kubernetes allow increase the overall utilization of the compute nodes that make up a cluster
* `Utilization` is defined as the amount of a resource actively being used divided by the amount of a resource that has been purchased
* Kubernetes allows users to specify two different resource metrics.
	* `requests`: specify the minimum amount of a resource required to run the application
	* `limits`: specify the maximum amount of a resource that an application can consume

### Resource Request

* Kubernets guarantees that the resources required to run a Pod are available to it. 
* The most commonly requested resources are CPU and memory

```
apiVersion: v1
kind: Pod
metadata: …
spec:
	containers:
		- image: …
		  name: …
		  resources:
			requests:
				cpu: "500m"
				memory: "128Mi"
		…
```

* The Kubernetes scheduler will ensure that the sum of all request of all Pods on a node does not exceed the capcity of the node. Therefore, a Pod is guaranteed to have at least the requested resources when running on the node
*  "request" specifies a minimun, it does not specify a maximum cap on the resources a Pod may use

### Capping resource usage with limits

* via resource `limits` a maximum can be set

```
apiVersion: v1
kind: Pod
metadata:
	name: kuard
spec:
	containers:
		- image: gcr.io/kuar-demo/kuard-amd64:blue
 		name: kuard
		resources:
			requests:
 				cpu: "500m"
 				memory: "128Mi"
			limits:
 				cpu: "1000m"
 				memory: "256Mi"
	...
```

## Persisting Data with Volumes

* When a Pod is deleted or a container restarts, any and all data in the container's filesystem is also deleted

### Using Volumes with Pods

* `spec.volumes` section: This array defines all of the volumes that may be accessed by containers in the Pod manifest
* `volumeMounts` array in the container definition: This array defines the volumes that are mounted into a particular container, and the path where each volumen should be mounted

```
apiVersion: v1
kind: Pod
metadata:
	name: kuard
spec:
	volumes:
		- name: "kuard-data"
		hostPath:
			path: "/var/lib/kuard"
	containers:
		- image: gcr.io/kuar-demo/kuard-amd64:blue
		  name: kuard
		  volumeMounts:
			- mountPath: "/data"
			  name: "kuard-data"
	… 
```

### Different ways of using Volumes with Pods

* Communication/synchronization: An `emptyDir` volume is created when a Pod is assigned to a node and exists as long as that Pod is running on that node. Because all containers in a Pod share the same network namespace and can share volume, the multiple containers running on that Pod can read and serve the files on that volume instantly.  
* Cache: An application may use a volumen that is valuable for performance, but not required for correct operation of the application. If a container crashes or fails a liveness probe, Kubernetes restarts only the container, the Pod itself remains alive on the node. Because the `emptyDir` volume is tied to the Pod's lifecycle, the newly restarted container will find its cache files completely intact, saving warmup time.
* Persistent Data: A volume for truly persistent data, data that is independent of the lifespan of a particular Pod, and should move between nodes in the cluster if a node fails or a Pod moves to a different machine for some reason. Kubernetes supports a wide varierty of remote network storage volumes as well as cloud provider network storage
* Mounting the host filesystem: Some applications don't actually need a persistent volumen, but they do need some access to the underlying host filesystem. For these cases, Kubernetes supports the hostPath volumen, which can mount arbitrary locations on the worker node into the container
* Persisting Data Using Remote Disks: Often, we want the data a Pod is using to staty with the Pod, even if it is restarted on a diferent host machine. To achieve this, we can mount a remote network storage volumen into our Pod. When using network-based storage, k8s automatically mounts and unmounts the appropiate storage whenever a Pod using that volumen is scheduled onto a particular machine. Kubernetes includes support for standard protocols such as NFS and iSCSI as well as cloud provider–based storage APIs for the major cloud providers
