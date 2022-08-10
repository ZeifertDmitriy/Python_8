# Создайте программу для игры в ""Крестики-нолики"".
import os
from random import randint

os.system('cls')
my_list = list(range(1,10))
kon_ig = 0
tek_igrok = randint(1, 2)
hod = lambda h: 'X' if tek_igrok == 1 else 'O'
perehod = lambda tek_igrok: tek_igrok + 1 if tek_igrok == 1 else tek_igrok - 1
vic = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
while kon_ig == 0:
    os.system('cls')
    print(' ' + str(my_list[0]) + ' | ' + str(my_list[1]) + ' | ' + str(my_list[2]) + ' \n---|---|---\n'
          ' ' + str(my_list[3]) + ' | ' + str(my_list[4]) + ' | ' + str(my_list[5]) + ' \n---|---|---\n'
          ' ' + str(my_list[6]) + ' | ' + str(my_list[7]) + ' | ' + str(my_list[8]) + ' ')
    print('Игрок № ' + str(tek_igrok) + ' выберите свободное поле:')
    my_list[int(input()) - 1] = hod('1')
    for i in vic:
        if my_list[i[0]] == my_list[i[1]] == my_list[i[2]] == 'X':
            kon_ig = 1
            break
        elif my_list[i[0]] == my_list[i[1]] == my_list[i[2]] == 'O':
            kon_ig = 2
            break
        else:
            break
    tek_igrok = perehod(tek_igrok)
os.system('cls')
print(' ' + str(my_list[0]) + ' | ' + str(my_list[1]) + ' | ' + str(my_list[2]) + ' \n---|---|---\n'
    ' ' + str(my_list[3]) + ' | ' + str(my_list[4]) + ' | ' + str(my_list[5]) + ' \n---|---|---\n'
    ' ' + str(my_list[6]) + ' | ' + str(my_list[7]) + ' | ' + str(my_list[8]) + ' ')
if kon_ig == 0:
    print('Ничья')
else:    
    print('Игрок № ' + str(kon_ig) + ' выиграл.')