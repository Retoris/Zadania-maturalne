#wiem że to na maturze raczej nie przejdzie LOL
import Zadanie_4_1 as z4_1
import Zadanie_4_2 as z4_2
import Zadanie_4_3 as z4_3

def main():
    z_4_1_odp = z4_1.IleCyfr()
    z_4_2_odp = z4_2.PodajHaslo()
    z_4_3_odp = z4_3.HasloPalindronow()

    odp = [z_4_1_odp,z_4_2_odp,z_4_3_odp]

    for i in range(len(odp)):
        with open("wyniki4.txt",'at') as output:
            output.write(f'Zadanie 4.{i+1}: {odp[i]}\n')

if __name__ == '__main__':
    main()
