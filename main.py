per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0} # Данный по условию словарь

deposit = [] # Создаем пустой список накоплений

money = float(input("Введите сумму для вклада - ")) # Получаем начальную сумму для вклада

for key in per_cent:
    percent = money * float(per_cent[key]) / 100 # Определяем накопленные средства за год для каждого банка

    deposit.append(percent) # Добавляем накопленные средства за год для каждого банка в список накоплений

print(deposit) # Выводим список накоплений

number = 0
max_number = 0
max_value = 0

for num in deposit:
    number += 1
    if num > max_value:
        max_number = number - 1
        max_value = num

print(f"Максимальная сумма, которую вы можете заработать — {deposit[max_number]}") # Выводим максимальную сумму
# print(f"Ее Вы можете заработать, если положите деньги в банк {per_cent[key(1)]}")