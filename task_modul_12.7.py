# Вам дан словарь per_cent с распределением процентных ставок
# по вкладам в различных банках таким образом,
# что ключ — название банка, значение — процент.
# Напишите программу, в результате которой будет сформирован
# список deposit значений — накопленные средства
# за год вклада в каждом из банков.
# На вход программы с клавиатуры вводится сумма money,
# которую человек планирует положить под проценты.

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = float(input("Enter money for deposit:"))

deposit_TKB = per_cent['ТКБ']*money/100
deposit_CKB = per_cent['СКБ']*money/100
deposit_VTB = per_cent['ВТБ']*money/100
deposit_SBER = per_cent['СБЕР']*money/100

vklad = [deposit_TKB, deposit_CKB, deposit_VTB, deposit_SBER]
deposit = list(map(round, vklad))
print("Summa nakoplenii za god", deposit)
print("-----------------")

# Добавьте в программу поиск максимального значения и его вывод на экран в формате:
# Максимальная сумма, которую вы можете заработать — deposit[i]
print("Max money: ", max(deposit))
