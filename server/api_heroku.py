from flask import Flask, make_response, request, render_template
import os

app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template('index.html')


@app.route("/info")
def limit_page():
    return render_template('info.html')


# configurar lo que va dentro de PORT es súper importante
app.run(host='0.0.0.0',port=os.getenv("PORT", 5000), debug=True)

