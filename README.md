# Horisontal AI scaling
*work for school*


## Important stuff

### ALPHAVANTAGE 
*API for all market data*

**API KEY:**
- KGNJMQQ0GZUCIB2R (nils@u1.se)
- LNE01TS7E5RFWHX7 (nils.malmberg@edu.jarfalla.se)
- U2QRUXVWDVWTRFHW (1@u1.se)
- Y8Z4GBMOF0K79BWU (2@u1.se)
- ZLQVK9D7UWWKU3UQ (3@u1.se)
- 58WOX8YU1UAZQDF4 (4@u1.se)
- 0UPD7VFKAP9RDL2X (5@u1.se)
- N5V14V3K3200W31J (6@u1.se)
- GIRQDLBGXHKGVJ39 (7@u1.se)
- 4CA3T536HNP3O89X (8@u1.se)
- P9LOX6BLJ9OMNE1O (9@u1.se)
- IWW9RBGER70UYAFH (10@u1.se)

**LInks**
- https://www.alphavantage.co/documentation/
- https://www.alphavantage.co/


### panda private doc

- print(df)
- pd.set_option("display.max_rows", 5000)
- print(df.head(1))
- print(df.loc[:178, ["time", "open"]])

- for index, row in df.iterrows():
      print(index, row["open"])
      if index > 99:
        break
- df.loc[df["close"] > 1000]
- df.describe()
- df.sort_values("volume", ascending=False)
- print(df["close"])
- df.loc[df["close"] < 800]


### Tensorflow testing statistics:

```
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10000, activation="relu"),
    tf.keras.layers.Dense(10000, activation="relu"),
    tf.keras.layers.Dense(5000, activation="relu"),
    tf.keras.layers.Dense(2500, activation="relu"),
    tf.keras.layers.Dense(500, activation="relu"),
    tf.keras.layers.Dense(100, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])
```
BATCH_SIZE = 10
EPOCHS = 5
```
Epoch 1/5
915/915 [==============================] - 60s 64ms/step - loss: 2363402.7500 - accuracy: 0.6550 - precision: 0.3190 - recall: 0.0218 - val_loss: 0.6369 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 2/5
915/915 [==============================] - 59s 64ms/step - loss: 0.6395 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6385 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 3/5
915/915 [==============================] - 59s 64ms/step - loss: 0.6402 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6367 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 4/5
915/915 [==============================] - 59s 64ms/step - loss: 0.6398 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6368 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 5/5
915/915 [==============================] - 59s 64ms/step - loss: 0.6401 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6387 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
```

---

```
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1000, activation="relu"),
    tf.keras.layers.Dense(1000, activation="relu"),
    tf.keras.layers.Dense(100, activation="relu"),
    tf.keras.layers.Dense(250, activation="relu"),
    tf.keras.layers.Dense(50, activation="relu"),
    tf.keras.layers.Dense(10, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])
```
BATCH_SIZE = 10
EPOCHS = 5
```
Epoch 1/5
915/915 [==============================] - 5s 4ms/step - loss: 14.2546 - accuracy: 0.6570 - precision: 0.3610 - recall: 0.0240 - val_loss: 0.6370 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 2/5
915/915 [==============================] - 4s 4ms/step - loss: 0.6395 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6385 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 3/5
915/915 [==============================] - 4s 4ms/step - loss: 0.6402 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6367 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 4/5
915/915 [==============================] - 4s 4ms/step - loss: 0.6398 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6368 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 5/5
915/915 [==============================] - 3s 4ms/step - loss: 0.6401 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6387 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
```

---
```
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1000, activation="relu"),
    tf.keras.layers.Dense(1000, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])
```
BATCH_SIZE = 10
EPOCHS = 5
```
Epoch 1/5
915/915 [==============================] - 4s 4ms/step - loss: 22.8660 - accuracy: 0.6526 - precision: 0.3567 - recall: 0.0396 - val_loss: 0.6371 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 2/5
915/915 [==============================] - 3s 3ms/step - loss: 0.6396 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6385 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 3/5
915/915 [==============================] - 3s 4ms/step - loss: 0.6402 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6367 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 4/5
915/915 [==============================] - 3s 3ms/step - loss: 0.6398 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6368 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 5/5
915/915 [==============================] - 3s 3ms/step - loss: 0.6401 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6387 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
```
---
```
model = tf.keras.Sequential([
    tf.keras.layers.Dense(500, activation="relu"),
    tf.keras.layers.Dense(500, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])
```
BATCH_SIZE = 10
EPOCHS = 5

