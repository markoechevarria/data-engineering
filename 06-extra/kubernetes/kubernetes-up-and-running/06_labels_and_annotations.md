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
