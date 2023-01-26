# x = 2

# if x:
#     print("yes")
# else:
#     print("No")

import time
import logging

start_time = time.perf_counter()

animals = ["goat", "dog", "cat", "lion", "monkey"]
price_tag = [2000, 2100, 1500, 1200, 3000]

for index, anim in enumerate(zip(animals, price_tag)): 
    print(f"{anim[0]} is {anim[1]} and is at index {index + 1}")
    

end_time = time.perf_counter()

logging.error(f"Time spent = {end_time - start_time}")