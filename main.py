from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>💪 Aborass Cotizador</h1>
    <p>Sistema activo correctamente.</p>
    <p>Tu aplicación está funcionando en Render 🚀</p>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
