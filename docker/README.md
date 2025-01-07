# Docker Compose Setup with Home-Assistant Demo Server

The pre-defined [docker-compose.yml](docker-compose.yml) is an all-in-one simulation setup including:
- Remote-core Simulator: [unfoldedcircle/core-simulator](https://hub.docker.com/r/unfoldedcircle/core-simulator)
- UC Remote Home-Assistant integration: [unfoldedcircle/integration-hass](https://hub.docker.com/r/unfoldedcircle/integration-hass)
- [Home-Assistant server](https://www.home-assistant.io/): [ghcr.io/home-assistant/home-assistant:stable](https://github.com/home-assistant/core/pkgs/container/home-assistant)
- The Home-Assistant data is persisted on the host in the [`hass_config`](hass_config) directory and bind-mounted into the container.
- The remote-core Simulator data is persisted in a Docker volume.

Important restrictions when used for developing custom integrations:
- The Simulator runs in a bridged Docker network. Therefore, mDNS discovery won't work for detecting drivers on the host!  
  See [networking](#networking) below for more information.
- There is no suspend mode as with a real remote device.  
  Depending on integration driver, suspend events must be handled and special actions be taken when the remote connects
  again.
- Custom integrations cannot be run in the Simulator.
  - Custom integration archives can be uploaded. They will be extracted, validated, and an integration driver registered.
  - The installation is performed in the volatile temp folder and is removed after the container is stopped.
  - The registered custom integration driver must be deleted manually in the web-configurator or with a Core-API call.
- Bluetooth is not available.
  - BT-remote entities cannot be created in the web-configurator.

## UC Remote Device Model

The Simulator acts as a Remote Two device by default. To enable Remote 3 specific features, the following environment
variable needs to be set in the `core-simulator` service:
```
UC_MODEL=UCR3
```

⚠️ When enabling the Remote 3 model, the web-configurator still shows the Remote Two image and is using an invalid
button layout mapping!  
The upcoming web-configurator 2.0 will support Remote 3 (ETA: November 2024).

## User Accounts

See [README in parent directory](../README.md) for the remote-core Simulator API accounts.  

Home-Assistant:

- Web page: <http://localhost:8123>
- user: `unfolded`
- password: `remotetwo`

## Docker Compose Commands

The default docker-compose file uses versioned images for the Core Simulator and the Home Assistant integration.
To use the `latest` images, uses `docker-compose-latest` configuration by adding the `-f docker-compose-latest.yml`
argument.

Check <https://hub.docker.com/u/unfoldedcircle> for new releases.  
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

## Optional Python integration library example

The [docker-compose.yml](docker-compose.yml) file contains a commented out service named `python-example` which starts
the [Python integration library setup_flow example](https://github.com/unfoldedcircle/integration-python-library).
This example is meant as a template for custom development or quickly trying out a Python based integration.

The Docker image will automatically be built when starting the services. It can also be built manually with
`docker-compose build`.

1. Uncomment the `python-example` service
2. Start as usual: `docker-compose up` 
3. Register the driver manually, if auto-discovery doesn't work:

```shell
curl 'http://localhost:8080/api/intg/drivers' \
  --header 'Content-Type: application/json' \
  -u "web-configurator:1234" \
  --data '{
    "driver_id": "python_flow",
    "name": {
        "en": "Python flow"
    },
    "driver_type": "EXTERNAL",
    "driver_url": "ws://python-example:9081",
    "version": "0.1",
    "icon": "uc:cool",
    "enabled": true,
    "device_discovery": false,
    "setup_data_schema": {
    "title": {
      "en": "Example settings",
      "de": "Beispiel Konfiguration",
      "fr": "Exemple de configuration"
    },
    "settings": [
      {
        "id": "expert",
        "label": {
          "en": "Configure enhanced options",
          "de": "Erweiterte Optionen konfigurieren",
          "fr": "Configurer les options avancées"
        },
        "field": {
          "checkbox": {
            "value": false
          }
        }
      }
    ]
    }
  }'
```

## Configuration

The remote-core Simulator runs with pre-configured defaults. Changing the configuration can have undesired effects,
and we cannot support custom configurations. 

### Networking

This docker-compose setup has been configured with a bridged network, to easily connect to the provided Home Assistant
integration and demo server. It requires a minimal set of mapped host ports and will work in every environment, even if
the mapped ports are changed, if for example port 8080 is already used by another service on your machine.

The downside is, that mDNS discovery for custom integrations won't work (unless they also run in a container and are
added to the docker-compose setup).

There are two solutions (plus a further one on Linux):

1. Not using mDNS with the setup as-is: the integration driver needs to be [registered manually](https://github.com/unfoldedcircle/core-api/blob/main/doc/integration-driver/driver-registration.md)
   with the REST Core-API.
2. Run the `core-simulator` service with host networking and reconfigure the existing Home Assistant driver url.
3. Only on Linux & unsupported: use an mDNS proxy or repeater, as for example [raetha/mdns_repeater-docker](https://github.com/raetha/mdns_repeater-docker).

#### Manual driver registration

Requirements to connect from a Docker container with bridge networking to a service running on your host:

- Accessible IP of your host. This is important!  
  - This is usually the IP address of your network adapter connecting to your network.
  - It should be in the same subnet as your router.
  - Any other "private" or virtual address, e.g. from Docker or virtualization software most likely won't work.
- Host IP / port may not be blocked by a firewall.
- Integration driver must bind to this network interface. Make sure it doesn't just listen on 127.0.0.1 or localhost.  
  Some frameworks bind to localhost only if not configured otherwise!

To test if the integration driver is accessible it's best to perform a connection test from another machine, to make
sure it's working. Either with a WebSocket client, or with a simple curl call:
```shell
curl $HOST_IP:9988 
```
- Port 9988 is the default port of the Node.js integration library. Adapt to your driver.
- If the call returns `Upgrade Required` then you are good to go. 

See [driver registration](https://github.com/unfoldedcircle/core-api/blob/main/doc/integration-driver/driver-registration.md)
in the core-api repository for a registration example with curl.

### Web Server
⚠️ The remote-core Simulator uses a very simple built-in webserver to serve the static pages and the web-configurator.  
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

#### FontAwesome6 fonts for Web-Configurator

The Simulator includes the free version of Font Awesome 6. The real Remote device is shipped with a licensed Pro version.  
Many icons are missing in the free version and therefore not available in the web-configurator of the Simulator.

If you have a Pro license of Font Awesome 6, you can put the font files into the ./fontawesome6 subdirectory to get the
same icons as with a Remote device. See `docker-compose.yml` for required font files and how to enable the volume mapping.

#### Certificates

Certificates for the TLS connection can be specified with environment variables:

```
UC_CERTS_PUBLIC=./data/certs/public.pem
UC_CERTS_PRIVATE=./data/certs/private.pem
```

Use [mkcert](https://github.com/FiloSottile/mkcert) for easy local development with self-signed certificates.

Set `UC_INTEGRATION_DISABLE_CERT_VERIFICATION=true` to disable verification.

### Logging

The log level of the Simulator can be changed through the environment variable `RUST_LOG=debug`.  
Valid log levels are: `debug`, `info`, `warn`, `error`.

Attention: `debug` logging is very verbose, especially mdns messages! Specific categories can be overridden or excluded.
Examples:
- Set debug logging only for integration module: `RUST_LOG=info,remote_core::intg=debug`
- Exclude mdns: `RUST_LOG=debug,mdns_sd=info`

#### Core-Simulator WebSocket Core-API message tracing

Container `core-simulator`:
- Set ENV variable `UC_API_MSG_TRACING` to enable Core-API WebSocket message tracing.
- Set ENV variable `UC_INTG_MSG_TRACING` to enable WebSocket Dock and Integration-API message tracing.

Message tracing is logged as `debug` level.

Values:
- `all`: enables incoming and outgoing message tracing
- `in`: incoming messages only
- `out`: outgoing messages only

⚠️ **Warning**: no message filtering is performed. Exchanged secrets like tokens or pins are exposed with this setting!

#### Home Assistant integration WebSocket message tracing

Container `integration-hass`:
- Set ENV variable `UC_API_MSG_TRACING` to enable Core-API WebSocket message tracing.
- Set ENV variable `UC_HASS_MSG_TRACING` to enable Home Assistant WS message tracing.

The same values are used as above.

## Remote-UI

To connect the [remote-ui application](https://github.com/unfoldedcircle/remote-ui) with the Simulator, the app requires
access to the dynamically created token file in `./ui-env/ws-token`. This file path must be specified in the environment
variable `UC_TOKEN_PATH`.

Linux example:
```
UC_TOKEN_PATH=/home/projects/core-simulator/docker/ui-env/ws-token remote-ui
```

macOS example:
```
UC_TOKEN_PATH=/Users/projects/core-simulator/docker/ui-env/ws-token Remote\ UI.app/Contents/MacOS/Remote\ UI
```
