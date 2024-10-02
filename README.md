# Análisis de Archivos de Texto

Propietario del repositorio: Ammy Zúñiga Mora

Este script permite analizar archivos de texto en un directorio específico, proporcionando información sobre la cantidad de líneas, palabras y el número de ocurrencias de la palabra "Python". El resultado se guarda en un archivo `informe.txt` dentro del mismo directorio.

## Instrucciones de uso

1. Clonar el repositorio en tu máquina local:
    ```bash
    git clone https://github.com/usuario/repositorio.git
    ```

2. Navegar al directorio del proyecto:
    ```bash
    cd repositorio
    ```

3. Ejecutar el script en la terminal, especificando el directorio que contiene los archivos `.txt`:
    ```bash
    python script.py <directorio>
    ```

   - Reemplaza `<directorio>` con la ruta al directorio donde se encuentran los archivos de texto.

4. El informe con los resultados será generado en un archivo `informe.txt` en el directorio especificado.

## Explicación de la implementación

El script realiza tres tareas principales:

1. **Contar líneas**: Lee el archivo línea por línea y devuelve el número total.
2. **Contar palabras**: Divide el contenido del archivo en palabras y cuenta cuántas hay.
3. **Contar la palabra "Python"**: Busca las ocurrencias de la palabra "python" (sin distinción de mayúsculas).

## Errores posibles

- Si el archivo no existe, se notificará en el informe.
- Si no se tienen permisos para leer el archivo, también se incluirá una advertencia en el informe.
