# import sqlite3

# conn = sqlite3.connect('Stationary.db')
# cursor = conn.cursor()

# # cursor.execute('''CREATE TABLE Stationary (Stationary_ID text,Stationary_Item text ,Total_Stock integer,Total_Sold integer,Stock_on_hand integer,'Threshold_to_restock' integer,Unit_Price integer)''')

# stationary_list = [
# ('IT001', 'Stapler', '10', '5', '5', '3', '500'),
# ('IT002', 'Eraser', '12', '4', '8', '3', '20'),
# ('IT003', 'Push-pin', '50', '12', '38', '10', '10'),
# ('IT004', 'Pencils', '80', '35', '45', '25', '15'),
# ('IT005', 'Paper clip', '70', '25', '45', '20', '5'),
# ('IT006', 'Rubber stamp', '13', '7', '6', '5', '20'),
# ('IT007', 'Notebooks', '40', '12', '28', '12', '100'),
# ('IT008', 'Fountain pen', '20', '18', '2', '5', '200'),
# ('IT009', 'Envelopes', '100', '45', '55', '24', '22'),
# ('IT010', 'Marker', '100', '64', '36', '20', '50'),
# ('IT011', 'Ballpoint', '19', '3', '16', '8', '29'),
# ('IT012', 'Tape dispenser', '20', '8', '12', '5', '20'),
# ('IT013', 'Pencil sharpener', '17', '12', '5', '6', '25'),
# ('IT014', 'Label', '25', '20', '5', '15', '20'),
# ('IT015', 'Calculator', '10', '3', '7', '5', '1000'),
# ('IT016', 'Glue', '14', '5', '9', '6', '20'),
# ('IT017', 'Scissors', '10', '1', '9', '3', '550'),
# ('IT018', 'Sticky notes', '30', '14', '16', '11', '40'),
# ('IT019', 'Paper', '55', '19', '36', '25', '80'),
# ('IT020', 'Envelope', '14', '9', '5', '7', '75'),
# ('IT021', 'Clipboard', '15', '11', '4', '6', '60'),
# ('IT022', 'Folder', '45', '29', '16', '14', '30'),
# ('IT023', 'Filing cabinet', '30', '5', '25', '10', '45'),
# ('IT024', 'Wastebasket', '5', '4', '1', '3', '40'),
# ('IT025', 'Toners', '6', '1', '5', '2', '55')
# ]

# # cursor.executemany('INSERT INTO Stationary VALUES (?,?,?,?,?,?,?)', stationary_list )
# # conn.commit()


# # cursor.execute('SELECT * FROM Stationary')
# # item = cursor.fetchmany(30)
# # print('Stationary_ID' + '\tStationary_Item' + '\tTotal_Stock' + '\tTotal_Sold' 
# # + '\tStock_on_hand'  + '\tThreshold_to_restock' + '\tUnit_Price')
# # print ('-----' + '\t\t-------' +'\t\t-------' + '\t\t------- ' + '\t\t------' + '\t\t------' + '\t\t------')

# # for item in item:
# #     print(item[0] + ' \t\t ' + item[1] + ' \t\t' +  str(item[2]) + '\t\t' + str(item[3]) + 
# #     '\t\t'  + str(item[4])+ '\t\t' + str(item[5])+ '\t\t' + str(item[6]))


# # # 1. '''Create an inventory table containing&nbsp; 10&nbsp; or more items, 
# # # showing price and the quantity in stock. Give each item an ID
# # #  The business owner wants to see the items to restock and which is sufficient from 
# # the highest to lowest cost price'''


# #function to get list of items from the table
# def fetch_data(sql_query):
#     cursor.execute(sql_query)
#     list=cursor.fetchall()
#     result = []
#     for item in list:
#         result.append(item)
#     return result
       
    
# def to_restock():
#     query = '''SELECT DISTINCT Stationary_Item, SUM(Unit_Price),
#                 CASE
#                 WHEN SUM(Stock_on_hand) < SUM(Threshold_to_restock) THEN "Restock"
#                 WHEN SUM(Stock_on_hand) > SUM(Threshold_to_restock) THEN "Sufficient"
#                 ELSE "PASS"
#             END
#             FROM Stationary GROUP BY Stationary_Item
#             ORDER BY SUM(Unit_Price) DESC
#             '''
#     data = fetch_data(query)
#     return data

# items_to_restock = to_restock()
# for items in items_to_restock:
#     print(items)



# x = (8, 2, 3, 0, 7)
# a = 0
# for y in x:
#   a = a + y
# print(a)


# x = (8, 2, 3, -1, 7)
# a = 1
# for y in x:
#     a = a * y
# print(a)  


# x = "1234abcd"
# y = str(x).revers
# print(y)


# def all_numbers(x):
#     if 90 in x:
#         return 'okay'

# y = all_numbers(range(10))
# print(y)



# def all_number(x):
#     k = 0
#     for y in x:
#         if y.isupper() is True:
#             k = k + 1
#     print(k)        

# all_number('The quick Brow Fox')



# Sample_Dictionary = {0: 10, 1: 20}
# Sample_Dictionary[2]=30
# print(Sample_Dictionary)


# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}

# x = dic1 + dic2 + dic3
# print(x)

x = [10, 20, 30]
y = [40, 50, 60]
a =x+y
print(a)



my_dict = {'data1':100,'data2':-54,'data3':247}
print(my_dict.keys())