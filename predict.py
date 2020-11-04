import cv2
import tensorflow as tf

CATEGORIES = ["Black spot", "Healthy"]


def prepare(filepath):
    IMG_SIZE = 256
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


model = tf.keras.models.load_model("64x3-CNN.model")

prediction = model.predict(
    [prepare('./Test/BLACK_SPOT.jpg')])
print(CATEGORIES[int(prediction[0][0])])
