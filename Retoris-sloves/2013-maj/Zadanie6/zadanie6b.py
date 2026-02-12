from zadanie6a import IleSpelniaWarunek
import requests

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

    SSOurl = "https://raw.githubusercontent.com/Retoris/Zadania-maturalne/refs/heads/main/Retoris-sloves/SaveSingleOutput.py"
    response = requests.get(SSOurl)
    if response.status_code == 200:
        code = response.text
        exec(code)
        print(globals().keys())

    print(transfertToDecimal)



main()
