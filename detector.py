import cv2
import mediapipe as mp
from tkinter import Tk, filedialog, messagebox, Button

# Inicializa MediaPipe Face Mesh.
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Inicializa los puntos de referencia faciales fuera de la función principal.


def select_image():
    try:
        # Crear una ventana de selección de archivo.
        root = Tk()
        root.withdraw()  # Ocultar la ventana principal.

        # Seleccionar un archivo de imagen.
        image_path = filedialog.askopenfilename(
            title="Seleccionar imagen",
            filetypes=(("Archivos JPG", "*.jpg"), ("Todos los archivos", "*.*"))
        )

        if not image_path:
            messagebox.showinfo("Información", "No se seleccionó ninguna imagen.")
        else:
            process_image(image_path)
    except Exception as e:
        messagebox.showerror("Error", f"Error al seleccionar la imagen: {str(e)}")

def process_image(image_path):
    try:
        # Cargar la imagen
        image = cv2.imread(image_path)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Procesar la imagen y extraer los puntos de referencia faciales.
        results = face_mesh.process(image_rgb)

        # Resto del código para procesar y mostrar la imagen...
    except Exception as e:
        messagebox.showerror("Error", f"Error al procesar la imagen: {str(e)}")

def main():
    try:
        # Crear el botón para seleccionar una imagen.
        select_image_button = Button(text="Seleccionar imagen", command=select_image)
        select_image_button.pack()

        # Mostrar la ventana principal.
        Tk().mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"Error al iniciar la aplicación: {str(e)}")

if __name__ == "__main__":
    main()


