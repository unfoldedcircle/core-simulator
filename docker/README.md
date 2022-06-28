# Docker Compose Setup with Home-Assistant Demo Server

The pre-defined [docker-compose.yml](docker-compose.yml) is an all-in-one simulation setup including:
- Simulator: core-simulator
- Home-Assistant integration: integration-homeassistant
- [Home-Assistant server](https://www.home-assistant.io/)
- The Home-Assistant data is persisted on the host in the [`hass_config`](hass_config) directory and bind-mounted into the container.
- The core-simulator data is persisted in an anonymous Docker volume.

Core-Simulator:

- Web page: <http://localhost:8080>
- user: `admin`
- password: `remote2`

Home-Assistant:

- Web page: <http://localhost:8123>
- user: `unfolded`
- password: `remotetwo`

## Docker Compose Commands

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

See [Docker Compose documentation](https://docs.docker.com/compose/) for more information.
