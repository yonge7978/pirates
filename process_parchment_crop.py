from PIL import Image, ImageDraw

def make_parchment_transparent_and_crop(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size
    
    # Floodfill from corners to make the outer white area transparent
    ImageDraw.floodfill(img, (0, 0), (0, 0, 0, 0), thresh=35)
    ImageDraw.floodfill(img, (width - 1, 0), (0, 0, 0, 0), thresh=35)
    ImageDraw.floodfill(img, (0, height - 1), (0, 0, 0, 0), thresh=35)
    ImageDraw.floodfill(img, (width - 1, height - 1), (0, 0, 0, 0), thresh=35)
    
    # Find the bounding box of non-transparent pixels (alpha > 0)
    bbox = img.getbbox()
    if bbox:
        # Crop the image to remove all transparent margins on the sides
        cropped_img = img.crop(bbox)
        cropped_img.save(output_path, "PNG")
        print(f"Successfully processed, cropped and saved to {output_path} (New Size: {cropped_img.size})")
    else:
        img.save(output_path, "PNG")
        print(f"Processed (not cropped) and saved to {output_path}")

if __name__ == "__main__":
    make_parchment_transparent_and_crop(
        "/Users/yong/.gemini/antigravity-cli/brain/94239e22-cba2-4161-b34b-e5c9b39ae674/letter_parchment_light_1779528794491.png",
        "/Users/yong/workspace/pirates/letter_parchment_light.png"
    )
