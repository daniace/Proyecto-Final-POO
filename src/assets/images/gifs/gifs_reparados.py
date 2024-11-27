from PIL import Image, ImageSequence
import os


def ensure_duration(input_path, output_path, default_duration=100):
    with Image.open(input_path) as gif:
        frames = []
        for frame in ImageSequence.Iterator(gif):
            frame = frame.copy()
            frame.info["duration"] = gif.info.get("duration", default_duration)
            frames.append(frame)

        # Guardar un nuevo GIF con la duración asegurada
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            loop=0,
            duration=default_duration,
        )


# Carpeta de entrada/salida
input_folder = "src/assets/images/gifs2rotos"
output_folder = "src/assets/images/gifs"
os.makedirs(output_folder, exist_ok=True)

# Procesar todos los GIFs
for gif_file in os.listdir(input_folder):
    if gif_file.endswith(".gif"):
        input_path = os.path.join(input_folder, gif_file)
        output_path = os.path.join(output_folder, gif_file)
        ensure_duration(input_path, output_path)

print("¡GIFs reparados correctamente!")
