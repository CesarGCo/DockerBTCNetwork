import psycopg2
from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    try:
        conn = psycopg2.connect(
            database="mydb",
            user="user",
            password="pass",
            host="postgres-db"
        )
        cur = conn.cursor()
        cur.execute("SELECT MAX(last_price) FROM bitcoin_variations;")
        result = cur.fetchone()

        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta http-equiv="refresh" content="2">
            <title>Preço do Bitcoin</title>
        </head>
        <body>
            <h1>Máximo preço do Bitcoin: {result[0]}</h1>
        </body>
        </html>
        """
    except Exception as e:
        return "Conexão negada"
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug = True)



