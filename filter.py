def filtered_dict(dictionary,keys):
    filtered_values = {key : dictionary[key] for key in keys if key in dictionary}
    return filtered_values
    
input_dictionary=input("enter the dictionaries:")
sample_dict=dict(item.split(":")for item in input_dictionary.split())

keys_input=input("enter the keys to filter:")
filtered_values=filtered_dict(sample_dict,keys_input)
print("filtered values:")
for key,value in filtered_values.items():
    print(f"{key}:{value}")


   
