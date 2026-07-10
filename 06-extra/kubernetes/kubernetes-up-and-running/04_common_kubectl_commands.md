# 04. Common kubectl commands

## Namespaces 

* Kubernetes uses namespaces to organize objects in the cluster
* We can think of each namespaces as a folder that holds a set of objects
* By default, the `kubectl` command-line tool interacts with the `default` namespace. In order to use a different namespace, we can pass `kubectl` the  `-- namespace` flag
* To interact with all namespaces we can pass the `--all-namespaces` flag

## Context

* We can use a `context` in order to change the default namespace more permanentlys
* `kubectl config set-context my-context --namespace=mynamespace`: to create a new context named 'my-context' with a different default namespace
* `kubectl config use-context my-context`: to use the newly created context named 'my-context'

## Viewing Kubernetes API objects

* Everything contained in Kubernetes is represented by a RESTful resource, them are refered as `kubernetes objects`
* Each Kubernetes object exists at a unique HTTP path
* 'http://our-k8s.com/api/v1/namespaces/default/pods/my-pod' leads to the representation of a Pod in the default namespaces named 'my-pod'
* `kubectl get <resource-name>` get a list of all resources in the current namespaces
* `kubectl get <resource-name> <obj-name>` get a specific resource
* the `-o wide` flag gives more information about the resources, it can be extended with `-o json` and `-o yaml`
* The `--no-headers` flag skip the headers at the top of the human-readable table
* `kubectl get pods,services` allow view multiple objects of diferente types
* `kubectl describe <resource-name> <obj-name>` show more detailed information about a particular object
* `kubectl explain pods` show a list of supported fields for each supported tpe of Kubernetes object

## Creating, Updating and Deleting Kubernetes objects

* Objects in the  Kubernetes API are represented as JSON or YAML files and can be used to create, update or delete objects
* `kubectl apply -f <obj-file.yaml>`: to create a object or update it (if it already was created)
* `kubectl delete <resource-name> <obj-name>`: to delete an object

## Labeling and Annotating Objects

* Labels and annotations are tags for the objects
* `kubectl label <type-object> <name-object> <key>=<value>`: to add the tag `key` with the value `value`
* `kubectl label <type-object> <name-object> <key->: remove the `key` label from the <type-object> named <name-object>

## Debugging commands

* `kubectl logs <pod-name>` to see the logs for a running container. If there are multiple containers in the Pod, we can choose the container to view using the -c flag
* By default `kubectl logs` lists the current logs and exists. To continuously stream the logs back to the terminal without exiting, we can add the -f (follow) command-line flag
* `kubectl exec -it <pod-name> -- bash`: the `exec` command is used to execute a command in a running contianer
* `kubectl attach -it <pod-name>: to attach the terminal to the running process. It is similar to kubectl logs but Will allow to send input to the runnign process.
* `kubectl cp <pod-name>:</path/to/remote/file> </path/to/local/file>`: copy files to and from a container
* `kubectl port-forward <pod-name> <local-port>:<remote-port> : allow access the Pod via the network. It opens up a connection that forwards traffic from the local machine on port <local-port> to the remote container on port <remote-port>
* `kubectl get events` return a list of the latest 10 events on all objects in a given namespace. We can stream events as they happend by adding `--watch`, the `-A` flag could  be included to see events in all namespaces
* `kubectl top <resource>`: to show the list of resources in use by either nodes or pods. The `--all-namespaces` flag can be added to see resource usage by all Pods in the cluster.

## Cluster Management

* The `kubectl` tool can also be used to manage the cluster itself
* When we `cordon` a node we prevent future Pods from being scheduled onto that machine
* When we `drain` a node, we remove any Pods that are currently running on that machine
