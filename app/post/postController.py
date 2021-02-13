from app.post.postModel import Post
from app import db


class PostController:
    def get_all(self):
        # post = Post.query.all()
        posts = Post.query.order_by(Post.fecha.desc()).all()
        return posts

    def crear_post(self, titulo, texto):
      post = Post(titulo=titulo, texto=texto)
      db.session.add(post)
      db.session.commit()
      return True

    def borrar(self, post_id):
        post = db.session.query(Post).filter(Post.id==post_id).first()
        db.session.delete(post)
        db.session.commit()
        return True