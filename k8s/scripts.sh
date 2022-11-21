#!/bin/bash

kubectl apply -f secrets.yaml

kubectl apply -f configmaps.yaml

kubectl apply -f postgres-deploy.yaml

kubectl apply -f purple-deploy.yaml

kubectl apply -f blue-deploy.yaml

kubectl apply -f ingress.yaml

kubectl apply -f clusterissuer.yaml