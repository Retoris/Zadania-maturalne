from zadanie6a import IleSpelniaWarunek

def OsemkowyNaDziesietny(file):
    base = 8
    array = []
    with open(file,'rt',newline='\n',encoding='utf-8') as f:
        for row in f.readlines():
            row = row.strip()
            powers = len(row)-1
            intDecimal = 0
            for i in range(len(row)):
                intDecimal += base**powers * int(row[i])
                powers -= 1
            array.append(intDecimal)
    return array


def main():
    file = "dane.txt"
    transfertToDecimal = OsemkowyNaDziesietny(file)

    with open("daneDecimal.txt",'wt',newline='\n') as daneD:
        for row in transfertToDecimal:
            row = str(row)
            daneD.write(row+'\n')

    odp = IleSpelniaWarunek("daneDecimal.txt")
    with open('wyniki6.txt','at',newline='\n') as f:
        f.write(f'\n6b: {odp}')


