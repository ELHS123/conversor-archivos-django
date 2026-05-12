import os
import time
import pandas as pd
from pdf2docx import Converter
from django.conf import settings

def ensure_directories():
    """
    Verifica si las carpetas 'uploads' y 'converted' existen dentro de MEDIA_ROOT.
    Si no existen, las crea. Devuelve las rutas absolutas.
    """
    uploads_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
    converted_dir = os.path.join(settings.MEDIA_ROOT, 'converted')
    
    os.makedirs(uploads_dir, exist_ok=True)
    os.makedirs(converted_dir, exist_ok=True)
    
    return uploads_dir, converted_dir

def cleanup_old_files(max_age_seconds=3600):
    """
    Elimina los archivos en las carpetas temporales que sean más antiguos
    que 'max_age_seconds' (por defecto 3600 segundos = 1 hora).
    """
    uploads_dir, converted_dir = ensure_directories()
    current_time = time.time()
    
    for directory in [uploads_dir, converted_dir]:
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                file_mtime = os.path.getmtime(filepath)
                # Si el archivo es más viejo que max_age_seconds, se elimina
                if (current_time - file_mtime) > max_age_seconds:
                    try:
                        os.remove(filepath)
                    except Exception as e:
                        print(f"Error al eliminar {filepath}: {e}")

def convert_csv_to_excel(csv_filename):
    """
    Toma el nombre de un archivo CSV en 'uploads', lo convierte a Excel (.xlsx)
    y lo guarda en 'converted'. Devuelve el nombre del archivo generado.
    """
    # 1. Preparar directorios y limpiar archivos viejos
    uploads_dir, converted_dir = ensure_directories()
    cleanup_old_files()
    
    # 2. Definir las rutas de entrada y salida
    input_path = os.path.join(uploads_dir, csv_filename)
    
    # Extraer el nombre sin extensión y agregar .xlsx
    base_name = os.path.splitext(csv_filename)[0]
    excel_filename = f"{base_name}.xlsx"
    output_path = os.path.join(converted_dir, excel_filename)
    
    # 3. Conversión usando Pandas
    try:
        # Intenta primero con la codificación y separador estándar (UTF-8 y coma)
        try:
            df = pd.read_csv(input_path)
        except Exception:
            # Si falla, intenta con la configuración típica de Excel en Windows/Español
            df = pd.read_csv(input_path, encoding='latin-1', sep=';')
            
        df.to_excel(output_path, index=False, engine='openpyxl')
        return excel_filename
    except Exception as e:
        print(f"Error en la conversión de CSV a Excel: {e}")
        return None

def convert_pdf_to_word(pdf_filename):
    """
    Toma el nombre de un archivo PDF en 'uploads', lo convierte a Word (.docx)
    y lo guarda en 'converted'. Devuelve el nombre del archivo generado.
    """
    # 1. Preparar directorios y limpiar archivos viejos
    uploads_dir, converted_dir = ensure_directories()
    cleanup_old_files()
    
    # 2. Definir las rutas de entrada y salida
    input_path = os.path.join(uploads_dir, pdf_filename)
    
    # Extraer el nombre sin extensión y agregar .docx
    base_name = os.path.splitext(pdf_filename)[0]
    word_filename = f"{base_name}.docx"
    output_path = os.path.join(converted_dir, word_filename)
    
    # 3. Conversión usando pdf2docx
    try:
        cv = Converter(input_path)
        cv.convert(output_path, start=0, end=None)
        cv.close()
        return word_filename
    except Exception as e:
        print(f"Error en la conversión de PDF a Word: {e}")
        return None