from pickletools import optimize
import pandas as pd
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf


pd.set_option("display.max_rows", 5000)


def get_data(index):
    arr = []
    for i in range(index):
        file = PATH_TO_FINAL_DATA + os.listdir(PATH_TO_FINAL_DATA)[i]
        print("Reading data: ", i + 1, "/",
              index, " (", file, ")", sep=None)
        arr.append(pd.read_csv(file))

    return pd.concat(arr)


def handle_data(df, target_column):
    """

    1. drop all data with missing target_column values
    2. drop all data with indexes before "target_column" 
    3. calculate the binary value to: "result"
    4. drop the "target_column" value (this is the value replaced by "result")
    5. create y_train, x_train, y_train, y_test
    6. apply scalers to the data
    6. return created tensors

    """

    # drop all missing data
    df = df.dropna(subset=target_column)
    # print(df.isnull().sum().head(100))

    # get the index of the "target_column" and drop all data in indexes before this
    column_index = df.columns.get_loc(target_column)

    # returns the column names as list, based on their indexes
    def return_column_names(column_index):
        return_arr = []
        for i in range(column_index):
            return_arr.append(df.columns[i])
        return return_arr

    df = df.drop(
        columns=return_column_names(column_index))

    # calculate binary value
    prev_target_column = df.columns[5]
    if "close" not in str(prev_target_column):
        raise("CUSOM ERR AT: create_training_data.py(FUNCTION: handle_data) selected column is not a close, something wrong with data")

    df["binary_result"] = df.apply(
        lambda x: 1 if x[target_column] > x[prev_target_column] else 0, axis=1)

    # drop "target_column"
    df = df.drop(columns=[target_column])

    # split the df into y_train, x_train, y_train, y_test

    x = df.drop("binary_result", axis=1)
    y = df["binary_result"]

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.1, random_state=50)

    print("x_train: ", x_train.shape, "\n",
          "x_test: ", x_test.shape, "\n",
          "y_train: ", y_train.shape, "\n",
          "y_test: ", y_test.shape, "\n", sep=None
          )

    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)

    return (x_train_scaled, x_test_scaled, y_train, y_test)

    ############# NO NEED TO MANUALY CALCULATE THIS #####################

    # for column in data.columns[::-1]:
    #     if target_column[-10:] in column:
    #         if target_column == column:
    #             continue
    #         data = data.drop(columns=[column])
    # return ([data.pop(target_column), data])


def neural_nets(input_value):
    x_train, x_test, y_train, y_test = input_value

    tf.random.set_seed(50)

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(50000, activation="relu"),
        tf.keras.layers.Dense(100000, activation="relu"),
        tf.keras.layers.Dense(100000, activation="relu"),
        tf.keras.layers.Dense(50000, activation="relu"),
        tf.keras.layers.Dense(1, activation="sigmoid")
    ])

    model.compile(
        loss=tf.keras.losses.binary_crossentropy,
        optimizer=tf.keras.optimizers.Adam(lr=0.03),
        metrics=[
            tf.keras.metrics.BinaryAccuracy(name="accuracy"),
            tf.keras.metrics.Precision(name="precision"),
            tf.keras.metrics.Recall(name="recall")
        ]
    )

    checkpoint_path = "training_1/cp.ckpt"
    checkpoint_dir = os.path.dirname(checkpoint_path)

    cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                     save_weights_only=True,
                                                     verbose=1)

    model.fit(x_train, y_train, epochs=15, validation_data=(x_test, y_test),
              callbacks=[cp_callback])


def main():
    """

    No need to save binary data, since only working with batches of 100, 
    instead save the model and run though multiple batches. 


    CURRENT PROBLEM
    The model is currently too big. Im calculating with a neural net with 2.5 * 10**19 connections. That is too much.

    Need more work with data preperations. Use 1 month worth of individual data + avrage daily data per week. 

    !!! Alternetivly try and adjust batch size to a verry small number. !!!


    1. drop all data missing latest close, only work with "complete" data
    2. replace latest close data with binary for up and down
    3. drop binary and point database to x 
    4. pop binary to y
    5. spit data into y_train, x_train, y_test, x_test
    6. create classification model
    7. profit



    """
    global PATH_TO_FINAL_DATA
    PATH_TO_FINAL_DATA = "./data_points/final_steps/"

    y_column = "close_2022-05-19"
    number_of_datapoints = 3

    handle_data_out = handle_data(get_data(number_of_datapoints), y_column)

    print("handle_data_out: ", type(handle_data_out[0]))

    neural_nets(handle_data_out)


if __name__ == "__main__":
    main()
