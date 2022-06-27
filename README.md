# Remote-Core simulator

The remote-core simulator is a dedicated binary containing a subset of features of the remote-core.

## Core-API

YAML specification files:

- [REST OpenAPI definition](core-api/rest/openapi.yaml)
- [WebSocket AsyncAPI definition](core-api/websocket/asyncapi.yaml)

The rendered html files are available from the built-in core-simulator webserver: <http://localhost:8080>

## Install

The Remote-Core simulator is a statically compiled binary with no external dependencies on macOS.  

### macOS

Built for: macOS Monterey 12.4

### Linux

On Ubuntu it requires avahi and the dns-sd compatibility library:
```bash
sudo apt install libavahi-compat-libdnssd-dev
```

## Run

Extract the archive, change into the extracted directory and run the `core-simulator` binary.

- Web page: <http://localhost:8080>
- Default API endpoints:
  - <http://localhost:8080/api>
  - <https://localhost:8443/api>
- At first run it will create a user data subdirectory `./data`.

## Configuration

The Remote-Core simulator runs with pre-configured defaults.

To change the web server ports, the following environment variables can be set:
```
UC_API_HTTP_PORT=8000
UC_API_HTTPS_PORT=9000
```

An optional configuration can be specified with the command line argument `--config FILE`.  
See `simulator.yaml` in the extracted directory for supported configuration options.

### Certificates

Certificates for the TLS connection can be specified with environment variables:

```
UC_CERTS_PUBLIC=./data/certs/public.pem
UC_CERTS_PRIVATE=./data/certs/private.pem
```

Use [mkcert](https://github.com/FiloSottile/mkcert) for easy local development with self-signed certificates.
