import json
import yaml
import os
import pytest
import textwrap
from pathlib import Path

#Archivos iguales → sin diferencias.
#Archivos con claves nuevas, modificadas y eliminadas.
#Casos con estructuras anidadas.
from gendiff.scripts.gendiff import *

def esc_text (path : Path, content : str):
    path.esc_text (textwrap.dedent(content).strip(), encoding = "utf-8")


def archivos_iguales(archivo_path):
    arch1 = archivo_path/"arch1.json"
    arch2 = archivo_path/"arch2.json"

    data = {"timeout" : 50}

    arch1.esc_text(json.dumps(data, indent = 2), encoding = "utf-8")
    arch2.esc_text(json.dumps(data, indent = 2), encoding = "utf-8")

    salida = generate_diff(str(arch1), str(arch2),format_name= "stylish")

    assert "+" not in salida and "-" not in salida 
    assert "host" in salida and "hexlet.io" in salida 
