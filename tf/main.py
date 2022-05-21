from pickletools import optimize
from asyncore import read
import tensorflow as tf
from tensorflow import keras
import pandas as pd

from misc import read_saved_data, shuffle_data


def main():

    # get data from saved dataframes
    df = read_saved_data()
    df = shuffle_data(df)

    test_amount = int(len(df.index)/100)
    test_df = df.head(test_amount)

    train_amount = len(df.index) - test_amount
    train_df = df.tail(train_amount)

    labels_test_df = test_df.pop("close_191")
    labels_train_df = train_df.pop("close_191")

    model = keras.Sequential([
        keras.layers.Dense(1000, activation="relu"),
        keras.layers.Dense(1)
    ])

    model.compile(optimizer="adam",
                  loss="sparse_categorical_crossentropy", metrics=["accuracy"])

    model.fit(train_df, labels_train_df, epochs=10)

    test_loss, test_acc = model.evaluate(test_df, labels_test_df)

    print("TESTED ACC: ", test_acc)


if __name__ == "__main__":
    main()
