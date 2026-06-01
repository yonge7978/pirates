from PIL import Image

def crop_to_1_3_banner(input_path, output_path):
    img = Image.open(input_path)
    
    # Target 1:3 aspect ratio
    # Width = 334, Height = 1002 (334 * 3)
    # Center of the 1024x1024 canvas is 512
    # So we crop from x = 512 - 167 = 345 to x = 512 + 167 = 679
    # Let's adjust slightly to center the scroll perfectly.
    # Looking at the scroll, the center is around x=500.
    # Let's use x_start = 500 - 167 = 333, x_end = 500 + 167 = 667.
    # For y, we crop from y = 18 to y = 1020 (height = 1002).
    crop_box = (333, 18, 667, 1020)
    
    cropped_img = img.crop(crop_box)
    cropped_img.save(output_path, "PNG")
    print(f"1:3 banner cropped successfully: {output_path} (Size: {cropped_img.size})")

if __name__ == "__main__":
    crop_to_1_3_banner(
        "/Users/yong/.gemini/antigravity-cli/brain/94239e22-cba2-4161-b34b-e5c9b39ae674/event_banner_letter_1_3_1780304477833.png",
        "/Users/yong/workspace/pirates/event_banner.png"
    )
