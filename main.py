##Integrate HTML With Flask
##HTTP verb GET and POST


##Jinja2 template engine
'''
{%...%} for statements
{{   }} expressions to print output
'''
from flask import Flask, redirect, url_for,render_template,request

app = Flask(__name__)

@app.route('/')
def welcome():
  return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score>=50:
        res='Pass'
    else:
        res='Fail'
    exp={'score':score,'res':res}
    return render_template('result.html',result=exp)

    
@app.route('/fails/<int:score>')
def fail(score):
    return "The Person has failed and the marks are " + str(score)

@app.route('/results/<int:marks>')
def results(marks):
    res = ''
    if marks < 50:
        res = 'fail'
    else:
        res = 'success'
    return redirect(url_for(res, score=marks))
### Result checker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    t=0
    if request.method=='POST':
        Science=float(request.form['Science'])
        Maths=float(request.form['Maths'])
        subject3=float(request.form['C'])
        subject4=float(request.form['datascience'])
        t=(Science+Maths+subject3+subject4)/4
    result=''
    if t >0:
        result='success'
    return redirect(url_for(result,score=t))





if __name__ == '__main__':
    app.run(debug=True)
