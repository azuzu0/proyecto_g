
# for line in open("files/cardWhite.txt"):
#     print(line)

archivo = open("files/cardWhite.txt", encoding="utf-8")  
a = archivo.readlines()
# b = archivo.read()

print(a)
# print(b)