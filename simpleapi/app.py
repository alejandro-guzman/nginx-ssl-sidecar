from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
  return jsonify({'message': 'Hello, World!'})

def main():
  app.run(host='0.0.0.0')

if __name__ == '__main__':
  main()