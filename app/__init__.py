import os
from flask import Flask
from flask import render_template
from flask import request

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

    @app.route('/api')
    @app.route('/api/v3')
    @app.route('/api/v4')
    @app.route('/api/v3/<action>')
    @app.route('/api/v4/<action>')
    @app.route('/api/v4/<action>/teste')
    def path(action=None):
        base_url = request.base_url
        if action:
            return render_template('path.html',base_url=base_url, action=action)
        else:
            return render_template('path.html',base_url=base_url)
        

    return app

app = Flask(__name__)
