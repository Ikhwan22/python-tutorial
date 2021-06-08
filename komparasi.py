# 'is' sebagai komparasi object identity


#assignment
x = 5 
y = 5
z = 6

print("\n object identity 'is' \n")
hasil = x is y
print("x = ", x, " id = ", hex(id(x)))
print("y = ", y, " id = ", hex(id(y)))
print(hasil)
'''
  kesimpulan 
  => 'is' memasukan nilai pada memori yang sama
  => 'is' akan eror jika perbandingan dengan nilai literal 
'''

print("\n object identity 'is not' \n")
hasil = x is not y
print("x = ", x, " id = ", hex(id(x)))
print("y = ", y, " id = ", hex(id(y)))
print(hasil)

hasil = x is not z
print("x = ", x, " id = ", hex(id(x)))
print("z = ", z, " id = ", hex(id(z)))
print(hasil)