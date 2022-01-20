from .Cryptography import Cryptography_Protocol
from .Superdense import Superdense_Protocol
from .Teleportation import Teleportation_Protocol

def choose_algorithm(algorithm, save_folder):
    if not algorithm:
        return
    elif algorithm == "cryptography":
        Cryptography_Protocol(save_folder+algorithm+"/")
    elif algorithm == "superdense":
        Superdense_Protocol(save_folder+algorithm+"/")
    elif algorithm == "teleportation":
        Teleportation_Protocol(save_folder+algorithm+"/")
