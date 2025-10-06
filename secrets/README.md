# ============================================

# Secrets Directory

# ============================================

# What? Directory for storing sensitive information

# For? Keep credentials and keys out of version control

# Impact? Prevents accidental exposure of sensitive data

# ============================================

This directory is used to store sensitive files like:

- Database passwords
- API keys
- SSL certificates
- Private keys

**IMPORTANT**: All files in this directory (except this README) are ignored by git.

## Usage Example

Create a file for database password:

```bash
echo "your_secure_password_here" > db_password.txt
```

The docker-compose.yml file will read this file as a Docker secret.

## Security Best Practices

1. Never commit sensitive files to version control
2. Use strong, randomly generated passwords
3. Rotate credentials regularly
4. Limit file permissions: `chmod 600 db_password.txt`
5. Consider using a password manager or vault service

## Creating Secrets

```bash
# Database password
echo "$(openssl rand -base64 32)" > secrets/db_password.txt

# API key
echo "$(openssl rand -hex 32)" > secrets/api_key.txt

# Set proper permissions
chmod 600 secrets/*.txt
```

## For Production

In production environments, use proper secret management:

- Docker Swarm secrets
- Kubernetes secrets
- HashiCorp Vault
- AWS Secrets Manager
- Azure Key Vault
- Google Secret Manager
