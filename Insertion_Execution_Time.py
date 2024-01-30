import random
import time
def insertion_sort_algorithm(array): #Inspiration from Lecture
    steps = 0
    for i in range(1, len(array)):
        key = array[i]
        j = i -1
        steps += 2 
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
            steps += 2
        array[j + 1] = key
        steps += 1
    return steps

def generate_random_array(size):
    return [random.randint(0, 100) for _ in range(size)]

input_sizes = [100, 1000, 5000, 20000, 50000, 100000]

for size in input_sizes:
    A = generate_random_array(size)
    start_time = time.time()
    steps = insertion_sort_algorithm(A)
    end_time = time.time() - start_time
    print("Size: ", size)
    print("Number of steps: ", steps)
    print("Time taken: ", end_time, "seconds")