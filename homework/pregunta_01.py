# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import os
import zipfile
import pandas as pd

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    # Descomprimir el archivo
    zPath = "files/input.zip"
    extractPath = "files"
    
    if os.path.exists(zPath):
        with zipfile.ZipFile(zPath, 'r') as zip_ref:
            zip_ref.extractall(extractPath)
    
    # Crear carpeta output si no existe
    output_path = "files/output"
    os.makedirs(output_path, exist_ok=True)
    
    # Procesar datasets
    for dataset_type in ["train", "test"]:
        data = []
        dataset_path = f"files/input/{dataset_type}"
        
        # Iterar sobre cada categoría (negative, positive, neutral)
        for category in os.listdir(dataset_path):
            category_path = os.path.join(dataset_path, category)
            
            if os.path.isdir(category_path):
                # Leer todos los archivos .txt en la categoría
                for filename in os.listdir(category_path):
                    if filename.endswith(".txt"):
                        file_path = os.path.join(category_path, filename)
                        with open(file_path, 'r', encoding='utf-8') as f:
                            phrase = f.read().strip()
                            data.append({"phrase": phrase, "target": category})
        
        # Crear DataFrame y guardarlo como CSV
        df = pd.DataFrame(data)
        output_file = f"files/output/{dataset_type}_dataset.csv"
        df.to_csv(output_file, index=False)
