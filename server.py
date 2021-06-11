from flask import Flask, render_template, redirect, session
app=Flask(__name__)

app.secret_key='tHis iS mY seCrEt kEY'


@app.route('/')
def index():
    if 'visit_count' not in session:
        session['visit_count']=0
    session['visit_count']+=1
    return render_template('index.html', count=session['visit_count'])


@app.route('/delete_session')
def delete_session():
    session.clear()
    return redirect('/')


@app.route('/two_visits')
def two_visits():
    session['visit_count']+=1
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)