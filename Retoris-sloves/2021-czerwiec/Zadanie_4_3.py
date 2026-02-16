def czyPalindrom(napis):
    return napis == napis[::-1]

def HasloPalindronow():
    file = "napisy.txt"
    haslo = ""
    with open(file,"rt") as data:
        for i in data:
            row = i.strip()
            poczatek = row[0]
            koniec = row[len(row)-1]
            test_pldrm = row + poczatek
            if czyPalindrom(test_pldrm):
                haslo += test_pldrm[len(row)//2]
                continue

            test_pldrm = koniec + row
            if czyPalindrom(test_pldrm):
                haslo += test_pldrm[len(row)//2]

    return haslo


