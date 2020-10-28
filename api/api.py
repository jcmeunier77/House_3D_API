from flask import Flask, render_template, url_for, request, redirect, send_file
from io import BytesIO
from PIL import Image
from flask_restx import Resource, Api
from werkzeug.middleware.proxy_fix import ProxyFix

# from api.utils import

# Create the API
app = Flask(__name__, template_folder='../templates')
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
# api = Api(app)

# creating route for typing address
@app.route("/", methods=["POST", "GET"])
def adress_form():
   if request.method == "POST":
      street = request.form["street"]
      return redirect(url_for("street", strt=street))
   else :
      return render_template("index.html")

@app.route("/<strt>")
def street(strt):
   return f"<1>{strt}</h1>"

# creating route for showing 3d building
@app.route("/map3d")
def map3d():
   return render_template("map3d.html")