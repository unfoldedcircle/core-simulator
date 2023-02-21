# Docker Compose Setup with Home-Assistant Demo Server

The pre-defined [docker-compose.yml](docker-compose.yml) is an all-in-one simulation setup including:
- RemoteTwo Core-Simulator: [unfoldedcircle/core-simulator](https://hub.docker.com/r/unfoldedcircle/core-simulator)
- RemoteTwo Home-Assistant integration: [unfoldedcircle/integration-hass](https://hub.docker.com/r/unfoldedcircle/integration-hass)
- [Home-Assistant server](https://www.home-assistant.io/): [ghcr.io/home-assistant/home-assistant:stable](https://github.com/home-assistant/core/pkgs/container/home-assistant)
- The Home-Assistant data is persisted on the host in the [`hass_config`](hass_config) directory and bind-mounted into the container.
- The core-simulator data is persisted in an anonymous Docker volume.

Core-Simulator:

- Web page: <http://localhost:8080>
- Web configurator user account (with admin rights):
  - user: `web-configurator`
  - password: `1234`
- Administrator user account:
  - user: `admin`
  - password: `remote2`

Home-Assistant:

- Web page: <http://localhost:8123>
- user: `unfolded`
- password: `remotetwo`

## Docker Compose Commands

The setup defines `latest` images. Check <https://hub.docker.com/u/unfoldedcircle> for new releases.  
ℹ️ Official documentation on Docker Hub will be provided later.

Start in foreground:
```shell
docker-compose up
```

Start in background:
```shell
docker-compose up -d
```

Update to latest version:
```shell
docker-compose pull
```

Remove all containers but keep persisted remote-simulator data in data volume:
```shell
docker-compose down
```

Delete everything, including remote-simulator data:
```shell
docker-compose rm -v
```

See [Docker Compose documentation](https://docs.docker.com/compose/) for more information.

## Configuration

The Remote-Core simulator runs with pre-configured defaults and should not be changed. 

To change the web server ports, the following environment variables can be set:
```
UC_API_HTTP_PORT=8000
UC_API_HTTPS_PORT=9000
```

Enable / disable http or https:
```
UC_API_HTTP_ENABLED=false
UC_API_HTTPS_ENABLED=true
```

### Certificates

Certificates for the TLS connection can be specified with environment variables:

```
UC_CERTS_PUBLIC=./data/certs/public.pem
UC_CERTS_PRIVATE=./data/certs/private.pem
```

Use [mkcert](https://github.com/FiloSottile/mkcert) for easy local development with self-signed certificates.

### Logging

The log level of the simulator can be changed through the environment variable `RUST_LOG=debug`.  
Valid log levels are: `debug`, `info`, `warn`, `error`.

