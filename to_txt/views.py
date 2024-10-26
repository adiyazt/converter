from django.shortcuts import render
from django.http import HttpResponse, FileResponse
import docx2txt
from .models import WordFile
import glob

# Create your views here.

import time
def index(request):
    if request.method == 'POST':
        status = 'loading'
        file = request.FILES['file']
        data = handle_upload_file(file=file)
        status = 'creating'
        txt_path = convert(data[0])
        return FileResponse(open(txt_path, 'rb'), as_attachment=True)
    else:
        return render(request, 'index.html')
    
    

def handle_upload_file(file):
    _filename = str(file)
    if _filename.split('.')[-1] in ('docx'):
        wordfile = WordFile(filename=_filename)
        wordfile.save()
        _path = f'to_txt/static/word_files/{wordfile.id}.docx'

        with open(_path, 'wb+') as _file:
            for chunk in file.chunks():
                _file.write(chunk)
                
        return [_path, wordfile]
        
                
import os
from docx import Document

def convert(docx_path):
    output_folder = 'to_txt/static/txt_files'
    file = docx_path.split('/')[3].split('.')[0]
    print(11111111111111111111, file)
    txt_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".txt")

    doc = Document(docx_path)
    content = [p.text for p in doc.paragraphs]

    with open(txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write("\n".join(content))

    return txt_path
