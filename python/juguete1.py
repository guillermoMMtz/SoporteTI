#<nombre> ha comenzado hoy su primer curso de Generation
#Se están formando como <nombre del puesto>
#Su compañero les pareció muy "adjetivo", pero su profesor era, cuando menos, <adjetivo>
#Para comer comen <comida> y <comida> mientras repasan sus notas
#Sienten <sentimeinto> pero están decididos a completar el curso

#nombre, puesto, adjetivo1, adjetivo2, comida1, comida2, sentimiento

print("Cuál es tu nombre?")
nombre = input()
print("¿Para que te estás formando en este bootcamp?")
puesto = input()
print("¿Primera impresión de tus compañeros?")
adjetivo1 = input()
print("¿Primera impresión de tu profesor?")
adjetivo2 = input()
print("¿Qué comiste hoy (platillo)?")
comida1 = input()
print("¿Y con qué lo acompañaste (acompañamiento)?")
comida2 = input()
print("¿Cómo te sientes al inciar hoy tu bootcamp?")
sentimiento = input()

print(
    nombre, "ha comenzado hoy su primer curso de Generation.",
"Se están formando como", puesto, ".",
"Su compañero les pareció muy", adjetivo1 ,"pero su profesor era, cuando menos", adjetivo2, ".",
"Para comer comen", comida1 , "y", comida2 , "mientras repasan sus notas", ".", 
"Sienten", sentimiento , "pero están decididos a completar el curso."
)

