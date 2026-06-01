from PIL import Image, ImageDraw, ImageFilter

def erase_text_with_parchment(banner_path, clean_parchment_path, output_path):
    banner = Image.open(banner_path)
    clean_p = Image.open(clean_parchment_path)
    
    # Crop a clean patch of size 294x270 from the clean parchment letter_parchment_light.png
    patch = clean_p.crop((180, 300, 474, 570))
    
    # Create the custom alpha mask for blending
    mask = Image.new("L", patch.size, 255)
    
    left_feather = 15.0
    right_feather = 15.0
    top_feather = 6.0
    bottom_feather = 20.0
    
    for y in range(patch.height):
        for x in range(patch.width):
            dist_left = x
            dist_right = patch.width - 1 - x
            dist_top = y
            dist_bottom = patch.height - 1 - y
            
            f_left = min(1.0, dist_left / left_feather)
            f_right = min(1.0, dist_right / right_feather)
            f_top = min(1.0, dist_top / top_feather)
            f_bottom = min(1.0, dist_bottom / bottom_feather)
            
            opacity = min(f_left, f_right, f_top, f_bottom)
            mask.putpixel((x, y), int(opacity * 255))
            
    feathered_mask = mask.filter(ImageFilter.GaussianBlur(1))
    
    # Paste the clean patch over the text at y = 618
    banner.paste(patch, (20, 618), mask=feathered_mask)
    
    banner.save(output_path)
    print(f"Eraser completed: {output_path}")

if __name__ == "__main__":
    erase_text_with_parchment(
        "/Users/yong/workspace/pirates/event_banner.png",
        "/Users/yong/workspace/pirates/letter_parchment_light.png",
        "/Users/yong/workspace/pirates/event_banner.png"
    )
