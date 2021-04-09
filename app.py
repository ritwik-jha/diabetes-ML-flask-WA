from flask import Flask
from flask import render_template
from tensorflow.keras.models import load_model
from flask import request
import subprocess



app = Flask('diabetes_app', template_folder='/code/templates')
model = load_model('/code/webapp.h5', compile = False)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/model', methods=['GET'])
def modelrun():
    preg = request.args.get('preg')
    glu = request.args.get('glu')
    bp = request.args.get('bp')
    thickness = request.args.get('thickness')
    insulin = request.args.get('insulin')
    bmi = request.args.get('bmi')
    dpf = request.args.get('dpf')
    age = request.args.get('age')
    output = model.predict([preg , glu , bp , thickness , insulin , bmi , dpf , age])
    if output > 0.5:
        return YES
    else:
        return NO

ip = subprocess.getoutput("hostname -I | awk '{print $1}'")
app.run(host = ip , port = 80)
