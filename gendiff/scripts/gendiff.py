import argparse
import json
import yaml
import os


from gendiff.scripts.gendiff import *


def recibir_archivo(ruta):
    extension_id = os.path.splitext(ruta)[1].lower()

    with open(ruta, "r", encoding="utf-8") as lectura:
        if extension_id == ".json":
            return (json.load(lectura))
        elif extension_id in (".yml", ".yaml"):
            return(yaml.safe_load(lectura))
        else:
            print ("extensión no value")


def generate_diff(val1, val2, format_name = "plain", path = ""):

    if isinstance (val1, str) and  isinstance (val2, str):
        data1= recibir_archivo(val1)
        data2= recibir_archivo(val2) 
    
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    
    mensaje= []

    for key in keys:

        if key not in data1:
            #append 1
            mensaje.append({
                "key": key,
                "type": "added",
                "value": data2[key],
            })
        elif key not in data2:
            #append 2
            mensaje.append({
                "key": key,
                "type": "removed",
                "value": data1[key],
            })
        else:
            valorA = data1[key]
            valorB = data2[key]


            if isinstance(valorA, dict)  and isinstance(valorB, dict):
                mensaje.append({
                    "key": key,
                    "type": "nested",
                    "children": generate_diff(valorA, valorB, format_name, _path_= False),
                })

            elif (data1 [key] == data2[key]):
                mensaje.append({
                    "key": key,
                    "type": "unchanged",
                    "value": valorA,
                })

            else: 
                mensaje.append({
                    "key": key,
                    "type": "updated",
                    "old": valorA,
                    "new": valorB,
                })

    #if __path__:
    #    return 
    return(mensaje)


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", help="First file to compare")
    parser.add_argument("second_file", help="Second file to compare")
    parser.add_argument("-f","--format", help="set format of output", default="plain")

    args = parser.parse_args()
    
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()