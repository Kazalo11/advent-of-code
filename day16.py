def max_pressure(valves, start_valve, time_left, opened=None,previous_value=None):
    if time_left <= 0:
        return 0
    if opened == None:
        opened =set()

    max_pressure_released = 0

    # Check all the tunnels that lead from the current valve
    for next_valve in valves[start_valve]['tunnels']:

        # Calculate the maximum pressure that can be released from the next valve
        pressure = max_pressure(valves, next_valve, time_left - 2, opened,start_valve)

        # Add the pressure released from the current valve
        pressure += valves[start_valve]['flow_rate'] * (time_left-1)

        # Update the maximum pressure
        max_pressure_released = max(max_pressure_released, pressure)

    return max_pressure_released


# Test the function
valves = {
    'AA': {'flow_rate': 0, 'tunnels': ['DD', 'II', 'BB']},
    'BB': {'flow_rate': 13, 'tunnels': ['CC', 'AA']},
    'CC': {'flow_rate': 2, 'tunnels': ['DD', 'BB']},
    'DD': {'flow_rate': 20, 'tunnels': ['CC', 'AA', 'EE']},
    'EE': {'flow_rate': 3, 'tunnels': ['FF', 'DD']},
    'FF': {'flow_rate': 0, 'tunnels': ['EE', 'GG']},
    'GG': {'flow_rate': 0, 'tunnels': ['FF', 'HH']},
    'HH': {'flow_rate': 22, 'tunnels': ['GG']},
    'II': {'flow_rate': 0, 'tunnels': ['AA', 'JJ']},
    'JJ': {'flow_rate': 21, 'tunnels': ['II']}
}
time_left = 30

print(max_pressure(valves, 'AA', time_left))