```
Epoch 1/5
915/915 [==============================] - 4s 3ms/step - loss: 6.4173 - accuracy: 0.6581 - precision: 0.3687 - recall: 0.0214 - val_loss: 0.6369 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 2/5
915/915 [==============================] - 3s 3ms/step - loss: 0.6395 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6385 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 3/5
915/915 [==============================] - 3s 3ms/step - loss: 0.6402 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6367 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 4/5
915/915 [==============================] - 3s 3ms/step - loss: 0.6398 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6368 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 5/5
915/915 [==============================] - 3s 3ms/step - loss: 0.6401 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6387 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
```
---
```
model = tf.keras.Sequential([
    tf.keras.layers.Dense(100, activation="relu"),
    tf.keras.layers.Dense(100, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])
```
BATCH_SIZE = 10
EPOCHS = 5
```
Epoch 1/5
915/915 [==============================] - 4s 3ms/step - loss: 1.5224 - accuracy: 0.6580 - precision: 0.3909 - recall: 0.0279 - val_loss: 0.6369 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 2/5
915/915 [==============================] - 2s 3ms/step - loss: 0.6395 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6385 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 3/5
915/915 [==============================] - 2s 3ms/step - loss: 0.6402 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6367 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 4/5
915/915 [==============================] - 2s 3ms/step - loss: 0.6398 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6368 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 5/5
915/915 [==============================] - 2s 3ms/step - loss: 0.6401 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6387 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
```

---
```
model = tf.keras.Sequential([
    tf.keras.layers.Dense(50, activation="relu"),
    tf.keras.layers.Dense(50, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])
```
BATCH_SIZE = 10
EPOCHS = 5
```
Epoch 1/5
915/915 [==============================] - 4s 3ms/step - loss: 1.2903 - accuracy: 0.6541 - precision: 0.3372 - recall: 0.0282 - val_loss: 0.6369 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 2/5
915/915 [==============================] - 2s 3ms/step - loss: 0.6395 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6385 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 3/5
915/915 [==============================] - 2s 3ms/step - loss: 0.6402 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6367 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 4/5
915/915 [==============================] - 2s 3ms/step - loss: 0.6398 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6368 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 5/5
915/915 [==============================] - 2s 3ms/step - loss: 0.6401 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6387 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
```
---
```
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation="relu"),
    tf.keras.layers.Dense(10, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])
```
BATCH_SIZE = 10
EPOCHS = 5
```
Epoch 1/5
915/915 [==============================] - 4s 3ms/step - loss: 0.8868 - accuracy: 0.6568 - precision: 0.3439 - recall: 0.0211 - val_loss: 0.6183 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 2/5
915/915 [==============================] - 2s 3ms/step - loss: 0.6256 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6385 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 3/5
915/915 [==============================] - 2s 3ms/step - loss: 0.6402 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6367 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 4/5
915/915 [==============================] - 2s 3ms/step - loss: 0.6398 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6368 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 5/5
915/915 [==============================] - 2s 3ms/step - loss: 0.6401 - accuracy: 0.6633 - precision: 0.0000e+00 - recall: 0.0000e+00 - val_loss: 0.6387 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
```
---
```
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1000, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])
```

BATCH_SIZE = 10
EPOCHS = 5

```
Epoch 1/5
915/915 [==============================] - 4s 3ms/step - loss: 124.0592 - accuracy: 0.5717 - precision: 0.3633 - recall: 0.3614 - val_loss: 34.0179 - val_accuracy: 0.6077 - val_precision: 0.4153 - val_recall: 0.4336
Epoch 2/5
915/915 [==============================] - 3s 3ms/step - loss: 137.6593 - accuracy: 0.5729 - precision: 0.3650 - recall: 0.3630 - val_loss: 52.6235 - val_accuracy: 0.6165 - val_precision: 0.4261 - val_recall: 0.4336
Epoch 3/5
915/915 [==============================] - 3s 3ms/step - loss: 181.5483 - accuracy: 0.5685 - precision: 0.3562 - recall: 0.3487 - val_loss: 50.6196 - val_accuracy: 0.6460 - val_precision: 0.4444 - val_recall: 0.2478
Epoch 4/5
915/915 [==============================] - 3s 3ms/step - loss: 56.3410 - accuracy: 0.5752 - precision: 0.3697 - recall: 0.3714 - val_loss: 88.2195 - val_accuracy: 0.6667 - val_precision: 0.0000e+00 - val_recall: 0.0000e+00
Epoch 5/5
915/915 [==============================] - 3s 3ms/step - loss: 143.5872 - accuracy: 0.5869 - precision: 0.3860 - recall: 0.3844 - val_loss: 276.9673 - val_accuracy: 0.4208 - val_precision: 0.2439 - val_recall: 0.3510
```


### stuff n things

