import sqlite3
import hashlib
from datetime import datetime

def con():
    conn = sqlite3.connect('dtb.db')
    return conn

def create_table_user():
    conn = con()
    cur = conn.cursor()
    cur.execute("""
        create table if not exists user(
            `id` integer not null primary key autoincrement,
            `first_name` varchar(30),
            `last_name` varchar(30),
            `email` varchar(50),
            `username` varchar(50),
            `password` varchar(150),
            `is_active` boolean default false,
            `registered_datetime` datetime
        )
    """)
    conn.commit()
    conn.close()


def insert_user(data: dict):
    conn = con()
    cur = conn.cursor()
    sha256 = hashlib.sha256()
    sha256.update(data['password1'].encode('utf-8'))
    hashed_password = sha256.hexdigest()
    query = """
        insert into user(
            `first_name`,
            `last_name`,
            `email`,
            `username`,
            `password`,
            `registered_datetime`
        ) values (?, ?, ?, ?, ?, ?)
    """
    values = (data['first_name'], data['last_name'], data['email'], data['username'], hashed_password, datetime.now())
    if data['password1'] == data['password2']:
        if is_exist('username', data['username']):
            print('This username is already exists!!!')
            return 405
        if is_exist('email', data['email']):
            print('This email is already exists!!!')
            return 405
        cur.execute(query, values)
        conn.commit()
        conn.close()
        return 201
    else:
        print('Passwords are not same!!!')
        return 405


def is_exist(field, field_data):
    query = f"""
        select count(id) from user where {field}=?
    """
    value = (field_data,)
    conn = con()
    cur = conn.cursor()
    cur.execute(query, value)
    return cur.fetchone()[0]
