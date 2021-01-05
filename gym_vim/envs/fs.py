import subprocess
import tempfile
import json
from dataclasses import dataclass
from pynvim import attach, api

from typing import Tuple, List

@dataclass(eq=True, frozen=True)
class VimState:
    mode: str
    curpos: List[int]
    strings: List[str]

def get_state(nvim: api.nvim.Nvim) -> VimState:
    return VimState(
            get_mode(nvim),
            get_curpos(nvim),
            get_strings(nvim))

def get_mode(nvim: api.nvim.Nvim) -> str:
    return nvim.command_output("echo mode()")

def get_strings(nvim: api.nvim.Nvim) -> List[str]:
    return list(nvim.current.buffer)

def get_curpos(nvim: api.nvim.Nvim) -> List[int]:
    s = nvim.command_output("echo getcurpos()")
    #[bufnum, lnum, col, off, curswant]
    return json.loads(s)

def is_valid(nvim: api.nvim.Nvim) -> bool:
    return nvim.current.buffer.valid

def feedkeys(nvim: api.nvim.Nvim, s: str) -> None:
    nvim.feedkeys(s)



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
