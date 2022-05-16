from __future__ import absolute_import, division, print_function, unicode_literals

import pandas as pd
import tensorflow as tf

# Load dataset.
dftrain = pd.read_csv(
    './data.csv')  # training data
dfeval = pd.read_csv(
    './data.csv')  # testing data


print(dftrain.shape)

print(dftrain.loc[0])

dftrain = dftrain.loc[::-1].set_index(dftrain.index)


def remake_data_to_classification(df):

    df_new = [0]
    df_compare = [0]

    for i in range(len(df["close"])):
        if i == 0:
            continue

        # print(df.loc[(i-1), "close"])
        # print(df.loc[i, "close"])

        df_compare.append(
            str(df.loc[(i-1), "close"]) + "->" + str(df.loc[i, "close"]))

        df_new.append((df.loc[(i-1), "close"]
                       <= df.loc[i, "close"]).astype(int))

    df["close"] = df_new
    # df["compare"] = df_compare

    return df


classified_data = remake_data_to_classification(dftrain)

print("-----------------------------------------   DAAAAATA --------------------------------------------------------------")

# pd.set_option('display.max_rows', None)

# print(dftrain.loc[1, "close"])

print(classified_data)


y_train = classified_data.pop('close')
y_eval = classified_data.pop('close')


CATEGORICAL_COLUMNS = ['time']
NUMERIC_COLUMNS = ['open', 'high', 'low', 'volume']

feature_columns = []
for feature_name in CATEGORICAL_COLUMNS:
    # gets a list of all unique values from given feature column
    vocabulary = classified_data[feature_name].unique()
    feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(
        feature_name, vocabulary))

for feature_name in NUMERIC_COLUMNS:
    feature_columns.append(tf.feature_column.numeric_column(
        feature_name, dtype=tf.float32))


def make_input_fn(data_df, label_df, num_epochs=15, shuffle=True, batch_size=32):
    def input_function():  # inner function, this will be returned
        # create tf.data.Dataset object with data and its label
        ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))
        if shuffle:
            ds = ds.shuffle(1000)  # randomize order of data
        # split dataset into batches of 32 and repeat process for number of epochs
        ds = ds.batch(batch_size).repeat(num_epochs)
        return ds  # return a batch of the dataset
    return input_function  # return a function object for use


# here we will call the input_function that was returned to us to get a dataset object we can feed to the model
train_input_fn = make_input_fn(classified_data, y_train)
eval_input_fn = make_input_fn(
    classified_data, y_eval, num_epochs=1, shuffle=False)

# We create a linear estimtor by passing the feature columns we created earlier
linear_est = tf.estimator.LinearRegressor(
    feature_columns=feature_columns)

linear_est.train(train_input_fn)  # train
# get model metrics/stats by testing on tetsing data
result = linear_est.evaluate(eval_input_fn)

# the result variable is simply a dict of stats about our model
print(result)

result = list(linear_est.predict(eval_input_fn))


print(result)
for index in range(10):
    print("\n")
    print("prediction: ", result[index]["predictions"])
    print("result: ", y_eval.loc[index])
