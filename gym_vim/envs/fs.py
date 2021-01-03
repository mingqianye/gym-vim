import subprocess
import tempfile
from pynvim import attach, api

from typing import Tuple, List

def simple(nvim: api.nvim.Nvim) -> int:
    nvim.feedkeys("iham")
    return nvim.current.buffer.api.line_count()

def get_mode(nvim: api.nvim.Nvim) -> str:
    return nvim.command_output("echo mode()")

def get_strings(nvim: api.nvim.Nvim) -> List[str]:
    return list(nvim.current.buffer)

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
