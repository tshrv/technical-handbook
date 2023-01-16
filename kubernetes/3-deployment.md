# Getting Familiar with Deployments
![Hierarchy](./static/images/deployment/3-deployment-1.jpg)

We are going to dive deep into “Deployment” Kubernetes workload:
- Creating Deployments
- Troubleshooting various issues with Deployments
- Getting familiar with how Kubernetes manages this workload

## 1. What is a Deployment?
Deployments represent a set of multiple, identical Pods with no unique identities. A Deployment runs multiple replicas of your application and automatically replaces any instances that fail or become unresponsive. In this way, Deployments help ensure that one or more instances of your application are available to serve user requests. Deployments are managed by the Kubernetes Deployment controller.

Deployments use a Pod template, which contains a specification for its Pods. The Pod specification determines how each Pod should look like: what applications should run inside its containers, which volumes the Pods should mount, its labels, and more.

When a Deployment’s Pod template is changed, new Pods are automatically created one at a time.

[Deployments in K8s - https://youtu.be/HPutXDwSWM0](https://youtu.be/HPutXDwSWM0)

> The deployment is (simply) responsible for rolling out your application, looking after its updates and rolling back to previous state - if needed. This is achieved because “Deployment” creates corresponding “Replicaset” per each deployment object

![Deployment Replicaset Pod](./static/images/deployment/3-deployment-2.jpg)

## 2. Creating Deployment

Example of Deployment Manifest:
```sh
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.7.9
        ports:
        - containerPort: 80
```

In this example:

- A Deployment named nginx-deployment is created, indicated by the .metadata.name field.
- The Deployment creates three replicated Pods, indicated by the `replicas field.
- The Pod template, or .spec.template field, indicates that its Pods are labeled app=nginx.
- The Pod template’s specification, or .spec.template.spec field, indicates that the Pods run one container, name=nginx, which runs the nginx:1.7.9 Docker Hub image.
- The Deployment opens port 80 for use by the Pods.

### Task:
Create a new deployment called `nginx-deploy`

### Requirements:

- Name: `nginx-deploy`
- Image: `nginx:1.19-alpine`
- Replicas: `1`
- Labels:
  - `app=nginx-deploy`
> Make sure that pods are running

### Verify:
```sh
$ kubectl get deploy -l app=nginx-deploy
NAME           READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deploy   1/1     1            1           1m17s

$ kubectl get replicaset -l app=nginx-deploy
NAME                      DESIRED   CURRENT   READY   AGE
nginx-deploy-5db957f468   1         1         1       1m19s

$ kubectl get pod -l app=nginx-deploy
NAME                            READY   STATUS    RESTARTS   AGE
nginx-deploy-5db957f468-frj8w   1/1     Running   0          1m22s
```

### Documentation:
- [https://kubernetes.io/docs/concepts/workloads/controllers/deployment/](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [https://cloud.google.com/kubernetes-engine/docs/concepts/deployment](https://cloud.google.com/kubernetes-engine/docs/concepts/deployment)


## 3. Creating Deployment. Quick Way

Please inspect following command:
```sh
kubectl create deployment --help
```
```
Create a deployment with the specified name.
Aliases:
deployment, deploy

Examples:
  # Create a deployment named my-dep that runs the busybox image.
  kubectl create deployment my-dep --image=busybox:1.34
  
  # Create a deployment with command
  kubectl create deployment my-dep --image=busybox -- date
  
  # Create a deployment named my-dep that runs the nginx image with 3 replicas.
  kubectl create deployment my-dep --image=nginx --replicas=3
  
  # Create a deployment named my-dep that runs the busybox image and expose port 5701.
  kubectl create deployment my-dep --image=busybox --port=5701

Options:
      --allow-missing-template-keys=true: If true, ignore any errors in templates when a field or
map key is missing in the template. Only applies to golang and jsonpath output formats.
      --dry-run='none': Must be "none", "server", or "client". If client strategy, only print the
object that would be sent, without sending it. If server strategy, submit server-side request
without persisting the resource.
      --field-manager='kubectl-create': Name of the manager used to track field ownership.
      --image=[]: Image names to run.
  -o, --output='': Output format. One of:
json|yaml|name|go-template|go-template-file|template|templatefile|jsonpath|jsonpath-as-json|jsonpath-file.
      --port=-1: The port that this container exposes.
  -r, --replicas=1: Number of replicas to create. Default is 1.
      --save-config=false: If true, the configuration of current object will be saved in its
annotation. Otherwise, the annotation will be unchanged. This flag is useful when you want to
perform kubectl apply on this object in the future.
      --template='': Template string or path to template file to use when -o=go-template,
-o=go-template-file. The template format is golang templates
[http://golang.org/pkg/text/template/#pkg-overview].
      --validate=true: If true, use a schema to validate the input before sending it

Usage:
  kubectl create deployment NAME --image=image -- [COMMAND] [args...] [options]

Use "kubectl options" for a list of global command-line options (applies to all commands).
```

### Task:
Inspect the details listed above, add necessary options to kubectl create deploy command to produce following deployment configuration:
- Name: `easy-peasy`
- Image: `quay.io/playpit/busybox:1.32`
- Replicas: `5`
- Command: `sleep infinity`

### Take into Account:
To **generate** Deployment manifest you should use the same command with these options:
```sh
--dry-run=client
-o yaml
```
> Make sure you use these options before command part `(-- ...)`

### Documentation:
- [https://kubernetes.io/docs/concepts/workloads/controllers/deployment/](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [https://cloud.google.com/kubernetes-engine/docs/concepts/deployment](https://cloud.google.com/kubernetes-engine/docs/concepts/deployment)