# Linux Runtime Installation

The following installation guide uses a minimal Ubuntu 22.04 desktop installation, but it should also work for other
Linux distributions.

We highly recommend using a dedicated virtual machine, especially if you are not yet familiar with setting up a Qt
runtime environment.

## Common

### Tools

Optional: install your favorite tools:
```bash
sudo apt update
sudo apt install -y \
  git \
  nano \
  openssh-server \
  rsync \
  unzip \
  wget
```

### Virtual Box Guest Additions

This is only required if running Virtual Box!

Prepare for VirtualBox guest edition:
```bash
sudo apt update
sudo apt install -y build-essential linux-headers-$(uname -r)
```
Afterwards mount the guest addition image in VirtualBox in menu Devices, Insert Guest Additions CD Image... and run 
`sudo ./VBoxLinuxAdditions.run` in the mounted image folder. 

## Simulator Runtime Environment

Checkout Unfolded Circle GitHub Projects:
```bash
mkdir ~/projects
cd ~/projects
git clone https://github.com/unfoldedcircle/core-api.git
git clone https://github.com/unfoldedcircle/core-simulator.git
```

Create runtime environment:
```bash
mkdir -p ~/Remote-Two/ui-env
chmod 777 ~/Remote-Two/ui-env
cp -r ~/projects/core-simulator/docker/* ~/Remote-Two/
cp -r ~/projects/core-simulator/linux-vm/pictures/* ~/Pictures/
mkdir -p ~/.local/share/applications
cp ~/projects/core-simulator/linux-vm/remote-ui.desktop ~/.local/share/applications/
```

Note: `ui-env` subdirectory is used to write the dynamic WebSocket access token for the remote-ui app.  
If you don't like 777: make the directory writeable for user id `10000` which is the core-simulator user.

Copy default media resources from core-simulator container image into bind-mounted directory so the remote-ui can directly access it:
```bash
docker run --rm -d --name temp-media  unfoldedcircle/core-simulator
docker cp temp-media:/data/upload ~/Remote-Two/
chmod -R 777 ~/Remote-Two/upload
docker stop temp-media
```

Again: 777 is quick and dirty! Files need to be rw for the core-simulator user in the container, and readable only for remote-ui.

Define remote-ui environment variables in `~/.profile`:
```bash
export UC_SOCKET_URL=ws://localhost:8080/ws
export UC_TOKEN_PATH="$HOME/Remote-Two/ui-env/ws-token"
export UC_RESOURCE_PATH="$HOME/Remote-Two/upload/media"
```

## Install Qt

The remote-ui simulator is a Qt application and requires the Qt framework library. Installing Qt with the system's
package manager usually doesn't work. We suggest using [Another Qt installer(aqt)](https://github.com/miurahr/aqtinstall)
to install the required Qt runtime.

### Install aqt installer

```bash
sudo apt install python3-pip
pip install aqtinstall
```

Add the local binary directory `~/.local/bin` to the search path (if not yet included):

1. Edit `~/.profile`
2. At the end of the file, add: `PATH="$HOME/.local/bin:$PATH"`

### Install Qt Runtime

Requirements:
- Qt version: 5.15.2
- Qt features: multimedia, qml, quick, quickcontrols2, virtualkeyboard, websockets, 

```bash
mkdir ~/Qt
aqt install-qt --outputdir ~/Qt linux desktop 5.15.2 gcc_64 -m qtvirtualkeyboard
```

Notes:
- Most Qt modules are already included in the default installation and therefore not included in the module parameter.
- See [aqtinstall docs](https://aqtinstall.readthedocs.io/en/latest/getting_started.html) for further information.

### Configure Environment

Some environment variables need to be set for the installed Qt runtime. `aqtinstall` will not set them automatically, to
not interfere with an existing installation.

```
export QT_VERSION=5.15.2
export QTDIR="$HOME/Qt/$QT_VERSION/gcc_64"
export PATH="$QTDIR/bin:$PATH"
export LD_LIBRARY_PATH="$QTDIR/lib:$LD_LIBRARY_PATH"
export QT_PLUGIN_PATH="$QTDIR/plugins"
export QT_QPA_PLATFORM=wayland
```

Attention if not using Ubuntu 22.04: `QT_QPA_PLATFORM` must be set to the correct graphical environment.  
E.g. for Lubuntu it's already set to `lxqt`. See Qt docs for more information.

If you are using a dedicated VM, you can add the required environment variables to the end of `~/.profile`. Otherwise,
it's better to create a start script for launching the simulator.

## Fonts

The remote-ui uses the following Google fonts families:

- [Poppins](https://fonts.google.com/specimen/Poppins)
- [Space Mono](https://fonts.google.com/specimen/Space+Mono)

These fonts are licensed under the [Open Font License](https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL).

### Fonts installation

Install fonts into your local `~/.fonts` directory:

```shell
mkdir -p ~/.fonts
cd ~/.fonts
wget 'https://fonts.google.com/download?family=Poppins' -O Poppins.zip
wget 'https://fonts.google.com/download?family=Space%20Mono' -O SpaceMono.zip
unzip Poppins.zip
unzip SpaceMono.zip
rm *.zip
```

## Container Runtime

The `remote-core` simulator is available as Docker image. One can either use Docker or Podman as container runtime.  
Let's use Docker for easier Home Assistant setup.  
Head over to <https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04> for
detailed instructions. In short:
```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install docker-ce
```

Add current user to docker group. Log out and back in afterwards.
```bash
sudo usermod -aG docker ${USER}
```

Install Docker Compose:
```bash
sudo apt install docker-compose-plugin
```

Depending on distribution, add `/usr/libexec/docker/cli-plugins` to your PATH in `~/.profile`.

## Home Assistant Server

If you don't already have a [Home Assistant](https://www.home-assistant.io/) installation you can easily install one in
a container to get started with the UC home-assistant integration for Remote Two.

Create configuration directory on the host: 
```bash
mkdir ~/hass_config
```

Run the container:
```bash
docker run -d \
  --name homeassistant \
  --privileged \
  --restart=unless-stopped \
  -e TZ=$MY_TIME_ZONE \
  -v ~/hass_config:/config \
  --network=host \
  ghcr.io/home-assistant/home-assistant:stable
```

Open a web browser at <http://localhost:8123> and start the onboarding.  
Afterwards go to your user profile (your name, bottom left) and create a long-lived access token to access the
Home Assistant API with the UC home-assistant integration. Copy and save it.

For further information please see: <https://www.home-assistant.io/installation/linux>

## Additional Tools

Install Postman for REST API testing:
```bash
sudo snap install postman
```

Install Firecamp for WebSocket API testing:
```bash
sudo snap install firecamp
```

