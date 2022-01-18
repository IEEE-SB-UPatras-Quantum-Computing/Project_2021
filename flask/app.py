from flask import Flask, redirect, render_template, request, session
from quantum_algorithms.main_qiskit import choose_algorithm
# from quantum_algorithms.Cryptography import Cryptography_Protocol
# from quantum_algorithms.Superdense import Superdense_Protocol
# from quantum_algorithms.Teleportation import Teleportation_Protocol

IMAGES_FOLDER = "../react/public/static/"

# Initialize images
for q_alg in ['cryptography', 'superdense', 'teleportation']:
    choose_algorithm( q_alg, IMAGES_FOLDER )


##------------------------------------------------- FLASK APP
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    print(request.args)
    choose_algorithm( request.args.get('algorithm'), IMAGES_FOLDER )#, int(request.args.get('q_num')) )
    return redirect("")


if __name__ == '__main__':
    app.run(host='localhost', port=80)
    #ON CMD: flask run --host=localhost --port=80
