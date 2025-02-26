from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Conversion functions
def toCelsius(fTemp):
    convert1 = (fTemp - 32) * (5/9)
    return convert1

def toFahrenheit(cTemp):
    convert2 = (cTemp * 9/5) + 32
    return convert2

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convertCelsius', methods=['POST'])
def convertCelsius():
    temp = float(request.form.get('Temperature'))
    conTemp = toCelsius(temp)
    return jsonify(result=f"{temp}°F is {conTemp:.2f}°C")

@app.route('/convertFahrenheit', methods=['POST'])
def convertFahrenheit():
    temp = float(request.form.get('Temperature'))
    conTemp = toFahrenheit(temp)
    return jsonify(result=f"{temp}°C is {conTemp:.2f}°F")

if __name__ == '__main__':
    app.run(debug=True)