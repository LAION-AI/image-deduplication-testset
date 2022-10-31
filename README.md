# Image Deduplication - Testset

This is a test set for finding duplicates of images.
It consists of 177 query images and 12 nearest neighbors from our LAION-5B Clip image embedding index.
The images of a query & the 12 neighbors are in a folder with the name "1" for the first query, "2" for the second query, ... up until "177".

The annotations are in a list of lists, where the first element is e.g. [0,0,1,1,0,0,0,1,1,1,1,1] and 0 means that it is non a duplicate and 1 that it is a duplicate.

As duplicates are considered images that show the same content from the same perspective, maybe with some slight crops, unimportant additional texts that don't change the meaning of the image, compression artefacts or slight blur, ... - If the same content is show from a different camera angle, it is not considered a duplicate.
