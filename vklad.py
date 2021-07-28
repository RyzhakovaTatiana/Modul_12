#Вам дан словарь per_cent с распределением процентных ставок по вкладам
# в различных банках таким образом, что ключ — название банка,
# значение — процент. Напишите программу, в результате которой будет сформирован
# список deposit значений — накопленные средства за год вклада в каждом из банков.
# На вход программы с клавиатуры вводится сумма money, которую человек
# планирует положить под проценты.

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print(per_cent)
money=input("Введите сумму взноса: ")
money_float=float(money)
deposit_tkb=money_float * per_cent['ТКБ']/100.0
print(deposit_tkb)

deposit_skb=money_float * per_cent['СКБ']/100.0
print(deposit_skb)

deposit_vtb=money_float * per_cent['ВТБ']/100.0
print(deposit_vtb)

deposit_sber=money_float * per_cent['СБЕР']/100.0
print(deposit_sber)
L=[deposit_tkb,deposit_skb,deposit_vtb,deposit_sber]
list_deposit=list(map(int,L))

print("Накопленные средства за год в банках ТКБ, СКБ, ВТБ, СБЕР",list_deposit)

print("Индекс максимального числа в списке: ",list_deposit.index(max(list_deposit)))
max_summa=max(list_deposit)
print("Максимальная сумма, которую вы можете заработать: ",max_summa)
