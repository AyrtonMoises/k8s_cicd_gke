#!/bin/bash
kubectl apply -f secrets.yaml

kubectl apply -f configmaps.yaml

kubectl apply -f postgres-deploy.yaml

kubectl apply -f purple-deploy.yaml

kubectl apply -f blue-deploy.yaml

kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.5.1/deploy/static/provider/cloud/deploy.yaml

kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.10.0/cert-manager.yaml

kubectl apply -f clusterissuer.yaml

kubectl apply -f ingress.yaml