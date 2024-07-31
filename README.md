# Remote-Core Simulator

The remote-core Simulator is a developer tool to simplify developing integration drivers for the
[Unfolded Circle Remotes](https://www.unfoldedcircle.com/).

It simulates the functionality of the core-services running on the embedded device and provides the same
[Core-APIs](https://github.com/unfoldedcircle/core-api) as a real device. The majority of the API functionality is
identical (using the same code base) with most of the hardware functions simulated.

The remote-core Simulator is available as a [Docker image](docker) and as a ready-made [Linux VM](linux-vm).

**Please note that this is a preview version and work-in-progress!**

Additional resources:
- Rust based [Home Assistant integration](https://github.com/unfoldedcircle/integration-home-assistant)
- [Node.js API wrapper for the UC Integration-API](https://github.com/unfoldedcircle/integration-node-library)
- [Python API wrapper library for the UC Integration-API](https://github.com/unfoldedcircle/integration-python-library)  
  Integrations using the Python API wrapper:
  - [Android TV integration](https://github.com/unfoldedcircle/integration-androidtv)
  - [Apple TV integration](https://github.com/unfoldedcircle/integration-appletv)
  - [Denon AVR integration](https://github.com/unfoldedcircle/integration-denonavr)
- Open Source [remote-ui application](https://github.com/unfoldedcircle/remote-ui).

More information and contact links are on our [main GitHub page](https://github.com/unfoldedcircle).

## Core-API

Please see our [core-api](https://github.com/unfoldedcircle/core-api) repository for more information, including the
AsyncAPI and OpenAPI definitions.

## Docker Compose Demo Setup

See [docker](docker) directory for an all-in-one simulation setup using Docker Compose.

## Linux VM for Core-Simulator

See [linux-vm](linux-vm) for a prepared Linux virtual machine containing the full remote-core simulator setup including
a preview of the Qt based remote-ui application.

## Usage

- Web page: <http://localhost:8080>
- Web-Configurator preview: <http://localhost:8080/configurator>
- Default REST API endpoints:
  - <http://localhost:8080/api>
  - <https://localhost:8443/api>
- Default WebSocket API endpoints:
  - <http://localhost:8080/ws>
  - <https://localhost:8443/ws>

### User Accounts

The remote-core simulator has the following predefined administrator accounts:

#### REST API

Either use Basic Authentication for each request (when doing single tests or using OpenAPI), or use the `/api/pub/login`
endpoint for a session login with cookie.

ℹ️ Note: user account management will be added in a future release.

##### User accounts

Web-configurator account (with admin rights):
- user: `web-configurator`
- password: `1234`

The web-configurator account can be enabled & disabled in the remote-ui application. It also allows to create a new pin.

Administrator account:
- user: `admin`
- password: `remote2`

##### API key

API keys can be generated with the `/api/auth/api_keys` endpoint and can be used for the REST and WebSocket APIs.

Use `Bearer Token` authorization with an API key.

#### WebSocket API

The WebSocket API uses token based authentication sent in the header:

- header: `API-KEY`
- admin key: `BtlCEne.OWU2YzBhZjMyNmI2NDQ5YWI3N2NmMGExYWU5ZTNlNDEuZmIzOTNkM2FhOGY2NDA1N2FjNzQzNDdlOWE1YTU0OTc`

Alternatively, the session cookie can be used from the REST login.

Simple html test console: <http://localhost:8080/ws.html>

## License

The API specifications and documentations are published under the [CC-BY-AS-4.0](https://creativecommons.org/licenses/by-sa/4.0/)
(Creative Commons Attribution-ShareAlike 4.0 International) license.  
Please see [LICENSE file in core-api repository](https://github.com/unfoldedcircle/core-api/blob/main/LICENSE).  

All code examples in this repository are licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).  

Remote-core simulator and all graphics copyright © Unfolded Circle ApS 2022-2023.

The remote-core simulator is provided for development use only. It is prohibited to use the remote-core simulator
application as part of other products, services and like.
 
See [3rd party license information](licenses) about used 3rd party libraries and technologies in our applications.
