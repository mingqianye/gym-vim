from typing import List

def all_chars() -> List[str]:
    lower_letters = "qwertyuiopasdfghjklzxcvbnm"
    upper_letters = lower_letters.upper()
    nums = "1234567890"
    symbs = '~!@#$%^&*()_+' + '[]\;,./' + "'" + '{}|:"<>?'
    return list(lower_letters + upper_letters + nums + symbs)

enter: str = "\n"
esc: str = "\x1b"

keystrokes: List[str] = all_chars() + [enter, esc]
