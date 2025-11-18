# DevSecOps Security Testing Pipeline

An automated security scanning pipeline that demonstrates real-world DevSecOps practices by integrating vulnerability scanning and dynamic security testing into the CI/CD process.

## 🎯 Project Overview

This project showcases a complete security testing pipeline for containerized applications. It automatically scans for vulnerabilities whenever code is pushed to GitHub, providing early detection of security issues before they reach production.

**Key Features:**
- Automated container image vulnerability scanning with Trivy
- Dynamic Application Security Testing (DAST) with OWASP ZAP
- CI/CD integration using GitHub Actions
- Email notifications for critical security findings
- Comprehensive security reports

## 🛠️ Technologies Used

- **Application**: Python, Flask
- **Containerization**: Docker, Docker Compose
- **Security Scanning**: 
  - Trivy (Container vulnerability scanning)
  - OWASP ZAP (Dynamic Application Security Testing)
- **CI/CD**: GitHub Actions
- **Notifications**: Email (SMTP)

## 🚀 Getting Started

### Prerequisites

- Docker and Docker Compose installed
- Git installed
- GitHub account
- (Optional) Gmail account for email notifications

### Local Setup

1. **Clone the repository**
```bash
   git clone <your-repo-url>
   cd devsecops-security-pipeline
```

2. **Build and run the application**
```bash
   docker-compose build
   docker-compose up
```

3. **Access the application**
   - Open browser to: `http://localhost:5000`
   - The application is a simple user lookup system

4. **Stop the application**
```bash
   docker-compose down
```

### Testing the Vulnerability

The application contains an intentional SQL injection vulnerability for demonstration purposes.

**Normal search:**