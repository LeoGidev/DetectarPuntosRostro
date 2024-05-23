import cv2
import mediapipe as mp
from tkinter import Tk, filedialog, messagebox, Button
import os

# Inicializa MediaPipe Face Mesh.
mp_face_mesh = mp.solutions.face_mesh

def select_image():
    try:
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
        # Verificar si la ruta del archivo es válida.
        if not os.path.exists(image_path):
            messagebox.showerror("Error", "La ruta del archivo de imagen no es válida.")
            return
        
        # Cargar la imagen.
        image = cv2.imread(image_path)
        
        # Verificar si la imagen se cargó correctamente.
        if image is None:
            messagebox.showerror("Error", "No se pudo cargar la imagen.")
            return

        # Convertir la imagen a RGB (MediaPipe requiere imágenes en RGB).
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Inicializar MediaPipe Face Mesh.
        with mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5) as face_mesh:
            # Procesar la imagen y extraer los puntos de referencia faciales.
            results = face_mesh.process(image_rgb)

        # Resto del código para procesar y mostrar la imagen...
    except Exception as e:
        messagebox.showerror("Error", f"Error al procesar la imagen: {str(e)}")

def main():
    try:
        print("Antes del bucle principal")
        # Crear la ventana principal.
        root = Tk()

        # Crear el botón para seleccionar una imagen.
        select_image_button = Button(root, text="Seleccionar imagen", command=select_image)
        select_image_button.pack()

        # Mostrar la ventana principal.
        root.mainloop()
        print("Después del bucle principal")
    except Exception as e:
        messagebox.showerror("Error", f"Error al iniciar la aplicación: {str(e)}")

if __name__ == "__main__":
    main()




