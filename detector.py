from tkinter import Tk, Button

def on_button_click():
    print("Botón presionado")

def main():
    
    print("Antes del bucle principal")
     # Crear la ventana principal.
    root = Tk()
    root.withdraw()  # Ocultar la ventana principal.

    # Crear el botón.
    button = Button(root, text="Presionar", command=on_button_click)
    button.pack()

    # Mostrar la ventana principal.
    root.mainloop()
    print("Después del bucle principal")
    

if __name__ == "__main__":
    main()
