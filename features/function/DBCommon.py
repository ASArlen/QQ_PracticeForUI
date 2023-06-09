"""
DB Common Operation
"""

import time
import pymssql

from features.function.Log import logger
from features.function.globalValues import globalValues

def DB_connection():
    conn = pymssql.connect(server=globalValues.DB_IP, port=globalValues.DB_PORT,
                           user=globalValues.DB_USER, password=globalValues.DB_PWD,
                           database=globalValues.DB, tds_version="7.0")  # UAT DB

    return conn

def DB_fetchall(sql):
    ##执行SQL语句
    loop = 0
    rows = ()
    while loop < 10:
        try:
            conn = DB_connection()
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            if len(rows) >=1:
                logger.info("sql: {} execute Success!RES:{}".format(sql, rows))
                break
            else:
                logger.info("sql {} Not find data, execute again,times:{}!".format(sql,loop))
                time.sleep(3)
                loop += 1
        except Exception as e:
            logger.info("Execute sql {}, error:{}".format(sql,e))
            time.sleep(3)
            loop += 1
        finally:
            cur.close()
    return rows

def DB_update(sql):
    loop = 0
    res = False
    while loop < 5:
        conn = DB_connection()
        cur = conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()
            res = True
        except Exception as e:
            logger.info("Execute sql {} error:{}".format(sql, e))
            time.sleep(3)
            loop += 1
        finally:
            cur.close()
    return res