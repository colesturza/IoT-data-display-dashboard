#  IoT-data-display-dashboard

A simple flask app that receives MQTT messages from an IoT device and displays the data on a dashboard. The data is stored in a MongoDB database. Chart.js is used to display the data. The Chart.js zoom and streaming plugins are used to make viewing the data easier. The app is meant to be deployed using Kubernetes and Docker. A DockerFile is provided in the app's directory.

## Development

First create and activate your virtualenv - with the `venv` package on OSX or Linux, this will be:

```bash
python3 -m venv venv
source venv/bin/activate
```

With your virtualenv active, install the project locally:

```bash
pip install ./services/dashboard/requirements.txt
```

You will also need Docker and Docker Compose. More instructions are provided in the README under services.

## How to deploy with Minikube

### Prereqs

- Docker (or similarly compatible) container or a Virtual Machine environment
- kubectl

### Instructions  

From a terminal with administrator access (but not logged in as root), run:

```bash
minikube start
```

To validate that the above worked run:

```bash
kubectl get po -A
```

If you see something similar to the following you're probably all set.

```
NAMESPACE              NAME                                                           READY   STATUS    RESTARTS      AGE
kube-system            coredns-78fcd69978-cgd89                                       1/1     Running   0             14m
kube-system            etcd-minikube                                                  1/1     Running   0             14m
kube-system            kube-apiserver-minikube                                        1/1     Running   0             14m
kube-system            kube-controller-manager-minikube                               1/1     Running   0             14m
kube-system            kube-proxy-qrvkj                                               1/1     Running   0             14m
kube-system            kube-scheduler-minikube                                        1/1     Running   0             14m
kube-system            storage-provisioner                                            1/1     Running   1 (14m ago)   14m
kubernetes-dashboard   dashboard-metrics-scraper-5594458c94-rblqv                     1/1     Running   0             14m
kubernetes-dashboard   kubernetes-dashboard-654cf69797-4srdb                          1/1     Running   0             14m
```

Change directories to the `kubernetes` directory, run:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

Wait for the `flask-iot-data-display-dashboard-deployment` pods to have a status of `Running`. Now we need to create a 
tunnel to the ` flask-iot-data-display-dashboard-service` service, run:

```bash
minikube service flask-iot-data-display-dashboard-service
```

Follow the link provided. On windows this was the second link provided when running all commands in wsl2. 


