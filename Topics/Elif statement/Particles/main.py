def particle_chooser(spin, charge):
    if spin == "1/2":
        if charge == "-1/3":
            return "Strange Quark"
        elif charge == "2/3":
            return "Charm Quark"
        elif charge == "-1":
            return "Electron Lepton"
        elif charge == "0":
            return "Neutrino Lepton"
        return "Unknown particle"
    elif spin == "1":
        if charge == "0":
            return "Photon Boson"
        return "Unknown particle"
    return "Unknown particle"


spins = input()
charges = input()
particle = particle_chooser(spins, charges)
print(particle)
