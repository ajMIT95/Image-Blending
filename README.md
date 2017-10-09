# Image-Blending

## pasting() function explanation
Pasting is a straightforward application of the copying. It is accomplished by using the Bergman image as the source and the Bogart image as the target. It simply requires looping over the pixels of the source and using their RGB values as replacement values for the corresponding pixel in the target. (Of course the target image should be larger than the source.)

![Image](https://raw.github.com/ajMIT95/Image-Blending/tree/master/Results/pasting.jpg)

## blend_33() function explanation
A much better effect would be combine the images to give the impression that Bogart's character, Rick, is thinking about Bergman's character, Ilsa. This requires blending the images together. When blending images the necessary step required is to combine the colors of corresponding pixels of the images together. The RGB values of the pixels to be blended are added together using a percentage of the color of each pixel. If even blending is desired then 50% of each RGB value of the source pixels is added to 50% of each RGB value of the target pixels to make the color of the blended pixel. In the Bergman/Bogart merging we do not wish an even blending instead we will use 33% of the Bergman pixel color and 67% of the Bogart pixel color.

![Image](https://raw.github.com/ajMIT95/Image-Blending/Results/master/blend_33.jpg)

## gradient_blend() function explanation
A smoother blending can be achieved by changing the percentage of the blending as the blending is taking place. For the images, the further along the x-axis the blending proceeds it would be better to use less of the source, (i.e. Bergman), image and more of the target, (i.e. Bogart), image. Of course the same decreased blending from the source should also occur the farther down the y-axis the blending proceeds. One easy technique to accomplish this is linear interpolation. As the blending traverses along the x-axis, the current column coordinate, x, can be divided by the source width. This results in a changing percentage that starts at 0.0 and gradually increases ending at almost 1.0. If we multiply the blending percentage by this changing percentage we can compute how much to decrease the blending percentage by in order to achieve a horizontal gradient blend. Performing the same computations down the y-axis results in a second vertical blending gradient decrease. Of course applying both the horizontal and vertical blending decrease would result in too much of a blending reduction. The simple solution is to choose the larger of the two reductions to use at any given pixel.
