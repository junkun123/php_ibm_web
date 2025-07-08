from flask import Flask
import ibm_db

app = Flask(__name__)

@app.route('/')
def index():
    # Datos de conexión - reemplaza estos si cambia el ngrok
    dsn = (
        "DATABASE=biblio;"
        "HOSTNAME=8.tcp.ngrok.io;"  # HOST de ngrok
        "PORT=17775;"               # PUERTO de ngrok
        "PROTOCOL=TCPIP;"
        "UID=db2inst1;"
        "PWD=juan22;"
    )

    try:
        conn = ibm_db.connect(dsn, "", "")
        return "<h2>✅ Conexión exitosa a IBM DB2 desde Flask</h2>"
    except Exception as e:
        return f"<h2>❌ Error al conectar: {str(e)}</h2>"

if __name__ == '__main__':
    # Escucha en todas las interfaces (requerido por Render)
    app.run(host="0.0.0.0", port=8080)
}
