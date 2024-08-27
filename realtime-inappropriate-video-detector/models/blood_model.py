import tensorflow as tf
import numpy as np
import cv2

class BloodDetector:
    def __init__(self, config):
        self.blood_model = tf.keras.models.load_model(config["pretrained_blood_detect"])


    def process(self, frame):
        """
        Resize video frame to (224, 224) for detect blood on (video) frames.
        ----------
        `frame`: numpy.ndarray | [A video frame]
        """

        # resize
        frame = cv2.resize(frame, (224, 224))

        # scale
        if np.max(frame) > 1:
            frame = frame / 255.0

        return frame 


    def predict(self, frame):
        frame = self.process(frame)
        frame = np.expand_dims(frame, axis=0)
        out = self.blood_model.predict(frame)
        return out[0][0] #Percentage of having blood on face
