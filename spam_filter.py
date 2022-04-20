import re

pattern = r"\bwww.clothingplus.fi\b|\bget software cds\b"

def filter(text):
    if re.findall(pattern, text):
        return True

    else:
        return False
