print("pilih operasi")
add = "1. tambah"
subtract = "2. kurang"
multiply = "3. kali"
devided = "4. bagi"
print(f"{add}\n{subtract}\n{multiply}\n{devided}")

input_user = input("masukkan pilihan sesuai nomor(1/2/3/4):  ")
input_user = int(input_user)

if 1<=input_user<=4:
    input1 = input("masukkan angka pertama:  ")
    input2 = input("masukkan angka kedua:  ")
    number1 = float(input1)
    number2 = float(input2)
    
    add         = number1 + number2
    subtract    = number1 - number2
    multiply    = number1 * number2
    
    if input_user == 1:
        print(f"{number1} + {number2} =",add)
    elif input_user == 2:
        print(f"{number1} - {number2} =",subtract)
    elif input_user == 3:
        print(f"{number1} x {number2} =",multiply)
    elif input_user == 4:
        """
        #Without Ternary
        if number2 == 0:
            print(f"{number1} : {number2} = Tidak Terdefinisi")
        else: 
            devided = number1 / number2
            print(f"{number1} : {number2} =",devided)
        """
        devided = "Tidak Terdefinisi" if number2 == 0 else number1 / number2
        print(f"{number1} : {number2} =", devided)
    
else:
     print("data yang anda masukkan salah")   
     
