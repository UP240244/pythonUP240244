print("Exercises: Level 3")

import random

def shuffle_list(lst):
    random.shuffle(lst)
    return lst
print(shuffle_list([1, 2, 3, 4, 5]))

def generate_unique_random_numbers():
    return random.sample(range(10), 7)
print(generate_unique_random_numbers())