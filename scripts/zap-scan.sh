#!/bin/bash

echo "Starting OWASP ZAP DAST scan..."

# Wait for the application to be ready
echo "Waiting for application to be ready..."
sleep 10

# Run ZAP scan using Docker
docker run --rm \
  --network devsecops-security-pipeline_default \
  -v $(pwd):/zap/wrk:rw \
  -v $(pwd)/zap-config.yaml:/zap/wrk/zap-config.yaml:ro \
  ghcr.io/zaproxy/zaproxy:stable \
  zap-automation.py -configfile /zap/wrk/zap-config.yaml

# Move report to reports directory
mkdir -p reports
mv zap-report.html reports/

echo "OWASP ZAP scan complete. Report saved to 
reports/zap-report.html"
