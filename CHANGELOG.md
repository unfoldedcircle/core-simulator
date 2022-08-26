# Core-API Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

## v0.12.2-alpha - 2022-08-26
### Fixed
- Simulator: keep existing entity options with `PATCH /remotes/:entityId`.  
  The entity options button_mapping, simple_commands, user_interface are no longer removed when patching an entity.
- Core-API definition:
  - Fix response payload of `PATCH /remotes/:entityId`
  - Fix parameter references of `/remotes/{entityId}/buttons/{buttonId}` and `/activities/{entityId}/buttons/{buttonId}`

## v0.12.1-alpha - 2022-08-23
### Fixed
- Simulator: activity & remote-entity: user interface page item placement validation.

## v0.12.0-alpha - 2022-08-21
### Added
- Simulator: custom IR codeset handling
### Changed
- **Breaking change**: refactor activity- and remote-entity management functions:  
  **Existing activity-, macro- and remote-entities must be re-created to avoid any potential data errors.**
  - Dedicated REST endpoints to modify button mappings and user interface pages
    Instead of a do-it-all PATCH method for button mappings and user interface definitions.
- Limit returned options in `GET /activities`, `GET /macros`, `GET /remotes`:  
  Strip all information from options besides `editable`.
- Refactor remote-entity create payload:
  - Add custom_codeset options to specify optional manufacturer and device type.
  - Remove options wrapper object for codeset_id.

## v0.11.3-alpha - 2022-08-19
### Added
- WebSocket `profile_change` event for profile, page and group modifications.
### Fixed
- Simulator: HTTP status code 200 for `GET /profiles/{profile_id}`.

## v0.11.2-alpha - 2022-08-12
### Added
-  Add `description` field in profile group.
### Fixed
- Use `GB` as default localization country if localization settings are reset.

## v0.11.1-alpha - 2022-08-11
### Changed
- Default localization: en_GB, UK, UTC, 24h, METRIC
- Core-API definitions:
  - Creating a profile page only requires the page name as mandatory message payload. Only the OpenAPI definition is affected,
    the implementation already accepted the single name field as message payload. New message object: PageCreate.
### Fixed
- Simulator implementations:
  - Creating multiple pages in a profile.
  - ActivitySequence serialization: use `type` as specified in OpenAPI (instead of `sequence_type`).
  - Default localization settings changed to use a valid timezone. Default is now: en_GB, UK, UTC, 24hour, METRIC.

## v0.11.0-alpha - 2022-08-07
### Added
- Core-API definition:
  - Activity & remote-entity user interface: optional page name.
- Simulator implementation:
  - Remote entity get & update endpoints.
  - Initial validation checks for updating activity, macro, and remote-entities.
  - Dummy implementations for remote ir endpoints with a static dataset.
### Changed
- Simulator implementations:
  - Major dependency updates in the web frameworks.
### Fixed
- Core-API definitions:
  - Integration driver & instance command enums: all commands are uppercase.
  - Remote update payload: align `button_mapping` and `user_interface` with activities & macro, add missing `ir` object.
  - Activity & remote-entity user interface: missing pages array for the defined user interface items.
  - Payload for updateRemoteIrCode may only contain value & format. Remaining properties are calculated.

## v0.10.6-alpha - 2022-08-03
### Added
- New query parameters to retrieve integration drivers: `instantiable`, `single_device`, `has_instances`

## v0.10.5-alpha - 2022-07-31
### Added
- Simulator implementations:
  - Retrieve IR emitter devices & send IR command in a codeset.
  - Search manufacturers and IR code sets with a test data set including the following manufacturers:  
    Apple, Bang & Olufsen, Bowers & Wilkins, Denon, LG, Philips, Samsonite, Samsung, Sony
- Core-API definitions:
  - Add optional `active` query parameter for IR emitter devices.
  - Add endpoint to retrieve an emitter device by id.
### Changed
- Core-API refactoring:
  - Send emitter command: Payload must include reference to codeset_id, cmd_id and port_id.
  - Dedicated definition for `active` query parameter.
  - Dedicated definition for `emitter` data object.
### Fixed
- CORS handling of custom `pagination-*` headers.

## v0.10.4-alpha - 2022-07-30 - internal release only

## v0.10.3-alpha - 2022-07-28
### Added
- Simulator implementations:
  - Activity update implementation with basic validations.
  - Macro retrieval and update implementations with basic validations.
  - Create a remote entity
  - Retrieve remote entity overview and single entity, but returned entity payload is not yet fully implemented!
  - Manufacturer IR codeset search implementation.
- Core-API definitions:
  - Remote-entity payload definitions
  - Infrared codeset definitions
  - Dedicated endpoint for IR code management & editing
  - IR emitter device retrieval response payload definition

## v0.10.2-alpha - 2022-07-26
### Added
- Activity and macro data objects: add integration name & icon to included_entities.
- Initial command metadata retrieval implementation.
### Changed
- Changed entity command metadata integer parameter to number.

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
