import cv2
import mediapipe as mp
from tkinter import Tk, filedialog, messagebox, Button

# Inicializa MediaPipe Face Mesh.
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Inicializa los puntos de referencia faciales.
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5)



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

     
    except Exception as e:
        messagebox.showerror("Error", f"Error al seleccionar la imagen: {str(e)}")

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

