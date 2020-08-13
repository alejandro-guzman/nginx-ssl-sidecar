# Generate certificate

## generate csr and key with openssl

```bash
openssl req -newkey rsa:2048 -nodes -keyout simpleapi.com.key -out simpleapi.com.csr
```

## generate cert with rootca

```bash
openssl x509 -req -in simpleapi.com.csr -CA ../../rootca/ca.crt -CAkey ../../rootca/ca.key -CAcreateserial -out simpleapi.com.crt -days 1825 -sha256
```