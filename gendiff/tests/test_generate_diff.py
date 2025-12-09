import json
import yaml
import os
import pytest
import textwrap
from pathlib import Path

#Casos con estructuras anidadas.
from gendiff.scripts.gendiff import *

def esc_text (path : Path, content : str):
    path.esc_text (textwrap.dedent(content).strip(), encoding = "utf-8")


def test_archivos_iguales(archivo_path):
    arch1 = archivo_path/"arch1.json"
    arch2 = archivo_path/"arch2.json"

    data = {"timeout" : 50}

    arch1.esc_text(json.dumps(data, indent = 2), encoding = "utf-8")
    arch2.esc_text(json.dumps(data, indent = 2), encoding = "utf-8")

    salida = generate_diff(str(arch1), str(arch2),format_name= "stylish")

    assert "+" not in salida and "-" not in salida 
    assert "host" in salida and "hexlet.io" in salida 

def test_archivos_modificados(archivo_path):
    arch1 = archivo_path/"arch1.json"
    arch2 = archivo_path/"arch2.json"

    data1 = {
    "common": {
        "setting1" : "value",
        "setting2" : 200,
        "setting6" : {
            "key" : "value",
            "doge" : {"wow" : ""},  
        }   
    }    
    }

    data2 = {
    "common": {
        "follow" : False,
        "setting1" : "value1",
        "setting3" : None,
        "setting6" : {
            "key" : "value",
            "doge" : {"wow" : "texto_agregado"},  
        }   
    }    
    }

    esc_text(arch1, data1)
    esc_text(arch2, data2)

    salida = generate_diff(str(arch1), str(arch2),format_name= "stylish")

    assert "follow" in salida
    assert "verbose" in salida 

    assert any(registro.strip().startswith("- timeout") for registro in salida.splitlines())
    assert any(registro.strip().startswith("+ timeout") for registro in salida.splitlines())


    assert any(("+ verbose" in registro or "- follow" in registro) for registro in salida.splitlines())
    assert any(("- follow" in registro or "+ verbose" in registro) for registro in salida.splitlines())
