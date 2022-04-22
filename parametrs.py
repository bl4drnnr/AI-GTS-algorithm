def H(Epb, Ep, E):
    if Ep / Epb == 1:
        return "rule"
    return format((Epb / E) + (Ep / Epb) ** 0.5, ".3f")


def strength(Ep):
    return Ep


def accuracy(Ep, Eb):
    return format(((Ep / Ep) + Eb), ".3f")


def generality(Ep, Eb, E):
    return format(((Ep + Eb) / E), ".3f")


def specificity(Ep, Eclass):
    return format((Ep / Eclass), ".3f")


def support(Ep, E):
    return format((Ep / E), ".3f")
