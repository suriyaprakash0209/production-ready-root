# 🚀 Production-Ready DevOps CI/CD Pipeline (Flask + Docker + AWS)

## 📌 Project Overview

This project demonstrates a **real-world, production-grade DevOps workflow** for deploying a Flask application using:

* GitHub Actions (CI/CD automation)
* Docker (containerization)
* AWS (ECR + EC2 deployment architecture)
* Gunicorn (production WSGI server)

The goal of this project is to simulate how modern software is built, tested, containerized, and deployed in real enterprise environments.

---

## 🏗️ System Architecture

```
Developer → GitHub Repo → GitHub Actions CI/CD → Docker Build → AWS ECR → AWS EC2 → Running Container
```

---

## ⚙️ Tech Stack

* **Backend**: Flask (Python)
* **Containerization**: Docker
* **CI/CD**: GitHub Actions
* **Cloud**: AWS (ECR + EC2)
* **Production Server**: Gunicorn
* **OS Environment**: Linux (EC2 Ubuntu)

---

## 📦 Project Structure

```
project-root/
│
├── app/
│   └── app.py
│
├── tests/
│   └── test_app.py
│
├── .github/workflows/
│   └── cicd.yml
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔁 CI/CD Pipeline Workflow

### Step 1: Code Push

Developer pushes code to GitHub repository

### Step 2: GitHub Actions Trigger

Workflow automatically starts on push to main branch

### Step 3: Build Stage

* Install dependencies from `requirements.txt`
* Run unit tests
* Validate application integrity

### Step 4: Docker Build

* Build Docker image using Dockerfile
* Package Flask app into container

### Step 5: Image Push (AWS ECR)

* Authenticate with AWS
* Push Docker image to Elastic Container Registry

### Step 6: Deployment (EC2)

* EC2 pulls latest image
* Runs container using Docker
* Exposes application on port 5000

---

## 🐳 Docker Implementation

### Dockerfile Features

* Python base image
* Dependency installation
* Gunicorn production server
* Lightweight container design

### Command Flow

```
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```

---

## 🔧 GitHub Actions CI/CD Pipeline

### Key Features

* Automated build on push
* Dependency installation check
* Docker image creation
* Optional AWS deployment step

### Common Issues Solved

* YAML syntax errors fixed
* Missing `jobs` structure corrected
* Path resolution issues resolved
* `requirements.txt` detection fixed

---

## ☁️ AWS Deployment Architecture

### Components Used

* **ECR (Elastic Container Registry)** → Stores Docker images
* **EC2 Instance** → Runs application container

### Flow

1. Docker image pushed to ECR
2. EC2 pulls image
3. Container runs with Gunicorn server
4. Application exposed via public IP

---

## 🧪 Testing Strategy

* Basic Flask route validation
* Unit testing via pytest (optional setup)
* Container-level execution testing

---

## ❗ Issues Encountered & Fixes

### 1. Missing requirements.txt

✔ Fixed by correcting repository structure

### 2. GitHub Actions failure

✔ Resolved YAML indentation and job configuration

### 3. Connection refused on EC2

✔ Identified as service not running / port not exposed

### 4. pip not recognized (Windows)

✔ Fixed via environment path configuration

---

## 📊 Skill Level Achieved

| Area                                  | Level                             |
| ------------------------------------- | --------------------------------- |
| Flask Development                     | Intermediate                      |
| Docker                                | Intermediate-Advanced             |
| CI/CD (GitHub Actions)                | Intermediate                      |
| AWS Deployment                        | Intermediate (practical exposure) |
| Production Architecture Understanding | Advanced                          |

---

## 🚀 Key Learnings

* Real-world CI/CD pipeline design
* Containerized deployment strategy
* Debugging deployment failures
* Multi-layer system integration
* Production vs development environment differences

---

## 🎯 Outcome

This project demonstrates a **junior-to-intermediate DevOps engineer capability** with exposure to production-style deployment pipelines and cloud infrastructure integration.

---

## 📌 Next Improvements (Roadmap)

* Add Terraform for Infrastructure as Code (IaC)
* Implement monitoring (CloudWatch / Prometheus)
* Add rollback strategy in CI/CD
* Add load balancing (ALB)
* Secure deployment with IAM roles & secrets manager

---

## 👨‍💻 Author

DevOps Learning Project – Full CI/CD Pipeline Simulation
