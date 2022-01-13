
def circuit(algorithm, save_folder, q_num):
    if algorithm == "cryptography": from .Cryptography import Cryptography_Protocol as algorithm_class
    elif algorithm == "superdense": from .Superdense import Superdense_Protocol as algorithm_class
    elif algorithm == "teleportation": from .Teleportation import Teleportation_Protocol as algorithm_class
    
    algorithm_class(save_folder+algorithm+"/", q_num)



