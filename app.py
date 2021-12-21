from flask import Flask, redirect, render_template, request, session
import Main

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/", methods=["GET", "POST"])
def index():
    """ Index """
    
    if request.method == "POST": # On Submit
        for name in request.form: # to get the request.form[0]
            return redirect('/'+ name) # the route has to be the same with the button[name] from index.html

    return render_template("index.html")


##----------------------------------------------------------- ALGORITHMS' PAGES-----------------------------------------

@app.route("/quantum-cryptography")
def cryptography():
    """ Quantum Cryptography """

    return render_template("algorithms/cryptography.html")

@app.route("/superdense-coding")
def superdense():
    """ Superdense Coding """

    return render_template("algorithms/superdense.html")

@app.route("/quantum-teleportation")
def teleportation():
    """ Quantum Teleportation """

    return render_template("algorithms/teleportation.html")
