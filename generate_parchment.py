from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import random
import numpy as np

def generate_vivid_parchment(width, height, output_path):
    # 1. Base color: Richer, more vivid parchment color
    # Antique brass / parchment blend
    base_color = np.array([245, 222, 179]) # Wheat color
    
    # 2. Add fine grain noise
    noise = np.random.randint(-10, 10, (height, width, 3))
    data = np.clip(base_color + noise, 0, 255).astype(np.uint8)
    img = Image.fromarray(data, 'RGB')
    
    # 3. Add organic stains with higher contrast
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Large soft stains
    for _ in range(15):
        x = random.randint(0, width)
        y = random.randint(0, height)
        r = random.randint(100, 250)
        # Deep brown with varying transparency
        splotch_color = (101, 67, 33, random.randint(20, 60))
        draw.ellipse([x-r, y-r, x+r, y+r], fill=splotch_color)
    
    overlay = overlay.filter(ImageFilter.GaussianBlur(radius=40))
    img.paste(overlay, (0, 0), overlay)
    
    # 4. Add smaller, sharper "ink" spots or damage marks
    spots = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(spots)
    for _ in range(30):
        x = random.randint(0, width)
        y = random.randint(0, height)
        r = random.randint(2, 5)
        spot_color = (60, 40, 20, random.randint(100, 200))
        s_draw.ellipse([x-r, y-r, x+r, y+r], fill=spot_color)
    
    spots = spots.filter(ImageFilter.GaussianBlur(radius=1))
    img.paste(spots, (0, 0), spots)

    # 5. Defined Vignette (Darker edges for depth)
    vignette = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    v_draw = ImageDraw.Draw(vignette)
    
    border = 100
    for i in range(border):
        alpha = int(180 * (1 - i/border)**2)
        v_draw.rectangle([i, i, width-i, height-i], outline=(60, 30, 10, alpha))
        
    vignette = vignette.filter(ImageFilter.GaussianBlur(radius=30))
    img.paste(vignette, (0, 0), vignette)

    # 6. Final Enhancement: Sharpness and Contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.2)
    
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(1.5)
    
    img = img.convert('RGBA')
    img.save(output_path)
    print(f"Vivid parchment generated: {output_path}")

if __name__ == "__main__":
    generate_vivid_parchment(800, 1000, 'parchment_bg.png')
