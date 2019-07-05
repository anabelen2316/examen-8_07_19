

class Autor(object):
    nombre =""
    apellido = ""
    identificador = 0
    nacimiento = ""


    def get_nombre(self):
        return self.nombre
    def set_nombre(self,valor):
        self.nombre = valor

    def get_apellido(self):
        return self.apellido
    def set_apellido(self,valor1):
        self.apellido = valor1

    def get_identificador(self):
        return self.identificador
    def set_identificador(self, valor2):
        self.identificador = valor2

    def get_nacimiento(self):
        return self.nacimiento
    def set_nacimiento(self,valor4):
        self.nacimiento = valor4


    def ComNombre(self):
        if self.nombre !="":
            print("Este campo esta vacio")
        else:
            print("Todo correcto")

    def ComApellido(self):
        if self.apellido != "":
                    print("Este campo esta vacio")
        else:
                    print("Todo correcto")
    """ Esta funcion comprueba el nombre """
    def ComIdentificar(self):
        if self.identificador !="":
            print("Este campo esta vacio")
        else:
            print("Todo correcto")

    def ComNacimiento(self):
        if self.nacimiento!="":
            print("Este campo esta vacio")
        else:
            print("Todo correcto")

















