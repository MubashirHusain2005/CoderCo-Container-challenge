import os
from flask import Flask
import redis

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.environ.get("REDIS_PORT", "6379"))
r = redis.Redis(host=redis_host, port=redis_port)

@app.route('/')
def hello():
    return "Hello, Welcome to the Coderco Containers Challenge"

@app.route('/count')
def count():
    count = r.incr('visitor_count')
    return f'This is visit count: {count}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)
