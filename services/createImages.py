# services that interact with wordcloud to create pretty images 

import numpy as np
from PIL import Image

def invert_mask(image_path):
    """
    Load and invert a mask image so that words can be drawn inside the shape.
    Args:
        image_path (str): Path to the image file.
    Returns:
        np.ndarray: Inverted mask array (2D, dtype=uint8)
    """
    mask_img = np.array(Image.open(image_path))

    # Convert RGB to grayscale if needed
    if mask_img.ndim == 3:
        mask_img = np.mean(mask_img, axis=2).astype(np.uint8)

    # Invert: 255 becomes 0, and anything else becomes 255
    inverted = np.where(mask_img == 255, 0, 255).astype(np.uint8)

    return inverted


from wordcloud import get_single_color_func
# colour words based on categories
class SimpleGroupedColor:
    """Color words based on categories or assign a random consistent color"""
    def __init__(self, color_list):
        self.color_list = color_list
        self.color_func_map = {}

    def __call__(self, word, **kwargs):
        if word not in self.color_func_map:
            color = np.random.choice(self.color_list)
            self.color_func_map[word] = get_single_color_func(color)
        return self.color_func_map[word](word, **kwargs)