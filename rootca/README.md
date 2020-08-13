# Generate self-signed certificate for root ca

> Warning: These certificates are not safe for production

```bash
openssl req -x509 -newkey rsa:2048 -nodes -keyout ca.key -sha256 -days 1825 -out ca.crt
```
