from flask import Flask, session
from blueprints.play import play
import redis
from flask_session import Session
import os

# Create the application
app = Flask(__name__)

# Config
app.secret_key = os.environ['SECRET_KEY']
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_REDIS'] = redis.from_url(os.environ['REDIS_URL'])

# Redis Session
server_session = Session(app)

# Register blueprints
app.register_blueprint(play)


if __name__ == '__main__':
    app.run(debug=True)
