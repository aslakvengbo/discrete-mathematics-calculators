# mod-Kalk, print
def modKalkPrint():
    print("a mod n")
    a = int(input("a: "))
    n = int(input("n: "))
    print(f"{a} mod {n} = {a % n}")



# mod-Kalk, return
def modKalk(a, n):
    return a % n



# Invers-Kalk, print
def inversKalkPrint():
    print("a^-1 mod n")
    a = int(input("a: "))
    n = int(input("n: "))
    k = 0
    A = a
    while a % n != 1:
        k += 1
        a = A
        a *= k
    if k == 0:
        k = A
    print(f"{A}^-1 mod {n} = {k}")
    


# Invers-Kalk, return
def inversKalk(a, n):
    k = 0
    A = a
    while a % n != 1:
        k += 1
        a = A
        a *= k
    if k == 0:
        k = A
    return k



# Kongruens-Kalk, print
def kongruensKalkPrint():
    print("c*x + b^k ≡ a^t (mod n)")
    c = int(input("c: "))
    b = int(input("b: "))
    k = int(input("k: "))
    a = int(input("a: "))
    t = int(input("t: "))
    n = int(input("n: "))
    
    b = b**k
    a = a**t
    
    a -= b
    x = (inversKalk(c, n) * a) % n
    print(f"x ≡ {x} (mod {n})")
    print(f"x = {x} for 0 <= x < {n-1}")


# Kongruesnssystem-Kalk, print
def kongruenssystemKalkPrint():
    
    # Antall kongrusnser
    antallKong = int(input("Antall kongruenser (3 eller 4): "))
    while antallKong not in [3, 4]:
        print("Du må skrive inn enten 3 eller 4.\n")
        antallKong = int(input("Antall kongruenser (3 eller 4): "))
    
    # Input for kongruens 1
    print("\nKongruens 1:")
    print("c_1*x ≡ a_1 (mod n_1)")
    c_1 = int(input("c_1: "))
    a_1 = int(input("a_1: "))
    n_1 = int(input("n_1: "))
    
    # Input for kongruens 2
    print("\nKongruens 2:")
    print("c_2*x ≡ a_2 (mod n_2)")
    c_2 = int(input("c_2: "))
    a_2 = int(input("a_2: "))
    n_2 = int(input("n_2: "))
    
    # Input for kongruens 3
    print("\nKongruens 3:")
    print("c_3*x ≡ a_3 (mod n_3)")
    c_3 = int(input("c_3: "))
    a_3 = int(input("a_3: "))
    n_3 = int(input("n_3: "))
    
    # Evt. input for kongruens 4
    if antallKong == 4:
        print("\nKongruens 4:")
        print("c_4*x ≡ a_4 (mod n_4)")
        c_4 = int(input("c_4: "))
        a_4 = int(input("a_4: "))
        n_4 = int(input("n_4: "))
    
    # Løser 1
    a_1 *= inversKalk(c_1, n_1)
    a_1 = a_1 % n_1
    print(f"\nKongruenssett (evt. etter beregninger):\nx ≡ {a_1} (mod {n_1})")
    
    # Løser 2
    a_2 *= inversKalk(c_2, n_2)
    a_2 = a_2 % n_2
    print(f"x ≡ {a_2} (mod {n_2})")
    
    # Løser 3
    a_3 *= inversKalk(c_3, n_3)
    a_3 = a_3 % n_3
    print(f"x ≡ {a_3} (mod {n_3})")
    
    # Evt. løser 4
    if antallKong == 4:
        a_4 *= inversKalk(c_4, n_4)
        a_4 = a_4 % n_4
        print(f"x ≡ {a_4} (mod {n_4})")
    
    # Finner M
    # Evt. M med n_4
    if antallKong == 4:
        M = n_1*n_2*n_3*n_4
    else:
        M = n_1*n_2*n_3
        
    # Finner M_n
    M_1 = int(M/n_1)
    M_2 = int(M/n_2)
    M_3 = int(M/n_3)
    # Evt. M_4
    if antallKong == 4:
        M_4 = int(M/n_4)
        print(f"\nM = {M}, M_1 = {M_1}, M_2 = {M_2}, M_3 = {M_3}, M_4 = {M_4}")
    else:
        print(f"\nM = {M}, M_1 = {M_1}, M_2 = {M_2}, M_3 = {M_3}")
    
    # Finner y_n
    y_1 = inversKalk(M_1, n_1) % n_1
    y_2 = inversKalk(M_2, n_2) % n_2   
    y_3 = inversKalk(M_3, n_3) % n_3
    # Evt. y_4
    if antallKong == 4:
        y_4 = inversKalk(M_4, n_4) % n_4
        print(f"y_1 = {y_1}, y_2 = {y_2}, y_3 = {y_3}, y_4 = {y_4}")
    else:
        print(f"y_1 = {y_1}, y_2 = {y_2}, y_3 = {y_3}")
    
    # Finner x
    # 4 kongruenser
    if antallKong == 4:
        x = a_1*M_1*y_1 + a_2*M_2*y_2 + a_3*M_3*y_3 + a_4*M_4*y_4
    # 3 kongruenser
    else:
        x = a_1*M_1*y_1 + a_2*M_2*y_2 + a_3*M_3*y_3
        
    print(f"\nx ≡ {x} (mod {M})\nx ≡ {x % M} (mod {M})")
    print(f"\nx = {x % M}, for 0 <= x < {M-1}")
    


