from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.urls import reverse
from django.conf import settings
from pdf2docx import Converter

# imports generales
import os
import uuid
import json
import base64

# convertidores
def convert_to_word(pdf_file, name):
    documents_folder = os.path.join(settings.BASE_DIR, 'documents/word')
    word_file = os.path.join(documents_folder, f'{name}.docx')
    cv = Converter(pdf_file)
    cv.convert(word_file, start=0, end=None)
    cv.close()
    
    return word_file


# Create your views here.

def inicio(request):
    if request.method == 'POST':
        print('peticion post')

    return render(request, 'pages/home/inicio.html',{
        'title': 'All in one'
    })

def tools(request):
    return render(request, 'pages/services/tools.html',{
        'title': 'Tools to meet all your needs'
    })




# Receptores De Archivos
def converter(request):
    if request.method == 'POST' and request.FILES.get('fileInput'):

        uploaded_file = request.FILES['fileInput']
        documents_folder = os.path.join(settings.BASE_DIR, 'documents')
        token = uuid.uuid4().hex

        if uploaded_file.content_type == 'application/pdf':

            if not os.path.exists(documents_folder):
                os.makedirs(documents_folder)

            file_path = os.path.join(documents_folder, token + '.pdf')


            with open(file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            word_file_path = convert_to_word(file_path, token)
            request.session['token'] = token
            request.session['format'] = '.docx'
            request.session['name_file'] = uploaded_file.name
            return JsonResponse(
                {
                    'redirect_url': reverse('download', kwargs={'token': token}),
                }
            )
        else:
            return JsonResponse({'error': 'El archivo no es un PDF'}, status=404)


    return render(request, 'pages/services/converter.html',{
        'title': 'File converter'
    })

# Compresor de archivos
def compress(request):
    return render(request, 'pages/services/compress.html',{
        'title': 'File Compress'
    })

# Descarga de archivos del servidor
def download(request, token=None):
    if token:
        general_name = token + '.docx'
        path_folder = os.path.join(settings.BASE_DIR, 'documents', 'word')
        path_exists = os.path.join(path_folder, general_name)
        value = os.path.exists(path_exists)
        if value:
            if request.method == 'POST':
                data = json.loads(request.body.decode('utf-8'))
                token = data.get('token')
                format = data.get('format')
                name_file = data.get('name_file')
                if format == '.docx':
                    file_name = token + format
                    documents_folder = os.path.join(settings.BASE_DIR, 'documents', 'word')
                    file_path = os.path.join(documents_folder, file_name)

                    if os.path.exists(file_path):
                        with open(file_path, 'rb') as file:
                            file_content = base64.b64encode(file.read()).decode('utf-8')
                            response_data = {
                                'file_name': name_file.split('.pdf')[0] + format,
                                'file_content_base64': file_content
                            }
                            return JsonResponse(response_data)
                    else:
                        return JsonResponse({"error": "El archivo no fue encontrado."}, status=404)
                else:
                    return JsonResponse({"error": "Error en el formato"}, status=404)  

            return render(request, 'pages/services/download.html',{
                'title': 'Tools to meet all your needs'
            })
        else:
            return redirect('converter')
    else:
        return redirect('converter')

# Eliminar los archivos del servidor
def delete_file(request):
    if request.method == 'POST':
        print('borrando archivos ......')

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        # Obtener el token del cuerpo de la solicitud
        token = body.get('token')

        general_name = token + '.docx'
        path_folder = os.path.join(settings.BASE_DIR, 'documents', 'word')
        path_exists = os.path.join(path_folder, general_name)
        value = os.path.exists(path_exists)
        if value:

            general_name2 = token + '.pdf'
            path_folder2 = os.path.join(settings.BASE_DIR, 'documents')
            path_exists2 = os.path.join(path_folder2, general_name2)

            os.remove(path_exists)
            os.remove(path_exists2)

            if 'token' in request.session:
                del request.session['token']

            if 'format' in request.session:
                del request.session['format']

            if 'name_file' in request.session:
                del request.session['name_file']

        return redirect('converter')

    return redirect('converter')



# views login's

def signup(request):
    return render(request, 'pages/login/signup.html',{
        'title': 'Account Center'
    })

def login(request):
    return render(request, 'pages/login/login.html',{
        'title': 'Account Center'
    })