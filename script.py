import os
import sys
 
def contar_lineas(ruta_archivo):
    archivo = open (ruta_archivo, 'r')
    lineas = archivo.readlines()
    return len(lineas)

def contar_palabras(ruta_archivo):
    archivo = open (ruta_archivo, 'r')
    palabras = archivo.read().split()
    return len(palabras)

def contar_python(ruta_archivo):
    archivo = open (ruta_archivo, 'r')
    contenido = archivo.read().lower()
    return contenido.count('python')

def crear_informe(directorio):
    informe = ""
    archivos_txt = []
    for archivo in os.listdir(directorio):
        if archivo.endswith('.txt'):
            archivos_txt.append(archivo)
    if not archivos_txt:
        informe += "No se encontraron archivos de texto\n"
    else:
        for archivo in archivos_txt:
            ruta_archivo = os.path.join(directorio, archivo)
            try:
                lineas = contar_lineas(ruta_archivo)
                palabras = contar_palabras(ruta_archivo)
                palabra_python = contar_python(ruta_archivo)
                informe += f"""
Archivo: {archivo}
Lineas: {lineas}
Palabras: {palabras}
Ocurrencias de Python: {palabra_python}\n
"""
            except FileNotFoundError:
                informe += f"Error: El archivo {archivo} no existe\n\n"
            except PermissionError:
                informe += f"Error: No se tienen permisos de lectura para el archivo {archivo}\n\n"
    archivo_informe = open(os.path.join(directorio, 'informe.txt'), 'w')
    archivo_informe.write(informe)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        directorio = sys.argv[1]
        crear_informe(directorio)
    print("Uso: python script.py <directorio>")
    sys.exit(1)