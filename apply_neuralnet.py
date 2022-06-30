from tkinter import NUMERIC
from create_training_data import get_data

import keras

PATH_TO_FINAL_DATA = "./grab_data_from_google/output_data/"
PATH_TO_MODELS = "training_1/cp.ckpt"


def main():

    x_test, y_test = get_data(PATH_TO_FINAL_DATA)

    model = keras.models.load_model("./saved_model/model")

    print(x_test)
    print(y_test)

    # Evaluate the model
    score = model.evaluate(x_test, y_test, verbose=1)
    print(f"accuracy: {100 * score[1]}%")

    NUMBER_OF_PREDICTIONS = 10

    x_pred_val = x_test[:NUMBER_OF_PREDICTIONS]
    y_pred_val = y_test[:NUMBER_OF_PREDICTIONS]

    predictions = model.predict(x_pred_val)

    print(predictions)
    print(y_pred_val)


if __name__ == "__main__":
    main()
