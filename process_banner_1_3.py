from PIL import Image, ImageDraw, ImageFilter

def generate_perfect_banner(src_path, clean_parchment_path, output_path):
    img = Image.open(src_path)
    
    # 1. Resize canvas horizontally to fit the scroll boundaries (360px wide scroll)
    # into the 1:3 vertical banner width (341px) without cropping the scroll edges.
    scaled_img = img.resize((900, 1024), Image.Resampling.LANCZOS)
    
    # 2. Crop the 1:3 banner (width=341, height=1024) centered on the scroll.
    # Center of scroll is at x = 510 in the original canvas (510 * 900 / 1024 = 448 in scaled).
    crop_box = (278, 0, 619, 1024)
    banner = scaled_img.crop(crop_box)
    
    # 3. Load clean parchment texture to erase the handwritten text below the QR frame
    clean_p = Image.open(clean_parchment_path)
    
    # Crop a clean patch of size 290x240 from clean parchment
    patch = clean_p.crop((180, 300, 470, 540))
    
    # 4. Create a custom blending mask to blend edges smoothly
    mask = Image.new("L", patch.size, 255)
    
    left_feather = 15.0
    right_feather = 15.0
    top_feather = 6.0
    bottom_feather = 6.0
    
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
            
    # Smooth the mask slightly
    feathered_mask = mask.filter(ImageFilter.GaussianBlur(1))
    
    # 5. Paste the clean patch over the text region (x=25, y=636)
    banner.paste(patch, (25, 636), mask=feathered_mask)
    
    # Save the final perfect banner
    banner.save(output_path, "PNG")
    print(f"Perfect 1:3 banner generated successfully: {output_path}")

if __name__ == "__main__":
    generate_perfect_banner(
        "/Users/yong/.gemini/antigravity-cli/brain/94239e22-cba2-4161-b34b-e5c9b39ae674/event_banner_letter_1_3_1780304477833.png",
        "/Users/yong/workspace/pirates/letter_parchment_light.png",
        "/Users/yong/workspace/pirates/event_banner.png"
    )
