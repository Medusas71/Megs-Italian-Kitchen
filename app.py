import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/get_recipes")
def get_recipes():
    """
    Created recipe template
    """
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/full_recipe/<recipe_id>")
def full_recipe(recipe_id):
    """
    Displays full recipe including steps and ingredients
    """
    recipes = mongo.db.recipes.find({"_id": ObjectId(recipe_id)})
    print(recipes)
    return render_template("full_recipe.html", recipes=recipes)


@app.route("/")
def index():
    """ Home Page
    """
    return render_template("index.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Search recipes
    """
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Checks if registered user is in DB,
    if not add them to DB,
    if yes advise username already exists
    """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # advise username already exists
            # added category so text could change colour - see Readme credits
            flash("Username already exists", category="red")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "favourites": []
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        # added category so text could change colour - see Readme credits
        flash("Registration Successful!", category="green")
        return redirect(url_for("my_recipes", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Checks if user is registered in DB,
    if yes, user is logged in,
    if no, direct to login page
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get(
                    "password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                        "my_recipes", username=session["user"]))
            else:
                # invalid password match
                # added category so text could change
                # colour - see Readme credits
                flash("Incorrect Username and/or Password", category="red")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            # added category so text could change colour - see Readme credits
            flash("Incorrect Username and/or Password", category="red")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/my_recipes/<username>", methods=["GET", "POST"])
def my_recipes(username):
    """
    grab the session user's username from db
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"].capitalize()

    if session["user"]:
        recipes = list(mongo.db.recipes.find({"created_by": session["user"]}))
        return render_template(
            "my_recipes.html", username=username, recipes=recipes)


@app.route("/logout")
def logout():
    """
    remove user from session cookies
    """
    flash("You have been logged out", category="green")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """
    add recipe to db
    """
    if request.method == "POST":
        recipe = {
            "category": request.form.get("category"),
            "recipe_name": request.form.get("recipe_name").capitalize(),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "servings": request.form.get("servings"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "recipe_image": request.form.get("recipe_image"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added", category="green")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category", 1)
    return render_template("add_recipe.html", categories=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    allows user to edit a recipe in the db
    """
    if request.method == "POST":
        submit = {'$set': {
            "category": request.form.get("category"),
            "recipe_name": request.form.get("recipe_name"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "servings": request.form.get("servings"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "recipe_image": request.form.get("recipe_image"),
            "created_by": session["user"]
        }}
        mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated", category="green")
        return redirect(url_for("get_recipes"))

    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category", 1)
    return render_template(
        "edit_recipe.html", recipe=recipes, categories=categories)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """
    allows user to delete a recipe in the db
    """
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted", category="green")
    return redirect(url_for("get_recipes", recipe_id=recipe_id))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
