from PIL import Image
import os


def add_watermark_to_images(input_dir: str, output_dir: str, logo_path: str):
    """
    Adds a centered watermark logo to every image in input_dir
    and saves the result to output_dir.

    Args:
        input_dir (str): Folder containing the original images.
        output_dir (str): Folder where watermarked images will be saved.
        logo_path (str): Path to the watermark logo (PNG with transparency).
    """

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Load logo
    logo = Image.open(logo_path).convert("RGBA")

    for filename in os.listdir(input_dir):
        if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
            continue

        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        try:
            # Load background
            background = Image.open(input_path).convert("RGBA")
            bg_width, bg_height = background.size

            # Resize logo to 40% of image width
            logo_width = int(bg_width * 0.40)
            scale = logo_width / logo.width
            logo_height = int(logo.height * scale)

            resized_logo = logo.resize(
                (logo_width, logo_height),
                Image.Resampling.LANCZOS
            )

            # Reduce logo opacity to 20%
            alpha = resized_logo.getchannel("A")
            alpha = alpha.point(lambda p: int(p * 0.20))
            resized_logo.putalpha(alpha)

            # Center logo
            x = (bg_width - logo_width) // 2
            y = (bg_height - logo_height) // 2

            # Paste watermark
            background.paste(resized_logo, (x, y), resized_logo)

            # Save to output directory
            background.convert("RGB").save(output_path)

            print(f"Saved: {output_path}")

        except Exception as e:
            print(f"Failed to process {filename}: {e}")


if __name__ == "__main__":
    input_directory = r"C:\files\radu\output\backgrounds"
    output_directory = r"C:\files\radu\output\mockedup"
    logo_file_path = r"C:\files\radu\output\logo.png"

    add_watermark_to_images(
        input_dir=input_directory,
        output_dir=output_directory,
        logo_path=logo_file_path
    )