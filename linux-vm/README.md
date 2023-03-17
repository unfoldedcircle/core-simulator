# Linux VM for Core-Simulator

Download link: <https://drive.google.com/drive/folders/1IneoOAUBACs3L9Oq1anqye3Iru0v6_rI>

- please [contact us](https://github.com/unfoldedcircle#contact-us-speech_balloon) if you get a download quota error,
  we'll look for another download solution.  
- downloading a full directory might not work, download the `.ova` & readme files one by one.
- switch to list view for easier navigation and use incognito / private mode if it interferes with your existing Google account.
- the `remote-ui` directory contains the UI binary only for manual updates of the ui app in `~/Remote-Two` without
downloading a full VM image.
- the other components can be updated with `docker-compose pull`, see [Docker Compose Commands](#docker-compose-commands).

Virtual machine:
- VirtualBox 7 (if the desktop keeps crashing, try another version or switch virtualization software)
- Ubuntu 22.04 minimal desktop installation
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
- Node.js 18
- VirtualBox guest additions

Installed Remote Two applications:
- Remote-core simulator with web-configurator
- Home-Assistant integration
- Remote-UI frontend

See [install.md](install.md) for how the Linux environment was installed.  

## Remote-Core Simulator

Web page: <http://localhost:8080> / <https://localhost:8443>

## Docker Compose Setup with Home-Assistant Demo Server

The pre-defined Docker Compose setup in `~/Remote-Two/docker-compose.yml` is an all-in-one simulation including:
- Remote-core simulator
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

See [README in parent directory](../README.md) for the remote-core simulator API accounts.

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
