#!/usr/bin/env python
# Batch thumbnail generation script using PIL

import sys
import os.path
import Image

thumbnail_size = (28, 28)

# Loop through all provided arguments
for i in range(1, len(sys.argv)):
    try:
        # Attempt to open an image file
        filepath = sys.argv[i]
        image = Image.open(filepath)
    except IOError, e:
        # Report error, and then skip to the next argument
        print "Problem opening", filepath, ":", e
        continue

    # Resize the image
    image = image.resize(thumbnail_size, Image.ANTIALIAS)
    
    # Split our original filename into name and extension
    (name, extension) = os.path.splitext(filepath)
    
    # Save the thumbnail as "(original_name)_thumb.png"
    image.save(name + '_thumb.png')