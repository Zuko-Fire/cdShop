import datetime
from ConnectedSettings import user,password,host,port,db_name

import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class PostgreS():
    def __init__(self):
        self.login = ''
        self.cursor = None
        self.conntion = None
        self.login = ''
        self.password = ''
        self.id = ''

    def connect(self):
        try:
            self.connection = psycopg2.connect(user=user,

                                      # пароль, который указали при установке PostgreSQL
                                      password=password,
                                      host=host,
                                      port=port,
                                        database=db_name)
            # Курсор для выполнения операций с базой данных
            self.cursor = self.connection.cursor()
            print('********************Соединение установлено********************')

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)



    def findData(self,findPredicate):

        findPredicate = findPredicate.lower()

        self.cursor.execute(f'SELECT * FROM public."product" WHERE lower (title) LIKE ' + f"'%{findPredicate}%'")
        self.connection.commit()
        result = []
        result = self.cursor.fetchall()
        return result




    def getData(self):
        self.cursor.execute(f'SELECT * FROM public."product"')
        self.connection.commit()
        result = []
        result = self.cursor.fetchall()
        return result




    def close(self):
        self.cursor.close()
        self.connection.close()
        print("********************Соединение с PostgreSQL закрыто********************")
    def commit(self, result, startTime, endTime):
        self.cursor.execute(f'INSERT INTO public."Results"' + f" (user_id, text_record, date_record) VALUES({self.id},'{result}','{datetime.datetime.today()}');")
        self.connection.commit()


        gametime = startTime - endTime









