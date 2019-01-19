# Domoticz

- [documentation](https://www.domoticz.com/wiki/Main_Page) of framework.
- `thingy` - folder with test object.

## How to use

1. [Install](https://www.domoticz.com/wiki/Raspberry_Pi) *Domoticz* (default configuration).
2. Copy `thingy` folder to `~/domoticz/plugins/`.
3. `sudo systemctl restart domoticz.service`
4. Open `Domoticz` on web.
5. Add (`Settings/Hardware`):
   - *MQTT Client Gateway with LAN interface* (or other - to provide *MQTT* data transfer),
   - *Weather Home, Thingy*.
6. [Provide](../component) a connection with *Thingy*.
7. Open `Log`. Check if data is being collected.
8. Go to `Hardware/Devices`.
9. You should be able to see incoming data in a row with added *Thingy* device.
