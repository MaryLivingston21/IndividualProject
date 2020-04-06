from AnimalShelter import ANIMALSHELTER
from simulation import SIMULATION


# ----------------------------------------

def main():
    shelter = ANIMALSHELTER().get()

    sim = SIMULATION(shelter)
    sim.run()


# ----------------------------------------

main()
