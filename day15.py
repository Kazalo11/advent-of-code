
sensors = [(2288642, 2282562), (2215505, 2975419),
           (275497, 3166843), (1189444, 2115305),
           (172215, 2327851), (3953907, 1957660),
           (685737, 2465261), (1458348, 2739442),
           (3742876, 2811554), (437819, 638526),
           (2537979, 1762726), (1368739, 2222863), (2743572, 3976937),
           (2180640, 105414), (3845753, 474814), (2493694, 3828087),
           (2786014, 3388077), (3593418, 3761871), (856288, 3880566),
           (1757086, 2518373), (2853518, 2939097), (1682023, 1449902),
           (3360575, 1739100), (2904259, 1465606), (3078500, 3564862),
           (2835288, 1011055), (2998762, 2414323)]

beacons = [(1581951, 2271709), (2229474, 3709584), (626874, 3143870),
           (1581951, 2271709), (-101830, 2000000), (2882446, 1934422),
           (1581951, 2271709), (1581951, 2271709), (3133845, 3162635),
           (-101830, 2000000), (2882446, 1934422), (1581951, 2271709),
           (2229474, 3709584), (3011118, -101788), (3011118, -101788),
           (2229474, 3709584), (3133845, 3162635), (3133845, 3162635),
           (2229474, 3709584), (1581951, 2271709), (3133845, 3162635),
           (1581951, 2271709), (2882446, 1934422), (2882446, 1934422),
           (3133845, 3162635), (2882446, 1934422), (2882446, 1934422)]

# sensors = [(2, 18), (9, 16), (13, 2), (12, 14), (10, 20), (14, 17), (8, 7), (2, 0), (0, 11), (20, 14), (17, 20),
#            (16, 7), (14, 3), (20, 1)]
#
# beacons = [(-2, 15), (10, 16), (15, 3), (10, 16), (10, 16), (10, 16), (2, 10), (2, 10), (2, 10), (25, 17), (21, 22),
#            (15, 3), (15, 3),
#            (15, 3)]

xmax1 = max(beacons, key=lambda x: x[0])[0]
ymax1 = max(beacons, key=lambda x: x[1])[1]
xmin1 = min(beacons, key=lambda x: x[0])[0]
ymin1 = min(beacons, key=lambda x: x[1])[1]

xmax2 = max(sensors, key=lambda x: x[0])[0]
ymax2 = max(sensors, key=lambda x: x[1])[1]
xmin2 = min(sensors, key=lambda x: x[0])[0]
ymin2 = min(sensors, key=lambda x: x[1])[1]

xmax = max(xmax2, xmax1)
ymax = max(ymax2, ymax1)
xmin = min(xmin1, xmin2)
ymin = min(ymin1, ymin2)

# grid = [['.' for _ in range(xmin, xmax + 1)] for _ in range(ymin, ymax + 1)]

beacons2 = []
sensors2 = []

# for item in sensors:
#     grid[item[1] - ymin][item[0] - xmin] = 'S'
#     sensors2.append((item[1] - ymin, item[0] - xmin))
#
# for item in beacons:
#     grid[item[1] - ymin][item[0] - xmin] = 'B'
#     beacons2.append((item[1] - ymin, item[0] - xmin))


def find_dist(sensor: tuple, beacon: tuple) -> int:
    return abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])


# for k in range(len(sensors)):
#     man_dist = find_dist(sensors2[k], beacons2[k])
#     for y in range(len(grid)):
#         for x in range(len(grid[0])):
#             if find_dist(sensors2[k], (y, x)) <= man_dist and grid[y][x] == '.':
#                 grid[y][x] = '#'

found = True
def find_sensor():
    for y in range(4000000):
        for x in range(4000000):
            found = True
            for k in range(len(sensors)):
                man_dist = find_dist(sensors[k], beacons[k])
                if find_dist(sensors[k],(x,y)) <= man_dist:
                    found = False
                    break
            if found:
                return (x,y)




print(find_sensor())