import re

def is_abba(chars: str) -> bool:
    return (len(chars) == 4) and (chars[0] != chars[1]) and (chars == chars[::-1])

def is_aba(chars: str) -> bool:
    return (len(chars) == 3) and (chars[0] != chars[1]) and (chars[0] == chars[2])

def is_bab(chars: str, aba: str) -> bool:
    return (len(chars) == 3) and (chars[0] == aba[1]) and (chars[1] == aba[0]) and (chars[0] == chars[2])

def iter_hypernet(chars: str):
    """hypernet sequences, which are contained by square brackets"""
    pattern = r"\[\w*\]" # capture substrings inside square brackets
    return (m.group().lstrip('[').rstrip(']') for m in re.finditer(pattern, chars))

def iter_supernet(chars: str):
    """supernet sequences (outside any square bracketed sections)"""
    pattern = r"(^\w*\[)|(\]\w*\[)|(\]\w*$)" # capture substrings outside square brackets
    return (m.group().lstrip(']').rstrip('[') for m in re.finditer(pattern, chars))

def iter_aba(chars: str):
    for supernet in iter_supernet(chars):
        for i in range(len(supernet)-2):
            candidate = supernet[i:i+3]
            if not is_aba(candidate): continue
            yield candidate

def iter_bab_candidates(chars: str):
    for hypernet in iter_hypernet(chars):
        for i in range(len(hypernet)-2):
            candidate = hypernet[i:i+3]
            yield candidate

def has_abba_substr(chars: str) -> bool:
    return any(is_abba(chars[i:i+4]) for i in range(len(chars)-3))

def supports_tls(chars: str) -> bool:
    return (
        any(map(has_abba_substr, iter_supernet(chars)))
    ) and not (
        any(map(has_abba_substr, iter_hypernet(chars)))
    )

def supports_ssl(chars: str) -> bool:
    for aba in iter_aba(chars):
        if any(is_bab(bab, aba) for bab in iter_bab_candidates(chars)):
            return True
    return False


with open("input.txt", 'r') as file:
    data = file.read().strip().split()


print(sum(map(supports_tls, data))) # PART 1: 105
print(sum(map(supports_ssl, data))) # PART 2: 258
