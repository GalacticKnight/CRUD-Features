from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
from friend import Friend

@app.route('/')
def index():
    friends = Friend.get_all()
    return render_template("index.html", all_friends = friends)

@app.route('/friends/new')
def new():
    return render_template("create_friend.html")

@app.route('/friend/create', methods=['POST'])
def create():
    Friend.save(request.form)
    return redirect('/')

@app.route('/friend/show/<int:friend_id>')
def show(friend_id):
    friend=Friend.get_one(friend_id)
    return render_template("show_friend.html",friend=friend)

@app.route('/friend/edit/<int:friend_id>')
def edit(friend_id):
    friend=Friend.get_one(friend_id)
    return render_template("update_friend.html",friend=friend)

@app.route('/friend/update', methods=['POST'])
def update():
    Friend.update(request.form)
    return redirect('/')

@app.route('/friend/delete/<int:friend_id>')
def delete(friend_id):
    Friend.delete(friend_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)