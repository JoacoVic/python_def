import tkinter

from tkinter.messagebox import showinfo as alert

from tkinter.messagebox import askyesno as question

from tkinter.simpledialog import askstring as prompt
import customtkinter


'''

Al presionar el botón 'CARGAR' se le solicitarán tres números al usuario mediante el Dialog Prompt, los mismos deberán ser almacenados en un vector lista_datos. 

Al presionar el botón 'MOSTRAR', se deberán mostrar los números almacenados en el vector utilizando Dialog Alert para informar cada elemento.

'''


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
        for item in self.lista_datos:
            alert("Titulo", f"{item}")
        

        
    def btn_cargar_on_click(self):
        self.lista_datos.clear()
        
        for item in range(3):
            numero_ingresado = prompt("Titulo", "Ingrese un numero")

            while not numero_ingresado or not numero_ingresado.isdigit():
                numero_ingresado = prompt("Error", "Ingrese un numero")
            self.lista_datos.append(int(numero_ingresado))

        
        
        
        # contador = 0
        # while contador < 3:
        #     elementos = prompt("Titulo", "Ingrese datos para acumular en la lista") 

        #     self.lista_datos.append(elementos)

        #     contador += 1
        
        

    

if __name__ == "__main__":

    app = App()

    app.geometry("300x300")
    app.mainloop()