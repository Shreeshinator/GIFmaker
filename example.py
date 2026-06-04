"""
Example script demonstrating how to create GIFs with imageio
"""
import imageio.v3 as iio
import os
from pathlib import Path

def create_gif(image_files, output_filename='output.gif', duration=100, loop=0):
    """
    Create an animated GIF from a list of image files.
    
    Args:
        image_files (list): List of image file paths
        output_filename (str): Name of the output GIF file
        duration (int): Duration of each frame in milliseconds (default: 100ms)
        loop (int): Number of loops (0 = infinite)
    
    Returns:
        bool: True if successful, False otherwise
    """
    images = []
    
    for filename in image_files:
        if not os.path.exists(filename):
            print(f"Warning: File '{filename}' not found!")
            continue
        try:
            img = iio.imread(filename)
            images.append(img)
            print(f"✓ Loaded: {filename}")
        except Exception as e:
            print(f"✗ Error loading {filename}: {e}")
    
    if not images:
        print("Error: No images were loaded!")
        return False
    
    try:
        iio.imwrite(output_filename, images, duration=duration, loop=loop)
        print(f"\n✓ GIF created successfully: {output_filename}")
        return True
    except Exception as e:
        print(f"✗ Error creating GIF: {e}")
        return False


# Example 1: Basic usage
if __name__ == "__main__":
    print("=" * 50)
    print("Example 1: Create a basic GIF")
    print("=" * 50)
    
    # List your image files here
    images = ['team-pic1.png', 'team-pic2.png']
    create_gif(images, 'team.gif', duration=100, loop=0)
    
    print("\n" + "=" * 50)
    print("Example 2: Different duration")
    print("=" * 50)
    
    # Slower animation (200ms per frame)
    create_gif(images, 'team_slow.gif', duration=200, loop=0)
    
    print("\n" + "=" * 50)
    print("Example 3: Limited loops")
    print("=" * 50)
    
    # Play animation 3 times then stop
    create_gif(images, 'team_limited.gif', duration=100, loop=3)
