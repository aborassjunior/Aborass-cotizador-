from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Aborass Cotizador</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            padding: 40px;
        }
        h1 {
            color: #111;
        }
        .box {
            background: white;
            padding: 25px;
            border-radius: 10px;
            max-width: 500px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            font-size: 16px;
        }
        button {
            background: black;
            color: white;
            padding: 12px;
            border: none;
            width: 100%;
            font-size: 16px;
            cursor: pointer;
        }
        .total {
            margin-top: 20px;
            font-size: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>💪 Aborass Cotizador</h1>

    <div class="box">
        <form method="POST">
            <label>Nombre del cliente:</label>
            <input type="text" name="cliente" required>

            <label>Precio unitario:</label>
            <input type="number" step="0.01" name="precio" required>

            <label>Cantidad:</label>
            <input type="number" name="cantidad" required>

            <button type="submit">Calcular Total</button>
        </form>

        {% if total %}
        <div class="total">
            Cliente: {{ cliente }} <br>
            Total: ${{ total }}
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        cliente = request.form["cliente"]
        precio = float(request.form["precio"])
        cantidad = int(request.form["cantidad"])
        total = round(precio * cantidad, 2)
        return render_template_string(HTML, total=total, cliente=cliente)
    return render_template_string(HTML, total=None)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
