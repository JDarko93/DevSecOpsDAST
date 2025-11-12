#!/bin/bash

echo "Running Trivy vulnerability scan..."

# Scan the Docker image
trivy image --format json --output reports/trivy-report.json 
devsecops-security-pipeline-web:latest

# Also create a readable format
trivy image --format table --output reports/trivy-report.txt 
devsecops-security-pipeline-web:latest

echo "Trivy scan complete. Reports saved to reports/"
