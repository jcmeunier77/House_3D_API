from flask import Flask, render_template, url_for, request, redirect, send_file
from io import BytesIO
from PIL import Image
from flask_restx import Resource, Api
from api.src.utils.a_addres_to_crs import AddressToCrs


import folium
from werkzeug.middleware.proxy_fix import ProxyFix
from api.src import Construct3D

# from api.utils import

# Create the API
app = Flask(__name__, template_folder='../templates')
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
# api = Api(app)

# creating route for typing address
@app.route("/", methods=["GET"])
def adress_form():
    return 'lapin'

#     pass
#    if request.method == "POST":
#       street = request.form["street"]
#       return redirect(url_for("street", strt=street))
#    else :
#       return render_template("index.html")

@app.route("/3d/<street>/<city>/<en3D>")
def view_3d(street, city, en3D):
    if en3D == "submit":
        return Construct3D(street, city).constructor()
        # return {
        #         street: 'True',
        #         city: 'The v2 API server is alive.',
        #         en3D:'connerie'
        #     }, 200

@app.route("/map/<street1>/<city1>/<enMap>")
def view_map(street1, city1, enMap):
    if enMap == "encode":
        Construct3D(street1, city1).map()
        return render_template('map.html')
        # print(TargetToMap(51.319986, 5.077554).to_map())
        #
        # targetLL = AddressToCrs(street1, city1).to_long_latt()
        # mappy = folium.Map(location=[targetLL[0], targetLL[1]], zoom_start=17)
        # folium.CircleMarker(location=[targetLL[0], targetLL[1]], radius=30, popup='Your address', color='#3186cc',
        #                     fill=True, fill_color='#3186cc').add_to(mappy)
        # mappy.save('map.html')
        # return render_template()


        #Construct3D(street1, city1).map()
        #return render_template("map.html")

    #print ({street:"rue", city:"rrr"})
    # print(street, city, en3D)
    # if en3D.value == 'submit':
    #return Construct3D(street, city).constructor()
         # return {
         #         street1: 'True',
         #         city1: 'The v2 API server is alive.',
         #         enMap:'connerie'
         #     }, 200


# creating route for showing 3d building
# @app.route("/map3d")
# def map3d():
#    return render_template("map3d.html")