from collections import deque


def maximize_geodes(blueprints, time_limit):
    # Parse the blueprints to get the cost and maximum number of geodes for each blueprint
    blueprint_costs = {}
    blueprint_geodes = {}
    for blueprint in blueprints:
        lines = blueprint.strip().split('\n')
        costs = {}
        geodes = 0
        for line in lines:
            tokens = line.split()
            resource = tokens[1]
            cost = int(tokens[3])
            if resource == "geode":
                geodes = int(tokens[5])
            else:
                costs[resource] = cost
        blueprint_costs[blueprint] = costs
        blueprint_geodes[blueprint] = geodes

    # Initialize the queue with the initial state (1 ore robot, 0 of each other type of robot)
    queue = deque([(1, 0, 0, 0)])
    max_geodes = 0

    # Perform the breadth-first search
    while queue:
        state = queue.popleft()
        ore, clay, obsidian, geode = state
        time_elapsed = ore + clay + obsidian + geode
        if time_elapsed > time_limit:
            continue
        for blueprint, costs in blueprint_costs.items():
            ore_cost = costs.get("ore", 0)
            clay_cost = costs.get("clay", 0)
            obsidian_cost = costs.get("obsidian", 0)
            if ore >= ore_cost and clay >= clay_cost and obsidian >= obsidian_cost:
                new_ore = ore - ore_cost
                new_clay = clay - clay_cost
                new_obsidian = obsidian - obsidian_cost
                new_geode = geode + blueprint_geodes[blueprint]
                queue.append((new_ore, new_clay, new_obsidian, new_geode))
                max_geodes = max(max_geodes, new_geode)

        # Collect resources
        ore += ore
        clay += clay
        obsidian += obsidian

    return max_geodes


# Test the function
blueprints = []
with open('day19input.txt') as f:
    for line in f:
        blueprints.append(line)

time_limit = 24
print(maximize_geodes(blueprints, time_limit))
# Output: 12