value_map = {
    "04:05": 0,
    "04:10": 1,
    "04:15": 2,
    "04:20": 3,
    "04:25": 4,
    "04:30": 5,
    "04:35": 6,
    "04:40": 7,
    "04:45": 8,
    "04:50": 9,
    "04:55": 10,
    "05:00": 11,
    "05:05": 12,
    "05:10": 13,
    "05:15": 14,
    "05:20": 15,
    "05:25": 16,
    "05:30": 17,
    "05:35": 18,
    "05:40": 19,
    "05:45": 20,
    "05:50": 21,
    "05:55": 22,
    "06:00": 23,
    "06:05": 24,
    "06:10": 25,
    "06:15": 26,
    "06:20": 27,
    "06:25": 28,
    "06:30": 29,
    "06:35": 30,
    "06:40": 31,
    "06:45": 32,
    "06:50": 33,
    "06:55": 34,
    "07:00": 35,
    "07:05": 36,
    "07:10": 37,
    "07:15": 38,
    "07:20": 39,
    "07:25": 40,
    "07:30": 41,
    "07:35": 42,
    "07:40": 43,
    "07:45": 44,
    "07:50": 45,
    "07:55": 46,
    "08:00": 47,
    "08:05": 48,
    "08:10": 49,
    "08:15": 50,
    "08:20": 51,
    "08:25": 52,
    "08:30": 53,
    "08:35": 54,
    "08:40": 55,
    "08:45": 56,
    "08:50": 57,
    "08:55": 58,
    "09:00": 59,
    "09:05": 60,
    "09:10": 61,
    "09:15": 62,
    "09:20": 63,
    "09:25": 64,
    "09:30": 65,
    "09:35": 66,
    "09:40": 67,
    "09:45": 68 ,
    "09:50": 69,
    "09:55": 70,
    "10:00": 71,
    "10:05": 72,
    "10:10": 73,
    "10:15": 74,
    "10:20": 75,
    "10:25": 76,
    "10:30": 77,
    "10:35": 78,
    "10:40": 79,
    "10:45": 80,
    "10:50": 81,
    "10:55": 82,
    "11:00": 83,
    "11:05": 84,
    "11:10": 85,
    "11:15": 86,
    "11:20": 87,
    "11:25": 88,
    "11:30": 89,
    "11:35": 90,
    "11:40": 91,
    "11:45": 92,
    "11:50": 93,
    "11:55": 94,
    "12:00": 95,
    "12:05": 96,
    "12:10": 97,
    "12:15": 98,
    "12:20": 99,
    "12:25": 100,
    "12:30": 101,
    "12:35": 102,
    "12:40": 103,
    "12:45": 104,
    "12:50": 105,
    "12:55": 106,
    "13:00": 107,
    "13:05": 108,
    "13:10": 109,
    "13:15": 110,
    "13:20": 111,
    "13:25": 112,
    "13:30": 113,
    "13:35": 114,
    "13:40": 115,
    "13:45": 116,
    "13:50": 117,
    "13:55": 118,
    "14:00": 119,
    "14:05": 120,
    "14:10": 121,
    "14:15": 122,
    "14:20": 123,
    "14:25": 124,
    "14:30": 125,
    "14:35": 126,
    "14:40": 127,
    "14:45": 128,
    "14:50": 129,
    "14:55": 130,
    "15:00": 131,
    "15:05": 132,
    "15:10": 133,
    "15:15": 134,
    "15:20": 135,
    "15:25": 136,
    "15:30": 137,
    "15:35": 138,
    "15:40": 139,
    "15:45": 140,
    "15:50": 141,
    "15:55": 142,
    "16:00": 143,
    "16:05": 144,
    "16:10": 145,
    "16:15": 146,
    "16:20": 147,
    "16:25": 148,
    "16:30": 149,
    "16:35": 150,
    "16:40": 151,
    "16:45": 152,
    "16:50": 153,
    "16:55": 154,
    "17:00": 155,
    "17:05": 156,
    "17:10": 157,
    "17:15": 158,
    "17:20": 159,
    "17:25": 160,
    "17:30": 161,
    "17:35": 162,
    "17:40": 163,
    "17:45": 164,
    "17:50": 165,
    "17:55": 166,
    "18:00": 167,
    "18:05": 168,
    "18:10": 168,
    "18:15": 170,
    "18:20": 171,
    "18:25": 172,
    "18:30": 173,
    "18:35": 174,
    "18:40": 175,
    "18:45": 176,
    "18:50": 177,
    "18:55": 178,
    "19:00": 179,
    "19:05": 180,
    "19:10": 181,
    "19:15": 182,
    "19:20": 183,
    "19:25": 184,
    "19:30": 185,
    "19:35": 186,
    "19:40": 187,
    "19:45": 188,
    "19:50": 189,
    "19:55": 190,
    "20:00": 191,    
}
