from PIL import Image
import os

def compress_images(directory, quality=100):
    """
    Compress all images in the specified directory without losing quality.
    :param directory: The directory containing images to be compressed.
    :param quality: Quality for image saving, 85 by default.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(root, file)
                img = Image.open(file_path)

                # Convert to RGB if image is RGBA (to prevent alpha channel issues)
                if img.mode == 'RGBA':
                    img = img.convert('RGB')

                # Save the image with the specified quality
                img.save(file_path, optimize=True, quality=quality)

# Replace 'your_folder_path' with the path to your folder containing images
compress_images('/Users/ruslantsitser/dev/projects/sandbox/compress_image/5.5')
