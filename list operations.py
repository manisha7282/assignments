def list_operations():
    print("choose an operation:")
    print("insert")
    print("print")
    print("remove")
    print("append")
    print("sort")
    print("pop")
    print("reverse")
    print("Exit")


lst=[]
while True:
    list_operations()
    choice=input("enter the choice:")
    if choice =='insert':
        element=int(input("enter the element"))
        position=int(input("enter the position:"))
        if 0 <= position <= len(lst):
            lst.insert(position,element)
        else:
            print("invalid position")
    elif choice == 'print':
            print(lst)
    elif choice == 'remove':
        element=("enter the element to remove:")
        if element in lst:
                lst.remove(element)
        else:
                print("element not found")    


    elif choice == 'append':
        element=input("enter the lement to append")
        lst.append(element)


    elif choice == 'sort':
        lst.sort()


    elif choice == 'pop': 
        if lst:
            element=lst.pop()
            print(f"element popped:{element}")
        else:
            print("list ie empty")
    elif choice == 'reverse':
            lst.reverse()
    elif choice=="exit":
            print("exit")
            break
    else:
        print("invalid choice")  

      

                




