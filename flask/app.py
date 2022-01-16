from flask import Flask, redirect, render_template, request, session
from quantum_algorithms.main_qiskit import choose_algorithm
# from quantum_algorithms.Cryptography import Cryptography_Protocol
# from quantum_algorithms.Superdense import Superdense_Protocol
# from quantum_algorithms.Teleportation import Teleportation_Protocol

IMAGES_FOLDER = "../react/public/static/"

# Initialize images
print("------------------------------------------------------- MYRON")
choose_algorithm( 'cryptography', IMAGES_FOLDER, 3 )
print("------------------------------------------------------- VASILIS")
choose_algorithm( 'superdense', IMAGES_FOLDER, 3 )
print("------------------------------------------------------- IOANNA")
choose_algorithm( 'teleportation', IMAGES_FOLDER, 3 )


##------------------------------------------------- FLASK APP
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    # for i in request.args:
    #     print(i, request.args.get(i))
    
    choose_algorithm( request.args.get('algorithm'), IMAGES_FOLDER, int(request.args.get('q_num')) )
    return redirect("")


if __name__ == '__main__':
    app.run(host='localhost', port=80)
    #ON CMD: flask run --host=localhost --port=80
