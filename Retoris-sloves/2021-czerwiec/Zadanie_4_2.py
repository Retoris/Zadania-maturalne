def PodajHaslo():
    file = "napisy.txt"
    index_hasla = 0
    haslo = ""
    with open(file,'rt') as data:
        rows = data.readlines()
        for i in range(19,1000,20):
            haslo += rows[i][index_hasla]
            index_hasla += 1
    return haslo
