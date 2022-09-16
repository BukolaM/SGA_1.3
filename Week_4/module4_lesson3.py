
import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

# cursor.execute('''CREATE TABLE Students (first_name text,last_name text,email text,course text)''')

students_list = [
                ('Aishat','Abass','aishatabass@gmail.com','Data Science'),
                ('Babajide','Adesugba','babajideadesugba@gmail.com','Data Science'), 
                ('Faith','Amure','faithamure@gmail.com','Data Science'),
                ('Deborah','Olorunnishola','deboraholorunnishola@gmail.com','Data Science'),
                ('Kafayat','Ibrahim','kafayatibrahim@gmail.com','Data Science'),
                ('Cynthia','Awiya','cynthiaawiya@gmail.com','Data Science'),
                ('Stephen','Ogungbile','stephenogunbile@gmail.com','Data Science'),
                ('Omowunmi', 'Awoniran','omowunmiawoniran@gmail.com','Data Science'),
                ('Tawakalitu', 'Awonaike','tawakalituawonaike@gmail.com','Data Science'),
                ('Afolabi', 'Ade','afolabiade@gmail.com','Data Science'),
                ('Ramotallah','Jubril','ramotallahjubril@gmail.com','Data Science'),
                ('Joyce','Ezeonwu','joyceezeonwu@gmail.com','Data Science'),
                ('Mariam','Adeoti','mariamadeoti@gmail.com','Data Science'),
                ('Praise','Emmanuel','praiseemmanuel@gmail.com','Data Science'),
                ('Kehinde','Orolade','kehindeorolade@gmail.com','Data Science'),
                ('Temitope','Bamidele','temitopbamidele@gmail.com','Data Science'),
                ('Christian','Uzondu','christianuzondu@gmail.com','Data Science'),
                ('Theresa', 'Karamor','theresakaramor@gmail.com','Data Science'),
                ('Uyateide','Tina','uyateidetina@gmail.com','Data Science'),
                ('Bukola','Ajayi','bukolaajayi@gmail.com','Data Science'),
                ('Gideon','George','sgideongeorge@gmail.com','Data Science'),
                ('Abubakar','Adisa','abubakaradisa@gmail.com','Data Science'),
                ('Deborah','Adesanya','deborahadesanya@gmail.com','Data Science'),
                ('Ogechi','Njemanze','ogechinjemanze@gmail.com','Data Science'),
                ('Victoria','Chukwuno','victoriachukwuno@gmail.com','Data Science'),
                ('Ganiyat','Shittu','ganiyatshittu@gmail.com','Data Science'),
                ('Eniola','Osadare','eniolaosadare@gmail.com','Data Science'),
                ('Lawrence','Aneshimokha','lawrenceaneshimoka@gmail.com','Data Science'),
                ('Eke','Ihuoma','ekeihuoma@gmail.com','Data Science'),
                ('Angela','Emmanuel', 'angelaemmanuel@gmail.com','Data Science'),
                ('Oluwaseyi','Nichiolas','oluwaseyinichiolas@gmail.com','Data Science'),
                ('Doyinsola','Esan','doyinsolaesan@gmail.com','Data Science'),
                ('Kehinde','Ayanleye','kehindeayanleye','Data Science'),
                ('Doyinsola','Esan','doyinsolaesan@gmail.com','Data Science')
                ]   
                              
# cursor.executemany('INSERT INTO Students VALUES(?, ?, ?, ?)', students_list)
# conn.commit()

# cursor.execute('SELECT * FROM Students')
# item = cursor.fetchmany(34)
# print('first_name' + '\tlast_name' + '\temail' + '\t\t\t\tcourse')
# print ('----------' + '\t\t-----------' +'\t\t-----------' + '\t\t------------')

# for item in item:
#     print(item[0] + ' \t\t\t ' + item[1] + ' \t\t\t ' + item[2] + '\t\t\t' + item[3])


# Alter the table we created in class today:
# Rename the table
# cursor.execute("ALTER TABLE Students RENAME TO students_details")
# conn.commit()
# print ('executed')


# # Add a new column
cursor.execute('ALTER TABLE students_details ADD students_bonus')
conn.commit()
print('success')

# # Use the update statement to add values to the new column 
cursor.execute('UPDATE students_details SET students_bonus = 1000')
conn.commit()
print('bonus added')

#test and run codes
cursor.execute('SELECT * FROM students_details')
item = cursor.fetchmany(34)
print('first_name' + '\t\tlast_name' + '\t\temail' + '\t\t\t\tcourse' + '\t\t\tstudents_bonus')
print ('----------' + '\t\t-----------' +'\t\t-----------' + '\t\t\t------------' + '\t\t\t----------')

for item in item:
    print(item[0] + ' \t\t\t' +  item[1] + ' \t\t\t' + str(item[2]) +  ' \t\t ' + str(item[3]) + ' \t\t ' + str(item[4]))


















