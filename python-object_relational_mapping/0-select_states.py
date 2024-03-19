#!/usr/bin/python3

''''
Select all lists from the database hbtn_0e_0usa
'''
import MySQLdb
import sys


class DataBase:
    '''
    Class representing connection to MySQL database
    '''
    def __init__(self, arg_user, arg_password, arg_database):
        self.user = arg_user
        self.password = arg_password
        self.database = arg_database
        db = MySQLdb.Connect(
                            host='localhost',
                            port=3306,
                            user=self.user,
                            password=self.password,
                            db=self.database
                            )
        self.cur = db.cursor()

    def print_all_states(self):
        self.cur.execute("SELECT * FROM states")
        all_states = self.cur.fetchall()
        for states in all_states:
            print(f"({states[0]}, '{states[1]}')")


if __name__ == "__main__":
    args = sys.argv
    arg_user = args[1]
    arg_password = args[2]
    arg_database = args[3]
    all_states = DataBase(arg_user, arg_password, arg_database)
    all_states.print_all_states()
