
def Ile(file):
    max = 0
    min = 100**777
    counter = 0
    with open(file,'rt') as f:
        for i in f:
            jest = True
            for j in range(1,len(i)-1):
                if int(i[j-1]) > int(i[j]):
                    jest = False
            if jest:
                counter += 1
                if max < int(i):
                    max = int(i)
                if min > int(i):
                    min = int(i)
    ar = [counter,min, max]
    return ar

def main():
    file = "dane.txt"
    ar = Ile(file)
    print(f"Liczba: {ar[0]}\nMin: {ar[1]}\nMax: {ar[2]}")
main()