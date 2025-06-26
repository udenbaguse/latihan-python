"""
Kode ini adalah salinan kode pada video Channel Udenbaguse
nonton untuk mengetahu penjelasan kode:
				https://youtu.be/wMg7j4Yz4Cw
	#atas berarti penjelasan
#kanan berarti kesalahan
"""

#kode_1

input1 = input("Masukkan angka pertama: ")
input2 = input("Masukkan angka kedua: ")

print(int(input1) + int(input2)) #konversi & operasi diprint


#kode_2

input1 = int(input("Masukkan angka pertama: ")) 				#input & konversi dalam satu variabel
input2 = int(input("Masukkan angka kedua: "))											#input & konversi dalam satu variabel

print(input1 + input2) #operasi diprint


#kode_3

input1 = input("Masukkan angka pertama: ")
input2 = input("Masukkan angka kedua: ")

#inisialisasi ulang untuk menangkap hasil konversi
input1 = int(input1)
input2 = int(input2)

print(input1 + input2) 	#operasi diprint


#kode_4

input1 = input("Masukkan angka pertama: ")
input2 = input("Masukkan angka kedua: ")

input1 = int(input1)
input2 = int(input2)

#tangkap hasil konversi dalam sebuah varibel
result = input1 + input2

print(result)
				
				
#kode_5 penanganan error untuk kesalahan user menginputkan bukan integer

try:
		input1 = input("Masukkan angka pertama: ")
		input2 = input("Masukkan angka kedua: ")

		input1 = int(input1)
		input2 = int(input2)

		#tangkap hasil konversi dalam sebuah varibel
		result = input1 + input2

		print(result) 	#operasi diprint		
				
except ValueError:
		print("input harus berupa bilangan bulat")
