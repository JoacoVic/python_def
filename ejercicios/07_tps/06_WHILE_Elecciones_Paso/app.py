'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        mayor_cantidad_votos = 0
        menor_cantidad_votos = 0
        edad_menos_votado = 0
        candidato_mas_votado = None
        candidato_menos_votado = None
        sumatoria_edades = 0
        cantidad_edades = 0
        votos_emitidos = 0
        bandera = True

        while True:

            nombre = prompt("Por favor","Ingrese su nombre")
            while not nombre or not nombre.isalpha():
                nombre = prompt("Por favor","Ingrese su nombre")

            edad = prompt("Por favor","Ingrese su edad")
            while not edad or not edad.isdigit() or int(edad) < 25 :
                edad = prompt("Por favor","Ingrese su edad")
            edad = int(edad)

            votos = prompt("Por favor","Ingrese su cantidad de votos")
            while not votos or not votos.isdigit() or int(votos) <= 0:
                votos = prompt("Por favor","Ingrese su cantidad de votos")
            votos = int(votos)

            if bandera == True:
                bandera = False
                candidato_menos_votado = nombre
                menor_cantidad_de_votos = votos
                edad_menos_votado = edad
                candidato_mas_votado = nombre
                mayor_cantidad_de_votos = votos
            elif votos < menor_cantidad_de_votos:
                candidato_menos_votado = nombre
                menor_cantidad_de_votos = votos
                edad_menos_votado = edad
            elif  votos > mayor_cantidad_votos:
                candidato_mas_votado = nombre
                mayor_cantidad_de_votos = votos


            sumatoria_edades += edad
            cantidad_edades += 1
            votos_emitidos += votos
            continuar = question("",'Desea continuar?')
            if continuar == False:
                break

        promedio_edades = sumatoria_edades / cantidad_edades

        print(f"El candidato con mas votos es {candidato_mas_votado}\n\
        El candidato con menos votos es {candidato_menos_votado} y su edad es {edad_menos_votado}\n\
        El promedio de las edades es {promedio_edades}\n\
        El total de votos emitidos es: {votos_emitidos}")

            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
