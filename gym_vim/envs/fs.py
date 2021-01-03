import subprocess

from typing import Tuple

def pwd() -> str:
    sh("pwd")

def sh(cmd: str) -> str:
    out, err = sh_unsafe(cmd)
    if err != None:
        raise RuntimeError(err)
    return out
    
def sh_unsafe(cmd: str) -> Tuple[str, str]:
    out = subprocess.Popen(cmd.split(" "),
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT)
    stdout, stderr = out.communicate()
    return (stdout, stderr)
