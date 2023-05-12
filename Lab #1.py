from flask import Flask

app = Flask(__name__)


@app.route("/")
def page_index():
    return "Hello world"
    
@app.route('/page_profile/<id646905133>')
def page_profile(id646905133):
    return f'<h1>Профиль пользователя{uid}</h1>'

@app.route("/feed/")
def page_feed():
      return "Лента пользователя"

@app.route("/messages/")
def page_messages():
    return "Сообщения пользователя"

@app.route('/user/<id646905133>')
def profile(uid):
    return f'<h1>Профиль{uid}<h1>'

@app.route('/catalog/items/<itemid>')
def profile(itemind):
        return f'<h1>Страничка  товара {itemind}<h1>'

@app.route("/users/<uid>")
def profile(uid):
    print(uid)
    print(type(uid))
    return""      

app.route("/error/")
def page_error():
    return "Ошибка"
    
app.run()