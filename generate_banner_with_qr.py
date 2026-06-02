import qrcode
from PIL import Image

def embed_qr_code(banner_path, url, output_path):
    # 1. Load the banner
    banner = Image.open(banner_path)
    
    # 2. Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=1,  # Slim border to fit maximum size
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create the QR image (size is determined by box_size and border, e.g., 29x10 + 2*10 = 310x310)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Resize QR image to fit our 150x150 target area perfectly
    qr_img_resized = qr_img.resize((150, 150), Image.Resampling.LANCZOS)
    
    # 3. Paste the QR code onto the banner at coordinates x=96, y=452 (centered inside the rope frame)
    banner.paste(qr_img_resized, (96, 452))
    
    # 4. Save the final banner
    banner.save(output_path, "PNG")
    print(f"Successfully embedded QR code for {url} onto {output_path}")

if __name__ == "__main__":
    embed_qr_code(
        "/Users/yong/workspace/pirates/event_banner.png",
        "https://romantic-pirates.vercel.app",
        "/Users/yong/workspace/pirates/event_banner.png"
    )
