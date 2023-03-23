# Docker Compose Setup with Home-Assistant Demo Server

The pre-defined [docker-compose.yml](docker-compose.yml) is an all-in-one simulation setup including:
- Remote-core simulator: [unfoldedcircle/core-simulator](https://hub.docker.com/r/unfoldedcircle/core-simulator)
- RemoteTwo Home-Assistant integration: [unfoldedcircle/integration-hass](https://hub.docker.com/r/unfoldedcircle/integration-hass)
- [Home-Assistant server](https://www.home-assistant.io/): [ghcr.io/home-assistant/home-assistant:stable](https://github.com/home-assistant/core/pkgs/container/home-assistant)
- The Home-Assistant data is persisted on the host in the [`hass_config`](hass_config) directory and bind-mounted into the container.
- The remote-core simulator data is persisted in a Docker volume.

## User Accounts

See [README in parent directory](../README.md) for the remote-core simulator API accounts.  

Home-Assistant:

- Web page: <http://localhost:8123>
- user: `unfolded`
- password: `remotetwo`

## Docker Compose Commands

The setup defines `latest` images. Check <https://hub.docker.com/u/unfoldedcircle> for new releases.  
ℹ️ Official documentation on Docker Hub will be provided later.

⚠️ if you are using Linux or macOS, please make sure the subdirectories `ui-env` and `upload` are world-writeable.  
If you get permission errors: `chmod 777 ui-env upload`.

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

The remote-core simulator runs with pre-configured defaults. Changing the configuration can have undesired effects and
we cannot support custom configurations. 

⚠️ The remote-core simulator uses a very simple built-in webserver to serve the static pages and the web-configurator.  
The real remote device runs a dedicated webserver as reverse-proxy for the APIs and performs SSL termination.

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

Set `UC_INTEGRATION_DISABLE_CERT_VERIFICATION=true` to disable verification.

### Logging

The log level of the simulator can be changed through the environment variable `RUST_LOG=debug`.  
Valid log levels are: `debug`, `info`, `warn`, `error`.

Attention: `debug` logging is very verbose, especially mdns messages! Specific categories can be overridden or excluded.
Examples:
- Set debug logging only for integration module: `RUST_LOG=info,remote_core::intg=debug`
- Exclude mdns: `RUST_LOG=debug,mdns_sd=info`

#### WebSocket Core-API message tracing

Set ENV variable `UC_API_MSG_TRACING` to enable full WebSocket Core-API message tracing as `debug` messages:
- `all`: enables incoming and outgoing message tracing
- `in`: incoming messages only
- `out`: outgoing messages only

⚠️ **Warning**: no message filtering is performed. Exchanged secrets like tokens or pins are exposed with this setting!
