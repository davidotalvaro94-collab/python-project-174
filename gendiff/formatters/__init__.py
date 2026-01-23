from gendiff.formatters.stylish import *
from gendiff.formatters.plain import *


def formato_diff(segmentacion, format_name):
    if format_name == "stylish":
        return(format_stylish(segmentacion))
    if format_name == "plain":
        return(format_plain(segmentacion))    
    