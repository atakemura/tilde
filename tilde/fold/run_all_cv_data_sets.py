import sys

import os

save_stdout = sys.stdout

# --------------------------------
# print("start mutab0")
# sys.stdout = open(os.devnull, "w")
# import tilde.fold.mutab0
# sys.stdout = save_stdout
# print("finished mutab0")
# print("---------------------------------------------------------------------------------------------------------------")
# --------------------------------
print("start mutaace1")
sys.stdout = open(os.devnull, "w")
import tilde.fold.mutaace1
sys.stdout = save_stdout
print("finished muataace1")
print("---------------------------------------------------------------------------------------------------------------")
# --------------------------------
print("start canc")
sys.stdout = open(os.devnull, "w")
import tilde.fold.canc
sys.stdout = save_stdout
print("finished canc")
print("---------------------------------------------------------------------------------------------------------------")
# -------------------------
print("start financial")
sys.stdout = open(os.devnull, "w")
import tilde.fold.financial
sys.stdout = save_stdout
print("finished financial")
print("---------------------------------------------------------------------------------------------------------------")
# -------------------------
print("start bongard4")
sys.stdout = open(os.devnull, "w")
import tilde.fold.bongard4
sys.stdout = save_stdout
print("finished bongard4")
print("---------------------------------------------------------------------------------------------------------------")
# -------------------------