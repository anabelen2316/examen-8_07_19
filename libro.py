# Ana Reyes
from autor import *


class Libro(Autor):
    isnb = ""
    titulo = ""
    autor = 0


    def get_isnb(self):
        return self.isnb
    def set_isbn(self,valor1):
        self.isnb = valor1

    def get_titular(self):
        return self.titular
    def set_titular(self, valor2):
        self.titular = valor2

    def get_autor(self):
        return self.autor
    def set_autor(self, valor3):
        self.autor = valor3



    def computor(self):
        """ Este funciónn se comprueba que es numerico el
         campo de autor """
        if str(self.autor).isdigit():
            return True
        else:
            return ("Este campo es un codigo")


    def __init__(self,titulo,autor, isbn):
        self.autor = autor
        self.titulo = titulo
        self.isbn = isbn

# """Esta funcion comprueba que el isbn10 es valido"""
    def compisb10(self):
        if len(self.isbn)== 10:
            return True
        else:
            return ("Este campo tiene que tener 10 digitos")

# """Esta funcion comprueba que el isbn13 es valido"""
    def comisb13(self):
        if len(self.isbn) == 13:
            return True
        else:
            return ("Este campo tiene que tener 13 digitos")

# """Esta funcion comprueba que el isbn es valido con isbn10 y el isbn13"""
#     def comprobarisnb():
#         if compisb10(isbn) or comisb13(isbn) == True:
#             return True
#         else:
#             return ("Eror en los campos de Isnb")
#
#
#
#     del validarisbn(self):
#     valor = ""
#     if len(valor)> 10:
#         pass
#

#
# def isValidISBN(code):
#     code = code.replace('-', '').replace(' ', '')
#     return {
#         10: isValidISBN10,
#         13: isValidISBN13
#     }.get(len(code), lambda n: False)(code)
#
#
# def isValidISBN10(code):
#     result = False
#
#     # isbn10 string have 10 chars.
#     # First 9 chars should be numbers and the 10th char can be a number or an 'X'
#     if re.match('^\d{9}[\d,X]{1}$', code):
#         sum = 0
#
#         # result = (isbn[0] * 1 + isbn[1] * 2 + ... + isbn[9] * 10) mod 11 == 0
#         for i in range(0, 9):
#             sum += int(code[i]) * (i + 1)
#
#         sum += 10 if code[9] == 'X' else int(code[9]) * 10
#
#         result = sum % 11 == 0
#
#     return result









