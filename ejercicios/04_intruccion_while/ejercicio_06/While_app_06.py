import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar 5 números mediante prompt. 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        # cantidad_necesaria = 5
        # suma_acumulada = 0
        # cantidad_ingresada = 0
        # promedio = 0

        # while cantidad_ingresada < cantidad_necesaria:
        #      numero = prompt(title="por favor",prompt="ingrese un numero")
        #      suma_acumulada += int(numero)
        #      cantidad_ingresada += 1
        # promedio = suma_acumulada / cantidad_necesaria
        # self.txt_suma_acumulada.delete(0, tkinter.END)
        # self.txt_suma_acumulada.insert(0, suma_acumulada)
        # self.txt_promedio.delete(0, tkinter.END)
        # self.txt_promedio.insert(0, promedio)

        contador = 0
        acumulador = 0
        promedio = 0

        while contador < 5:
            numero_ingresado = int(prompt("Titulo", "Ingrese un numero"))
            contador += 1
            acumulador += numero_ingresado

        promedio = acumulador / contador
        
        self.txt_suma_acumulada.delete(0, 100)
        self.txt_promedio.delete(0, acumulador)
        self.txt_suma_acumulada.insert(0, acumulador)
        self.txt_promedio.insert(0, promedio)





    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
