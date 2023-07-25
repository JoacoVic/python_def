import tkinter

from tkinter.messagebox import showinfo as alert

from tkinter.messagebox import askyesno as question

from tkinter.simpledialog import askstring as prompt
import customtkinter

# Es la gala de eliminación del Gran Utniano y la producción nos pide un programa para contar los votos de los televidentes y saber cuál será el participante que deberá abandonar la casa más famosa del mundo.
# Los participantes en la placa son: Giovanni, Gianni y Facundo. Fausto no fue nominado y Marina no está en la placa esta semana por haber ganado la inmunidad.

# Cada televidente que vota deberá ingresar:
# Nombre del votante
# Edad del votante (debe ser mayor a 13)
# Género del votante (Masculino, Femenino, Otro)
# El nombre del participante a quien le dará el voto negativo (Debe estar en placa)
# No se sabe cuántos votos entrarán durante la gala.
# Se debe informar al usuario:
# El promedio de edad de las votantes de género Femenino 
# Cantidad de personas de género masculino entre 25 y 40 años que votaron a Giovanni o a Facundo.
# Nombre del votante más joven qué votó a Gianni.
# Nombre de cada participante y porcentaje de los votos qué recibió.
# El nombre del participante que debe dejar la casa (El que tiene más votos)

class App(customtkinter.CTk):
    

    def __init__(self):
        super().__init__()


        # configure window

        self.title("UTN FRA")


        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)

        self.btn_mostrar.grid(row=2, pady=10, columnspan=2, sticky="nsew")


        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar", command=self.btn_cargar_on_click)

        self.btn_cargar.grid(row=3, pady=10, columnspan=2, sticky="nsew")


        self.lista_datos = []



    def btn_mostrar_on_click(self):
        alert("Titulo", "Hola")
        

        
    def btn_cargar_on_click(self):
        alert("Titulo", "Hola")

        
        
        

    

if __name__ == "__main__":

    app = App()

    app.geometry("300x300")
    app.mainloop()