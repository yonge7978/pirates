from PIL import Image

def colorize_and_transparent(input_path, output_path, target_rgb=(139, 0, 0)):
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size
    
    data = img.getdata()
    new_data = []
    
    for r, g, b, a in data:
        # Convert to grayscale
        gray = int(0.299 * r + 0.587 * g + 0.114 * b)
        
        # Extract the ink:
        # Near-white (background) becomes transparent.
        # Dark lines (ink) become opaque.
        if gray >= 240:
            alpha = 0
        elif gray <= 90:
            alpha = 255
        else:
            # Smooth interpolation
            alpha = int((240 - gray) / (240 - 90) * 255)
            
        # Apply the target red color with the calculated alpha channel
        new_data.append((target_rgb[0], target_rgb[1], target_rgb[2], alpha))
        
    img.putdata(new_data)
    img.save(output_path, "PNG")
    print(f"Processed: {input_path} -> {output_path}")

if __name__ == "__main__":
    # Target color: #8B0000 (Dark Red)
    target_red = (139, 0, 0)
    
    # 1. Swingship Stamp
    colorize_and_transparent(
        "/Users/yong/.gemini/antigravity-cli/brain/94239e22-cba2-4161-b34b-e5c9b39ae674/stamp_swingship_nospoiler_1779353975514.png",
        "/Users/yong/workspace/pirates/stamp_swingship.png",
        target_red
    )
    
    # 2. Splash Stamp
    colorize_and_transparent(
        "/Users/yong/.gemini/antigravity-cli/brain/94239e22-cba2-4161-b34b-e5c9b39ae674/stamp_splash_1779505441644.png",
        "/Users/yong/workspace/pirates/stamp_splash.png",
        target_red
    )
    
    # 3. Flume Stamp
    colorize_and_transparent(
        "/Users/yong/.gemini/antigravity-cli/brain/94239e22-cba2-4161-b34b-e5c9b39ae674/stamp_flume_1779505660109.png",
        "/Users/yong/workspace/pirates/stamp_flume.png",
        target_red
    )
