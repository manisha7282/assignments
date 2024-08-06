import numpy as np
def input_array(array_numbers):
    return np.array(list(map(int,input(array_numbers).split())))
user_input=input_array("enter the elements:")
print("original array:")
print(user_input)

user_append=input_array("enter the elements to append:")
print("appended array:")
print(user_append)
new_array=np.append(user_input,user_append)
print(new_array)