# Core-API Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased
### Added
- Core-API: new endpoints and messages to retrieve language and country lists for localization configuration.

## v0.8.2-alpha - 2022-07-07
### Added
- Linux VM setup instructions and download link.
### Fixed
- WS Core-API: `get_active_profile` response msg type.
- CORS: missing PATCH, HEAD methods & allow any headers for the time being for WebSocket upgrade & authentication.
- REST Core-API endpoints: corrected time zone name endpoint & typo in OpenAPI software update cfg endpoint.

## v0.8.1-alpha - 2022-07-01
### Added
- Dedicated `web-configurator` account usable for pin entry.
- Generic /api endpoint in OpenAPI specification for easier testing.
- Active profile switching and retrieval of active profile identifier.

## v0.8.0-alpha - 2022-06-30
### Added
- Login & logout functionality with cookie based session handling in the REST Core-API.

## v0.7.1-alpha - 2022-06-29
### Added
- User account documentation.
- Docker Compose demo setup with pre-configured Home Assistant server.

### Fixed
- Custom certificate configuration settings.

## 0.7.0-alpha - 2022-06-26
### Added
- Initial configuration Core-API definition and implementation.
