import cv2
import mediapipe as mp
from tkinter import Tk, Button, Label, filedialog
from PIL import Image, ImageTk

# Inicializar MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic