import matplotlib.pyplot as plt
import pandas as pd 


def d_RBM(position,bundle = True):
    """
    Calculates the nanotubes diameter from the RBM Raman position. 
    Source: M.S. Dresselhaus et al. / Physics Reports 409 (2005) 47 – 99
    """
    A = 248
    B = 10 if bundle else 0
    return A / (position - B)

def RBM_d(d,bundle = True):
    """
    Calculates the nanotubes RBM Raman position from the diameter. Inverse function of d_RBM 
    Source: M.S. Dresselhaus et al. / Physics Reports 409 (2005) 47 – 99
    """
    A = 248
    B = 10 if bundle else 0
    return A /d + B

def d_G(position):
    """
    Calculates the nanotubes diameter from G- Raman position. 
    Source: M.S. Dresselhaus et al. / Physics Reports 409 (2005) 47 – 99
    """
    A = -45.7
    B = 1591
    n = 2 
    return (A / (position - B))**(1/n)



def P_collapse(diameter,alpha = 1):
    """
    Determine collapse pressure from diameter (in nm). alpha = 1 for the collapse start and 1.5 end.
    Source: A.C. Torres-Dias et al. / Carbon 123 (2017) 145e150
    """
    D = 1.7 * 1.602e-19
    beta = 0.51
    conversion = 1e18 #conversion Pa/nm**3 GPa/m

    return 24 * alpha * D * (1 - beta ** 2 / diameter ** 2) / diameter ** 3 * conversion
