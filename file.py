def write_file(file_name,text):
    with open(file_name,'w') as file:
        file.write(text)
def read_file(file_name):
    with open(file_name,'r') as file:
        return file.read()  

file_name="data.txt"

user_input=input("enter the text:")
same_output=write_file(file_name,user_input)
same_output= read_file(file_name)
#print("read text from file")
print(same_output)
    