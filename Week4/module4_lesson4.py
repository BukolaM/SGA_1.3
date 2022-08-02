import sqlite3

conn = sqlite3.connect('celebrity.db')
cursor = conn.cursor()

# cursor.execute('''CREATE TABLE Celebrity (Name text, Genre text, Num_albums integer, Age integer, Awards integer,Years_in_industry interger)''')

celebrity_list = [
('Wizkid', 'afro dancehall', 4, 32, 80, 21),
('Tiwa Savage', 'afro beats', 3, 42, 7, 26),
('Arianda grande', 'pop', 11, 29, 360, 14),
('Davido', 'afro pop', 3, 29, 21, 13),
('Don Jazzy', 'afro beats', 9, 39, 3, 20),
('Mr Eazi', 'afro beats', 5, 31, 6, 10),
('Nicki minaj', 'hip hop rap', 4, 39, 12, 18),
('Cardi b', 'hip hop rap', 1, 29, 9, 15),
('Omah Lay', 'afro beats', 2, 25, 0, 4),
('Timi dakola', 'r&b', 1, 41, 1, 7),
('TClassic', 'afro beats', 2, 24, 0,3),
('Crayon',  'afro beats',1, 21, 0, 2),
('Felakuti','Afrobeat highlife jazz', 77,58, 2, 39),
('2Baba', 'afro pop', 6, 46, 50, 26),
('Timaya', 'afro dancehall', 6, 41, 2, 10),
('Olamide', 'afro beats', 9, 33, 4, 12),
('Asake', 'afro beats', 1, 27, 0, 2),
('Chrisbrown', 'r&b', 10, 33, 124, 20),
('Neyo', 'r&b', 11, 42, 8, 24),
('Joe', 'r&b', 11, 50, 3, 21),
('Oxlade', 'afro beats', 1, 24, 0, 2),
('Dbanj', 'afro beats', 2, 42, 7, 17),
('Flavour', 'afro beats', 17, 38, 5, 9),
('PSquare', 'afro pop', 6, 40, 2, 18),
('Rema', 'afro beats', 4, 22, 3,4),
('Falz', 'afro pop', 8, 31, 0, 7),
('DJ Neptune', 'afro dancehall', 3, 31, 3, 8),
('Banky W', 'afro dancehall', 5, 41, 4, 9),
('Korede Bello', 'afro dancehall', 3, 26, 2, 6),
('Kizz Daniel', 'afro dancehall', 4, 28, 8, 8),
('Sugarboy', 'nigerian pop', 2, 25, 0,5),
('Adekunle Gold', 'afro dancehall', 4, 35, 6, 8),
('Naeto C', 'afro dancehall', 2, 40, 2,10),
('Master Kraft', 'afro beats', 1, 35, 0,9),
('PSquare', 'afro pop', 6, 40, 2, 18),
('Flavour', 'afro beats', 17, 38, 5, 9),
('Wande Coal', 'afro dancehall', 6, 36, 2, 15),
('Wizkid', 'afro dancehall', 4, 32, 4, 21),
('Banky W', 'afro dancehall', 5, 41, 4, 9),
('PSquare', 'afro pop', 6, 40, 2,18),
('Kizz Daniel', 'afro dancehall', 4, 28, 8, 8),
('Davido', 'afro pop', 3, 29, 21, 13),
('Boj', 'afro dancehall', 6, 28, 1, 5),
('Banky W.', 'afro dancehall',5, 41,4, 9),
('Adekunle Gold', 'afro dancehall', 4, 35, 6, 8),
('Flavour', 'afro beats', 17, 38, 5, 9),
('Skales', 'afro dancehall', 12, 31, 7, 12),
('Kuami Eugene', 'afro pop', 0, 25, 5, 8),
('9ice', 'afro dancehall', 17, 42, 3, 22),
]
# cursor.executemany('INSERT INTO Celebrity VALUES(?, ?, ?, ?, ? ,?)', celebrity_list)
# conn.commit()

# cursor.execute('SELECT * FROM Celebrity')
# item = cursor.fetchmany(51)
# print('Name' +   ' \t\tGenre' +   ' \t\tNum_albums' +   ' \t\tAge' +   ' \t\tAwards' +'\t\tYears_in_industry ')

# print ('------------' +    ' \t-------------' + ' \t--------------'+ ' \t-------------' + ' \t------------- ' + '\t--------------' )

# for item in item:
#     print(item[0] + ' \t ' +  item[1] + ' \t\t' + str(item[2]) +  ' \t\t ' + str(item[3]) + ' \t\t ' + str(item[4]) + '\t\t' +str(item[5]))




#function to get list of items from the table
def fetch_data(list):
    cursor.execute(list)
    list=cursor.fetchall()
    result = []
    for item in list:
        result.append(item)
    return result

# 1. ##Who is the most decorated celebrity
def most_celebrated():
    query = '''SELECT DISTINCT Name, SUM(Awards) 
            FROM Celebrity 
            GROUP BY Name 
            ORDER BY SUM(Awards) DESC
            LIMIT 1 '''
    data = fetch_data(query)
    return data

most_decorated_celebrity = most_celebrated()
print(most_decorated_celebrity)


#2. Who is the oldest celebrity?
def oldest():
    query= '''SELECT DISTINCT Name, MAX(Age)
            FROM Celebrity
            GROUP BY Name
            ORDER BY MAX(Age) DESC
            LIMIT 1'''
    data = fetch_data(query)
    return data           

oldest_celebrity= oldest()
print(oldest_celebrity)


 #3. Which celebrity has been in the industry the longest?
def longest_in_industry():
    query= '''SELECT DISTINCT Name, MAX(Years_in_industry)
            FROM Celebrity
            GROUP BY Name
            ORDER BY MAX(Years_in_industry) DESC
            LIMIT 1'''
    data = fetch_data(query)
    return data           

longest_celebrity_in_industry= longest_in_industry()
print(longest_celebrity_in_industry)

#4. Which celebrity has the least number of albums?
def least_album():
    query= '''SELECT DISTINCT Name, MIN(Num_albums)
            FROM Celebrity
            GROUP BY Name
            ORDER BY MIN(Num_albums) ASC
            LIMIT 1'''
    data = fetch_data(query)
    return data  

celebrity_with_least_album= least_album()
print(celebrity_with_least_album)


#What is the most popular genre of music amongst all celebrities in the dataset
def music_genre():
    query= '''SELECT DISTINCT Genre, COUNT(Genre)
            FROM Celebrity
             GROUP BY Genre
             ORDER BY COUNT(Genre) DESC
             LIMIT 1'''
    data = fetch_data(query)
    return data  
most_popular_music_genre = music_genre()
print(most_popular_music_genre)