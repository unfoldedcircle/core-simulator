# 3rd Party & Open Source Licenses

Unfolded Circle Remote Two software uses a number of 3rd party libraries and technologies. 

This page lists the licenses of the projects used in Remote-Core Simulator.

## Unfolded Circle Applications
### Remote-Core

- [Licenses of the Rust crates used in Remote-Core](remote-core_licenses.md)
- Linked or embedded libraries:
  - [SQLite](https://www.sqlite.org/): [Public Domain](https://www.sqlite.org/copyright.html)
  - [SWUpdate](https://github.com/sbabic/swupdate): library is released under LGPLv2.1
- Base Docker image is `debian:bookworm-slim`. See [license information linked on Docker image page](https://hub.docker.com/_/debian).

### Home Assistant Integration

- [Licenses of the Rust crates used in integration-hass](integration-hass_licenses.md)
- Base Docker image is `debian:bookworm-slim`. See [license information linked on Docker image page](https://hub.docker.com/_/debian).

### Remote-UI

The distributed remote-ui app in the simulator is a dynamically linked Qt5 application.

- The majority of the Qt modules are available under the [LGPL v3](https://www.gnu.org/licenses/lgpl-3.0.en.html) and
[GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html) open source license.
- Qt5 source code can be found on GitHub: <https://github.com/qt/qt5>
- [Licenses Used in Qt](https://doc.qt.io/qt-5/licenses-used-in-qt.html).
- Linked or embedded libraries:
  - [QR Code generator library](https://github.com/nayuki/QR-Code-generator): MIT

### Web-Configurator

- [Licenses of the web-configurator dependencies](web-configurator_licenses.md)

## Core-Simulator 3rd Party Components

The Remote Two Core-Simulator packages the following 3rd party components in the Docker compose setup:

- [Home Assistant](https://www.home-assistant.io/): [Apache License 2.0](https://github.com/home-assistant/core/blob/dev/LICENSE.md)
- Google fonts, licensed under the [Open Font License](https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL):
  - [Poppins](https://fonts.google.com/specimen/Poppins)
  - [Space Mono](https://fonts.google.com/specimen/Space+Mono)

Developer VM:

- Using Ubuntu 22.04. See [Ubuntu legal terms and conditions](https://ubuntu.com/legal).
- See [Linux Runtime Installation](../linux-vm/install.md) for installed components.
- Setup with VirtualBox and exported as OVA image. See [Virtual Box Licensing FAQ](https://www.virtualbox.org/wiki/Licensing_FAQ).
- VirtualBox Guest Additions are licensed under the GPLv2.
