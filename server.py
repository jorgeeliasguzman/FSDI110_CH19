from flask import Flask, abort, request, render_template
import json
from data import data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#dictionary
me = {
    "name" : "Jorge",
    "last" : "Guzman",
    "email" : "jorgeeliasguzman@gmail.com",
}

#list
products = data


@app.route("/")
@app.route("/home")
def index():
    return "Hello from Flask"


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/about/name")
def name():
    return me["name"]


@app.route("/about/fullname")
def full_name():
    return me["name"] + " " + ["last"]


@app.route("/api/catalog")
def get_catalog():
    return json.dumps(products)

@app.route("/api/catalog", methods=['POST'])
def save_product():
    prod = request.get_json()
    products.append(prod)
    return json.dumps(prod)

    

# get product by ID
@app.route("/api/catalog/id/<id>")
def get_product_by_id(id):
    for prod in products:
        if(prod["_id"].lower() == id):
            return json.dumps(prod)
    
    abort(404)
# get the cheapest product
# /api/catalog/cheapest

@app.route("/api/catalog/cheapest")
def get_cheapest():
    cheapest = products[0]
    for prod in products:
        if(prod["price"] < cheapest["price"]):
                cheapest = prod
    
    return json.dumps(cheapest)





@app.route("/api/catalog/<category>")
def get_product_by_category(category):
    # find the products that belong to the category
    results = []
    for prod in products:
        if (prod["category"].lower() == category.lower):
            results.append(prod)

    return json.dumps(results)


# HERE
@app.route("/api/categories")
def get_categories():
    unique_categories = []
    # do the magic

    return json.dumps(unique_categories)




@app.route("/api/test")
def test():

    # add
    products.append("strawberry")
    products.append("dragon fruit")

    # length
    print(f"You have: {len(products)} products in your catalog" )

    #iterate
    for fruit in products:
        print(fruit)
    
    products.remove("apple")
    print(products)





    return "check your terminal"


#if __name__ == '__main__':
#    app.run(debug=True)



#adding cool code that might fix everything... or not
# another change

# command line:
"""
git add .
git commit -m "<a message>"
git push
"""
