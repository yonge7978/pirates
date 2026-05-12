from rembg import remove
from PIL import Image
import io

def remove_bg(input_path, output_path):
    with open(input_path, 'rb') as i:
        input_image = i.read()
        output_image = remove(input_image)
        with open(output_path, 'wb') as o:
            o.write(output_image)

if __name__ == "__main__":
    remove_bg('logo_treasure.png', 'logo_treasure_nobg.png')
