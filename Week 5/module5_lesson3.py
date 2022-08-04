import sqlite3

conn = sqlite3.connect('Stationaries.db')
cursor = conn.cursor()

# cursor.execute('''CREATE TABLE Stationaries (Stationary_ID text,Stationary_Item text ,Total_Stock integer,Total_Sold integer,Stock_on_hand integer,'Threshold_to_restock' integer,Unit_Price integer)''')

stationary_list = [
('IT001', 'Stapler', '10', '5', '5', '3', '500'),
('IT002', 'Eraser', '12', '4', '8', '3', '20'),
('IT003', 'Push-pin', '50', '12', '38', '10', '10'),
('IT004', 'Pencils', '80', '35', '45', '25', '15'),
('IT005', 'Paper clip', '70', '25', '45', '20', '5'),
('IT006', 'Rubber stamp', '13', '7', '6', '5', '20'),
('IT007', 'Notebooks', '40', '12', '28', '12', '100'),
('IT008', 'Fountain pen', '20', '18', '2', '5', '200'),
('IT009', 'Envelopes', '100', '45', '55', '24', '22'),
('IT010', 'Marker', '100', '64', '36', '20', '50'),
('IT011', 'Ballpoint', '19', '3', '16', '8', '29'),
('IT012', 'Tape dispenser', '20', '8', '12', '5', '20'),
('IT013', 'Pencil sharpener', '17', '12', '5', '6', '25'),
('IT014', 'Label', '25', '20', '5', '15', '20'),
('IT015', 'Calculator', '10', '3', '7', '5', '1000'),
('IT016', 'Glue', '14', '5', '9', '6', '20'),
('IT017', 'Scissors', '10', '1', '9', '3', '550'),
('IT018', 'Sticky notes', '30', '14', '16', '11', '40'),
('IT019', 'Paper', '55', '19', '36', '25', '80'),
('IT020', 'Envelope', '14', '9', '5', '7', '75'),
('IT021', 'Clipboard', '15', '11', '4', '6', '60'),
('IT022', 'Folder', '45', '29', '16', '14', '30'),
('IT023', 'Filing cabinet', '30', '5', '25', '10', '45'),
('IT024', 'Wastebasket', '5', '4', '1', '3', '40'),
('IT025', 'Toners', '6', '1', '5', '2', '55')
]

# cursor.executemany('INSERT INTO Stationaries VALUES (?,?,?,?,?,?,?)', stationary_list )
# conn.commit()


# cursor.execute('SELECT * FROM Stationaries')
# item = cursor.fetchmany(30)
# print('Stationary_ID' + '\tStationary_Item' + '\tTotal_Stock' + '\tTotal_Sold' 
# + '\tStock_on_hand'  + '\tThreshold_to_restock' + '\tUnit_Price')
# print ('-----' + '\t\t-------' +'\t\t-------' + '\t\t------- ' + '\t\t------' + '\t\t------' + '\t\t------')

# for item in item:
#     print(item[0] + ' \t\t ' + item[1] + ' \t\t' +  str(item[2]) + '\t\t' + str(item[3]) + 
#     '\t\t'  + str(item[4])+ '\t\t' + str(item[5])+ '\t\t' + str(item[6]))



#function to get list of items from the table
def fetch_data(sql_query):
    cursor.execute(sql_query)
    list=cursor.fetchall()
    for item in list:
        print(item)


# 1. Calculate the amount the business owner invested in the procurement of the items.   
def total_amount_invested():
    query = '''SELECT SUM(Unit_Price)
            FROM Stationaries
            '''
    data = fetch_data(query)
    return data
total_amount_invested()


# 2. Calculate the average quantity of items in stock.
def avg_quantity_of_itemsinstock():
    query = '''SELECT AVG(Stock_on_hand)
                FROM Stationaries
            '''
    data = fetch_data(query)
    return data
avg_quantity_of_itemsinstock()


# 3. Determine the item with the least quantity in stock
def least_quantity_instock():
    query = '''SELECT Stationary_Item, MIN(Stock_on_hand)
            FROM Stationaries
            GROUP BY Stationary_Item
            ORDER BY MIN(Stock_on_hand) ASC
            LIMIT 1
            '''
    data = fetch_data(query)
    return data
least_quantity_instock()


# #4. Determine the item with the most quantity in stock
def most_quantity_instock():
    query = '''SELECT Stationary_Item, MAX(Stock_on_hand)
            FROM Stationaries
            GROUP BY Stationary_Item
            ORDER BY MAX(Stock_on_hand) DESC
            LIMIT 1
            '''
    data = fetch_data(query)
    return data
most_quantity_instock()




