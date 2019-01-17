#!/bin/bash
sigint_handler() {
    echo "Closing Home Assistant environment"
    exit
}

trap sigint_handler SIGINT

source /srv/homeassistant/bin/activate
cd /srv/homeassistant
hass
