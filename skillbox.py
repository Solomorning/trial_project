from collections import Counter
from copy import deepcopy


def Sub_Counter(count1, count2):
    new_counter = deepcopy(count1)
    new_counter.subtract(count2)
    return new_counter


cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']
counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)
print(Sub_Counter(counter_moscow, counter_spb))
print(counter_moscow)
