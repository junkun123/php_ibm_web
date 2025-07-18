from flask import Flask
import ibm_db

app = Flask(__name__)

@app.route('/')
def conectar_db2():
    # Usa tu túnel activo de ngrok
    conn_str = (
        "DATABASE=BIBLIO;"
        "HOSTNAME=0.tcp.ngrok.io;"
        "PORT=11721;"
        "PROTOCOL=TCPIP;"
        "UID=db2inst1;"
        "PWD=juan22;"
    )
    try:
        conn = ibm_db.connect(conn_str, '', '')
        if conn:
            return "✅ Conexión exitosa a DB2 desde Render usando ngrok"
        else:
            return "❌ No se pudo conectar a DB2"
    except Exception as e:
        return f"❌ Error de conexión: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
