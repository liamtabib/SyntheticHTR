import json
import shlex
import subprocess

wd = json.load( open( "/mimer/NOBACKUP/groups/naiss2023-22-1160/ds_project/SyntheticHTR/word_dict.json" ) )

from string import punctuation as punc
oov = []
for e in wd.keys():
    if wd[e] == 0:
        if (e not in oov) and not any(p in e for p in punc):
            oov.append(e)

l = []

for i in range(len(oov)):
    if len(oov[i]) == 5:
        l.append(oov[i])


###############################################################################
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

c = 0
for word in l:
    
    command = f"python /mimer/NOBACKUP/groups/naiss2023-22-1160/ds_project/SyntheticHTR/sampling/sampling.py --save_path /mimer/NOBACKUP/groups/naiss2023-22-1160/ds_project/SyntheticHTR/synthetic_datasets/oov-IAM_5 --models_path model/OurModel_model --words {word}"
    run_shell_command(command)
    print(c)
    c += 1

print("finished all")
