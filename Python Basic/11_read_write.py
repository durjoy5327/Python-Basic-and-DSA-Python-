<<<<<<< HEAD
"""
f= open("serial_killer.txt","a")
f.write("\nSujan Dipu Nafis Jabed Abir")
f.close()
"""

"""
f= open("K:\\sys.txt","r")
print(f.read())
f.close()
"""
"""
k=0
f= open("K:\\sys.txt","r")
for line in f:
     k+= len(line.split(' '))
     print(line," Total Word : ",len(line.split()) )

print(k)
f.close()
"""
with open("K:\\sys.txt","r") as f:
    print(f.read())
print(f.closed)

=======
"""
f= open("serial_killer.txt","a")
f.write("\nSujan Dipu Nafis Jabed Abir")
f.close()
"""

"""
f= open("K:\\sys.txt","r")
print(f.read())
f.close()
"""
"""
k=0
f= open("K:\\sys.txt","r")
for line in f:
     k+= len(line.split(' '))
     print(line," Total Word : ",len(line.split()) )

print(k)
f.close()
"""
with open("K:\\sys.txt","r") as f:
    print(f.read())
print(f.closed)

>>>>>>> 10cbc65009b60475ef6701b2a2dcf71afacc3cd4
