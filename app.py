from flask import Flask
import ibm_db

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Cambia aquí el HOSTNAME y PORT según tu túnel ngrok activo
        conn_str = (
            "DATABASE=biblio;"
            "HOSTNAME=2.tcp.ngrok.io;"
            "PORT=12587;"
            "PROTOCOL=TCPIP;"
            "UID=db2inst1;"
            "PWD=juan22;"
        )

        conn = ibm_db.connect(conn_str, "", "")
        if conn:
            ibm_db.close(conn)
            return "<h2 style='color: green;'>✅ Conexión a DB2 exitosa</h2>"
        else:
            return "<h2 style='color: red;'>❌ No se pudo conectar a DB2</h2>"
    except Exception as e:
        return f"<h2 style='color: red;'>❌ Error de conexión: {e}</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
