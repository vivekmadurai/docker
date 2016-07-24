import os

from flask import Flask, request, jsonify
from flask.ext.redis import FlaskRedis

app = Flask(__name__)
app.config.update(
    REDIS_URL="redis://redis:6379/0"
)

redis_store = FlaskRedis(app)


@app.route('/')
def index():
    addr = request.remote_addr
    redis_store.incr(addr)
    visits = redis_store.get(addr)

    return jsonify({
        'ip': addr,
        'visits': visits,
    })

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)