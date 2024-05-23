import cv2
import mediapipe as mp
from tkinter import Tk, filedialog, messagebox, Button




def select_image():
    # Crear una ventana de selección de archivo.
    image_path = filedialog.askopenfilename(
        title="Seleccionar imagen",
        filetypes=(("Archivos JPG", "*.jpg"), ("Todos los archivos", "*.*"))
    )

    if not image_path:
        messagebox.showinfo("Información", "No se seleccionó ninguna imagen.")
    else:
        
        messagebox.showinfo("Información", f"Imagen procesada y guardada en:")

def main():
    # Crear la ventana principal.
    root = Tk()

    # Crear el botón para seleccionar una imagen.
    select_image_button = Button(root, text="Seleccionar imagen", command=select_image)
    select_image_button.pack()

    # Mostrar la ventana principal.
    root.mainloop()

if __name__ == "__main__":
    main()


