def IleSpelniaWarunek(file): #Ostatnia cyfra == pierwszej
    counter = 0
    with open(file,'rt',newline='\n',encoding='utf-8') as f:
        for row in f.readlines():
            row = row.strip()
            first = row[len(row)-1]
            last = row[0]
            if first == last:
                counter += 1
    return counter

def main():
    file = "dane.txt"
    odp = IleSpelniaWarunek(file)
    with open("wyniki6.txt", 'at') as output:
        output.write(f"6a: {str(odp)}")

