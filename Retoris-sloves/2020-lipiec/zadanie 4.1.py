"""import requests

id_main = "https://raw.githubusercontent.com/Retoris/Zadania-maturalne/refs/heads/main/Arkusze%20maturalne/2020-lipiec/DANE/identyfikator.txt?token=GHSAT0AAAAAADU6H3PL42CZWSQPFUO7F52C2MGCMHA"
main_input = requests.get(id_main).text

id_test = "https://raw.githubusercontent.com/Retoris/Zadania-maturalne/refs/heads/main/Arkusze%20maturalne/2020-lipiec/DANE/identyfikator_przyklad.txt?token=GHSAT0AAAAAADU6H3PLVEIZGHGQVXSBUOA42MGCLLA"
test_input = requests.get(id_test).text"""

def zad4_1():
    filename = "identyfikator.txt"
    solve = "Error"
    with open(filename,'rt',newline='\r',encoding='utf-8') as file:
        max = 0
        index = 0
        id_max = 0
        reader = file.readlines()
        for row in reader:
            row = row.strip()
            numer = row[3:]
            suma = 0
            numer = numer.strip()
            for cyfra in numer:
                suma += int(cyfra)
            if suma > max:
                max = suma
                id_max = index
            index += 1
        solve = reader[id_max]
    return solve

def main():
    odp = zad4_1()
    print(odp)

if __name__ == '__main__':
    main()