import csv

path = "data.csv"

def read_csv(path):
    with open(path, 'r') as file:
        rows = list(csv.reader(file))
        keys = rows.pop(0)
        return [
            {key: value for key, value in zip(keys, row)}
            for row in rows
        ]

print(read_csv(path))

# my_data = [{
#     "name": "John Doe",
#     "balance": 30,
#     "date": "2023-01-01"
# }, {
#     "name": "Jane Smith",
#     "balance": 40,
#     "date": "2023-01-02"
# }, {
#     "name": "Bob Johnson",
#     "balance": 50,
#     "date": "2023-01-03"
# }]
