# Remote Two Core Simulator

The remote-core simulator is a dedicated binary containing a subset of features of the remote-core.

## Core-API

API specification files in [OpenAPI](https://swagger.io/specification/) & [AsyncAPI](https://www.asyncapi.com/)
YAML format:

- [REST OpenAPI definition](core-api/rest/openapi.yaml)
- [WebSocket AsyncAPI definition](core-api/websocket/asyncapi.yaml)

The rendered html files are available from the built-in core-simulator webserver: <http://localhost:8080/docs>

Please see our [Core APIs](https://github.com/unfoldedcircle/core-api) repository for more information.
The Core-API definitions in this core-simulator repository will soon be migrated to the dedicated API repository.

## Docker Compose Demo Setup

See [docker](docker) directory for an all-in-one simulation setup using Docker Compose.

## Linux VM for Core-Simulator

See [linux-vm](linux-vm) for a prepared Linux virtual machine containing the full Remote-Core simulator setup including
a preview of the Qt based remote-ui application.

## Usage

Extract the archive, change into the extracted directory and run the `core-simulator` binary.

- Web page: <http://localhost:8080>
- Web-Configurator preview: <http://localhost:8080/configurator>
- Default REST API endpoints:
  - <http://localhost:8080/api>
  - <https://localhost:8443/api>
- Default WebSocket API endpoints:
  - <http://localhost:8080/ws>
  - <https://localhost:8443/ws>

### User Accounts

The Remote-Core simulator has the following predefined administrator accounts:

#### REST API

Either use Basic Authentication for each request (when doing single tests or using OpenAPI), or use the `/api/pub/login`
endpoint for a session login with cookie.

ℹ️ Note: user account management will be added in a future release.

##### User accounts

Web configurator account (with admin rights):
- user: `web-configurator`
- password: `1234`

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

## License

The API specifications and documentations are published under the [CC-BY-AS-4.0](https://creativecommons.org/licenses/by-sa/4.0/)
(Creative Commons Attribution-ShareAlike 4.0 International) license.  
Please see [LICENSE file in core-api repository](https://github.com/unfoldedcircle/core-api/blob/main/LICENSE).  

All code examples in this repository are licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).  

Remote-core simulator and all graphics copyright © Unfolded Circle ApS 2022-2023.
 