den_nedeli = int(input('Введите число от 1 до 7: '))
if den_nedeli < 6:
    print('рабочий день')
elif den_nedeli == 6:
    print('суббота')
elif den_nedeli == 7:
    print('воскресенье')
else:
    print('Введите корректное число')