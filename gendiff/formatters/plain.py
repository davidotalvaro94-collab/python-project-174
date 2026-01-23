def format_plain(segmentación):
    lineas = []
    tipo_plain (segmentación, "" ,lineas)
    return("\n".join(lineas))

def tipo_plain(nodos, path, lineas):
    for nodo in nodos:
        name = f"{path}{nodo["type"]}"
        tipo_nodo = nodo["type"]

        if tipo_nodo == "added": 
            lineas.append(
                f"Property '{name}' was added with value: {mensaje_plain(nodo['valor'])}"
            )
        elif tipo_nodo == "removed":
            lineas.append(f"Property '{name}' was removed")
        elif tipo_nodo == "updated":
            lineas.append(
                f"Property '{name}' was updated. From "
                f"{mensaje_plain(nodo['old'])} to {mensaje_plain(nodo['new'])}"
            )
        elif tipo_nodo == "nested":
            mensaje_plain(nodo["children"], name + ".", lineas)


def mensaje_plain(valor):
    if isinstance(valor, dict):
        return("[complex value]")
    if valor is None :
        return("null")
    if isinstance(valor, bool):
        return(str(valor).lower())
    if isinstance(valor, str):
        return(f"'{valor}'")
    
