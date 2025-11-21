import argparse
import json

from gendiff.scripts.gendiff import *

def generate_diff(val1, val2, format_name= "plain"):

    with open(val1, "r", encoding="utf-8") as lectura1:
        data1= json.load(lectura1)
    with open(val2, "r", encoding="utf-8") as lectura2:
        data2= json.load(lectura2)
    
    keys = set(data1.keys()) | set(data2.keys())
    

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
    

    # Agregamos en paso 4
    diff = generate_diff(args.first_file, args.second_file, args.__format__)
    print(diff)


if __name__ == "__main__":
    main()