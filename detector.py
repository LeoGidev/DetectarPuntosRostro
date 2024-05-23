import cv2
import mediapipe as mp
from tkinter import Tk, Button, Label, filedialog
from PIL import Image, ImageTk

# Inicializar MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

def detect_and_mark(image_path):
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    with mp_holistic.Holistic(static_image_mode=True) as holistic:
        results = holistic.process(img_rgb)

        # Dibuja los resultados de detección
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(img, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

        if results.face_landmarks:
            mp_drawing.draw_landmarks(img, results.face_landmarks, mp_holistic.FACE_CONNECTIONS)

        if results.left_hand_landmarks:
            mp_drawing.draw_landmarks(img, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

        if results.right_hand_landmarks:
            mp_drawing.draw_landmarks(img, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

    # Guardar la imagen resultado
    result_path = "resultado.jpg"
    cv2.imwrite(result_path, img)
    return result_path

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        result_path = detect_and_mark(file_path)
        display_image(result_path)

def display_image(image_path):
    img = Image.open(image_path)
    img = img.resize((500, 500))  # Redimensionar la imagen para que se ajuste a la ventana
    img = ImageTk.PhotoImage(img)
    panel.config(image=img)
    panel.image = img


# Crear la interfaz gráfica
root = Tk()
root.title("Detección de partes del cuerpo")

panel = Label(root)
panel.pack(padx=10, pady=10)

btn = Button(root, text="Abrir imagen", command=open_file)
btn.pack(pady=20)

root.mainloop()