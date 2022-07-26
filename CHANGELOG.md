# Core-API Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

## v0.10.1-alpha - 2022-07-26
### Added
- Initial macro implementation.
  - Entity command definitions are not yet included.
  - Update operation not fully working yet (options are ignored).
- Core-API definitions:
  - IR data definitions for `/ir/codes/manufacturers/*` for searching & retrieving IR code sets.  
  - New endpoint `/cfg/entity/commands` to return the metadata of the entity commands.
### Changed
- Core-API definitions:
  - Stabilize & enhance documentation of `/activities` & `/macros` endpoint definitions.
  - Move remotes endpoint to `/remotes` & rename available_commands to simple_commands to align with activities and macros.

## v0.10.0-alpha - 2022-07-24
### Added
- Initial activity implementation.
  - Entity command definitions are not yet included.
  - Update operation is partially working.
- Skeleton implementations for macro & remote handling.
  - Read & delete operations are working, remaining operations will follow in an upcoming release.
### Changed
- Refined Core-API definitions for activity, macro & remote entity management.
  - Refactored remote-entity handling with user interfaces.
  - Added initial infrared code set search and custom code set handling.
- Updated icon mapping definition.

## v0.9.3-alpha - 2022-07-18
### Added
- Retrieve button layout metadata definition for assigning functions to physical buttons: `/api/cfg/device/button_layout`.
- Retrieve icon mapping with `/api/cfg/device/icon_mapping`.
- Core-API definition enhancements for activity, macro & remote user-interface management.  
  This is a **preview version**. Implementation will follow in upcoming releases.
### Changed
- Home Assistant configuration features additional devices (based on templates) for testing: light, cover, climate, media player 

## v0.9.2-alpha - 2022-07-15
### Added
- Core-API: new configuration option to retrieve and change remote device name.

## v0.9.1-alpha - 2022-07-14
### Added
- HTML WebSocket test console `/ws.html` with session based login.
- Send WebSocket `authentication` message after successful session connection setup.
### Fixed
- Only send WebSocket `get_location_languages` message after login for UI clients (= accounts having `remote-ui` role).
### Changed
- Improved WebSocket connection setup description.

## v0.9.0-alpha - 2022-07-11
### Changed
- Refactor Core-API with proper API keys instead of simple tokens.  
  API keys cannot be retrieved and are only displayed at creation time. They can be used for the WebSocket and REST APIs.
- Rename WS authentication header to API-KEY.
### Added
- Allow session cookie from REST login for WebSocket connection.

## v0.8.3-alpha - 2022-07-10
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
