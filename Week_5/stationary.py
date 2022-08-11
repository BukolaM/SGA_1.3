with open ('/Users/bukola/Downloads/Stationary_List.csv') as file:
   file_list = file.read()
 
all_list = file_list.split('\n')

header = all_list[0]
my_header = header.split(',')

del all_list[0]

for item in all_list:
    all_rows = item.split(',')
    print(all_rows)


