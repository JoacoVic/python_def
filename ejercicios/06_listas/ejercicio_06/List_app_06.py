import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón 'PROMEDIO' se analizará el vector lista_datos a efectos de calcular 
el promedio el cual deberá ser informado utilizando Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_calcular = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = [1,80,5,0,15,-5,1,79]


    def btn_calcular_on_click(self):
        acumulador_suma = 0

        for numero in self.lista_datos:
            acumulador_suma += numero

        cantidad_lista = len(self.lista_datos)

        if cantidad_lista != 0:
            promedio = acumulador_suma / cantidad_lista
            alert("Titulo", f"El promedio es: {promedio}")
        else:
            alert("Titulo", "La lista está vacia")
        
        
        
        # suma_datos = sum(self.lista_datos)
        # promedio = suma_datos / len(self.lista_datos)
        # alert("Titulo", f"El promedio es: {promedio}")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()