# Kongruesnssystem-Kalk, return
def kongruenssystemKalk(Kongruens_1, Kongruens_2, Kongruens_3, Kongruens_4=[]):
    
    # Kongruens_n skal være en liste der kongruensen c_n*x ≡ a_n (mod n_n)
    # er representert ved [c_n, a_n, n_n]
    
    # Dersom kongruenssystemet kun har 3 kongruenser;
    # ikke sett en parameter for Kongruens_4 (evt. sett Kongruens_4 = [])
    
    # Input for kongruens 1
    c_1 = Kongruens_1[0]
    a_1 = Kongruens_1[1]
    n_1 = Kongruens_1[2]
    
    # Input for Kongruens 2
    c_2 = Kongruens_2[0]
    a_2 = Kongruens_2[1]
    n_2 = Kongruens_2[2]
    
    # Input for Kongruens 3
    c_3 = Kongruens_3[0]
    a_3 = Kongruens_3[1]
    n_3 = Kongruens_3[2]
    
    # Evt. Input for Kongruens 4
    if Kongruens_4 != []:
        c_4 = Kongruens_4[0]
        a_4 = Kongruens_4[1]
        n_4 = Kongruens_4[2]
    
    # Løser 1
    a_1 *= inversKalk(c_1, n_1)
    a_1 = a_1 % n_1
    
    # Løser 2
    a_2 *= inversKalk(c_2, n_2)
    a_2 = a_2 % n_2
    
    # Løser 3
    a_3 *= inversKalk(c_3, n_3)
    a_3 = a_3 % n_3
    
    # Evt. Løser 4
    if Kongruens_4 != []:
        a_4 *= inversKalk(c_4, n_4)
        a_4 = a_4 % n_4
    
    # Finner M
    # Evt. M med n_4
    if Kongruens_4 != []:
        M = n_1*n_2*n_3*n_4
    # M uten n_4
    else:
        M = n_1*n_2*n_3
        
    # Finner M_n
    M_1 = int(M/n_1)
    M_2 = int(M/n_2)
    M_3 = int(M/n_3)
    # Evt. Finner M_4
    if Kongruens_4 != []:
        M_4 = int(M/n_4)
    
    # Finner y_n
    y_1 = inversKalk(M_1, n_1) % n_1
    y_2 = inversKalk(M_2, n_2) % n_2
    y_3 = inversKalk(M_3, n_3) % n_3
    # Evt. Finner y_4
    if Kongruens_4 != []:
        y_4 = inversKalk(M_4, n_4) % n_4
    
    # Finner x
    # 4 kongruenser
    if Kongruens_4 != []:
        x = a_1*M_1*y_1 + a_2*M_2*y_2 + a_3*M_3*y_3 + a_4*M_4*y_4
    # 3 kongruenser
    else:
        x = a_1*M_1*y_1 + a_2*M_2*y_2 + a_3*M_3*y_3
    return f"{x % M} (mod {M})"



# Bruksmanual for funksjonene:

# 1. modKalkPrint() for å bli forespurt en mod
# og deretterdirekte printe ut:
#  løsningen b på formen a mod n = b.

# 2. modKalk(a, n) for å returnere:
# b ved "a mod n = b".

# 3. inversKalkPrint() for å bli forespurt en invers
# og deretter printe ut:
# inversen til a på formen "a^-1 ≡ k (mod n) + liten begrunnelse".

# 4. inversKalk(a, n) for å returnere:
# inversen til a ved "a^-1 mod n = k".

# 3. kongruensKalkPrint() for å bli forespurt en kongruens
# og deretter printe ut:
# løsningen x av en kongruens på formen c*x + b^k ≡ a^t (mod n).
# NB: Sett b = 0 om b ikke forekommer, c = 1 om x ikke har en faktor
# og k,t = 1 om b,a ikke har eksponent.

# 5. kongruenssystemKalkPrint() for å blir forespurt et kongruenssystem
# og deretter printe ut:
# løsnigen x av et system med 3 eller 4 kongruensKongruenser.
# Her printes også utregningene for bla. M, m_n og y_n!

# 6. kongruenssystemKalk(K_1, K_2, K_3, K_4=[]) for å returnere:
# løsnigen x (mod M) av et system med 3 eller 4 kongruenser.
# Her skal K_n skal være en liste der kongruensen c_n*x ≡ a_n (mod n_n)
# er representert ved [c_n, a_n, n_n]