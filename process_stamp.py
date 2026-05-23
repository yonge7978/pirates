from PIL import Image, ImageDraw

def make_stamp_transparent(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size
    
    # Perform floodfill from all four corners to make the outer white area transparent
    ImageDraw.floodfill(img, (0, 0), (0, 0, 0, 0), thresh=20)
    ImageDraw.floodfill(img, (width - 1, 0), (0, 0, 0, 0), thresh=20)
    ImageDraw.floodfill(img, (0, height - 1), (0, 0, 0, 0), thresh=20)
    ImageDraw.floodfill(img, (width - 1, height - 1), (0, 0, 0, 0), thresh=20)
    
    img.save(output_path, "PNG")
    print(f"Processed stamp saved to {output_path}")

if __name__ == "__main__":
    # Swingship Stamp
    make_stamp_transparent(
        "/Users/yong/.gemini/antigravity-cli/brain/94239e22-cba2-4161-b34b-e5c9b39ae674/stamp_swingship_nospoiler_1779353975514.png",
        "/Users/yong/workspace/pirates/stamp_swingship.png"
    )
    # Splash Stamp
    make_stamp_transparent(
        "/Users/yong/.gemini/antigravity-cli/brain/94239e22-cba2-4161-b34b-e5c9b39ae674/stamp_splash_1779505441644.png",
        "/Users/yong/workspace/pirates/stamp_splash.png"
    )
