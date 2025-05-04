from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Ganti dengan API key milikmu
API_KEY = "13e6d7c303786efcc75ccb09"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            amount = float(request.form["amount"])
            from_cur = request.form["from_currency"].upper()
            to_cur = request.form["to_currency"].upper()

            # Panggil API ExchangeRate
            url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{from_cur}/{to_cur}/{amount}"
            response = requests.get(url)
            data = response.json()

            # Cek apakah sukses
            if data["result"] == "success":
                converted = data["conversion_result"]
                result = f"{from_cur} {amount:,.2f} = {to_cur} {converted:,.2f}"
            else:
                result = "Gagal mengambil data dari API."
        except Exception as e:
            result = f"Terjadi kesalahan: {e}"

    return render_template("tampilan.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
