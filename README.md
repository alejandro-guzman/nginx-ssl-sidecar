# Nginx SSL sidecar example for API

## Run the example

```bash
docker-compose up --build
```

In a separate terminal

```bash
curl https://simpleapi.com:8443 --cacert rootca/ca.crt --resolve simpleapi.com:8443:127.0.0.1 -i
```