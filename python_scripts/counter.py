counter = hass.states.get('sensor.my_counter')

value = 0 if counter is None else int(counter.state)
hass.states.set('sensor.my_counter', value + 1)
