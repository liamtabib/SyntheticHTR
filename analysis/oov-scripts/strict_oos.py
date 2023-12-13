#from matplotlib import pyplot as plt
import json
import random
import numpy as np

iam_path = "/mimer/NOBACKUP/groups/naiss2023-22-1160/ds_project/SyntheticHTR/datasets/IAM_gt/gan.iam.tr_va.gt.filter27"

#writer style
ws = json.load( open( "/mimer/NOBACKUP/groups/naiss2023-22-1160/ds_project/SyntheticHTR/datasets/writers_dict_train_IAM.json" ) )

oos = dict()
voc = []

with open(iam_path, "r") as file:
    l = file.read().split("\n")


for i in range(len(l)):

    style = ws[ l[i].split(",")[0].strip() ]
    word = l[i].split()[1]

    if word not in voc:
        voc.append(word)

    if style not in oos:
        oos[style] = [word]
    else:
        if word in oos[style]:
            pass
        else:
            oos[style].append(word)

#print( oos )
# print(len(oos.keys()))
# print(len(voc))
# print(oos[338])



###############################################################################
import shlex
import subprocess

def run_shell_command(command: str, verbose: bool = False):
    """
    Execute shell command.

    Parameters
    ----------
    command : str
        Shell command to be executed

    Raises
    ------
    RuntimeError
        Shell command execution failure
    """
    if verbose:
        print(f"Executing command:\t{command}", end="\n")
    args = shlex.split(command)
    try:
        return_code = subprocess.call(args)
    except Exception as e:
        message = (
            "Failed to execute the following command:\n{command}\n"
            "The following exception was raised:\n{exception}".format(
                command=command, exception=e
            )
        )
        print(message)
        raise
    if return_code != 0:
        message = (
            "Execution of the following command:\n{command}\n"
            "Returned non-zero exit code!".format(command=command)
        )
        raise RuntimeError(message)
###############################################################################



for i in range(339):
    
    for j in range(50):

        w = random.sample(voc,1)[0]

        if w not in oos[i]:

            command = f"python3 /mimer/NOBACKUP/groups/naiss2023-22-1160/ds_project/SyntheticHTR/sampling/sampling.py --save_path /mimer/NOBACKUP/groups/naiss2023-22-1160/ds_project/SyntheticHTR/synthetic_datasets/strict-OOS/images --models_path model/OurModel_model --word {w} --style {i}"
            run_shell_command(command)

