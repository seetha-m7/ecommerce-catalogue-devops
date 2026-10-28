
from flask import Flask, render_template, abort
from products import products

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", products=products)


@app.route("/product/<int:product_id>")
def product_page(product_id):
    product = next(
        (p for p in products if p["id"] == product_id),
        None
    )

    if product is None:
        abort(404)

    return render_template("product_detail.html", product=product)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
