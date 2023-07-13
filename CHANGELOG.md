# Core-Simulator Changelog
All notable changes to this project will be documented in this file. The release version number relates to the 
`unfoldedcircle/core-simulator` Docker image.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased
### Added
- WS Core-API: 
  - IR repeat support for remote-entity to use new continuous IR repeat feature.
    - new `cmd_id: stop_send` command to stop an active IR repeat command
    - optional `repeat` parameter for `cmd_id: send`
  - `get_entity_command_metadata` message to retrieve meta-information about the entity commands. This is equivalent to
    `GET /api/cfg/entity/commands`.
- REST Core-API: enhance IR emitters with repeat option and `stop_send` endpoint.
### Breaking changes
- Profile pin refactoring in Core-API:
  - There are no longer "protected" profiles with individual pins, but "restricted" profiles intended for guests and children.
  - Restricted profiles require the admin pin to switch to other profiles.
  - The configuration settings has now a profile setting for the admin pin (web-configurator implementation will follow soon).
### Changed
- Core-API: more metadata information in `DockFirmwareUpdate` and `DockConfiguration` objects like revision and serial.

---

## v0.29.1-alpha - 2023-07-04
### Added
- Configure multiple entities from an integration
- Configure all available entities from an integration
- Remove multiple configured entities
- Remove all configured entities from an integration
- Filter available and configured entities by multiple entity types
- Filter configured entities by multiple integration IDs
- Full text search for available and configured entities.
  - Available entities: search in entity name, entity identifier and area.
  - Configured entities: search in entity name, entity identifier and integration name.
### Breaking changes
- `entity_change` event message doesn't require `entity_id` anymore and is now optional!
- The following Core WS message fields and REST query parameters were renamed:
  - WS: entityFilter fields have changed to `integration_ids` & `entity_types`
  - WS: availableEntityFilter `entity_type` field has been renamed to `entity_types`
  - REST: available & configured entities query parameter `entity_type` renamed to `entity_types`
  - REST: configured entities query parameter `intg_id` renamed to `intg_ids`
### Fixed
- Simulator Docker image: missing libdbus library for slipped in DBus dependency in the Simulator build.

## v0.28.0-alpha - 2023-06-14
### Added
- Initial IR codeset UI page mappings in IR entity
### Fixed
- web-configurator 0.10.3
  - load max 100 remote entities instead of 10
  - language texts without an english entry
- Map power toggle in IR remote entity to physical button
- Update icon mapping metadata

## v0.27.0-alpha - 2023-06-11
### Added
- Core-API: expert network settings for reconnect handling
### Fixed
- web-configurator 0.10.2: handle all integration states
### Changed
- Physical device only:
  - mDNS hostname lookup & IP caching
  - Reconnection logic for docks & external integrations

## v0.26.1-alpha - 2023-06-05
### Added
- Core-API: add `power_supply` flag in BatteryStatus to indicate if the remote is connected to a charger.  
  The `status` field is not sufficient. The battery may still temporarily discharge, even if it is in the docking station.
- Provide Bluetooth MAC address in `GET /api/cfg/network`.
### Fixed
- Add `jpeg` to resource upload metadata field `file_formats` for Firefox & Safari to be able to upload .jpeg files in
  the web-configurator. Only Chrome treats jpeg files automatically as jpg.
- Only connect configured integration drivers and during setup.

## v0.26.0-alpha - 2023-06-01
### Added
- web-configurator 0.10.1:
  - Custom IR code dataset CSV upload & download.
  - Force re-load entities from an integration.
### Fixed
- Don't expose integration setup password field values in Core API.
- web-configurator: many small fixes again.
### Changed
- Service discovery, using OS services for mDNS resolving. Simulator version still uses 3rd party application library. 

## v0.25.3-alpha - 2023-05-31
### Fixed
- Add content-disposition to CORS exposed headers for CSV file download in web-configurator.

## v0.25.2-alpha - 2023-05-25

