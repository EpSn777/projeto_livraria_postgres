from settings import *

import psycopg2

class ConenexaoFactory:
    def get_conexao(self):
        return psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD) 