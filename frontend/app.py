from flask import Flask, render_template, session, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
import os

app = Flask(__name__)
app.secret_key = 'mi_llave_secreta_muy_segura' # Necesario para sesiones

# 20 Artículos Reales (Tecnología y Ropa)
productos = [
    {"id": 1, "nombre": "Laptop Pro 14", "precio": 1200, "imagen": "https://images.unsplash.com"},
    {"id": 2, "nombre": "Smartphone X", "precio": 800, "imagen": "https://images.unsplash.com"},
    {"id": 3, "nombre": "Audífonos Noise Cancel", "precio": 250, "imagen": "https://images.unsplash.com"},
    {"id": 4, "nombre": "Reloj Inteligente", "precio": 199, "imagen": "https://images.unsplash.com"},
    {"id": 5, "nombre": "Cámara Mirrorless", "precio": 950, "imagen": "https://images.unsplash.com"},
    {"id": 6, "nombre": "Teclado Mecánico", "precio": 120, "imagen": "https://images.unsplash.com"},
    {"id": 7, "nombre": "Monitor 4K", "precio": 400, "imagen": "https://images.unsplash.com"},
    {"id": 8, "nombre": "Mochila Tech", "precio": 85, "imagen": "https://images.unsplash.com"},
    {"id": 9, "nombre": "Chaqueta Cuero", "precio": 150, "imagen": "https://images.unsplash.com"},
    {"id": 10, "nombre": "Zapatillas Sport", "precio": 95, "imagen": "https://images.unsplash.com"},
    {"id": 11, "nombre": "Gafas de Sol", "precio": 55, "imagen": "https://images.unsplash.com"},
    {"id": 12, "nombre": "Sudadera Minimal", "precio": 45, "imagen": "https://images.unsplash.com"},
    {"id": 13, "nombre": "Altavoz Bluetooth", "precio": 70, "imagen": "https://images.unsplash.com"},
    {"id": 14, "nombre": "Tablet Air", "precio": 500, "imagen": "https://images.unsplash.com"},
    {"id": 15, "nombre": "Mouse Gamer", "precio": 65, "imagen": "https://images.unsplash.com"},
    {"id": 16, "nombre": "Camiseta Algodón", "precio": 25, "imagen": "https://images.unsplash.com"},
    {"id": 17, "nombre": "Power Bank", "precio": 40, "imagen": "https://images.unsplash.com"},
    {"id": 18, "nombre": "Dron Explorer", "precio": 350, "imagen": "https://images.unsplash.com"},
    {"id": 19, "nombre": "Jeans Slim", "precio": 60, "imagen": "https://images.unsplash.com"},
    {"id": 20, "nombre": "Gorra Urbana", "precio": 20, "imagen": "https://images.unsplash.com"},
]

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://os.environ.get("POSTGRES_USER"):os.environ.get("POSTGRES_PASSWORD")@my-db:5432/store-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = 'products'  # Nombre exacto de la tabla en Postgres
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(250))

print("Intentando conectar a la base de datos...")

@app.route('/')
def home():
    # Iniciamos el carrito en la sesión si no existe
    lista = Product.query.all()
    with app.app_context():
        inspector = inspect(db.engine)
        if inspector.has_table("products"):
            print("¡Conexión exitosa! La tabla 'products' existe.")
        else:
            print("Error: No se encontró la tabla 'products'.")
    if 'cart' not in session:
        session['cart'] = []
    return render_template('index.html', productos=productos, cart_count=len(session['cart']))

@app.route('/add/<int:product_id>')
def add_to_cart(product_id):
    # Buscamos el producto y lo añadimos a la lista de la sesión
    for p in productos:
        if p['id'] == product_id:
            session['cart'].append(p)
            session.modified = True
            break
    return redirect(url_for('home'))

@app.route('/cart')
def view_cart():
    items = session.get('cart', [])
    total = sum(item['precio'] for item in items)
    return render_template('cart.html', items=items, total=total)

@app.route('/clear')
def clear_cart():
    session['cart'] = [] # Limpiar el carrito
    return redirect(url_for('home'))

@app.route('/ready')
def ready():
    return "OK", 200

@app.route('/healthz')
def healthz():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
