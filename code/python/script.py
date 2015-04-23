__author__ = 'Shamir Eyram Adjkau'
import csv


def is_complete(row_item):
    """
    This method checks a row to make sure all columns have valid values.
    :param row_item: The row to check
    :return: true if all columns have valid values and false if a column has ".." or "#N/A"
    """
    for column in row_item:
        if column == '..' or column == '#N/A':
            return False
    return True


with open('../../modified/integrated_data.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    all_rows_test = []
    all_rows_train = []
    all_rows = []

    for row in reader:
        all_rows_test.append(row)
        all_rows_train.append(row)
        all_rows.append(row)
        break

    switch = 0
    # read the csv file
    for row in reader:
        # check if it is complete
        if is_complete(row):
            # add to the list of complete rows
            if switch == 1:
                all_rows_test.append(row)
                switch = 0
            else:
                all_rows_train.append(row)
                switch = 1
            all_rows.append(row)

    # create output file and open for writing
    test_writer = csv.writer(open('../../modified/integrated_data_cleaned_test.csv', 'wb'), delimiter=',')
    train_writer = csv.writer(open('../../modified/integrated_data_cleaned_train.csv', 'wb'), delimiter=',')
    _writer = csv.writer(open('../../modified/integrated_data_cleaned_all.csv', 'wb'), delimiter=',')
    print()

    # write each row into the file
    for row in all_rows_test:
        test_writer.writerow(row)

    for row in all_rows_train:
        train_writer.writerow(row)

    for row in all_rows:
        _writer.writerow(row)


