import random
import statistics as st

numbers_list = []
while True:
    user_input = input("ВВедите число: ")
    try:
        if user_input == "stop":
            break
        user_input = int(user_input)
        numbers_list.append(user_input)
    except ValueError:
        print("Это не число")

if numbers_list:
    sum_list = sum(numbers_list)
    mean = st.mean(numbers_list)
    median = st.median(numbers_list)

print(sum_list)
print(mean)
print(median)


random_number = random.randint(1, 100)
attempts = 0
while True:
    try:
        number_input = int(input("Введите число: "))
    except ValueError:
        print("Введите елое число")
    attempts += 1
    if number_input > random_number:
        print("Lower")
    elif number_input < random_number:
        print("more")
    else:
        print(f"Поздравляем вы угадали число {random_number}, за {attempts} попыток")
        break


