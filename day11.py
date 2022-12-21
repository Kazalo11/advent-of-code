m0 = [79,98]
m1 = [54,65,75,74]
m2 = [79,60,97]
m3 = [74]


m0count, m1count, m2count, m3count = 0, 0, 0, 0

for j in range(3,100):
    for i in range(20):
        while len(m0) > 0:
            m0count += 1
            item = m0.pop(0)
            test = int(item * 19 / j)
            if test % 23 == 0:
                m2.append(test)
            else:
                m3.append(test)
        while len(m1) > 0:
            m1count += 1
            item = m1.pop(0)
            test = int((item + 6) / j)
            if test % 19 == 0:
                m2.append(test)
            else:
                m0.append(test)
        while len(m2) > 0:
            m2count += 1
            item = m2.pop(0)
            test = int((item ** 2) / j)
            if test % 13 == 0:
                m1.append(test)
            else:
                m3.append(test)
        while len(m3) > 0:
            m3count += 1
            item = m3.pop(0)
            test = int((item + 3) / j)
            if test % 17 == 0:
                m0.append(test)
            else:
                m1.append(test)
    counting = [m0count, m1count, m2count, m3count]
    if counting == [99,97,8,103]:
        print(j)
        break


counting = [m0count, m1count, m2count, m3count]
counting.sort()
print(counting[-1] * counting[-2])
