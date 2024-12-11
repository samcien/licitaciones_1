import mysql.connector

def connect():
    return mysql.connector.connect(
        host="junction.proxy.rlwy.net",
        user="root",
        password="LbvDgiSovKycsLRnCylcpsruUzptMfeo",
        database="railway",
        port=29230
    )
