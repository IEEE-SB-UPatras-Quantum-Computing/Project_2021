from flask import Flask, redirect, render_template, request, session
from quantum_algorithms.my_qiskit import circuit
# from quantum_algorithms.Cryptography import Cryptography_Protocol as Cryptography
# from quantum_algorithms.Superdense import Superdense_Protocol as Superdense
# from quantum_algorithms.Teleportation import Teleportation_Protocol as Teleportation

images_folder = "../react/public/static/"

# Initialize images
circuit( 'cryptography', images_folder, 3 )
circuit( 'teleportation', images_folder, 3 )
circuit( 'superdense', images_folder, 3 )


##------------------------------------------------- FLASK APP

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    # for i in request.args:
    #     print(i, request.args.get(i))
    
    circuit( request.args.get('algorithm'), images_folder, int(request.args.get('q_num')) )
    return redirect("")


if __name__ == '__main__':
    app.run(host='localhost', port=80)
    #ON CMD: flask run --host=localhost --port=80

