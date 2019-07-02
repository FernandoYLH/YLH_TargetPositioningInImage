# YLH_TargetPositioningInImage
## Target Positioning In an Image
Some python code are provided. <br>
Run the code "YLH_ObjDet.py" in your Python interface by:<br>
python YLH_ObjDet.py image1.jpg image2.jpg

## Approach evaluation

The task achieved from the method of these code is to utilize Aircv target location method based on the python-opencv2 to search or match the location of the given image (the target image) in a large background picture. An intuitive understanding is template matching.

This method is simple and effective, which can locate all the similar images (similarity reaches 99% or so), find the small target image by drawing a circle. The output includes the center coordinates, the number of targets and the spatial coordinates of four corners of rectangle.

The shortcomings of this approach is that getting a small target image depends on a screenshot of a large background image or high similarity pictures. In addition, the number of channels in the image is also an issue because this method does not consider color matching.

## Other possible approaches
The reason why the two photos can match is that their feature points have a high degree of similarity. The other feasible method is to use SIFT feature matching algorithm to find image feature points.
