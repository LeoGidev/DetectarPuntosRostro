import cv2
import mediapipe as mp

# Inicializa MediaPipe Face Mesh.
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Inicializa los puntos de referencia faciales.
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5)

# Cargar la imagen
image_path = 'ruta/a/tu/imagen.jpg'
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Procesar la imagen y extraer los puntos de referencia faciales.
results = face_mesh.process(image_rgb)

# Dibujar puntos de referencia específicos (ojos, nariz, boca) en la imagen.
if results.multi_face_landmarks:
    for face_landmarks in results.multi_face_landmarks:
        # Dibuja la malla facial completa.
        mp_drawing.draw_landmarks(
            image=image,
            landmark_list=face_landmarks,
            connections=mp_face_mesh.FACEMESH_TESSELATION,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style())
        
        # Dibuja contornos específicos de ojos, nariz y boca.
        mp_drawing.draw_landmarks(
            image=image,
            landmark_list=face_landmarks,
            connections=mp_face_mesh.FACEMESH_CONTOURS,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style())
        
        # Dibuja puntos de referencia específicos (ojos, labios e iris).
        mp_drawing.draw_landmarks(
            image=image,
            landmark_list=face_landmarks,
            connections=mp_face_mesh.FACEMESH_IRISES,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_iris_connections_style())

# Guardar la imagen con los puntos de referencia.
output_image_path = 'ruta/a/la/salida/imagen_con_puntos_de_referencia.jpg'
cv2.imwrite(output_image_path, image)

# Mostrar la imagen.
cv2.imshow('Image with facial landmarks', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
