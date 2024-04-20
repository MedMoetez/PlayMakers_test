from PIL import Image, ImageDraw

#this function will be used0 to create the badge
def find_circular_boundary(image):
    width, height = image.size
    center_x = width // 2
    center_y = height // 2
    radius = min(center_x, center_y)

    # Iterate over each pixel
    for x in range(width):
        for y in range(height):
            # Check if the pixel is within the circular boundary
            if (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2:
                if image.getpixel((x, y))[3] != 0:  # Check if the pixel is non-transparent
                    return center_x, center_y, radius

    # If no circular boundary is found, return the center of the image and a default radius
    return center_x, center_y, radius

def create_badge(image_path):
    image = Image.open(image_path)
    image = image.convert("RGBA")
    image = image.resize((512, 512))

    center_x, center_y, radius = find_circular_boundary(image)
    badge_image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))# RGBA image with transparent background

    mask = Image.new("L", (512, 512), 0)#grayscale mode ("L"), with dimensions 512x512 pixels.
    draw = ImageDraw.Draw(mask)

    # Calculate the bounding box for the ellipse
    x0 = max(0, center_x - radius)
    y0 = max(0, center_y - radius)
    x1 = min(512, center_x + radius)
    y1 = min(512, center_y + radius)

    draw.ellipse((x0, y0, x1, y1), fill=255)

    masked_image = image.copy()
    masked_image.putalpha(mask)#Pixels with a value of 0 in the mask become fully transparent, while pixels with a value of 255 become fully opaque

    badge_image.paste(masked_image, (0, 0), masked_image)#Paste the masket photo in the badge_image

    return badge_image

# Create badge using circular mask
badge_image = create_badge("test2.png")

# Save the badge image
badge_image.save('badge_image.png')
