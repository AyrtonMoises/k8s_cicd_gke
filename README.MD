# Flask Steam com Kubernetes 

- Projeto para busca de jogos exibindo os valores no Brasil e Argentina

### Rodar com docker-compose
```
docker-compose up -d
```

### Remover containers
```
docker-compose down -v
```

### Rodar para aplicar alterações no Kubernetes local ou cloud
```
./scripts.sh
```

## Implementação no GKE do Google Cloud com CI/CD

### Cria cluster via CLI
```
gcloud container clusters create $GKE_CLUSTER \
	--project=$GKE_PROJECT \
	--zone=$GKE_ZONE
```

### Habilitar produtos do GCloud
```
gcloud services enable \
	containerregistry.googleapis.com \
	container.googleapis.com
```

### Criar credencial via terminal
```
gcloud iam service-accounts create my-service-account
```

### Pegar na listagem o email(aquele q gcloud cria automatico) do usuario criado
```
gcloud iam service-accounts list 
```

### pegar id do projeto que o cluster pertence caso n saiba
```
gcloud projects list --sort-by=projectId --limit=5
```

### Comandos para colocar permissões(podem ter mais restritivas q essas)
```
gcloud projects add-iam-policy-binding my-project \
	--member=serviceAccount:my-service-account@my-project.iam.gserviceaccount.com \
	--role=roles/container.admin
```
```
gcloud projects add-iam-policy-binding my-project \
	--member=serviceAccount:my-service-account@my-project.iam.gserviceaccount.com \
	--role=roles/storage.admin
```
```
gcloud projects add-iam-policy-binding my-project \
	--member=serviceAccount:my-service-account@my-project.iam.gserviceaccount.com \
	--role=roles/container.clusterViewer
```

### Faça o download do arquivo de chave JSON para a conta de serviço:
```
gcloud iam service-accounts keys create key.json --iam-account=$SA_EMAIL
```

### Armazene a chave da conta de serviço como um segredo chamado GKE_SA_KEY ou copie e jogue para seus secrets:
```
export GKE_SA_KEY=$(cat key.json | base64)
```
-APÓS PEGAR O DADO, EXCLUA O ARQUIVO DO REPOSITORIO