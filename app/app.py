import re

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    user_attrs = {}
    if request.method == 'POST':
        raw = request.form.to_dict()
    elif request.args:
        raw = request.args.to_dict()
    else:
        raw = {}
    user_attrs = {k: v for k, v in raw.items() if re.match(r'^[a-zA-Z]', k)}
    return render_template('index.html', user_attrs=user_attrs)


@app.route('/health')
def health():
    return {'status': 'healthy'}, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
