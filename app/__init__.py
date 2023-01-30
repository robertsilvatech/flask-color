import os
from flask import Flask
from flask import render_template

def create_app():
    app = Flask(__name__)
    if 'FLASK_CONFIG' in os.environ.keys():
        app.config.from_object('app.settings.' + os.environ['FLASK_CONFIG'])
    else:
        app.config.from_object('app.settings.Development')

    @app.route('/')
    @app.route('/<name>')
    def hello(name=None):
        color = os.getenv('COLOR')
        return render_template('index.html',name=name, color=color)
    
    return app

app = Flask(__name__)
