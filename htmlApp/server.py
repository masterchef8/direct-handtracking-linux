from flask import Flask, render_template
app = Flask(__name__)

@app.route('/cross')
def cross():
	return render_template('task_cross.html');

if __name__ == '__main__':
	app.run()