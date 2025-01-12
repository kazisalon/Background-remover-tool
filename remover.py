from rembg import remove
from PIL import Image

def remove_background(input_path):
    """Remove background from an image"""
    # Load image
    input_image = Image.open(input_path)
    
    # Remove background
    output_image = remove(input_image)
    
    # Create output filename
    output_path = "nobg_" + input_path
    
    # Save image
    output_image.save(output_path)
    print(f"Saved image as: {output_path}")

# Get input from user
image_path = input("Drag and drop your image here and press Enter: ")
# Remove extra quotes if present
image_path = image_path.strip('"').strip("'")

try:
    remove_background(image_path)
    print("Background removed successfully!")
except Exception as e:
    print(f"An error occurred: {str(e)}")

input("Press Enter to exit...")