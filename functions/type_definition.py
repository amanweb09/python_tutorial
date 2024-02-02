# define type of a param
# this doesnt make it strict i.e. no error will pop in runtime if you send other datatype

def add(a: int, b: int) -> int:
    return a + b

def join_words(sentence: str) -> str:
    words = sentence.split()
    return "".join(words)

print(join_words("Hello brother how are you"))

# handling elements of the list
from typing import *

def calc_sum(l: List[int]): #yeh List typing module se aa rhi h
    return sum(l)
