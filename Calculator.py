def input_matrix(name):
    rows = int(input(f"Enter no of rows for {name}\n : "))
    cols = int(input(f"Enter no of columns for {name}\n : "))
    matrix = []

    print(f"Enter the elements for {name} row by row : ")
    for i in range(rows):
        while True:
            row = input(f"Row {i+1}: ").split()
            if len(row) != cols:
                print(f"Enter the exactly {cols} values.")
            else:
                matrix.append([int(x) for x in row])
                break
    return matrix

def display_matrix(matrix):
    print("Matrix: ")
    for row in matrix:
        print(" "+" ".join(f"{val:.1f}" for val in row))

def add_matrices(m1, m2):
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[0])):
            row.append(m1[i][j] + m2[i][j])
        result.append(row)
    return result   

def subtract_matrix(m1,m2):
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[0])):
            row.append(m1[i][j] - m2[i][j])
        result.append(row)
    return result

def matrix_operations():
    print("\n     === Simple Matrix Operations ===\n")
    
    m1 =input_matrix("Matrix A")
    m2 = input_matrix("Matrix B")

    print("Choose an operation : ")
    print("    0   -   Exit")
    print("    1   -   Addition ➕ ")
    print("    2   -   Subtraction ➖")
    choice = input("Enter your choice :")

    if choice == '0':
        print("   Exiting Program\n.")
        print("        Goodbye  :)")
        return
    elif choice == '1':
        result = add_matrices(m1,m2)
        display_matrix(result)

    elif choice == '2':
        result = subtract_matrix(m1,m2)
        display_matrix(result)
    
    else:
        print("Invalid choice! Please try again.")
 #  Secret Code Verification
code = input('\n🔑 Enter the secret code 🔑 : ')

if code == "shaunthegreat":
   print("\n\n  ✅ ACCESS GRANTED ✅\n" )
   while True:
      try:
         print("\nChoose : ")
         print("        0️⃣   - Exit ❌ \n")
         print("        1️⃣   - Basic Math Operations\n")
         print("        2️⃣   - MATRICES\n")
         print("        3️⃣   - maths quiz (coming soon)\n")
         ip = input("\nEnter here : ")

         if ip == '0':
            print(" \n 👋 Goodbye buddy :)\n")
            break
         if ip not in['0','1','2']:
            print("Invalid selection" )
         
            continue
         
         elif ip == '1':
            while True:
               try:
                  print("\nChoose an operation: \n")
                  print(" ➕  :  Addition \n")
                  print(" ➖  :  Subtraction \n")
                  print(" ✖️  :  Multiplication  \n")
                  print(" ➗  :  Division  \n")
                  print(" 0️⃣  :  Exit  \n\n")
                  op = input("Enter operator: ")
                  
                  if op == '0':
                     print("\n\nExiting the calculator.\n\n👋 Goodbye Buddy :)\n")
                     break
                  
                  if op not in ['+','-','*','/','0']:
                     print("Invalid operator, please try again")
                     continue
                  
                  no1 = float(input('Enter first no: '))
                  no2 = float(input('Enter second no: '))
                  
                  if op == '+':
                     result = no1 + no2
                     print(f"Result : {round(result, 2)}")
                     
                  elif op == '-':
                     result = no1 - no2
                     print(f"Result : {round(result, 2)}")
                  elif op == "*":
                     result = no1 * no2
                     print(f"Result : {round(result, 2)}")
                     
                  elif op == '/':
                    if no2 == 0:
                        print("Error: Division by zero is not allowed.")
                        continue
                    result = no1 / no2
                    print(f"Result : {round(result, 2)}")
               except ValueError:
                  print("Invalid input: please enter numeric value")
         elif ip == '2':
            matrix_operations()
            continue
      
      except ValueError:
         print("Invalid input: please enter numeric value")

else:
  print("\n\n     ❌🔒  ACCESS DENIED  🔒❌  \n\n")
        