import os
from PIL import Image


def process_images(input_folder, output_folder):
    # Crear la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Procesar cada imagen en la carpeta de entrada
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(
            (".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif")
        ):
            # Abrir la imagen
            with Image.open(os.path.join(input_folder, filename)) as img:
                # Obtener las dimensiones originales
                width, height = img.size

                # Calcular las nuevas dimensiones (la mitad del tamaño original)
                new_width = width // 2
                new_height = height // 2

                # Redimensionar la imagen
                resized_img = img.resize((new_width, new_height), Image.LANCZOS)

                # Cambiar el nombre del archivo para la versión WebP
                new_filename = os.path.splitext(filename)[0] + ".webp"

                # Guardar la imagen redimensionada en formato WebP
                resized_img.save(os.path.join(output_folder, new_filename), "WEBP")

                print(f"Procesada: {filename} -> {new_filename}")


# Uso del script
input_folder = "pages/chapters/chapter_4/assets"
output_folder = f"{input_folder}/dist"

process_images(input_folder, output_folder)
