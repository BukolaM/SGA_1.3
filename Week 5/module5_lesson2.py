import sqlite3
import csv

conn= sqlite3.connect('WAEC_Stores.db')
cursor = conn.cursor()

 
create_table = '''
CREATE TABLE Scores
(first_name text, 
last_name text, 
General_Mathematics float,
English_Language float, 
Chemistry float,
Physics float, 
Economics float, 
Geography float, 
Biology float, 
Agricultural_Science float, 
Further_Mathematics float
)
'''

# cursor.execute(create_table)
with open ('/Users/bukola/Downloads/WAEC Results.csv', "r") as file_list:
    read_file = csv.reader(file_list)
    next(read_file)

    cursor.executemany('''INSERT INTO Scores VALUES(?, ?, ?, ?, ? ,?, ?, ?, ?, ?, ?)''', read_file)
    conn.commit()


# cursor.execute('SELECT * FROM Scores')
# items = cursor.fetchmany(20)
# print('first_name' +   '\tlast_name' +  '\tGeneral_Mathematics' +  '\tEnglish_Language' +  '\tChemistry' + '\tPhysics' + '\tEconomics' + '\tGeography' + '\tBiology' + '\tAgricultural_Science' + '\tFurther_Mathematics')

# print ('----' + '\t---' + '\t----'+ '\t----' + '\t----' + '\t------'  + '\t------' + '\t-------' + '\t------' + '\t------' + '\t------')

# for item in items:
#     print(item[0] + '\t' +  item[1] + '\t' + str(item[2]) +  '\t' + str(item[3]) +  '\t ' + str(item[4]) + '\t' + str(item[5]) + '\t' + str(item[6])+ '\t' + str(item[7]) + '\t' + str(item[8]) + '\t' + str(item[9]) + '\t' + str(item[10])) 



##function to get list of items from the table
def fetch_data(sql_query):
    cursor.execute(sql_query)
    items = cursor.fetchmany(20)
    for item in items:
        print(item)


# 1. Which student scored the highest in maths
def highest_math(): 
    query = ''' SELECT  first_name , last_name , MAX(General_Mathematics)
                FROM Scores
                GROUP BY first_name, last_name 
                ORDER BY MAX(General_Mathematics) DESC
                LIMIT 2
                '''
    data = fetch_data(query)  
    return data
highest_math()
# pls note there are two students with the same highest scores, hence why i had to limit to two

# 2.Which student scored the lowest in english
def lowest_english(): 
    query = ''' SELECT  first_name , last_name , MIN(English_Language)
                FROM Scores
                GROUP BY first_name, last_name 
                ORDER BY MIN(English_Language) ASC
                LIMIT 1'''            
    data = fetch_data(query)  
    return data
lowest_english()


#3. What is the average score of students in maths
def average_maths(): 
    query = ''' SELECT  ROUND(AVG(General_Mathematics))
                FROM Scores'''              
    data = fetch_data(query)  
    return data
average_maths()


# 4. What is the average score of students in english
def average_english(): 
    query = ''' SELECT  ROUND(AVG(English_Language))
                FROM Scores '''              
    data = fetch_data(query)  
    return data
average_english()


# 5. Who is the best performing student across all nine subjects in terms of overall scores
def highest_overall_scores(): 
    query = ''' SELECT first_name , last_name , ( ROUND( ( ( General_Mathematics + English_Language + Chemistry + Physics + Economics + Geography + Biology + Agricultural_Science + Further_Mathematics) / (900) ) * 100) )  AS TOTAL_PERCENTAGE
                FROM Scores
                ORDER BY TOTAL_PERCENTAGE DESC
                LIMIT 1'''               
    data = fetch_data(query)  
    return data
highest_overall_scores()



# 6. Who is the best performing student across all nine subjects in term of average scores
def highest_avg_scores(): 
    query = ''' SELECT first_name , last_name , (ROUND((General_Mathematics + English_Language + Chemistry + Physics + Economics + Geography + Biology + Agricultural_Science + Further_Mathematics) / (9) ))  AS AVERAGE_PERCENTAGE
                FROM Scores
                ORDER BY AVERAGE_PERCENTAGE DESC
                LIMIT 1 ''' 
    data = fetch_data(query)  
    return data
highest_avg_scores()










