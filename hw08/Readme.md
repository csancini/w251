## ANSWERS

#### Part 1: Image Annotation

1. In the time allowed, how many images did you annotate?  
```In one hour 118 images were annotated.``` 

2. Home many instances of the Millennium Falcon did you annotate? How many TIE Fighters?  
```There are 77 instances of the Millennium Falcon and 106 of the TIE Fighters annotated.```     
```$ grep -roh mf . | wc -w```  
```62```  
```$ grep -roh tf . | wc -w```  
```76``` 

3. Based on this experience, how would you handle the annotation of large image data set?  
```I would use paid services such as Mechanical Turk as the annotating process is tedious and time consuming.```

4. Think about image augmentation? How would augmentations such as flip, rotation, scale, cropping, and translation effect the annotations?  
```The annotation points to a coordinate location and polygon dimensions. The augmentation process would have to account for label changes as well.```

#### Part 2: Image Augmentation

1. Describe the following augmentations in your own words
-	Flip: ```mirrors the image around a vertical or horizontal line in the center of the image.```
- 	Rotation: ```turns the image around its center by some angle.```
-	Scale: ```changes the definition of image by zooming in or out.```
-	Crop: ```cuts parts of the image.```
-	Translation: ```moves parts of the image to a new center, eventuall cropping and rescaling.```
-	Noise: ```changes values of pixels using a given pattern to add noise to the image.```

#### Part 3: Audio Annotation

1. Image annotations require the coordinates of the objects and their classes; in your option, what is needed for an audio annotation?  
```It is needed a visual representation of the of the audio file that shows intensity of sounds and when they takes place in time. Features to raise the volume in particular moments are also helpful to distingish distant labels.```
