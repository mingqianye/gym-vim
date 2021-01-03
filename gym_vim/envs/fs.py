import subprocess
import tempfile
import headlessvim

from typing import Tuple, List

def tt():
    out = ""
    with headlessvim.open(args="-N -i NONE -n -u NONE") as vim:
        vim.send_keys("iham")
        out = vim.echo('"blah"')
        vim.close()
    return out

def sh(cmd: str) -> List[str]:
    out, err = sh_unsafe(cmd)
    if err != None:
        raise RuntimeError(err)
    return out.decode("utf-8").strip().split("\n")
    
def sh_unsafe(cmd: str) -> Tuple[str, str]:
    out = subprocess.Popen(cmd.split(" "),
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT)
    stdout, stderr = out.communicate()
    return (stdout, stderr)
