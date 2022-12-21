m0 = [96, 60, 68, 91, 83, 57, 85]
m1 = [75, 78, 68, 81, 73, 99]
m2 = [69, 86, 67, 55, 96, 69, 94, 85]
m3 = [88, 75, 74, 98, 80]
m4 = [82]
m5 = [72, 92, 92]
m6 = [74, 61]
m7 = [76, 86, 83, 55]

m0count, m1count, m2count, m3count, m4count, m5count, m6count, m7count = 0, 0, 0, 0, 0, 0, 0, 0

for i in range(20):
    while len(m0) > 0:
        m0count += 1
        item = m0.pop(0)
        test = int(item * 2 / 3)
        if test % 17 == 0:
            m2.append(test)
        else:
            m5.append(test)
    while len(m1) > 0:
        m1count += 1
        item = m1.pop(0)
        test = int((item + 3) / 3)
        if test % 13 == 0:
            m7.append(test)
        else:
            m4.append(test)
    while len(m2) > 0:
        m2count += 1
        item = m2.pop(0)
        test = int((item + 6) / 3)
        if test % 19 == 0:
            m6.append(test)
        else:
            m5.append(test)
    while len(m3) > 0:
        m3count += 1
        item = m3.pop(0)
        test = int((item + 5) / 3)
        if test % 7 == 0:
            m7.append(test)
        else:
            m1.append(test)
    while len(m4) > 0:
        m4count += 1
        item = m4.pop(0)
        test = int((item + 8) / 3)
        if test % 11 == 0:
            m0.append(test)
        else:
            m2.append(test)
    while len(m5) > 0:
        m5count += 1
        item = m5.pop(0)
        test = int((item * 5) / 3)
        if test % 3 == 0:
            m6.append(test)
        else:
            m3.append(test)
    while len(m6) > 0:
        m6count += 1
        item = m6.pop(0)
        test = int((item * item) / 3)
        if test % 2 == 0:
            m3.append(test)
        else:
            m1.append(test)
    while len(m7) > 0:
        m7count += 1
        item = m7.pop(0)
        test = int((item + 4) / 3)
        if test % 5 == 0:
            m4.append(test)
        else:
            m0.append(test)

counting = [m0count, m1count, m2count, m3count, m4count, m5count, m6count, m7count]
counting.sort()
print(counting[-1] * counting[-2])
