from PIL import Image, ImageDraw

def make_parchment_transparent(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size
    
    # We use a threshold of 35 to clean up near-white pixels around the deckled edges.
    ImageDraw.floodfill(img, (0, 0), (0, 0, 0, 0), thresh=35)
    ImageDraw.floodfill(img, (width - 1, 0), (0, 0, 0, 0), thresh=35)
    ImageDraw.floodfill(img, (0, height - 1), (0, 0, 0, 0), thresh=35)
    ImageDraw.floodfill(img, (width - 1, height - 1), (0, 0, 0, 0), thresh=35)
    
    img.save(output_path, "PNG")
    print(f"Processed parchment saved to {output_path}")

if __name__ == "__main__":
    make_parchment_transparent(
        "/Users/yong/.gemini/antigravity-cli/brain/94239e22-cba2-4161-b34b-e5c9b39ae674/letter_parchment_light_1779528794491.png",
        "/Users/yong/workspace/pirates/letter_parchment.png"
    )
