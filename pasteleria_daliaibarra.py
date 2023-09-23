print('Bienvenido a la Pasteleria Delix')
print("Pasteles disponibles") 

class pasteles:
    def inicializar(self,sab,tam,pre):
        self.sabor=sab
        self.tamano=tam
        self.precio=pre
 
    def mostrar(self):
        print("Nombre del pastel: ",self.sabor,"medida:",self.tamano,"su precio es de:",self.precio)
 
 

pasteles1=pasteles()
pasteles1.inicializar("fresa delicia","chico","190")
pasteles1.mostrar()
 
pasteles2=pasteles()
pasteles2.inicializar("mango tentacion","mediano","350")
pasteles2.mostrar()

pasteles3=pasteles()
pasteles3.inicializar("chocolatei","grande","560")
pasteles3.mostrar()
 
pasteles4=pasteles()
pasteles4.inicializar("frutal","mediano","400")
pasteles4.mostrar()

pasteles5=pasteles()
pasteles5.inicializar("fantastico","chico","190")
pasteles5.mostrar()