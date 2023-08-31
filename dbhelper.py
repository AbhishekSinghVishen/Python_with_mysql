import mysql.connector as connector
import pandas as pd 
import os

class DBhelper:
    def __init__(self) -> None:
        self.con=connector.connect(host='localhost',port='3306',user='root',password='system',database='pythontest')

        query='create table if not exists user(userId int primary key,userName varchar(200),phone varchar(12))'

        cur=self.con.cursor()
        cur.execute(query)
        print("created")
    def insert_user(self,userid,username,phone):
        query="insert into user(userId,userName,phone)values('{}','{}','{}')".format(userid,username,phone)
        print(query) 
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")
        return True
    
    def fetch_all(self):
        query="select * from user"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("userId:",row[0])
            print("username:",row[1])
            print("userphone:",row[2])
            print()
            print()
    

    def delete_user(self,userid):
        query="delete from user where userId={}".format(userid)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()

    def update_user(self,userId,username,phone):
        query="update user set userName='{}',phone='{}' where userId={}".format(username,phone,userId)
        d=self.con.cursor()
        d.execute(query)
        self.con.commit()
        print("updated successfully")
    
    def extract_csv(self):
        try:
            mydb = connector.connect(host='localhost',port='3306',user='root',password='system',database='pythontest',use_pure=True)
            query = "Select * from user;"
            result_dataFrame = pd.read_sql(query,mydb)  # importing data set
            mydb.close() #close the connection
        except Exception as e:
            mydb.close()
            print(str(e))


        print(result_dataFrame.head())
        result_dataFrame.to_csv('database.csv')  # export dataframe
                

