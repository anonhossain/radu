# from openai import OpenAI
# import base64
# from dotenv import load_dotenv
# import os

# load_dotenv()

# api_key = os.getenv("OPENAI_API_KEY")
# client = OpenAI(api_key=api_key)
# client = OpenAI()

# def generate_quote_background(quote: str, output_file: str = "quote_background.png"):
#     prompt = f"""
# Create a premium, modern quote background for a mobile application.

# Theme:
# - Generate a clean, elegant, minimalistic design.
# - The quote should be the primary focus.
# - Maintain generous padding around the quote.
# - Avoid clutter and unnecessary decorative elements.

# Color Palette:
# - Dark Theme Background: #051123
# - Light Theme Background: #FFFFFF
# - Accent Gradient: #FFA500 → #D4902A
# - Use the orange gradient only for highlights, dividers, quotation marks, abstract shapes, or subtle decorative elements.
# - Do not overuse the accent colors.

# Typography:
# - Place the quote in the center.
# - Use large, bold, premium-looking typography.
# - Ensure excellent readability and visual hierarchy.
# - Highlight only one or two important words using the orange gradient.
# - Keep the remaining text white on dark backgrounds or #051123 on light backgrounds.

# Background:
# - Create a soft abstract background with subtle gradients, glowing shapes, geometric patterns, or elegant curves.
# - The background should enhance the quote without distracting from it.
# - No stock-photo look.

# Requirements:
# - Quote: "{quote}"
# - Image size: 1024 × 1024 pixels.
# - Premium mobile app aesthetic.
# - Flat, modern UI style.
# - High contrast.
# - No logos.
# - No watermarks.
# - No signatures.
# - No borders around the entire image.
# - Produce a polished, App Store-quality design suitable for sharing on social media.
# """

#     result = client.images.generate(
#         model="gpt-image-2",
#         prompt=prompt,
#         size="1024x1024",
#         n=1,
#         output_format= "png",
#         quality="high",
#         temperature=0.7,
#     )

#     image_base64 = result.data[0].b64_json
#     image_bytes = base64.b64decode(image_base64)

#     with open(output_file, "wb") as f:
#         f.write(image_bytes)

#     print(f"Image saved as '{output_file}'")

# if __name__ == "__main__":
#     quote = "The only limit to our realization of tomorrow is our doubts of today."
#     output_file = "output/quote_background.png"
#     if not os.path.exists(output_file):
#         os.makedirs(os.path.dirname(output_file), exist_ok=True)
#     generate_quote_background(quote, output_file)



dark_theme_prompt = """
Create a premium, modern abstract background for a mobile application quote card.

Theme & Style:
- Clean, elegant, minimalistic design.
- Abstract background with soft gradients, subtle glowing geometric shapes, or fluid organic curves.
- Premium mobile app aesthetic with a flat, modern UI style.
- No stock-photo look.

Color Palette:
- Dark theme primary: #051123
- Accent Gradient: Subtle touches of #FFA500 -> #D4902A for highlights, dividers, or abstract accents.

Composition Requirements:
- NO text, NO quotes, NO letters, NO numbers.
- NO logos, watermarks, signatures, or outer borders.
- Keep the central area clean, spacious, and low-contrast so text placed over it will be highly legible."""

white_theme_prompt = """

Create a premium, modern abstract background for a mobile application quote card.

Theme & Style:
- Clean, elegant, minimalistic design.
- Bright, airy, and sophisticated aesthetic.
- Abstract background with soft gradients, subtle glowing geometric shapes, translucent glass-like elements, or fluid organic curves.
- Premium mobile app aesthetic with a flat, modern UI style.
- Soft depth and gentle lighting without appearing busy or distracting.
- No stock-photo look.

Color Palette:
- Primary background: #FFF7ED
- Use soft harmonious gradients inspired by:
  - #FFF7ED (warm cream)
  - #F0FDF4 (soft mint)
  - #EFF6FF (light sky blue)
  - #FFEFFE (light blush pink)
- Accent elements may include subtle touches of:
  - #22504D (deep teal)
  - #504D4A (warm charcoal)
  - #B4AB9C (muted warm gray)
- Colors should blend naturally with smooth transitions and a premium, calming appearance.
- Avoid overly saturated or harsh colors.

Composition Requirements:
- NO text, NO quotes, NO letters, NO numbers.
- NO logos, watermarks, signatures, or outer borders.
- Keep the central area clean, spacious, and low-contrast so text placed over it will be highly legible.
- Place visual interest mainly around the edges and corners, leaving the center suitable for text overlays.
- Maintain generous negative space and balanced composition.
- Design should feel luxurious, modern, calming, and suitable for a premium productivity, motivation, or journaling application.
"""

import sys
import os
from urllib import response
from urllib import response
import urllib.request
from dotenv import load_dotenv
from openai import OpenAI
import base64

load_dotenv()

# Client automatically reads OPENAI_API_KEY from environment variables
client = OpenAI()


def generate_background_images(output_dir: str, num_images: int):
    """Generates a series of abstract background images designed for text overlays."""
    os.makedirs(output_dir, exist_ok=True)

    # Prompt updated to generate pure backgrounds without any text
    prompt = """

Create a premium, modern abstract background for a mobile application quote card.

Theme & Style:
- Clean, elegant, minimalistic design.
- Bright, airy, and sophisticated aesthetic.
- Abstract background with soft gradients, subtle glowing geometric shapes, translucent glass-like elements, or fluid organic curves.
- Premium mobile app aesthetic with a flat, modern UI style.
- Soft depth and gentle lighting without appearing busy or distracting.
- No stock-photo look.

Color Palette:
- Primary background: #FFF7ED
- Use soft harmonious gradients inspired by:
  - #FFF7ED (warm cream)
  - #F0FDF4 (soft mint)
  - #EFF6FF (light sky blue)
  - #FFEFFE (light blush pink)
- Accent elements may include subtle touches of:
  - #22504D (deep teal)
  - #504D4A (warm charcoal)
  - #B4AB9C (muted warm gray)
- Colors should blend naturally with smooth transitions and a premium, calming appearance.
- Avoid overly saturated or harsh colors.

Composition Requirements:
- NO text, NO quotes, NO letters, NO numbers.
- NO logos, watermarks, signatures, or outer borders.
- Keep the central area clean, spacious, and low-contrast so text placed over it will be highly legible.
- Place visual interest mainly around the edges and corners, leaving the center suitable for text overlays.
- Maintain generous negative space and balanced composition.
- Design should feel luxurious, modern, calming, and suitable for a premium productivity, motivation, or journaling application.

"""

    for i in range(1, num_images + 1):
        print(f"Generating white background {i}/{num_images}...")

        try:
            result = client.images.generate(
                model="gpt-image-2",
                prompt=prompt,
                size="1024x1024",
                n=1,
                output_format="png",
                quality="high",
            )

            output_file = os.path.join(output_dir, f"background_{i:02d}.png")

            # Decode and save the image
            image_bytes = base64.b64decode(result.data[0].b64_json)

            with open(output_file, "wb") as f:
                f.write(image_bytes)

            print(f"Saved: {output_file}")

        except Exception as e:
            print(f"Failed to generate background {i}: {e}")


if __name__ == "__main__":
    # Check if command-line arguments are provided, otherwise use default values
    output_directory = sys.argv[1] if len(sys.argv) > 1 else "output/backgrounds"
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    print(f"Output Directory: {output_directory}")
    print(f"Images to Generate: {count}")

    # Values passed directly from main to function
    generate_background_images(output_dir=output_directory, num_images=count)