# Remote-Core simulator

The remote-core simulator is a dedicated binary containing a subset of features of the remote-core.

## Core-API

YAML specification files:

- [REST OpenAPI definition](core-api/rest/openapi.yaml)
- [WebSocket AsyncAPI definition](core-api/websocket/asyncapi.yaml)

The rendered html files are available from the built-in core-simulator webserver: <http://localhost:8080>

## Installation

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
- Default REST API endpoints:
  - <http://localhost:8080/api>
  - <https://localhost:8443/api>
- Default WebSocket API endpoints:
  - <http://localhost:8080/ws>
  - <https://localhost:8443/ws>
- At first run it will create a user data subdirectory `./data`.

### User Accounts

The Remote-Core simulator has the following predefined administrator accounts:

#### REST API

Web configurator account (with admin rights):
- user: `web-configurator`
- password: `1234`

Administrator account:
- user: `admin`
- password: `remote2`

Either use Basic Authentication for each request (when doing single tests or using OpenAPI), or use the `/api/pub/login`
endpoint for a session login with cookie.

ℹ️ Note: user account management will be added in a future release. 

#### WebSocket API

The WebSocket API uses token based authentication sent in the header:

- header: `auth-token`
- admin token: `1-2-3`

⚠️ WebSocket authentication will be reworked in a future version to simplify login flow with a REST session.

## Configuration

The Remote-Core simulator runs with pre-configured defaults.

To change the web server ports, the following environment variables can be set:
```
UC_API_HTTP_PORT=8000
UC_API_HTTPS_PORT=9000
```

An optional configuration can be specified with the command line argument `--config FILE`.  
See `simulator.yaml` in the extracted directory for supported configuration options.

- The configuration file may only contain sub-sections. It's not required to uncomment and use the full configuration.
  - Example with just re-defining the http settings:

```
api:
  http:
    enabled: true
    port: 9000
  https:
    enabled: false
    port: 8443
```
- `userdata` is an absolute directory if the path starts with `/`, otherwise it's a relative directory.

### Certificates

Certificates for the TLS connection can be specified with environment variables:

```
UC_CERTS_PUBLIC=./data/certs/public.pem
UC_CERTS_PRIVATE=./data/certs/private.pem
```

Use [mkcert](https://github.com/FiloSottile/mkcert) for easy local development with self-signed certificates.

### Logging

The log level of the simulator can be changed through the environment variable `RUST_LOG=debug`.  
Valid log levels are: debug, info, warn, error.

## Docker Compose Demo Setup

See [docker](docker) directory for an all-in-one simulation setup using Docker Compose.

## Linux VM for Core-Simulator

See [linux-vm](linux-vm) for a prepared Linux virtual machine containing the full Remote-Core simulator setup including
the Qt based remote-ui application.
