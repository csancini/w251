import matplotlib.pylab as plt
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

MODEL_PATH ="/notebooks/repo/part2/output/new_model"
LABELS_PATH ="/notebooks/repo/part2/class_labels.txt"
IMAGE_SHAPE = (224, 224)

classifier = tf.keras.Sequential([
    hub.KerasLayer(MODEL_PATH, input_shape=IMAGE_SHAPE+(3,))
])

imagenet_labels = np.array(open(LABELS_PATH).read().splitlines())

data_root = tf.keras.utils.get_file(
  'flower_photos','https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz',
   untar=True)

image_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1/255)
image_data = image_generator.flow_from_directory(str(data_root), target_size=IMAGE_SHAPE)

image_batch, _ = next(image_data)
predicted = classifier.predict(image_batch)

top3_pred = np.argsort(predicted[0])[:-4:-1]

print(
    "First - class: ",
    imagenet_labels[top3_pred[0]],
    ", probability: ",
    np.round(100*predicted[0][top3_pred[0]],2),
    "%",
    sep='')

print(
    "Second - class: ",
    imagenet_labels[top3_pred[1]],
    ", probability: ",
    np.round(100*predicted[0][top3_pred[1]],2),
    "%",
    sep='')

print(
    "Third - class: ",
    imagenet_labels[top3_pred[2]],
    ", probability: ",
    np.round(100*predicted[0][top3_pred[2]],2),
    "%",
    sep='')


