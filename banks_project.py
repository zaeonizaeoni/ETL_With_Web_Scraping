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
    html_page = requests.get(url).text
    data = BeautifulSoup(html_page, 'html.parser')
    table = data.fin_all('tbody')
    rows = table[2].find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        if len(cols) != 0:
            t_dict = {
                'Name': cols[0].a.contents,
                'MC_USD_Billion' : cols[2].contents
            }
            df1 = pd.DataFrame(t_dict)
            df = pd.concat([table_attribute, df1], ignore_index=True)
    return df

def transform(df, csv_path):
    return df

def load_to_csv(df, output_path):
    pass

def load_to_db(df, sql_connection, table_name):
    pass

def log_process(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    timestamp = datetime.strftime(timestamp_format)
    now = datetime.now()
    with open(log_file, 'a') as f:
        print(f'{timestamp} : {message}')


def run_query(query_statement, sql_connection):
    pass