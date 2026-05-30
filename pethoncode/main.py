import sys
import subprocess
import re

# traducciones 
traducciones = {
    # Keywords
    "Falso": "False",
    "Nulo": "None",
    "Verdadero": "True",
    "y": "and",
    "como": "as",
    "asegurar": "assert",
    "asincrono": "async",
    "esperar": "await",
    "romper": "break",
    "clase": "class",
    "continuar": "continue",
    "definir": "def",
    "eliminar": "del",
    "si_no_si": "elif",
    "sino": "else",
    "excepcion": "except",
    "finalmente": "finally",
    "para": "for",
    "desde": "from",
    "global": "global",
    "si": "if",
    "importar": "import",
    "en": "in",
    "es": "is",
    "lambda": "lambda",
    "no_local": "nonlocal",
    "no": "not",
    "o": "or",
    "pasar": "pass",
    "elevar": "raise",
    "retornar": "return",
    "intentar": "try",
    "mientras": "while",
    "con": "with",
    "producir": "yield",

    # Built-in Functions
    "absoluto": "abs",
    "iterador_asincrono": "aiter",
    "todo": "all",
    "siguiente_asincrono": "anext",
    "alguno": "any",
    "ascii": "ascii",
    "binario": "bin",
    "booleano": "bool",
    "punto_ruptura": "breakpoint",
    "array_bytes": "bytearray",
    "bytes": "bytes",
    "llamable": "callable",
    "caracter": "chr",
    "metodo_clase": "classmethod",
    "compilar": "compile",
    "complejo": "complex",
    "copyright": "copyright",
    "creditos": "credits",
    "eliminar_atributo": "delattr",
    "diccionario": "dict",
    "dir": "dir",
    "divmod": "divmod",
    "enumerar": "enumerate",
    "evaluar": "eval",
    "ejecutar": "exec",
    "salir": "exit",
    "filtrar": "filter",
    "flotante": "float",
    "formatear": "format",
    "conjunto_congelado": "frozenset",
    "obtener_atributo": "getattr",
    "globales": "globals",
    "tiene_atributo": "hasattr",
    "hash": "hash",
    "ayuda": "help",
    "hexadecimal": "hex",
    "id": "id",
    "entrada": "input",
    "entero": "int",
    "es_instancia": "isinstance",
    "es_subclase": "issubclass",
    "iterar": "iter",
    "longitud": "len",
    "licencia": "license",
    "lista": "list",
    "locales": "locals",
    "mapear": "map",
    "maximo": "max",
    "vista_memoria": "memoryview",
    "minimo": "min",
    "siguiente": "next",
    "objeto": "object",
    "octal": "oct",
    "abrir": "open",
    "orden": "ord",
    "potencia": "pow",
    "imprimir": "print",
    "propiedad": "property",
    "cerrar": "quit",
    "rango": "range",
    "representacion": "repr",
    "revertir": "reversed",
    "redondear": "round",
    "conjunto": "set",
    "establecer_atributo": "setattr",
    "rebanada": "slice",
    "ordenar": "sorted",
    "metodo_estatico": "staticmethod",
    "texto": "str",
    "sumar": "sum",
    "super": "super",
    "tupla": "tuple",
    "tipo": "type",
    "variables": "vars",
    "unir": "zip"
}

def transpilar(archivo_pe):
    with open(archivo_pe, 'r', encoding='utf-8') as f:
        contenido = f.read()

    # Control de traduccion
    for pe, python in traducciones.items():
        # \b no se que hace pero la ia me dijo que lo ponga
        contenido = re.sub(r'\b' + pe + r'\b', python, contenido)

    return contenido

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python pe.py tu_archivo.pe")
    else:
        nombre_archivo = sys.argv[1]
        codigo_python = transpilar(nombre_archivo)
        
        with open("temp_pethon.py", "w", encoding='utf-8') as f:
            f.write(codigo_python)
        
        # Ejecutamos el archivo resultante
        subprocess.run(["python3", "temp_pethon.py"])
