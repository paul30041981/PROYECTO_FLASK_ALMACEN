from app import app
from flask import render_template, redirect, url_for, request, flash, get_flashed_messages
from sqlalchemy.sql.expression import not_, or_
from flask_login import login_required
#import proyecto
# from productsBD import PRODUCTS
from app.producto.productoModel import Product, ProductForm
from app.category.categoryModel import Category
from app import db
# from werkzeug import abort 

# @app.before_request
# @login_required
# def constructor():
#    pass

@app.route('/productos')
@app.route('/product/<int:page>')
@login_required
def productos(page=1):
    return render_template('producto/productos.html', productos = Product.query.paginate(page,5))

@app.route('/producto_delete/<int:id>')
@login_required
def producto_delete(id):
    prod = Product.query.get_or_404(id)#devuelve un objeto
    db.session.delete(prod)
    db.session.commit()
    flash("Producto Eliminado con Exito")
    return redirect(url_for('productos'))

@app.route('/producto_create', methods=('GET', 'POST'))
@login_required
def producto_create():
    
    form = ProductForm(meta={'csrf':False})
    categories = [ (c.id, c.name) for c in Category.query.all() ]
    form.category_id.choices = categories

    if form.validate_on_submit():
        p = Product(request.form['name'], request.form['price'], request.form['category_id'])
        db.session.add(p)
        db.session.commit()
        flash("Producto Creado con Exito")
        return redirect(url_for('producto_create'))
    
    if form.errors:
        flash(form.errors, 'danger')

    return render_template('producto/producto_create.html', form=form)

@app.route('/producto_update/<int:id>', methods=('GET', 'POST'))
@login_required
def producto_update(id):
    prod = Product.query.get_or_404(id)
    form = ProductForm(meta={'csrf':False})

    categories = [ (c.id, c.name) for c in Category.query.all() ]
    form.category_id.choices = categories

    if request.method == "GET":
        form.name.data = prod.name
        form.price.data = prod.price
        form.category_id.data = prod.category_id

    if form.validate_on_submit():
        prod.name = form.name.data
        prod.price = form.price.data
        prod.category_id = form.category_id.data
        db.session.add(prod)
        db.session.commit()
        flash("Producto Actualizado con Exito")
        return redirect(url_for('producto_update', id = prod.id ))
    
    if form.errors:
        flash(form.errors, 'danger')
   
    return render_template('producto/producto_edit.html',prod = prod ,form=form)


@app.route('/detalle/<int:id>')
@login_required
def detalle(id):
    prod = Product.query.get(id)
    prod = Product.query.get_or_404(id)
    return render_template("producto/detalle.html", prod = prod)


# @app.route('/producto_insert', methods=["POST"])
# def producto_insert():
#     p = Product(request.form['name'], request.form['price'])
#     db.session.add(p)
#     db.session.commit()
#     flash("Producto Creado con Exito")
#     return redirect(url_for('producto_create'))

# @app.route('/producto_edit/<int:id>')
# def producto_edit(id):
#     # print(get_flashed_messages())
#     prod = Product.query.get_or_404(id)
#     return render_template('producto/producto_edit.html', prod = prod)

# @app.route('/test')
# def test():
#     # prod = Product.query.limit(2).all()
#     # print(prod)
#     # prod = Product.query.limit(2).first()
#     # print(prod)
#     # prod = Product.query.order_by(Product.id).limit(2).all()
#     # print(prod)
#     # prod = Product.query.order_by(Product.id.desc()).limit(2).all()
#     # print(prod)
#     # prod = Product.query.get({"id":1})
#     # print(prod)
#     # prod = Product.query.filter_by(name="producto 1").all()#devuelve una coleccion de un objeto
#     # print(prod)
#     # prod = Product.query.filter_by(name="producto 1", id=1).first()#devuelve un objeto
#     # print(prod)
#     # prod = Product.query.filter_by(name="producto 1").first()#devuelve un objeto
#     # print(prod)
#     # prod = Product.query.filter(Product.id > 1 ).all()#devuelve un objeto, para operadores < y > se debe de usar filter y no filter_by
#     # print(prod)
#     # prod = Product.query.filter(Product.id > 1 ).all()#devuelve un objeto, para operadores < y > se debe de usar filter y no filter_by
#     # print(prod)
#     # prod = Product.query.filter(Product.name.like('prod%') ).all()#devuelve un objeto, para operadores < y > se debe de usar filter y no filter_by
#     # print(prod)
#     # prod = Product.query.filter(not_(Product.id > 1 )).all()#devuelve un objeto, para operadores < y > se debe de usar filter y no filter_by
#     # print(prod)
#     # prod = Product.query.filter(or_(Product.id > 1, Product.name=="producto 2")).all()
#     # print(prod)

#     # #Agregar
#     # p = Product("Iphone", 50.5)
#     # db.session.add(p)
#     # db.session.commit()

#     # #Actualizar
#     # prod = Product.query.filter_by(name="producto 1").first()#devuelve un objeto
#     # prod.name = "UP1"
#     # db.session.add(prod)
#     # db.session.commit()

#     # #Eliminar
#     prod = Product.query.filter_by(name="UP1").first()#devuelve un objeto
#     db.session.delete(prod)
#     db.session.commit()

# @app.route('/productos')
# def productos():
#     # print(PRODUCTS.items())
#     # print(PRODUCTS.get(1))
#     print(Product.query.all())
#     # return render_template('producto/productos.html', productos = PRODUCTS)
#     return render_template('producto/productos.html', productos = Product.query.all())

#     return "Flask"