@app.route("/")
def hello(name):
    user_data = {
        "name":"Ivan",
        "phone":"+7 123 456 78 90",
        "email":"ivan_dev@gmail.com",
        "telegram":"ivan_dev",
    }
    return render_template('hello.html',user=user_data)