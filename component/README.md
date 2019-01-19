# Environmental Data Collector&Publisher

- periodically get `temperature`, `humidity` and `pressure` from [Thingy](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/Nordic-Thingy-52),

- publish data via `MQTT broker`  on single topic `domoticz/in` which has the following format:

  ```json
  {
      "idx": <id>,
      "svalue": "<temperature>;<humidity>;0;<pressure>;0",
      "nvalue": 0
  }
  ```

**Note**: 

- `id` - identifier of the device registered in [domoticz](../domoticz).

## Requirements

- [bluepy](https://github.com/IanHarvey/bluepy)
- [paho-mqtt](https://github.com/eclipse/paho.mqtt.python)

## How to use

1. Update firmware on Thingy using [mobile application](https://www.nordicsemi.com/Software-and-Tools/Development-Tools/Nordic-Thingy-52-App).
2. Provide `.secrets` (check `.secrets.template`). Watch out: `topic` parameter in`.secrets.template` is obsolete, because the topic is always `domoticz/in`.
3. Configure script: `config.json`.
4. `python main.py`
