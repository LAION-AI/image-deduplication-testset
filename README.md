# Image Deduplication - Testset

This is a test set for finding duplicates of images.
It consists of 177 query images and 12 nearest neighbors from our LAION-5B Clip image embedding index.
The images of a query & the 12 neighbors are in a folder with the name "1" for the first query, "2" for the second query, ... up until "177".

The downloaded and zipped image folders can be found here: https://drive.google.com/file/d/1wfdcenzGKf-XjzJTlLhzCA6rT5haqtAL/view?usp=sharing

Here can you find visualizations of the samples:
http://captions.christoph-schuhmann.de/visualizations-of-the-samples.html


The annotations are in a list of lists, where the first element is e.g. [0,0,1,1,0,0,0,1,1,1,1,1] and 0 means that it is non a duplicate and 1 that it is a duplicate.

As duplicates are considered images that show the same content from the same perspective, maybe with some slight crops, unimportant additional texts that don't change the meaning of the image, compression artefacts or slight blur, ... - If the same content is show from a different camera angle, it is not considered a duplicate.

## Hash from [imagededup](https://github.com/idealo/imagededup)

| Type & distance  | Result |
| ------------- | ------------- |
| PHash_1  | 0.7947269303201506  |
| PHash_2  | 0.8300376647834274  |
| AHash_1  | 0.8286252354048964  |
| AHash_2  | 0.8432203389830508  |
| DHash_1  | 0.8130885122410546  |
| DHash_2  | 0.8314500941619586  |
| WHash_1  | 0.8173258003766478  |
| WHash_2  | 0.8493408662900188  |
