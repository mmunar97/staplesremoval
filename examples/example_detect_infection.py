from staplesremoval import detect_infection
from staplesremoval import data
from skimage import transform
from skimage import io


if __name__ == "__main__":

    image_infection = data.load_infection_example_image()
    print(image_infection.shape)
    red_proportion_infection = detect_infection.detect_infection(image_infection)
    print("The image with infection has degree of infection {}".format(red_proportion_infection))

    image_noinfection = data.load_noinfection_example_image()
    red_proportion_noinfection = detect_infection.detect_infection(image_noinfection)
    print("The image without infection has degree of infection {}".format(red_proportion_noinfection))
