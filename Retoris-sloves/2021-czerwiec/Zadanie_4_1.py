def IleCyfr():
    file = "napisy.txt"
    digits_amount = 0
    with open(file,"rt") as data:
        for i in data:
            for j in range(len(i)):
                if i[j].isdigit():
                    digits_amount += 1
    return digits_amount

