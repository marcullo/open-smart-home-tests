# Environmental Data Collector&Publisher

- periodically get `temperature`, `humidity` and `pressure` from [Thingy](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/Nordic-Thingy-52),
- publish data via `MQTT broker`  on separate channels `<topic>/<type>`.

**Note**: 

1. Publishing is being triggered by notifications received from the device.
2. `topic` can be set in `.secrets` file.

## Requirements

- [bluepy](https://github.com/IanHarvey/bluepy)
- [paho-mqtt](https://github.com/eclipse/paho.mqtt.python)

## How to use

1. Update firmware on Thingy using [mobile application](https://www.nordicsemi.com/Software-and-Tools/Development-Tools/Nordic-Thingy-52-App).
2. Provide `.secrets` (check `.secrets.template`).
3. Configure script: `config.json`.
4. `python main.py`
