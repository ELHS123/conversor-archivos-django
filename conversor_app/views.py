import os
from django.shortcuts import render
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage
from .forms import CSVUploadForm, PDFUploadForm
from .utils import ensure_directories, convert_csv_to_excel, convert_pdf_to_word

# Create your views here.
def home_view(request):
    """Vista de la página principal para mostrar opciones al usuario."""
    return render(request, 'conversor_app/index.html')

def csv_to_excel_view(request):
    """Maneja el formulario de subida, guarda el CSV y devuelve el Excel."""
    form = CSVUploadForm(request.POST or None, request.FILES or None)
    
    if request.method == 'POST' and form.is_valid():
        uploaded_file = request.FILES['file']
        
        # 1. Obtenemos las rutas y aseguramos que las carpetas existan
        uploads_dir, converted_dir = ensure_directories()
        
        # 2. Guardamos físicamente el archivo original en la carpeta 'uploads'
        fs = FileSystemStorage(location=uploads_dir)
        filename = fs.save(uploaded_file.name, uploaded_file)
        
        # 3. Pasamos el nombre del archivo guardado a nuestra utilidad de conversión
        excel_filename = convert_csv_to_excel(filename)
        
        if excel_filename:
            # 4. Le devolvemos al usuario el archivo resultante como una descarga
            output_path = os.path.join(converted_dir, excel_filename)
            return FileResponse(open(output_path, 'rb'), as_attachment=True, filename=excel_filename)
        else:
            form.add_error(None, 'Hubo un error al convertir el archivo CSV.')
            
    return render(request, 'conversor_app/upload_form.html', {'form': form, 'title': 'Convertir CSV a Excel'})

def pdf_to_word_view(request):
    """Maneja el formulario de subida, guarda el PDF y devuelve el Word."""
    form = PDFUploadForm(request.POST or None, request.FILES or None)
    
    if request.method == 'POST' and form.is_valid():
        uploaded_file = request.FILES['file']
        
        # 1. Obtenemos las rutas y aseguramos que las carpetas existan
        uploads_dir, converted_dir = ensure_directories()
        
        # 2. Guardamos físicamente el archivo original en la carpeta 'uploads'
        fs = FileSystemStorage(location=uploads_dir)
        filename = fs.save(uploaded_file.name, uploaded_file)
        
        # 3. Pasamos el nombre del archivo guardado a nuestra utilidad de conversión
        word_filename = convert_pdf_to_word(filename)
        
        if word_filename:
            # 4. Le devolvemos al usuario el archivo resultante como una descarga
            output_path = os.path.join(converted_dir, word_filename)
            return FileResponse(open(output_path, 'rb'), as_attachment=True, filename=word_filename)
        else:
            form.add_error(None, 'Hubo un error al convertir el archivo PDF.')
            
    return render(request, 'conversor_app/upload_form.html', {'form': form, 'title': 'Convertir PDF a Word'})
