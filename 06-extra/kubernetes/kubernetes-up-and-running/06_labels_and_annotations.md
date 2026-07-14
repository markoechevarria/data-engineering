# 05. Label and Annotations

* Labels and annotations let work in sets of things that map to how we thinkg about our application
* It allows organize, mark, and cross-index all of the resources to represent the groups that make the most sense for the application
* `Labels` are key/value pairs used rot attaching identifying information to k8s objects, can be attached to K8s objects such as Pods and ReplicaSets
* `Annotations` are key/value pairs designed to hold nonidentifying information that tools and libraries can leverage

## Labels

* Provide identifying metadata for objects. These are fundamental qualities of the object that will be used for grouping, viewing, and operating
* They are key/value pairs, where both the key and value are represented by strings
* Label keys can be broken down into two parts separated by a slash:
	* Prefix (optional), it must be a DNS subdomain with a 253-character limit
	* Name (required), must be shorted than 63 characters. Also must start and end with an alphanumeric charecterr and permit the use of dashed, underscores and dot between characters

### Applying Labels

* `kubectl run ... --image ... --labels="key=one1,key2=2,key3=three"`: create an Pod specifying labels

### Modifying Labels

* `kubectl labels deployments ... "key=two2"`: apply or update labels on object after they were created
* `kubectl get deployments -L key`: to show a label value as a column

### Label Selectors

* Are used to filters Kubernetes objects based on a set of labels
* Selectors are used both by end users (via tools like `kubectl`) and by different types of objects (such as how a ReplicaSet relates to its Pods)
* `kubectl get pods --show-labels`: list pods along with their labels
* `kubectl get pods --selector="key1=one,key2=two2"`: list pods that have the key1 label set to 'one' and the key2 label set to 'two2'
* `kubectl get pods --selector="key1 in (one,two)"`: list all pods that have the key1 label set to 'one' or 'two'
* `kubectl get deployments --select="key1"`: list all deployments with the key1 label set to anything

### Label Selectors in API objects

* A k8s object uses a label selector to refer to a set of other k8s objects
* `key1=value1, key2 in (value2, value3)` would be converted to 

```
selector:
	matchLabels:
		key1: value1
	matchExpressions:
		- { key: key2, operator: In, values: [value2, value3] }
```

* The older form `key1=value1,key2=value2` would be represented like this;

```
selector:
	key1: value1
	key2: value2
```

### Labels in the Kubernetes architecture

* Kubernetes is a purposefully decoupled system. There is no hierarchy and all components operate independently
* In many cases objects needs to relate to one another, and these relationships are defined by labels and label selector
* Cases where labels are used
	* ReplicaSets, which create and maintain multiple replicas of a Pod, find the Pods that they are managing via a selector
	* A service load balancer find the Pods to which it should bring traffic via a selector query
	* When a Pod is created, it can use a node selector to identify a particular set of nodes onto which it can be scheduled
	* When people want to restrict network traffic in their cluster, they use NetworkPolicy in conjunction with specific labels to identify Pods that should or should not be allowed to communicate with each other

## Annotations

* Annotations provide a place to store additional metadata for Kubernetes objects where the sole purpose of the metadata is assisting tools and libraries
* While labels are used to identify and group objects, annotations are used to provide extra information about where an object came from, how to use it, or policy around that object
* Annotations are used in various places in Kubernetes, with the primary use case being rolling deployments. During rolling deployments, annotations are used to track rollout status and provide the necessary information required to roll back a deployment to a previous state

### Defining Annotations

* Because the annotations are often used to communicate information between tools, the "namespace" part of they key is more important
* The value component of an annotation is a free-form string field. This allows maximum flexibility and not have validation
* Annotations are defined in the common `metadata` section in every k8s object

```
metadata:
	annotations:
		example.com/icon-url: "https://example.com/icon.png"
```
