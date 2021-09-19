#Project by Y.Yasaswini Lakshmi -(Python Programmer)

#Creating function called Swapfiledata
def Swapfiledata():
    file1 = input("Enter the file name:")
    file2 = input("Enter the file name:")

    #These lines helps to Open the first file in reading format ,  Save data in the variable
    with open(file1, 'r') as a:
         data_a = a.read()

   #These lines helps to Open the Second file in reading format ,  Save data in the variable
    with open(file2 , 'r') as b:
         data_b = b.read()

    #These lines helps to Open the first file in writing format ,  Save data in the variable
    with open(file1 , 'w') as a:
        a.write(data_b)
    
    #These lines helps to Open the Second file in writing format ,  Save data in the variable
    with open(file2 , 'w') as b:
        b.write(data_b) 
        

print()
#Project Name (Title)
print("SwapFiles Data")
print()
#DOne by ---
print("Project was done by - Y. Yasaswini Lakshmi")

Swapfiledata()

print("Data Swapped Successfully , Note : ")
print("Open the terminal on vs code and run the code on the terminal ")
print("From the project developer lakshmi")

   