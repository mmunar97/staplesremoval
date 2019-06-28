from staplesremoval import data
from staplesremoval import staples_detector
from staplesremoval import inpainting
from staplesremoval import triangular_fuzzy_color_segmentation
from skimage import io

if __name__ == "__main__":
    infection_image = data.load_infection_example_image()
    colormask_infection, mask_infection = staples_detector.generate_mask(infection_image)
    inpainted_infection = inpainting.inpaint_from_mask(infection_image, mask_infection)
    segmented_infection = triangular_fuzzy_color_segmentation(inpainted_infection)

    io.imshow(segmented_infection)
    io.show()


    # noinfection_image = data.load_noinfection_example_image()
    # colormask_noinfection, mask_noinfection = staples_detector.generate_mask(noinfection_image)
    # inpainted_noinfection = inpainting.inpaint_from_mask(noinfection_image, mask_noinfection)
    # segmented_noinfection = triangular_fuzzy_color_segmentation(inpainted_noinfection)
    #
    # io.imshow(segmented_noinfection)
    # io.show()