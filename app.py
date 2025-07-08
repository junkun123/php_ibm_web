from flask import Flask
import ibm_db

app = Flask(__name__)

@app.route('/')
def conectar_db2():
    conn_str = (
        "DATABASE=BIBLIO;"
        "HOSTNAME=0.tcp.ngrok.io;"
        "PORT=17893;"
        "PROTOCOL=TCPIP;"
        "UID=db2inst1;"
        "PWD=juan22;"
    )

    try:
        conn = ibm_db.connect(conn_str, '', '')
        return "✅ Conexión exitosa a DB2" if conn else "❌ No se pudo conectar a DB2"
    except Exception as e:
        return f"❌ Error de conexión: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
