import psycopg2


'''Обьект подключения'''
with psycopg2.connect(database='DS1', user='postgres', password='sfdr34wrtyi') as conn: 
    '''Помогает выполнять запросы и получать ответы обратно от базы'''
    with conn.cursor() as cur:        
        cur.execute("DROP TABLE Client; DROP TABLE Email; DROP TABLE Telephone;")
        def DS1(cursor, d, f):
            '''запрос SQL'''
            cur.execute(
                'CREATE TABLE if not exists Client(client_id SERIAL PRIMARY KEY, \
                Name VARCHAR(50) UNIQUE NOT null, \
                Surname VARCHAR(50) UNIQUE NOT null);') 
            for u, w in zip(d, f):
                u1 = u
                w1 = w
                print(u1, w1)
           
            cur.execute(             
                "INSERT INTO Client(Name, Surname) VALUES(%s, %s);", (d, f,))
               
            conn.commit() 
            
    
        Na =['Сидоров', 'Петров', 'Иванов']         
        Sur = ['Том', 'Боб', 'Иванов']    
        DS1(cur, Na, Sur)
        

        def DS2(cursor, a, s):
            cur.execute(
                'CREATE TABLE if not exists Email(email_id SERIAL PRIMARY KEY, \
                email VARCHAR(50) UNIQUE NOT null, \
                Client integer references Client(client_id));')
                                    
            cur.execute("INSERT INTO Email(email) values(%s), (%s)  RETURNING email;", (a, s,))             
            print(cur.fetchall())
        
        DS2(cur, 'gfd.ru', 'dfg.ru')

        def DS3(cursor, mn):
            cur.execute(
                'CREATE TABLE if not exists Telephone(telephone_id SERIAL PRIMARY KEY, \
                telephone VARCHAR(50) UNIQUE NOT null, \
                Client integer references Client(client_id));')
            cur.execute('INSERT INTO Telephone(telephone) VALUES(%s) RETURNING telephone;', (mn,)) 
            print(cur.fetchall())

        DS3(cur, '89876542365')

        def DS4(cursor, N, S):
            '''Добовляет нового клиента'''
            cur.execute("INSERT INTO Client(Name, Surname) VALUES(%s, %s) RETURNING Name, Surname;", (N, S,)) 
            print(cur.fetchall())           

        DS4(cur, 'Сидоров', 'Юрьевна')  

        def DS5(cursor, tel, id):
            '''Добовляет телефон для уже существующего клиента''' 
            cur.execute("INSERT INTO Telephone(telephone, Client) VALUES(%s, %s) RETURNING telephone, Client;", (tel, id,))             
            print(cur.fetchall())

        DS5(cur, 8987654321, 1)  

        def DS6(cursor, up, uo):
            cur.execute('UPDATE Client SET Name=%s WHERE client_id=%s RETURNING Name;', (up, uo,))
            return cur.fetchone() 
        
        r = DS6(cur, 'Маша', 1)
        print(r)

        def DS7(cursor, up1, uo1):   
            cur.execute('UPDATE Client SET Surname=%s WHERE client_id=%s RETURNING Surname;', (up1, uo1,))
            return cur.fetchone()   
        
        r1 = DS7(cur, 'Арнольд', 1)  
        print(r1)

        def DS8(cursor, id, tel):
            """Функция, позволяющая удалить телефон для существующего клиента"""
            cur.execute('DELETE FROM Telephone WHERE Client=%s and telephone=%s;', (id, tel,))  
            conn.commit()
            
        DS8(cur, 1, '89876542365')

        def DS9(cursor, tel2, id):
            """Функция, позволяющая удалить существующего клиента."""
            cur.execute('DELETE FROM Telephone WHERE telephone=%s and Client=%s;', (tel2, id,))  
            conn.commit()

        DS9(cur, '8987654321', 1)    

        def DS10(cursor, n, s, id):    
            cur.execute('DELETE FROM Client WHERE Name=%s and Surname=%s and client_id=%s;', (n, s, id,))          
            conn.commit()
            
        DS10(cur, 'Маша', 'Арнольд', 1)

        def DS11(cur, Name, Surname, telephone, email): 
            '''Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.'''         
            cur.execute("SELECT Name, Surname, email, telephone FROM Client c JOIN Email e on e.email_id = e.Client \
            JOIN Telephone t on t.telephone_id = t.Client WHERE Name=%s and Surname=%s and telephone=%s or email=%s;", (Name, Surname, telephone, email,))
            return cur.fetchall()
    
        p = DS11(cur, 'Иванов', 'Иванов', '89876542365', 'dfg.ru')
        print('Client:', p)
conn.close()
          
        
       




