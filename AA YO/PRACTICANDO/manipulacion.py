# path = r"C:\Users\nicol\OneDrive\Escritorio\informatica\hola_como_estas.txt"

# with open(path, "r+") as file:
#     leer_archivo = file.read()
#     print(leer_archivo)
    
#     lineas = file.readlines()
#     print(lineas)

#     coso = file.readline(2)
#     print(coso)
    
#     file.write("\nHola")

# path_nuevo =  r"C:\Users\nicol\OneDrive\Escritorio\informatica\archivo_de_preueba.txt"

# with open(path_nuevo, "a") as coso:
#     coso.write("\nKAKAKAAKAKAAKAKAKA")


#Ejercicio 6
#Realizá un programa que lea un archivo,
#elimine todos los saltos de línea y 
#lo guarde en otro archivo.
import re

path2 = r"C:\Users\nicol\OneDrive\Escritorio\informatica\archivo_coso.txt"
path1 = r"C:\Users\nicol\OneDrive\Escritorio\informatica\hola_como_estas.txt"
with open (path1,"r") as file:
    texto = file.read()
    with open (path2,"a") as file2:
        file2.write(re.sub("\n","",texto))
