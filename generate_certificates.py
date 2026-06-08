from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

# Load the Excel file
df = pd.read_excel('automation test.xlsx')  # Make sure column is called 'Name'

# Load certificate template
TEMPLATE_PATH = 'AI unpluged certificate.png'
OUTPUT_DIR = 'output'
FONT_PATH = 'arial'  # Change if you want a custom font
FONT_SIZE = 65
FONT_PATH_ITALIC = 'arialf'  # Change if you want a custom italic font

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Loop through each name and generate certificate
for index, row in df.iterrows():
    name = row['Name']

    # Open template
    image = Image.open(TEMPLATE_PATH).convert("RGB")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    # === Change these values to position the name correctly ===
    text_width = draw.textlength(name, font=font)
    image_width, image_height = image.size
    # x= 582  # Adjust based on your template (horizontal position)
    x = (image_width - text_width) / 2  # Centered horizontally
    y = 650  # Adjust based on your template (vertical position)

    # Draw name
    draw.text((x, y), name, fill="black", font=font)

    # Save output with name in filename
    file_name = f"{name.replace(' ', '_')}.png"
    image.save(os.path.join(OUTPUT_DIR, file_name))

    print(f"✅ Certificate generated for {name}")

print("🎉 All certificates generated!")
