s = 8
while s <= 9:
    e = 0
    while e <= 9:
        n = 0
        while n <= 9:
            d = 0
            while d <= 9:
                m = 1
                while m <= 1:
                    o = 0
                    while o <= 9:
                        r = 0
                        while r <= 9:
                            y = 0
                            while y <= 9:
                                els = [s, e, n, d, m, o, r, y]
                                if len(set(els)) == 8:
                                    word1 = str(s) + str(e) + str(n) + str(d)
                                    word2 = str(m) + str(o) + str(r) + str(e)
                                    left_part = word1 + " + " + word2
                                    right_part = str(m) + str(o) + str(n) + str(e) + str(y)
                                    if eval(left_part) == int(right_part):
                                        print (left_part + " = " + right_part)
                                y = y + 1
                            r = r + 1
                        o = o + 1
                    m = m + 1
                d = d + 1
            n = n + 1
        e = e + 1
    s = s + 1

