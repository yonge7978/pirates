from PIL import Image, ImageDraw

def blank_qr_code(input_path, output_path):
    img = Image.open(input_path)
    draw = ImageDraw.Draw(img)
    
    # Draw a solid white rectangle covering the mock QR code area inside the red rope border
    # Coordinates are mapped to the 1024x1024 canvas center
    draw.rectangle([382, 392, 617, 624], fill=(255, 255, 255))
    
    img.save(output_path)
    print(f"Blanked QR code and saved to {output_path}")

if __name__ == "__main__":
    blank_qr_code(
        "/Users/yong/.gemini/antigravity-cli/brain/94239e22-cba2-4161-b34b-e5c9b39ae674/event_banner_letter_1780300242992.png",
        "/Users/yong/workspace/pirates/event_banner.png"
    )
