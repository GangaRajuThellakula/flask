from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/success/<int:score>')
def success(score):
    return "The Person has passed and the marks are " + str(score)

@app.route('/fails/<int:score>')
def fail(score):
    return "The Person has failed and the marks are " + str(score)

@app.route('/results/<int:marks>')
def results(marks):
    res=''
    if marks < 40:
        res='fail'
    else:
        res='success'
    return redirect(url_for(res, score=marks))


if __name__ == '__main__':
    app.run(debug=True)
