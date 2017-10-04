
from flask import Flask, request, render_template
app = Flask(__name__)
app.debug = True

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'

# This route is a good example
@app.route('/user/<name>')
def hello_user(name):
   return '<h1>Hello {0}</h1>'.format(name)

@app.route('/form',methods= ['POST','GET'])
def enter_data():
    return render_template("age.html")

@app.route('/result',methods = ['POST', 'GET'])
def res():
    if request.method == 'GET':
        result = request.args
        birth = result.get('birthday')
        year=birth[:4]
        curr = result.get('current')
        curryear=curr[:4]
        new= 100 - (int(curryear) - int(year))
        neww=str(new)
        return render_template("result.html",result = neww)
        

if __name__ == '__main__':
    app.run()


    #done