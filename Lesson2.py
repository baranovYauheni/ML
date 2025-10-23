import statistics as st


def filter_even(numbers):
    evens = [n for n in numbers if n % 2 == 0]
    return  evens

def calculate_stats(numbers):
    total = st.median(numbers) + st.mean(numbers)
    return st.mean(numbers), st.median(numbers), total

kort = calculate_stats(numbers)
print(kort)

def greet_users(*names):
    for i in names:
        print(f"Hello {i}")