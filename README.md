Contact Management Application – DevOps Project

Project Overview

The Contact Management Application is a Python Flask-based web application developed and deployed as a hands-on DevOps project. The application provides REST API endpoints for managing user/contact information
and uses Microsoft SQL Server as its backend database.

 Project Objectives
 
The primary objectives of this project were:
- Develop and containerize a Flask-based REST API application.
- Integrate the application with Microsoft SQL Server.
- Automate application testing using pytest.
- Implement a CI pipeline using GitHub Actions.
- Build, version, and publish Docker images to GitHub Container Registry (GHCR).
- Deploy the application and database on Kubernetes using Minikube.
- Implement persistent database storage using Kubernetes PersistentVolumeClaims.
- Configure Kubernetes Services and internal DNS for application-to-database communication.
- Secure sensitive configuration using GitHub Actions Secrets and Kubernetes Secrets.
- Configure NGINX Ingress for host-based HTTP routing.
- Implement automated Kubernetes deployments and rollout validation.

Technologies Used

•   Programming and Application Development

Python 3.12
Flask
REST APIs
Pyodbc

•	Database

Microsoft SQL Server

•	Containerization

Docker

•	GitHub Container Registry (GHCR)

CI/CD and Version Control
 GitHub
 GitHub Actions
 pytest

•	Container Orchestration and Networking

 Kubernetes
Minikube
Kubernetes Deployments
StatefulSets
Services
ConfigMaps
Secrets
PersistentVolumeClaims (PVCs)
NGINX Ingress

Application Architecture

The project follows a containerized application architecture in which the Flask application and Microsoft SQL Server run as separate components.
The Flask application exposes REST API endpoints that process incoming HTTP requests. When a request requires database access, the application connects to Microsoft SQL Server through pyodbc and ODBC Driver 18.
Docker is used to package the application and its dependencies into a container image. GitHub Actions automates testing and image publishing. Kubernetes manages the application and database workloads, while Kubernetes Services provide internal connectivity. NGINX Ingress provides an HTTP entry point to the Flask application through a configured hostname.

The overall workflow is:
Developer → GitHub Repository → GitHub Actions CI → Automated Tests → Docker Image Build → GHCR → Kubernetes Deployment → NGINX Ingress → Flask REST API → Microsoft SQL Server.

