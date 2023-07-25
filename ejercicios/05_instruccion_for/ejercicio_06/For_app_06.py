import tkinter

from tkinter.messagebox import showinfo as alert

from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''

Al presionar el botón Mostrar pedir un número. mostrar los números pares desde 

el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.

'''


class App(customtkinter.CTk):
    

    def __init__(self):
        super().__init__()


        # configure window

        self.title("UTN Fra")
        

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)

        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")



    def btn_mostrar_on_click(self):
        numero_pedido = prompt("Numero", "Ingrese un numero")
        contador_numeros_pares = 0

        while numero_pedido == None or not numero_pedido.isdigit():
            numero_pedido = prompt("Numero", "Ingresa un numero")

        numero_pedido = int(numero_pedido)

        rango_a_recorrer = range(1, numero_pedido + 1)
        rango_a_recorrer2 = range(2, numero_pedido + 1, 2)

        for numero in rango_a_recorrer2:
            print(numero)

        alert("Titulo", f"Se encontraron {len(rango_a_recorrer2)} numeros pares")

        # for numero in rango_a_recorrer:
        #     if numero % 2 == 0:
        #         contador_numeros_pares += 1
        #         print(numero)        
        # alert("Titulo", f"Se encontraron {contador_numeros_pares} numeros pares")
        
        
        # numero_ingresado = prompt("Titulo", "Ingrese un numero")
        # pares = 0
        # numeros_pares = ""
        # numero_ingresado = int(numero_ingresado)

        # for numero in range(1, numero_ingresado+1):
        #     if numero % 2 == 0:
        #         pares += 1
        #         numeros_pares += str(numero) + ","

        # alert("Titulo", f"Los numeros pares son: {numeros_pares}\nLa cantidad de numeros pares es de: {pares}")



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()