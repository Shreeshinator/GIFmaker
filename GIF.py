import imageio.v3 as iio
import os

# add your file names here!
filenames = ['team-pic1.png', 'team-pic2.png']

def makeGIF(filenames):
    """
    Create an animated GIF from a list of image files.
    
    Args:
        filenames (list): List of image file paths
    
    Returns:
        list: List of loaded images, or empty list if no images were loaded
    """
    images = []
    
    # Load images with error handling
    for filename in filenames:
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found!")
            continue
        try:
            images.append(iio.imread(filename))
            print(f"Loaded: {filename}")
        except Exception as e:
            print(f"Error loading {filename}: {e}")
    
    # Create GIF if images were loaded
    if images:
        iio.imwrite('team.gif', images, duration=100, loop=0)
        print("GIF created successfully: team.gif")
    else:
        print("No images loaded. GIF creation failed.")
    
    return images


# Example usage
if __name__ == "__main__":
    makeGIF(filenames)
