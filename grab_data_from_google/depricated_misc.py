def start_format_data():

    INDEX_FOLDER = "./index_data/"
    DATA_FOLDER = "./downloaded_data/"
    EARLIEST_INDEX_DATE = "1971-02-05"

    test_data = "AAPL.csv"

    format_data(test_data, INDEX_FOLDER, DATA_FOLDER, EARLIEST_INDEX_DATE)


def format_data(file_name, INDEX_FOLDER, DATA_FOLDER, EARLIEST_INDEX_DATE):
    """

    THE FORMAT OF THE DATA: 

    100 days if actual data

    10 years of index close data.

    NASDAQ (IXIC) from: 1971-02-05
    Dow Jones (DJI) from:  1970-01-02
    S&P (INX) from: 1970-01-02


    Calc spans:

    The oldest index span must start at 1971-02-05 because IXIC





    """

    def calc_spans(dates):

        # check if first date is before limit, set by index + 10y
        valid_dates = []
        for date in dates:

            date_formated = datetime.datetime.strptime(
                str(date.split(" ")[0]), "%Y-%m-%d")

            index_date = datetime.datetime.strptime(
                EARLIEST_INDEX_DATE, "%Y-%m-%d")

            if date_formated < datetime.datetime(index_date.year + 10, index_date.month, index_date.day):
                print("Date before index, skipping: ", date_formated)
                continue

            valid_dates.append(date)

        amount_of_splits = int(round(len(valid_dates) / 100, 1))

        print(amount_of_splits)

        if amount_of_splits < 1:
            print("THIS STOCK HAS LESS THAN 100 DATAPOINTS")
            return

        spans = []
        for split in range(amount_of_splits):

            BATCH_SIZE_OF_ACTUAL_STOCK = 100

            span_index = [(BATCH_SIZE_OF_ACTUAL_STOCK * split),
                          (BATCH_SIZE_OF_ACTUAL_STOCK * split + BATCH_SIZE_OF_ACTUAL_STOCK)]
            span_inner = []
            for i in span_index:
                span_inner.append(valid_dates[i].split(" ")[0])
            spans.append(span_inner)

        # for i, value in enumerate(span):
        #     print(f"INDEX: {i}, SPAN: {value}")

        return spans

    def get_index_values(spans):

        # load index data:
        data_obj = [
            pd.read_csv(INDEX_FOLDER + "DJI_close.csv"),  # 0 = DJI
            pd.read_csv(INDEX_FOLDER + "INX_close.csv"),  # 1 = INX
            pd.read_csv(INDEX_FOLDER + "IXIC_close.csv")  # 2 = IXIC
        ]

        # DJI_df = pd.read_csv(INDEX_FOLDER + "DJI_close.csv")
        # INX_df = pd.read_csv(INDEX_FOLDER + "INX_close.csv")
        # IXIC_df = pd.read_csv(INDEX_FOLDER + "IXIC_close.csv")

        def check_if_date_is_valid(date):

            # Check if index start is a valid date, make sure its not during weekend or something alike
            df = pd.read_csv(INDEX_FOLDER + "DJI_close.csv")

            df["Date"] = df["Date"].str.replace(" 16.00.00", "")
            index_for_date = df.index[df["Date"] ==
                                      date.strftime("%Y-%m-%d")]

            if len(index_for_date.values):
                #print("Returning valid date: ", date.strftime("%Y-%m-%d"))
                return date

            #print("Date not valid, rechecking...")
            return check_if_date_is_valid(date + relativedelta(days=1))

        index_spans = []
        for index, span in enumerate(spans):

            span_start_date = datetime.datetime.strptime(span[0], "%Y-%m-%d")

            index_start_date = span_start_date + relativedelta(years=-10)

            index_start_date = check_if_date_is_valid(index_start_date)

            #print(f"INDEX: {index}, SPAN: {index_start_date}")

            index_spans.append([
                index_start_date.strftime("%Y-%m-%d"),
                span_start_date.strftime("%Y-%m-%d")
            ])

        # Mapping data to spans
        for span in index_spans:
            for index, df in enumerate(data_obj):
                #print("KEY: ", key)
                #print("VALUE: ", value)

                df["Date"] = df["Date"].str.replace(" 16.00.00", "")

                start_index = df.index[df["Date"] == span[0]]
                end_index = df.index[start_index - 2600]

                if not len(start_index.values):
                    print(f"Start date wrong: {span[0]}")

                if not len(end_index.values):
                    print(f"End date wrong: {span[1]}")

                print(start_index, end_index)
                print("START_VALUES: ",
                      df.at[start_index.values[0], "Date"], "||",  span[0])
                print("END_VALUES: ",
                      df.at[end_index.values[0], "Date"], "||",  span[1])
                print("\n")

        return index_spans

    df = pd.read_csv(DATA_FOLDER + file_name)

    spans = calc_spans(df["Date"])

    get_index_values(spans)
