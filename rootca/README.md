# Generate self-signed certificate for root ca

```bash
openssl req -x509 -newkey rsa:2048 -nodes -keyout ca.key -sha256 -days 1825 -out ca.crt
```
