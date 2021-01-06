import subprocess
import tempfile
import json
import time
from dataclasses import dataclass
from pynvim import attach, api

from typing import Tuple, List

@dataclass(eq=True, frozen=True)
class VimState:
    mode: str
    blocking: bool
    curpos: List[int]
    strings: List[str]

def get_state(nvim: api.nvim.Nvim) -> VimState:
    mode = get_mode(nvim)
    return VimState(
            mode["mode"],
            mode["blocking"],
            [] if mode["blocking"] else get_curpos(nvim),
            [] if mode["blocking"] else get_strings(nvim))

# returns: {'mode': 'n', 'blocking': False}, only this call is async
def get_mode(nvim: api.nvim.Nvim) -> str:
    return nvim.request("nvim_get_mode")

def get_strings(nvim: api.nvim.Nvim) -> List[str]:
    return list(nvim.current.buffer)

def get_curpos(nvim: api.nvim.Nvim) -> List[int]:
    s = nvim.command_output("echo getcurpos()")
    #[bufnum, lnum, col, off, curswant]
    return json.loads(s)

def is_valid(nvim: api.nvim.Nvim) -> bool:
    # cannot use .valid because it is blocking
    #return nvim.current.buffer.valid 
    return get_mode(nvim) is not None

def feedkeys(nvim: api.nvim.Nvim, s: str) -> None:
    nvim.input(s)
    #nvim.feedkeys(s)

# Not used
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
