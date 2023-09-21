class bienvenida():
  def __init__(self,precio,nombre):
      self.precio  = precio
      self.nombre = nombre
  def saludar(self):
      print(f'bienvenido {self.nombre}')
b = bienvenida('530','Dalia')
b.saludar()

class cakes:
    def __init__(self,precio):
        self.precio  = precio
    def tamaño (self, mensaje):
            print(mensaje)

mermelada = cakes (250)
gansito = cakes (250)

print ('El pastel de mermelada tiene un costo de: ', mermelada.precio)
print ('El pastel de gansito tiene un costo de: ', gansito.precio)

mermelada.tamaño  ('El precio del pastel de mermelada  es de tamaño grande')
gansito.tamaño  ('El precio del pastel de gansito es de tamaño grande')

class cakes:
    def __init__(self,sabor,precio,tamaño):
        self.sabor= sabor
        self.precio= precio
        self.tamaño= tamaño

        print(f"El pastel de {self.sabor} tiene un precio de ${self.precio} el de tamaño {self.tamaño}")

print("PASTELERIA BEATRIZ")
print("MENU")
mermelada = cakes("mermelada","530", "grande")

mermelada2= cakes("mermelada2","320", "mediano")

gansito = cakes("gansito","350","grande")

gansito2= cakes("gansito2","250", "mediano")

cereza = cakes("cereza","390", "grande")

cereza2= cakes("cereza2","149", "mediano")

pastel=input("que sabor de pastel deseas ")

size=input("que tamano deseas ")
if pastel== "mermelada":
    print("pastel de mermelada de tamaño ",size)
    if size==("grande"):
        print("costo de $530")
    if size==("mediano"):
        print("costo de $320")
if pastel== "gansito":
    print("pastel de gansito de tamaño ",size)
    if size==("grande"):
        print("costo de $350")
    if size==("mediano"):
        print("costo de $250")
if pastel== "fresa":
    print("pastel de cereza de tamaño ",size, )
    if size==("grande"):
        print("costo de $390")
    if size==("mediano"):
        print("costo de $149")

opcion=input("desea imprimir su comprobante?")
if opcion== "si":
    print("PASTELERIA BEATRIZ")
    print("sabor de pastel", cake,"tamano del pastel",size)
    if size=="grande":
        print("TOTAL: $390")
    if size=="mediano":
        print("TOTAL: $250")
    print("Que vuelva pronto")
if opcion=="no":
    print("lindo dia")






class bienvenida:
    def __init__(self,mensaje,nombre):
        self.mensaje=mensaje
        self.nombre=nombre
        print(f"{self.mensaje} seas {self.nombre}")

usuario = saludo("Hola Bienvenido","Dalia")
    