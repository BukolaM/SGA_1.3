with open ('/Users/bukola/Downloads/dummy_celebrity_dataset.csv') as file:
    dummy_celebrity = file.read()
    print(dummy_celebrity)
 

dummy_celebrity_data = dummy_celebrity.split('\n')


header = dummy_celebrity_data[0]
my_header = header.split(',')


del dummy_celebrity_data[0]
print(dummy_celebrity_data)

for item in dummy_celebrity_data:
    print(item.split(','))