### Added
- REST Core-API: bulk CSV export of custom IR datasets.
### Fixed
- web-configurator 0.8.0:
  - general fixes, dock state update handling.
  - IR device search now properly searches in the core and doesn't just show generic code sets.  
    Note: the Simulator only includes a few dummy manufacturer & device entries!

## v0.25.1-alpha - 2023-05-24
### Fixed
- Filter invalid characters in manufacturer search to prevent internal server errors.
- web-configurator 0.7.0: many small fixes and enhancements with focus on IR remotes.

## v0.25.0-alpha - 2023-05-23
### Added
- REST Core-API:
  - bulk CSV import of custom IR datasets.
  - IR code search: return custom flag for user code sets.
### Fixed
- Removing a custom Dock URL will reconnect to the default service URL. Service restart is no longer required.
- OpenAPI definition of the HealthStatus object reference.
### Changed
- Core-API:
  - Updating a dock with an empty `custom_ws_url` value will remove the custom URL.
  - IR device query requires at least 2 characters.
  - Allow more custom characters in IR key.

## v0.24.0-alpha - 2023-05-18
### Added
- Core-API:
  - WebSocket event `wifi_change` to notify about WiFi events like connected / disconnected from network.
  - Enhance NetworkState with `OUT_OF_RANGE`. 
  - Provide WiFi network signal level and secured flag in saved networks, if they are in range.
### Fixed
- Initial workaround for mDNS `openthread.thread.home.arpa.` request flooding if a newer Apple TV is on the network
  (and probably other devices as well).
- Web-configurator 0.5.0: showing errors on form elements, 
### Changed
- Core-API:
  - IR code key now also allows lower case letters.

## v0.23.2-alpha - 2023-05-08
### Added
- Core-API:
  - Enhanced software update configuration with OTA update window & channel.
  - Returning next scheduled auto-update check date in available system updates response.
  - Returning `restart_required` flag in configuration response.
### Fixed
- Web-configurator 0.5.0: design fixes, esc key, filtering entities from lists where not required / usable, version information.
### Changed
- Home Assistant demo server:
  - Update to 2023.5.2
  - Remove non-working San Francisco Intl FAA Delays integration

## v0.23.1-alpha - 2023-04-29
### Added
- Core-API:
  - New force dock firmware update check operation.
  - Retrieve battery status and WebSocket `battery_status` event.
  - Get current system power mode, set a power mode, and WebSocket `power_mode_change` event.
  - Get current ambient light reading from light sensor and WebSocket `ambient_light_change` event during normal power mode.
  - WebSocket warning event for important system events like low battery or shutdown.
- The force system update check `PUT /api/system/update` will now contact an Unfolded Circle cloud update server.
  - Auto-update checks & installation are not active in the Simulator. Only the manual force check connects to an external server.
  - The `GET` operation only returns already downloaded information.
  - The simulator cannot be updated with our update server.
- Web-configurator: sequence command parameters, e.g. setting light brightness
### Fixed
- REST Core-API:
  - Proper object definition of `IrEmitterLearnStatus`
- Web-configurator: many little improvements and fixes
- Docker image: missing libssl dependency in pulled 0.23.0 release. Sorry about that!
### Changed
- REST Core-API 0.21.1 / WS Core-API 0.19.0-alpha:
  - Remove not required `cmd` parameter in integration driver connection test: `PUT /intg/discover/{driverId}`
  - Update system: new response message indicating if the update is being downloaded or installed.

## v0.22.2-alpha - 2023-03-23
### Added
- Web-configurator: improved full text search for entities and commands.
- Core-simulator: configure Dock & Integration-API WS message tracing with `UC_INTG_MSG_TRACING` env variable: `all` | `in` | `out`
- Home Assistant integration v0.2.0:
  - driver mDNS advertising and setup flow
  - initial TLS WebSocket support
  - configurable WebSocket message tracing with `UC_API_MSG_TRACING` and `UC_HASS_MSG_TRACING` env variables
- Docker: add sample background images and integration icons

### Fixed
- Simulator-VM: https image loading in remote-ui. Required OpenSSL 1.1.1 libraries were missing.
- Core-simulator: activity entity commands return all available commands.  
  - The parameterized commands like setting brightness on a light were missing.
  - Note: parameterized commands are not yet working in the web-configurator, except the delay command!

