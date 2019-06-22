from staplesremoval import data
from staplesremoval import staples_detector
from staplesremoval import inpainting
from skimage import io


if __name__ == "__main__":

    infection_image = data.load_infection_example_image()
    colormask_infection, mask_infection = staples_detector.generate_mask(infection_image)
    inpainted_infection = inpainting.inpaint_from_mask(infection_image, mask_infection)
    io.imshow(inpainted_infection)
    io.show()

    noinfection_image = data.load_noinfection_example_image()
    colormask_noinfection, mask_noinfection = staples_detector.generate_mask(noinfection_image)
    inpainted_noinfection = inpainting.inpaint_from_mask(noinfection_image, mask_noinfection)
    io.imshow(inpainted_noinfection)
    io.show()