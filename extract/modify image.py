from PIL import Image, ImageDraw, ImageFont

# Open image using PIL
img = Image.open(r'C:\Users\jayapradha\Desktop\extract\d.png')

# Initialize drawing context
draw = ImageDraw.Draw(img)

# Define text string
text = 'Date: 10-04-2023'
text1 = "jayapradha"

# Define font and font size
font = ImageFont.truetype('arial.ttf', size=18)

# Define text color
color = (20, 20, 20)

# Get text bounding box
text_bbox = draw.textbbox((1, 1), text, font=font)
text_bbox1 = draw.textbbox((1, 1), text1, font=font)

# Calculate text position
x = img.width - text_bbox[2] - 70
y = img.height - text_bbox[3] - 150

b = img.height - text_bbox[3] - 130


# Add text to image
draw.text((x, y), text, font=font, fill=color)
draw.text((x, b), text1, font=font, fill=color)


# Save image as PNG
img.save('output_image.png', format='PNG')
