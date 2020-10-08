a1 = 0
while a1 <= 9:
    a2 = 0
    while a2 <= 9:
        a3 = 0
        while a3 <= 9:
            a4 = 0
            while a4 <= 9:
                a5 = 0
                while a5 <= 9:
                    a6 = 0
                    while a6 <= 9:
                        if a2 == a6 and a3 == a5:
                            n = str(a1) + str(a2) + str(a3) + str(a4) + str(a5) + str(a6)
                            answer = n
                            n = str(int(n) + 1).zfill(6)

                            if n[1] == n[5] and n[2] == n[4]:

                                n = str(int(n) + 1).zfill(6)
                                if n[1] == n[4] and n[2] == n[3]:
                                    n = str(int(n) + 1).zfill(6)
                                    if n[0] == n[5] and n[1] == n[4] and n[2] == n[3]:
                                        print (answer)
                        a6 = a6 + 1
                    a5 = a5 + 1
                a4 = a4 + 1
            a3 = a3 + 1
        a2 = a2 + 1
    a1 = a1 + 1

