import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: instrucion_if_04
---
Enunciado:
Al presionar el botón  'Calcular', se deberá obtener contenido en la caja de texto txtEdad, 
transformarlo en número y calcular si es adolescente (edad entre 13 y 17 años). Se deberá informar utilizando el Dialog alert.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        """
        Operadores Logicos
        and
        or
        not
        """
        """

        """

        txt_mensaje = None
        edad = self.txt_edad.get()
        edad = int(edad)

        if edad >= 13 and edad <= 17:
            alert("Titulo", "Usted es adolescente")
        else: alert("Titulo", "Usted no es adolescente")

        # if edad >= 13:
        #     if edad < 18:
        #         txt_mensaje = "Es adolescente"
        #     else: #edad mayor o igual a 18
        #         if edad > 65:
        #             txt_mensaje = "Es jubilado"
        #             if edad > 100
        #             txt_mensaje = "Es centenario"
        #         txt_mensaje = "Es adulto"
                
        # else:
        #     txt_mensaje = "Es niño"

        # alert("Resultado", txt_mensaje)

        # if edad > 17:
        #     mensaje = "Usted es mayor de edad"
        # else:
        #     if edad < 13:


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
