import Cryptography, Superdense, Teleportation


def choose():
    circuit = input("Choose algorithm: ")

    if circuit == 0:
        Cryptography.Cryptography_Protocol()

    elif circuit == 1:
        Superdense.Superdense_Protocol()

    elif circuit == 2:
        Teleportation.Teleportation_Protocol()

