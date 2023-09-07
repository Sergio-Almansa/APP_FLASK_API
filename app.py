# EXTENSIONES VSCODE INSTALADAS 
# Bootstrap 4, Font awesome 4, Font Awesome 5 Free & Pro snippets
# flask-snippets

#----------#

# CREAMOS ENTORNO VIRTUAL #

# virtualvenv venv  // Donde venv es el nombre que le hemos dado al entorno virtual

# ACTIVAMOS ENTORNO VIRTUAL #

# venv\Scripts\activate

#----------#

# LIBRERIAS INSTALADAS, con "pip list" podemos ver las dependencias instaladas en el entorno del proyecto #

# pip install flask
# pip install jinja2
# pip install requests


from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder= "template")


@app.route('/')
def index():
    
    datosObtenidos = requests.get('https://api.dailymotion.com/videos?channel=news&limit=12&language=es')
    datosFormatoJSON = datosObtenidos.json()
    print(datosFormatoJSON)

    return render_template('index.html', datos=datosFormatoJSON['list']) # Con la variable datos le pasamos los resultados al template

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
