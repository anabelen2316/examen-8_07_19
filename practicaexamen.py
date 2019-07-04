# Ana Reyes
from principalexamen import *



class Libro(object):
    isnb = ""
    titulo = ""
    autor = 0

""" Este funciónn se comprueba que es numerico
 el campo de autor"""
    def computor(self):
        if str(self.autor).isdigit():
            return True
        else("Este campo es un codigo")

    # def __init__(self)
    #
    # def __init__(self, titulo, autor, isbn):
    #     self.autor = autor
    #     self.titulo = titulo
    #     self.isbn = compisb10()






    # def get_insb(self):



    def compisb10(self):
        if len(self.isbn)== 10:
            return True
        else ("Este campo tiene que tener 10 digitos")

    def comisb13(self):
        if len(self.isbn) == 13:
            return True
        else ("Este campo tiene que tener 13 digitos")

     def comprobarisnb():
        if compisb10(isbn) or comisb13(isbn) == True:
            return True
        else ("Eror en los campos de Isnb")





class Autor():
    nombre =""
    apellido = ""
    identificador = 0
    nacimiento = ""






class Principal():
    def main(self):
        pass


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