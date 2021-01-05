from typing import List

def all_chars() -> List[str]:
    lower_letters = "qwertyuiopasdfghjklzxcvbnm"
    upper_letters = lower_letters.upper()
    nums = "1234567890"
    symbs = '~!@#$%^&*()_+' + '[]\;,./' + "'" + '{}|:"<>?'
    space = " "
    enter = "\n"
    return list(space + lower_letters + upper_letters + nums + symbs)

esc: str = "\x1b"

displayable_chars: List[str] = all_chars() + [""]

keystrokes: List[str] = all_chars() + [esc, ""]

modes: List[str] = ["n", "no", "nov", "noV", "noCTRL-V", "niI", "niR", "niV", "v", "V", "CTRL-V", "s", "S", "CTRL-S", "i", "ic", "ix", "R", "Rc", "Rv", "Rx", "c", "cv", "ce", "r", "rm", "r?", "!", "t"]
