# Nginx SSL sidecar example for API

```bash
curl https://simpleapi.com:8443 --cacert rootca/ca.crt --resolve simpleapi.com:8443:127.0.0.1 -i
```