@app.route('/')
def hello():
    is_blocked = True # Или isblocked = False
    return render_template('hello.html1,is_blocked=is_blocked')
