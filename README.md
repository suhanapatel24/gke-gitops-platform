# GKE GitOps Platform

Production-oriented GitOps portfolio project on Google Kubernetes Engine using Terraform, Docker, Kubernetes, Argo CD, and GitHub Actions.

> Status: application and delivery definitions are implemented in code. Live GCP deployment evidence will be added only after deployment is verified.

## Architecture
```text
Developer -> GitHub -> GitHub Actions
Terraform -> VPC -> GKE <- Argo CD <- Kubernetes manifests
                         |
                         v
                     Flask API
```

## Stack
GCP, GKE, Terraform, Docker, Kubernetes, Argo CD, GitHub Actions, Python/Flask.

## Repository
- `app/`: application, tests, container
- `terraform/`: GKE infrastructure
- `k8s/`: Kubernetes desired state
- `argocd/`: GitOps application
- `.github/`: CI
- `docs/`: architecture and verified deployment evidence

## Local
```bash
cd app
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
python app.py
```

## Infrastructure
```bash
cd terraform
cp terraform.tfvars.example terraform.tfvars
terraform init
terraform fmt -check
terraform validate
terraform plan
terraform apply
```

Never commit credentials or terraform.tfvars. See `docs/deployment-evidence.md` before making live-deployment claims.
