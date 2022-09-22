from flask import Flask, render_template, request, jsonify
import redis

app = Flask(__name__)

cache=redis.Redis(host= 'redis-server', port= 6379) #get from docker-compose yaml
# cache=redis.Redis(host= '127.0.0.1', port= '6379') 

cache.set('visits', 0)

@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    value = cache.get('visits')
    cache.set('visits', int(value) + 1)
    return jsonify(f"Number of visit is = {value}")



if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host="127.0.0.1", port=8080,debug=True)