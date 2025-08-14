from django.shortcuts import render
from .models import File
from .forms import Image
import imageio.v3 as iio
import matplotlib.pyplot as plt, mpld3
import skimage.draw            # form 2, load skimage.draw module only
from skimage.draw import disk  # form 3, load only the disk function
import skimage as ski
import numpy as np
from skimage.util import img_as_ubyte
from skimage.util import invert
from django.shortcuts import render
import io
import os




# Create your views here.
def page(request):
    
    
    slider_value = 0.5
    if request.POST:
        if 'update' in request.POST:
            slider_value = float(request.POST.get('slider_value'))
        if 'colony-image' in request.POST:
            form = Image(request.POST, request.FILES)
            
            form.save()

    posts = File.objects.all().order_by("-date_created")
    flage = True
    try:
        img = File.objects.latest("date_created")
    except:
        flage = False
        img = None


    if flage:
        # load an image
        name = img.filename

        #print(type(image1))
        image = iio.imread(uri=img.image)
        image = invert(image)
        image_gray = ski.color.rgb2gray(image)

        # define the pixels for which we want to view the intensity (profile)
        xmin, xmax = (0, image_gray.shape[1])
        Y = ymin = ymax = int(image_gray.shape[0]/2)

        # view the image indicating the profile pixels position
        image_blur = ski.filters.gaussian(image_gray, sigma=1)

        # like before, plot the pixels profile along "Y"
        image_blur_pixels_slice = image_blur[Y, :]
        image_blur_pixels_slice = ski.img_as_ubyte(image_blur_pixels_slice)

        size = min(image_gray.shape)

        t = slider_value
        binary_mask = image_blur < t
        labeled_image, count = ski.measure.label(binary_mask,
                                                        connectivity=2, return_num=True)
        colored_label_image = ski.color.label2rgb(labeled_image, bg_label=0)
        object_features = ski.measure.regionprops(labeled_image)
        object_areas = [objf["area"] for objf in object_features]

        fig, ax = plt.subplots()
        ax.hist(object_areas)
        ax.set_xlabel("Area (pixels)")
        ax.set_ylabel("Number of objects")
        plt.savefig(f"static/files/hist_{name}.png")
        plt.close()

        min_area = 700
        large_objects = []
        for objf in object_features:
            if objf["area"] < min_area:
                large_objects.append(objf["label"])
        print("Found", len(large_objects), "objects!")

        object_areas = np.array([objf["area"] for objf in ski.measure.regionprops(labeled_image)])
        # prepend zero to object_areas array for background pixels
        object_areas = np.insert(0, obj=1, values=object_areas)

        summary_image = ski.color.gray2rgb(image_gray)
        summary_image[binary_mask] = colored_label_image[binary_mask]

        # plot overlay
        fig, ax = plt.subplots()
        plt.imshow(summary_image)
        plt.savefig(f"static/files/proces_{name}.png")
        plt.close()

        img.pimage = f"proces_{name}.png"
        img.himage = f"hist_{name}.png"
        img.save()
    context = {'posts':posts, "s_v":slider_value, "imageform":Image, "img":img}



    return render(request, 'index.html', context)




