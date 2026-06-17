import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import sqlite3

url = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribute = ['Name', 'MC_USD_Billion']
csv_path = 'Largest_banks_data.csv'
db_name = 'Banks.db'
table_name = 'Largest_banks'
log_file = 'code_log.txt'


def extract(url, table_attribute):
    pass

def transform(df, csv_path):
    return df

def load_to_csv(df, output_path):
    pass

def load_to_db(df, sql_connection, table_name):
    pass

def log_process(message):
    pass

def run_query(query_statement, sql_connection):
    pass