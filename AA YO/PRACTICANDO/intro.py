año = "Hola"
if año == "Hola":
    print("Como estás")


año = input("Dame un año:")
if año == 2011 and año >= 2000:
    print(año)
if año != 2011 or año <= 2000:
    print("este no es mi año")



#Escribir un programa para calcular la nota final de un estudiante, teniendo en cuenta que por cada respuesta correcta el estudiante suma 4 puntos,
#por cada incorrecta se le resta 1 punto y si la respuesta está en blanco no se le suma ni se le resta.

numero_de_respuestas_correctas = int(input("nota correctas: "))
numero_de_respuestas_incorrectas = int(input("nota incorrecta:"))
nota_en_blanco = 0
nota_final = nota_en_blanco + (numero_de_respuestas_correctas*4) - (numero_de_respuestas_incorrectas*1)
print(nota_final)

lista = ["hola","como","estas"]
print("hola" in lista)

proveedores = ["Verduleria 1", "Verdu 2", "verdu 4"]

pedidos_detallado = {"Martin": 5000, "Juan": 20000, "Nicolás": 305.5}

print(pedidos_detallado.keys())
print(pedidos_detallado.values())

print(pedidos_detallado["Juan"])
pedidos_detallado["nico"] = 6000
print(pedidos_detallado)





