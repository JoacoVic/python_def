'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

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
        #Variable A
        cant_especifica = 0

        #Variable B
        edad_jr = 0

        #Variables C
        sum_edad_m = 0
        cant_edad_m = 0
        sum_edad_f = 0
        cant_edad_f = 0
        sum_edad_nb = 0
        cant_edad_nb = 0
        
        #Variables D
        post_python = 0
        post_js = 0
        post_asp = 0
        tec_mas_post = None

        #Variables E
        cant_post_m = 0
        cant_post_f = 0
        cant_post_nb = 0 
        
        
        
        for item in range(10):
            nombre = prompt("Nombre", "Ingrese su nombre")
            while not nombre or not nombre.isalpha():
                nombre = prompt("Nombre", "Error: Ingrese su nombre")
        
            edad = prompt("Edad", "Ingrese su edad")
            while not edad or not edad.isdigit() or int(edad) < 18:
                edad = prompt("Edad", "Error: Ingrese su edad")
            edad = int(edad)

            genero = prompt("Género", "Ingrese su género (F, M o NB)")
            while not genero or not genero.isalpha() or (genero != "F" and genero != "M" and genero != "NB"):
                genero = prompt("Género", "Error: Ingrese su género (F, M o NB)")
        
            tecnologia = prompt("Tecnología", "Ingrese tecnología (PYTHON, JS o ASP.NET)")
            while not tecnologia or (tecnologia!= "PYTHON" and tecnologia!= "JS" and tecnologia!= "ASP.NET"):
                tecnologia = prompt("Tecnología", "Error: Ingrese tecnología (PYTHON, JS o ASP.NET)")

            puesto = prompt("Puesto", "Ingrese su puesto (Jr, Sr o Ssr)")
            while not puesto or not puesto.isalpha() or (puesto!= "Jr" and puesto!= "Sr" and puesto!= "Ssr"):
                puesto = prompt("Puesto", "Error: Ingrese su puesto (Jr, Sr o Ssr)")

            # Punto A
            if genero == "NB" and (tecnologia == "ASP.NET" or tecnologia == "JS") and (edad > 25 and edad < 40) and puesto == "Ssr":
                cant_especifica += 1

            # Punto B
            if (edad_jr == 0 or edad_jr > edad) and puesto == "Jr":
                edad_jr = edad
                nombre_postulante_jr = nombre

            # Punto C
            if genero == "M":
                sum_edad_m += edad
                cant_edad_m += 1
            elif genero == "F":
                sum_edad_f += edad
                cant_edad_f += 1
            else:
                sum_edad_nb += edad
                cant_edad_nb += 1
            #Punto D
            if tecnologia == "PYTHON":
                post_python += 1
            elif tecnologia == "JS":
                post_js += 1
            else:
                post_asp += 1

            #Punto E
            if genero == "M":
                cant_post_m += 1
            elif genero == "F":
                cant_post_f += 1
            else:
                cant_post_nb += 1

        # Calculo C
        prom_m = sum_edad_m / cant_edad_m
        prom_f = sum_edad_f / cant_edad_f
        prom_nb = sum_edad_nb / cant_edad_nb

        #Calculo D
        if post_python > post_js and post_python > post_asp:
            tec_mas_post = "PYTHON"
        elif post_js > post_python and post_js > post_asp:
            tec_mas_post = "JS"
        else:
            tec_mas_post = "ASP.NET"


        #Calculo E
        porcentaje_m = cant_post_m * 100 / 10
        porcentaje_f = cant_post_f * 100 / 10
        porcentaje_nb = cant_post_nb * 100 / 10



        print(f"La Cantidad de postulantes NB que programan en ASP.NET o JS, cuya edad está entre 25 y 40 y se hayan postulado para un puesto Ssr es: {cant_especifica}\nEl nombre del postulante a Jr con menos edad es: {nombre_postulante_jr}\nEl promedio de edad masculino es {prom_m}, el femenino es {prom_f} y el no binario es {prom_nb}\nLa tecnologia con mas postulantes es: {tec_mas_post}\nLos postulantes masculinos son el {porcentaje_m}%, el femenino es el {porcentaje_f}% y los no binarios son el {porcentaje_nb}% del total de los postulantes")






if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
