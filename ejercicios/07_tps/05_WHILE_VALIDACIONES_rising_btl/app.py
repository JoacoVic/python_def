import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        apellido = prompt("apellido", "ingrese su apellido")
        while not apellido or not apellido.isalpha():
            apellido = prompt("Titulo", "Reingrese su apellido")

        edad = prompt("edad", "ingrese su edad (entre 18 y 90)")
        while not edad or not edad.isdigit() or int(edad) < 18 or int(edad) > 90:
            edad = prompt("edad", "ingrese una edad valida (entre 18 y 90)")
        edad = int(edad)

        estado_civil = prompt("estado_civil", "Ingrese su estado civil (Soltero/a, Divorciado/a, Casado/a, Viudo/a)").capitalize()
        while not estado_civil or not estado_civil.isalpha() or (estado_civil != "Soltero" and estado_civil != "Soltera" and estado_civil != "Casado" and estado_civil != "Casada" and estado_civil != "Divorciado" and estado_civil != "Divorciada" and estado_civil != "Viudo" and estado_civil != "Viuda"):
            estado_civil = prompt("estado_civil", "Reingrese su estado civil (Soltero/a, Divorciado/a, Casado/a, Viudo/a)").capitalize()
        
        if estado_civil == "Soltero" or estado_civil == "Soltera":
            estado_civil = "Soltero/a"
        elif estado_civil == "Casado" or estado_civil == "Casada":
            estado_civil = "Casado/a"
        elif estado_civil == "Divorciado" or estado_civil == "Divorciada":
            estado_civil = "Divorciado/a"
        else:
            estado_civil = "Viudo/a"

        legajo = prompt("legajo", "ingrese su legajo (4 cifras)")
        while not legajo or not legajo.isdigit() or int(legajo) < 1000 or int(legajo) > 9999:
            legajo = prompt("legajo", "ingrese un legajo valido (4 cifras)")
        legajo = int(legajo)

        self.txt_apellido.delete(0, tkinter.END)
        self.txt_apellido.insert(0, apellido)
        self.txt_edad.delete(0, tkinter.END)
        self.txt_edad.insert(0, edad)
        self.combobox_tipo.set(estado_civil)
        self.txt_legajo.delete(0, tkinter.END)
        self.txt_legajo.insert(0, legajo)








        # apellido = prompt("Toma de datos", "Ingrese su apellido")

        # while apellido == None or not apellido.isalpha():
        #     apellido = prompt("Toma de datos", "Ingresa tu apellido")
            

        # edad = prompt(title='validar', prompt='ingrese su edad')
        
        # while edad == None or not edad.isdigit():
        #     edad = prompt(title='validar', prompt='ingrese su edad otra vez')
        #     if edad != None and edad.isdigit():
        #         edad = int(edad)
        #         while edad < 18 or edad > 90:
        #             edad = prompt(title='validar', prompt='ingrese su edad (entre 18 y 90)')
        #             if edad!= None and edad.isdigit():
        #                 edad = int(edad)
        #             continue

        # edad = int(edad)        
        # while edad < 18 or edad > 90:
        #             edad = prompt(title='validar', prompt='ingrese su edad (entre 18 y 90)')
        #             if edad!= None and edad.isdigit():
        #                 edad = int(edad)
        #             continue


        # numero_legajo = prompt("Titulo", "Ingrese su numero de legajo")

        # while numero_legajo == None or not numero_legajo.isdigit():
        #     numero_legajo = prompt("Titulo", "Ingrese su numero de legajo otra vez")
        #     if numero_legajo!= None and numero_legajo.isdigit():
        #         numero_legajo = int(numero_legajo)
        #         while numero_legajo < 999:
        #             numero_legajo = prompt("Titulo", "Ingrese su numero de legajo nuevamente")
        #             if numero_legajo!= None and numero_legajo.isdigit():
        #                 numero_legajo = int(numero_legajo)
        #             continue





        
            

                
        


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
