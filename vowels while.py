def count_vowels(input_str):
    vowels="aeiouAEIOU"
    count = 0
    index = 0
    while  index< len(input_str):
        if input_str[index] in vowels:
            count+=1
        index+=1
    return count
input_str =input("enter a string")
vowels_count=count_vowels(input_str)
print(f"number of vowels in given string : {vowels_count}")        