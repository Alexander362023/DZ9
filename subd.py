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
            Sur = ['Том', 'Боб', 'Джек']    
            DS1(cur, Na, Sur)


        def DS2(cursor):
            cur.execute(
                'CREATE TABLE if not exists Email(email_id SERIAL PRIMARY KEY, \
                email VARCHAR(50) UNIQUE NOT null, \
                Client integer references Client(client_id));')
    
            cur.execute(             
                'INSERT INTO Telephone(telephone) VALUES(%s);', (89876541287,))
            return cur.fetchmany()
        emai = DS2(cur)
        print(emai)    
    
    cur.execute(
        'CREATE TABLE if not exists Telephone(telephone_id SERIAL PRIMARY KEY, \
        telephone integer UNIQUE NOT null, \
        Client integer references Client(client_id));')
               
   
                     
    cur.execute(             
            'INSERT INTO Telephone(telephone) VALUES(%s);', S)             

    cur.execute("INSERT INTO Email(email) values('gfd.ru'), ('dfg.ru');")
            
    conn.commit()



DS1(cur, e) 
       
def DS2(cursor, Name, Surname):
    '''Добовляет нового клиента'''
    cur.execute("INSERT INTO Client(Name, Surname) VALUES(%s, %s);", Name, Surname) 
    conn.commit()

DS2(cur, ('Сидоров', 'Иван'), ('Мария', 'Юрьевна'))        
         

def DS3(cursor, ):
    '''Добовляет телефон для уже существующего клиента''' 
    cur.execute("INSERT INTO Telephone(telephone, Client) VALUES(%s, %s);", (8987654321, 1), (8974563214, 1)) 
    conn.commit()
DS3((8987654321, 1), (8974563214, 1))   

def DS4():
    cur.execute('UPDATE Client SET Name=%s WHERE id=%s;', ('Сидоров', id))
    cur.execute('UPDATE Client SET Surname=%s WHERE id=%s;', ('Потапов', id))
    '''запрос данных автоматически зафиксирует изменения'''   
    print(cur.fetchall())  
        
DS4()

def DS5():
    cur.execute('DELETE FROM Telephone WHERE telephone=%s;', (8988756431))  
    print(cur.fetchone())
    conn.connection.commit()
DS5()

def DS6():
    cur.execute('DELETE FROM Telephone WHERE telephone=%s, telephone_id=%s;', (8988756431, 'Client'))          
    cur.execute('DELETE FROM Client WHERE Name=%s, Surname=%s;', ('Сидоров', 'Иван'))          
    print(cur.fetchone())
    conn.connection.commit()
DS6()



def DS7(cur, Name, Surname, telephone, email): 
    '''Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.'''         
    cur.execute("SELECT Name, Surname, email, telephone FROM Client c JOIN Email e on e.email_id = c.Client \
        JOIN Telephone t on t.telephone_id = c.Client WHERE Name=%s or Surname=%s or telephone=%s, email=%s;", (Name, Surname, telephone, email))
       
    return cur.fetchone()
    
p = DS7(cur, 'Сидоров', 'Иван', 8988756431, 'dfg.ru')
print('Client:', p)

conn.close() 
    

