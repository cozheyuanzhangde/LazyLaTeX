import re
from ..parsers import matrix

def start(text):
    regex_matrix = r'matrix\{(.*?)\}'
    text = text.replace(r"\n", r"\newline ")
    return re.sub(regex_matrix, lambda x: matrix.parse(x.group(1)), text)