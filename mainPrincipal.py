# Ana Reyes
from libro import *
from autor import *



pepe = Autor()
pepe.set_nombre("Antonio")
pepe.set_apellido("Rodrigez")
pepe.set_identificador(456)
pepe.set_nacimiento("8 de diciembre del 2019")
print("Tu Nombre es :", pepe.get_nombre())
print("Tu Apellido es :", pepe.get_apellido())
print("Tu identificador es :", int(pepe.get_identificador()))
print("Tu nacimiento es en :",pepe.get_nacimiento())



librito = Libro(autor="ana",titulo="50 sombras de Ana",isbn="1234567890")
# librito.set_autor("Ana")
# librito.set_isbn("1234567890")
librito.set_titular("Ankilionatylia")
print("El autor es :", int(librito.get_autor()))
print("Tu Titulares es :", librito.get.titular())
print("El ISNB es :", int(librito.get_isnb()))





# class Principal():
#     def main(self):
#         pass
#



# def main():
#     while True:
#         fecha_entrega = input("Ingrese la fecha de entrega (ddmmyyyy): ").strip()
#         largo_fecha = len(fecha_entrega)
#         if largo_fecha > 0 and largo_fecha == 8:
#             f1 = date.today()
#             f2 = str_to_date(fecha_entrega)
#             result = diferencia(f1, f2)
#             if result > 0:
#                 # fecha correcta
#                 break
#             elif result < 0:
#                 print "Ingrese una fecha posterior a {0}".format(f1)
#         else:
#             print "Formato de fecha incorrecto!!"
#
#
# main()





