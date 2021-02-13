from app import app
from flask import render_template, redirect, url_for, request
from app.post.postController import PostController


@app.route('/')
def post():
    controller = PostController()
    posts = controller.get_all()
    return render_template('post/post.html', posts = posts)

@app.route('/agregar')
def agregar():
    return render_template('post/agregar.html')

@app.route("/crear", methods=["POST"])
def crear_post():
    titulo = request.form.get("titulo")
    texto = request.form.get("texto")
    controller = PostController()
    controller.crear_post(titulo,texto)
    return redirect("/")

@app.route("/borrar", methods=["POST"])
def borrar():
    post_id = request.form.get("post_id")
    controller = PostController()
    controller.borrar(post_id)
    return redirect("/")