### Changed
- **Breaking change** WebSocket Core-API: `get_entity_commands` returns mapping command identifiers for `GET /api/cfg/entity/commands`

## v0.22.1-alpha - 2023-03-15
### Added
- Integration driver discovery & setup flow for external integrations:
  - Integration-API definitions and documentation with initial implementation in the core.
  - POC example in the [Node integration library](https://github.com/unfoldedcircle/integration-node-library/tree/main/examples).
- Remote-UI app v0.4.6:
  - Integration setup
  - Group switch to control the state of all entities in the group
  - Tap area for button in main screen to directly push the button without opening the entity
  - Initial loading screen during startup
  - Add shuffle and repeat icons to media player

### Changed
- Web-configurator: disabled integrations are now hidden since this is a developer feature only.
- Rust API models for integration setup flow.

### Fixed
- Docker: Mapped media folder in Core-Simulator container image for remote-ui.  
  Resource upload failed because of different filesystem devices.
- Core-simulator:
  - reset integration reconnect timeout once connected.
  - propagate button-entity state & fixed documentation.
- Remote-UI app:
  - remove entities when integration is deleted
  - multiple entity handling and display fixes
- Web-configurator:
  - remove hard-coded `en` language text access
  - search function searches all languages, not just the default and `en`
  - integration driver connection test
  - propagate setup process cancellation
  - integration setup try again button restarts setup
  - clear previously discovered integration drivers before starting setup
  - refresh integration screen after driver creation

## v0.21.5-alpha - 2023-03-06
### Added
- WebSocket Core-API integration discovery & setup flow functionality as in REST API.

### Changed
- Increase integration driver reconnect count to 100.

### Fixed
- Integration driver `subscribe_events` message handling.

## v0.21.4-alpha - 2023-03-02
### Added
- Download link for Core-Simulator VM.

### Fixed
- Enabled entity command execution in REST Core-API: `PUT /api/entities/:entityId/command`
- Typo in `execute_entity_command` WS Core-API.

## v0.21.3-alpha - 2023-03-02
### Added
- License information of used 3rd party components in the simulator.

### Changed
- Update HomeAssistant configuration to 2023.3.0

### Fixed
- Integration driver `authentication` message handling if the session was already authenticated, e.g. header based authentication or multiple authentication messages.
- Improved integration driver connect / disconnect error & reconnection handling.  
  Return `ServiceUnavailable` in Core-API if integration driver connection is not established.
- Send `entity_subscribe` & `_unsubscribe` messages to integration driver when a new entity is configured or removed with the Core-API.

## v0.21.2-alpha - 2023-02-28
### Added
- ENV variable to disable certificate verification for integration TLS connections.  
  Set `UC_INTEGRATION_DISABLE_CERT_VERIFICATION=true` in the `core-simulator` container to disable verification.
- ENV variable `UC_API_MSG_TRACING` to enable WebSocket Core-API message tracing:
  - `all`: enables incoming and outgoing message tracing
  - `in`: incoming messages only
  - `out`: outgoing messages only

### Fixed
- Retrieving entity states from integration driver after it sends the connected event ([#12](https://github.com/unfoldedcircle/core-simulator/issues/12)).  
  This fixes the Home Assistant sensors (and most likely other entities) to immediately show their current value.
- Missing glibc error in Home Assistant integration Docker image ([#13](https://github.com/unfoldedcircle/core-simulator/issues/13)).
- Swagger editor link in index pages for REST Core-API ([#8](https://github.com/unfoldedcircle/core-simulator/issues/8)).

## v0.21.1-alpha - 2023-02-26
### Added
- Enable activity & macro execution in simulator.
- Send `entity_change` events for all steps in an activity & macro sequence.

### Changed
- Public release of the simulator.
- Update web-configurator.

## v0.20.0-alpha - 2023-02-22
### Added
- Temporary, non-persistent UI access token to prevent lock-out when deleting user accounts or API tokens.  
  Activated with ENV variable `UC_TOKEN_PATH` specifying an absolute file location to write the token.
- Simulated factory reset and most system commands.

### Changed
- From now on the Simulator is only distributed as Docker image.
- Enforce WS Core-API authentication and auto-disconnect after 15s if not authenticated.

### Fixed
- Name clash of simulated IR emitter and simulated dock. Adding a simulated dock no longer overrides the IR emitter.
- Dock discovery no longer returns the simulated Bluetooth dock if BT is disabled.
- Simulated Bluetooth dock setup flow works again.
- [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5) compliant date-time values. Certain timestamps didn't include the timezone.
- Embed swagger js & css files in the Docker image Core-API OpenAPI packaging and don't rely on external downloads.

## v0.19.1-alpha - 2023-02-15
### Added
- Include web-configurator preview
- Core API: system update check & installation

### Changed
- Disable Bluetooth handling in Simulator. Bt dock discovery is only simulated.

### Fixed
- Graceful shutdown
- Missing dependencies in Simulator Docker image
- Propagate disabled Bluetooth state in dock discovery

## v0.18.0-alpha - 2023-01-11
### Added
- WiFi management with REST & WS Core-API
- Dock handling with WS Core-API
- Bluetooth dock setup flow on Linux

## v0.17.0-alpha - 2022-12-23
### Added
- Full dock setup flow with physical docks.
- WebSocket `dock_state` and `dock_change` event messages.

### Changed
- Remove dock configuration after dock factory reset.

### Fixed
- Clear dock device discovery only when starting a new discovery but not when manually stopping the discovery.
- Propagate all dock configuration changes to physical dock device.
- Reconnect to dock after cfg change (e.g. new WiFi settings or token change).
- Dock URL handling from provided dock address, which can either be a hostname, IP address or WS URL.

## v0.16.6-alpha - 2022-12-12
### Added
- Validation error details for status code 400 in `ValidationErrorResponse`. If validation error details are available,
  they are returned to the client, describing which field(s) are invalid, instead of a generic error description.
### Fixed
- Remote button mapping: assign a custom IR command is no longer rejected.

## v0.16.5-alpha - 2022-12-05
### Added
- IntegrationState enum instead of untyped string.
- Add pwd_protected field to IntegrationDriver object.
### Fixed
- Clear integration driver discovery data only at discovery restart, not when stopping it.

## v0.16.4-alpha - 2022-11-28
### Added
- Save integration at end of integration setup flow. The setup flow cannot be started again if the integration already exists.
### Fixed
- Virtual docks (model `UCD2_VIRTUAL`) are always connected and don't return errors when sending commands.
- IntegrationState enum instead of untyped string

## v0.16.3-alpha - 2022-11-27
### Added
- REST Core-API v0.16 integration setup flow:
  - Integration discovery with `/intg/discover` endpoints.
  - Integration setup with `/intg/setup` endpoints.
  - Integration driver connection test command.
  - State field in integration driver & instance data objects. The state was only returned in `GET /intg` until now.
- Demo integration setup flows in Simulator:
  - The simulator defines a few integration drivers with setup data schemas & icons. See Postman collection examples
    defined in `integrations/setup`.
  - Defined external drivers in discovery:
    - `sim-foobar`: requires driver setup data, without setup flow user interaction
    - `sim-test`: no driver setup data, user input screen with single text input
    - `sim-intg`: no driver setup data, user input screen during setup flow with dropdown, text, number inputs
  - Defined local drivers:
    - `uc:bo`: no driver setup data, without setup flow user interaction
    - `uc:homey`: requires driver setup data, without setup flow user interaction
    - `uc:hue`: no driver setup data, with user confirmation page in setup flow
  - ⚠️ After a successful integration setup flow the integration instance is not yet persisted! This will be implemented
       in a future release.
- WS Core-API v0.12:
  - `integration_discovery` & `integration_setup_change` event messages.
- Include a set of default icons for integrations and background images, accessible with `/resources/:type`.  
  ⚠️ **Delete old Docker volume to enable the included resource files.**
### Changed
- REST Core-API integration handling:
  - Refactored integration overview data returned in `GET /intg`:  common `state` property.
    - Deprecated fields `driver_state` and `device_state`. They will soon be removed in the response.
  - Manual driver registration now fetches metadata from running driver, instead of providing all data during registration.
  - Move `PUT /intg` operation to connect / disconnect integrations to `/intg/instances`.
  - Declare `enabled` flag for development use only.

## v0.15.6-alpha - 2022-11-15
### Changed
- REST Core-API: manually set up a dock with the dock setup flow
  - CreateDockSetup is now a oneOf object for either a discovered dock (same structure as before) or a manual setup.
  - Manual setup uses the existing `DockSetup` object in the `POST /docks/setup` request and then automatically starts
    the setup process without calling `PUT /docks/setup/:dockId`.
- If a dock setup process is already running, it can't be aborted with another POST request and returns 409.

## v0.15.5-alpha - 2022-11-11
### Changed
- Use uppercase dock state enum values to use same naming pattern as for entities and integrations.

## v0.15.4-alpha - 2022-11-09
### Changed
- PRONTO hex code validation now also allows non-zero prefixed values.
### Fixed
- Simulated emitter learning returns proper PRONTO hex codes. 

## v0.15.3-alpha - 2022-11-09
### Added
- REST Core-API: add custom IR code payload to `PUT /ir/emitters/:deviceId/send` to send learned IR codes.
### Changed
- Enhance documentation of Core-API dock endpoints.

## v0.15.2-alpha - 2022-11-06
### Added
- REST Core-API:
  - `HEAD /docks` endpoint to retrieve number of configured docks.
  - Add `IDENTIFY` command to `POST /docks/devices/:dock_id/command`.
  - Add `connection_type` and `version` fields to dock data in `GET /docks` and `GET /docks/devices/:dock_id`.
  - Simulate dock bluetooth discovery & setup.
  - Simulate dock firmware update.
  - Dock update abort operation `DELETE /docks/devices/:dock_id/update`.
### Changed
- REST Core-API:
  - Remove `token` requirement for `RESET` command in `POST /docks/devices/:dock_id/command`.

## v0.15.1-alpha - 2022-11-05
### Added
- Dock firmware event message `dock_update_change`.
### Changed
- Core-API dock object refactoring.
  - Use constant naming, `dock_id` everywhere instead mix and match with `service_name`.
  - Return dock model as string to clearly identify dock.
  - Use a single command to set dock brightness.

## v0.15.0-alpha - 2022-11-04
### Added
- REST Core-API: dock discovery, setup and update endpoints
  - Implemented dock network discovery. The simulated device `sim.1` will always be returned, no physical docking station is required.  
    Bluetooth discovery will be added later. 
  - Dock setup flow is simulated. Does not yet work with real devices.
  - Dock firmware update check is simulated. Update function will be added in the next release.
### Fixed
- Docker image: updated to Debian testing due to new glibc requirements.

## v0.14.1-alpha - 2022-10-27
### Added
- Validate IR codes, formats, manufacturers and devices. An IR code value must now in the correct PRONTO or HEX format.
### Changed
- Restricted valid characters in custom IR keys to upper case, dash, underscore and dot only. Lower case characters are no longer valid.
### Fixed
- OpenAPI definition: fixed invalid regex format patterns (dash character needs escaping).

## v0.14.0-alpha - 2022-10-17
### Added
- REST Core-API: IR learning with emitters. New endpoint: `/ir/emitters/{emitterId}/learn`.
  - New WebSocket event `ir_learning` for IR learning events: start / learn / stop.
  - Enhance `Emitter` data object with new fields:
    - `type`: type of IR emitter (docking station, IR blaster, other)
    - `capabilities`: optional features of an emitter like IR learning (not every emitter is capable of learning).
- Improve documentation of icon & image identifiers and make prefix mandatory in regex.
- Validate icon and image identifiers in create & update operations.
- Rewrite resource identifiers during upload: replace all non-valid resource-id characters with an underscore `_`.  
  Valid characters are: ASCII letters, digits, dash, underscore and dot (regex: `[a-zA-Z0-9-_\\.]`). 
### Fixed
- Add media_player commands to command definitions in `GET /api/cfg/entity/commands`.

## v0.13.7-alpha - 2022-10-03
### Fixed
- Retain activity button mappings when patching an activity entity.  
  If a button mapping has a dangling entity in a command, only the command needs to be removed and not the whole mapping.
- REST Core-API: return status code 200 for `PATCH /docks/:dock_id`.
- Setting an inactive dock to active allows starting dock connection with `POST /api/docks/:dock_id/connect`.

## v0.13.6-alpha - 2022-10-02
### Added
- REST Core-API sound resource upload:
  - Add supported channel and bit depth information in metadata.
  - Implement WAV file validation during upload.
- WS Core-API messages to control API access of the web-configurator. 
### Changed
- WS event message `profile_change`: change category from `ENTITY` to `UI`.  
  The event categories of the individual event messages are now defined in the AsyncAPI specification.
### Fixed
- Core-API: metadata information for background images. Width & height were mixed up.
- Proper error propagation for dock connection issues instead of always returning internal server error.

## v0.13.5-alpha - 2022-09-30
### Added
- Core-API resource upload:
  - Return metadata information for supported resource formats in `GET /api/resources`.
  - Check image type and size during upload when the first file chunk is received.
  - Check free disk space while uploading new resources. Add status code 507 if not enough free disk space.
### Changed
- Removing an included entity in an activity or macro removes all references in sequences and ui-pages.
- Enforce hard limits:
  - Profiles: max 30 profiles, 30 pages per profile and 30 groups per profile.
  - Ui pages: 15
  - Macros & activities: 50 steps, 50 included entities
  - Custom resources: 256 icons, 256 tv channel icons, 30 background images, 50 sound files
### Fixed
- Don't return 404 when retrieving a macro or activity where an included remote-entity has been deleted.
- Core-API resource upload:
  - Response data structure as defined in OpenAPI: resource information object instead of only resource identifier.
  - Bad Request error if upload file parameters are not correct instead of an internal server error.
  - Sound file content type: `audio/wav`

## v0.13.4-alpha - 2022-09-03
### Added
- Add `device_name` to `GET /api/pub/version` response. This allows to display the device name on the login page.
- Implement `DELETE /api/resources/:type/:resource`.
- Validate resource type file extensions when uploading files with `POST /api/resources/:type`.
### Changed
- Core-API `GET /api/pub/version` response: rename `app` to `ui` to align with WebSocket API.
- Don't allow macros and activities to include themselves. The included entities must reference other entities.
### Fixed
- Profile page rearrange after page deletion.

## v0.13.3-alpha - 2022-09-02
### Added
- Add CORS header `access-control-allow-credentials: true`.

## v0.13.2-alpha - 2022-09-01
### Added
- Enhance `entity_change` WebSocket event message with `entity_type`.

## v0.13.1-alpha - 2022-09-01
### Fixed
- Remove double `remote.send` command in the remote-entity `entity_commands` object. E.g. returned in `activities.options.included_entities.entity_commands`.
- Return correct `simple_commands` for remote-entities in activities and macros. There was still a hard coded command set.
- Entity command descriptions in `GET /cfg/entity/commands` for activity, macro and remote-entities.

## v0.13.0-alpha - 2022-08-28
### Added
- Validate IR emitter device and output port when updating a remote-entity.
### Changed
- **Breaking change**: `/api/remotes/:entityId/ir/*` endpoints no longer use a static, hard-coded test dataset.    
  All changes are now persisted. **Existing remote-entities are automatically deleted during the update!**
### Fixed
- `DELETE /api/remotes/:entityId/ui/pages` validation. Resetting remote-entity ui pages now works correctly.

## v0.12.2-alpha - 2022-08-26
### Fixed
- Core-API definition:
  - Correct invalid previous fix of `PATCH /remotes/:entityId`: revert request payload and specify correct `Remote` object response.

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
