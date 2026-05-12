from PIL import Image

def remove_background(input_path, output_path):
    img = Image.open(input_path)
    img = img.convert("RGBA")
    
    data = img.getdata()
    
    new_data = []
    # Background color is around (253, 253, 253)
    target_color = (253, 253, 253)
    tolerance = 10
    
    for item in data:
        # Check if the pixel color is within the tolerance of the target color
        if all(abs(item[i] - target_color[i]) <= tolerance for i in range(3)):
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(output_path, "PNG")

if __name__ == "__main__":
    remove_background("logo_treasure.png", "logo_treasure_nobg.png")
