import mysql.connector


mydb=mysql.connector.connect(host="localhost",user="root",password="123654",database="employee")
if mydb.is_connected():
    print("databse is connected")


mycursor = mydb.cursor()   
mycursor.execute( """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        address VARCHAR(255) NOT NULL
    )
    """)
    
mydb.commit()
name = input("Enter name: ")
email = input("Enter email: ")
address = input("Enter address: ")     
    

    
try:
        mycursor.execute( """
        INSERT INTO users (name, email, address) VALUES (%s, %s, %s)
    """
        ,(name, email, address))
        mydb.commit()
        print("User data inserted successfully.")
except mysql.connector.IntegrityError as e:
        print(f"Error: {e}")
        print("Email already exists in the database. Please choose a different email.")

mydb.close()