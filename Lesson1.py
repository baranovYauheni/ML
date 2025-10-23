import random
import statistics as st
from statistics import median

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

print(numbers_list)

if len(numbers_list) > 0:
    sum_list = sum(numbers_list)
    mean = st.mean(numbers_list)
    median = st.median(numbers_list)

print(sum_list)
print(mean)
print(median)


random_number = random.randint(1, 100)
print(random_number)
while True:
    number_input = int(input("Введите число: "))
    if number_input > random_number:
        print("Lower")
    elif number_input < random_number:
        print("more")
    else:
        print("Congrat")
        break


