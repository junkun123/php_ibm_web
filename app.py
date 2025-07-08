from flask import Flask, render_template_string
import ibm_db

app = Flask(__name__)

# Configuración conexión DB2
db_config = {
    'database': 'biblio',
    'hostname': '8.tcp.ngrok.io',  # Cambia aquí por tu host ngrok actual
    'port': '17190',               # Cambia aquí por tu puerto ngrok actual
    'user': 'db2inst1',
    'password': 'juan22'
}

conn_str = (
    f"DATABASE={db_config['database']};"
    f"HOSTNAME={db_config['hostname']};"
    f"PORT={db_config['port']};"
    "PROTOCOL=TCPIP;"
    f"UID={db_config['user']};"
    f"PWD={db_config['password']};"
)

@app.route('/')
def index():
    try:
        conn = ibm_db.connect(conn_str, '', '')
        if conn:
            msg = "✅ Conexión a DB2 exitosa."
            ibm_db.close(conn)
        else:
            msg = "❌ No se pudo conectar a DB2."
    except Exception as e:
        msg = f"❌ Error de conexión: {str(e)}"

    html = f"""
    <html>
        <head><title>Flask DB2 App</title></head>
        <body>
            <h1>Estado de conexión a DB2</h1>
            <p>{msg}</p>
        </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
