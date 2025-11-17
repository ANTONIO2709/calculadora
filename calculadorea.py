import tkinter as tk

def calcular():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        operacion = operacion_var.get()

        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            resultado = num1 / num2

        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except:
        etiqueta_resultado.config(text="Error en los datos")

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x250")

tk.Label(ventana, text="Número 1").pack()
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Número 2").pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()

operacion_var = tk.StringVar(value="+")
tk.OptionMenu(ventana, operacion_var, "+", "-", "*", "/").pack(pady=10)

boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.pack(pady=10)

etiqueta_resultado = tk.Label(ventana, text="Resultado:")
etiqueta_resultado.pack(pady=10)

ventana.mainloop()
