from __init__ import app
from auth import authbp
from bksf import bksfbp

app.register_blueprint(authbp)
app.register_blueprint(bksfbp)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
