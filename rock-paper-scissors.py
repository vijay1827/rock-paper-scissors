import cv2
import numpy as np
from random import choice
from tensorflow.keras.models import load_model

# custom pre-process techniques
# import this incase you want to resume the pre-processing techniques
# for the model creation and model predection while playing
# import preprocess

# DO NOT MODIFY THIS
REV_CLASS_MAP = {
    0: "empty",
    1: "rock",
    2: "paper",
    3: "scissors"
}

# DO NOT MODIFY THIS
def mapper(value):
    return REV_CLASS_MAP[value]

def main():
    # note make sure the img_shape = (225, 225)
    # if you are chaning this make sure to update the code in the model
    model = load_model("rock-paper-scissors-model.h5")

    # once you have written the code to play the game uncommend the below lines 
    # and place them where required so that the model can predict
    # pred = model.predict(np.array([img]))
    # move_made_by_you = mapper(np.argmax(pred[0]))
