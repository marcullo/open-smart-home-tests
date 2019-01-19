# Home Assistant

- [documentation](https://developers.home-assistant.io/en/) of framework.
- `init.sh`, `start.sh` - basic scripts (installation required first),
- `environment` - folder with test configuration.

## How to use

1. [Install](https://www.home-assistant.io/docs/installation/raspberry-pi/) *Home Assistant* on a virtual environment (default configuration).
2. Provide `secrets.yaml` in `environment` (check `secrets.yaml.template`).
3. Run `init.sh`.
4. Copy the content of `environment` to `~/.homeassistant/`.
5. [Provide](../component) a connection with *Thingy*.
6. Run `start.sh`. Home assistant should be reachable from: `localhost:8123`.
