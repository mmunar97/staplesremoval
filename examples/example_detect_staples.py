from staplesremoval import data
from staplesremoval import staples_detector
from skimage import io

if __name__ == "__main__":
    infection_image = data.load_infection_example_image()

    colormask_infection, mask_infection = staples_detector.generate_mask(infection_image)
    io.imshow(colormask_infection)
    io.show()

    noinfection_image = data.load_noinfection_example_image()
    colormask_noinfection, mask_noinfection = staples_detector.generate_mask(noinfection_image)
    io.imshow(colormask_noinfection)
    io.show()