from django.db import models
from tensorflow.keras.preprocessing import image as tf_image
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions
import numpy as np
from django.core.files.storage import default_storage

# Create your models here.

class ImageElement(models.Model):
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='mediaphoto', blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.photo:
            try:
                file_path = self.photo.path
                if default_storage.exists(file_path):
                    # target_size is size of loaded image
                    pill_image = tf_image.load_img(file_path, target_size=(299, 299))
                    # convert image to numpy array
                    img_array = tf_image.img_to_array(pill_image)
                    # extend numpy array with new dimension
                    img_array = np.expand_dims(img_array, axis=())
                    # process obraz with model requirements
                    img_array = preprocess_input(img_array)

                    model = InceptionV3(weights='imagenent')
                    predictions = model.predict(img_array)
                    decoded_predictions = decode_predictions(predictions, top=1)[0]
                    best_guess = decoded_predictions[0][1]
                    self.title = best_guess
                    self.content = ', '.join([f"{pred[1]}: {pred[2] * 100:.2f}%" for pred in decoded_predictions])
                    super().save(*args, **kwargs)
            except Exception as e:
                print(e)