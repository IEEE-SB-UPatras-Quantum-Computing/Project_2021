from flask import Flask, redirect, render_template, request, session
from constants import ApiConstants
from quantum_algorithms.QKD import QKD_Protocol
from quantum_algorithms.Superdense import Superdense_Protocol
from quantum_algorithms.Teleportation import Teleportation_Protocol
import matplotlib
matplotlib.use('agg')

IMAGES_FOLDER = "./static"


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    # choose_algorithm( request.args.get('algorithm'), IMAGES_FOLDER, request.args.get('q_num'))
    return "Welcome to the Backend's API :)"

@app.route(ApiConstants.SUPERDENSE, methods=["GET"])
def superdense():
    Superdense_Protocol(IMAGES_FOLDER + ApiConstants.SUPERDENSE)
    return "Successfully ran Superdense!"

@app.route(ApiConstants.QKD, methods=["GET"])
def qkd():
    QKD_Protocol(IMAGES_FOLDER + ApiConstants.QKD)
    return "Successfully ran Quantum Key Distribution!"

@app.route(ApiConstants.TELEPORTATION, methods=["GET"])
def teleportation():
    Teleportation_Protocol(IMAGES_FOLDER + ApiConstants.TELEPORTATION)
    return "Successfully ran Teleport!"


app.run(host='localhost', port=80)
