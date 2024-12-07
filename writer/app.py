import requests
import time
import psycopg2
from psycopg2 import OperationalError

while True:
    try:
        conn = psycopg2.connect(database="mydb", 
                                user="user", 
                                host="postgres-db", 
                                password="pass")
        cur = conn.cursor()
        
        cur.execute("""CREATE TABLE IF NOT EXISTS bitcoin_variations(
                    last_price FLOAT,
                    volume FLOAT)
                    """)
        
        while True:
            try:
                data = requests.get('http://cointradermonitor.com/api/pbb/v1/ticker').json()
                cur.execute(
                    "INSERT INTO bitcoin_variations (last_price, volume) VALUES (%s, %s)",
                    (data['last'], data['volume24h']))
                conn.commit()
                time.sleep(1)
            except requests.RequestException as e:
                print(f"Erro ao obter dados da API: {e}")
                time.sleep(5)
            
    except OperationalError as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        time.sleep(5) 
    finally:
        if 'cur' in locals() and cur:
            cur.close()
        if 'conn' in locals() and conn:
            conn.close()
