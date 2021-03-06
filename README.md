# Staples Removal

Detection and automatic deletion of staples in images of wound of abdominal surgery.

```
Munar, M., González-Hidalgo, M., & Moyà, G. (2019).
Final Degree Project 
Universitat de les Illes Balears
``` 

## Installation

The developed package contains the main functions for the segmentation of an image in smaller regions, detection of the presence of staple in each region, location of the staples, elimination using inpainting methods (for more information, see PBibiloni/softcolor) and chromatic segmentation to determine the proportion of infection.

To install, type in terminal:
```bash
pip install staplesremoval
```
## Example images

In order to verify the proposed methods, the two test images attached to the code can be considered. For the examples, the following image classified with infection will be used:

<p align="center">
  <img src="staplesremoval/images/image_infection.png" height="400">
</p>
