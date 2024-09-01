import csv


def read_csv_to_dict(file_name, skip_header=False):
    data = {}
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        if skip_header:
            next(reader)
        for row in reader:
            contact_id = row[0]
            rest_of_row = tuple(row[1:])
            data[rest_of_row] = contact_id
    return data


with open('random.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    header = next(reader)

data1 = read_csv_to_dict('random.csv', skip_header=True)
data2 = read_csv_to_dict('random-michaels.csv', skip_header=True)

combined_data = {**data1, **data2}

with open('result_savchyn.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for rest_of_row, contact_id in combined_data.items():
        writer.writerow((contact_id,) + rest_of_row)
