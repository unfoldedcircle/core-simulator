# Linux VM for Core-Simulator

Download link: <https://drive.google.com/drive/folders/1xIz2iwHZTM9RsKTXzhmAtTFlcb1iT7b2>  
Note: downloading a full directory might not work, download the `.ova` & readme files one by one.  
The `remote-ui` directory contains the UI binary only for manual updates of the ui app in `~/Remote-Two` without
downloading a full VM image.

Virtual machine:
- VirtualBox 6.1
- Ubuntu 22.04 minimal desktop
- user: `unfolded`
- password: `remotetwo`
- Configured with 2 cores & 4GB RAM: please adjust to your environment

Installed applications & tools:
- Docker and Docker Compose
- Firefox
- Postman for REST API testing
- Firecamp for WebSocket API testing
- Home Assistant Server
- mkcert
- Qt 5.15.2
- VirtualBox guest additions

Installed Remote Two applications:
- Remote-Core simulator
- Home-Assistant integration
- Remote-UI frontend

See [install.md](install.md) for how the Linux environment was installed.  

## Remote-Core Simulator

Web page: <http://localhost:8080> / <https://localhost:8443>

## Docker Compose Setup with Home-Assistant Demo Server

The pre-defined Docker Compose setup in `~/Remote-Two/docker-compose.yml` is an all-in-one simulation including:
- Remote-Core simulator
- Home-Assistant integration: integration-homeassistant
- [Home-Assistant server](https://www.home-assistant.io/)
- The Home-Assistant data is persisted on the host in the `~/Remote-Two/hass_config` directory and bind-mounted into the container.
- The remote-core simulator data is persisted in an anonymous Docker volume.
- All services are set to auto-start at boot (unless they have been manually stopped).

### Remote-Core Simulator:

- Web page: <http://localhost:8080> / <https://localhost:8443>
- Home-Assistant: <http://localhost:8123>
  - user: `unfolded`
  - password: `remotetwo`

The Remote-Core simulator has the following predefined administrator accounts:

#### REST API

Endpoint: <http://localhost:8080/api>

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

Endpoint: <ws://localhost:8080/ws>

The WebSocket API uses token based authentication sent in the header:

- header: `API-KEY`
- admin key: `BtlCEne.OWU2YzBhZjMyNmI2NDQ5YWI3N2NmMGExYWU5ZTNlNDEuZmIzOTNkM2FhOGY2NDA1N2FjNzQzNDdlOWE1YTU0OTc`

Alternatively, the session cookie can be used from the REST login.

Simple html test console: <http://localhost:8080/ws.html>

### Docker Compose Commands

The setup defines `latest` images. Check <https://hub.docker.com/u/unfoldedcircle> for new releases.  
ℹ️ Official documentation on Docker Hub will be provided later.

Start in foreground:
```bash
docker-compose up
```

Start in background:
```bash
docker-compose up -d
```

Update to latest version:
```bash
docker-compose pull
```

Remove all containers but keep persisted remote-simulator data in data volume:
```bash
docker-compose down
```

Delete everything, including remote-simulator data:
```bash
docker-compose rm -v
```

See official [Docker Compose documentation](https://docs.docker.com/compose/) for more information.
