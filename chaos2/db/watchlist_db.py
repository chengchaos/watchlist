# -*- coding:utf-8 -*-
import mysql.connector

conn = mysql.connector.connect(
    host="47.114.98.28",
    user="chengchao",
    password="Mima@2016:abcd",
    database="demo_01",
)


def get_watch_list(page):
    dbcursor = conn.cursor()
    limit = 10
    offset = (page - 1) * limit
    str_sql = "select id, title, `year` from watch_list order by id desc limit %s offset %s "
    data_var = (limit, offset)
    dbcursor.execute(str_sql, data_var)
    db_result = dbcursor.fetchall()

    data_res = []
    print(db_result)
    for dr in db_result:
        inst = {
            "title": dr[1],
            "year": dr[2],
        }
        data_res.append(inst)

    return data_res
