import argparse
import json
import yaml
import os


from gendiff.scripts.gendiff import *


def recibir_archivo(ruta):
    extension_id = os.path.splitext(ruta)[1].lower()

    with open(ruta, "r") as lectura:
        if extension_id == ".json":
            return (json.load(lectura))
        elif extension_id in (".yml", ".yaml"):
            return(yaml.safe_load(lectura))
        else: 
            print ("extensión no value")


def generate_diff(val1, val2, format_name= "stylish"):

    data1= recibir_archivo(val1)
    data2= recibir_archivo(val2)
    
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    

    mensaje= ["{"]

    for key in keys:

        inp1 = key in data1
        inp2 = key in data2

        if (inp1 and not inp2): 
            mensaje.append(f" - {key}: {data1[key]}")
        elif (not inp1 and inp2):
            mensaje.append(f" + {key}: {data2[key]}")
        else: 
            if (data1 [key] == data2[key]):
                mensaje.append(f"   {key}: {data1[key]}")
            else: 
                mensaje.append(f" - {key}: {data1[key]}")
                mensaje.append(f" + {key}: {data2[key]}")

    mensaje.append("}")
    mensaje="\n".join(mensaje)
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