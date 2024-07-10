from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
from .convert import convertPDF_to_word, convertTXT_to_pdf, converterJPG_to_PDF, compress_to_pdf
from django.utils import timezone

# imports generales
import os
import uuid
import json
import base64
from PIL import Image

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
            
            word_file_path = convertPDF_to_word(file_path, token)
            request.session['token'] = token
            request.session['format'] = '.docx'
            request.session['name_file'] = uploaded_file.name

            if 'tokens' not in request.session:
                request.session['tokens'] = []
            else:
                tokens = request.session['tokens']

                if token not in tokens:
                    tokens.append(token)
                    request.session['tokens'] = tokens
            return JsonResponse(
                {
                    'redirect_url': reverse('download', kwargs={'token': token, 'format': '.docx'}),
                }
            )
            
        else:
            return JsonResponse({'error': 'El archivo no es un PDF'}, status=404)


    return render(request, 'pages/services/converter.html',{
        'title': 'File converter'
    })

def converter_txt(request):
    if request.method == 'POST' and request.FILES.get('fileInput'):
        uploaded_file = request.FILES['fileInput']
        documents_folder = os.path.join(settings.BASE_DIR, 'documents')
        token = uuid.uuid4().hex
        if uploaded_file.content_type == 'text/plain':

            if not os.path.exists(documents_folder):
                os.makedirs(documents_folder)

            file_path = os.path.join(documents_folder, token + '.txt')

            with open(file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            
            txt_file_path = convertTXT_to_pdf(file_path, token)
            request.session['token'] = token
            request.session['format'] = '.pdf'
            request.session['name_file'] = uploaded_file.name

            if 'tokens' not in request.session:
                request.session['tokens'] = []
            else:
                tokens = request.session['tokens']

                if token not in tokens:
                    tokens.append(token)
                    request.session['tokens'] = tokens
            return JsonResponse(
                {
                    'redirect_url': reverse('download', kwargs={'token': token, 'format': '.pdf'}),
                }
            )
            
        else:
            return JsonResponse({'error': 'El archivo no es un TXT'}, status=404)

    return render(request, 'pages/services/tools/converter_txt.html',{
        'title': 'File converter'
    })

def converter_jpg(request):
    if request.method == 'POST' and request.FILES.get('fileInput'):
        uploaded_file = request.FILES['fileInput']
        documents_folder = os.path.join(settings.BASE_DIR, 'documents')
        token = uuid.uuid4().hex

        if uploaded_file.content_type == 'image/jpeg':

            img = Image.open(uploaded_file)
            width, height = img.size

            if not os.path.exists(documents_folder):
                os.makedirs(documents_folder)

            file_path = os.path.join(documents_folder, token + '.jpg')

            with open(file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            
            jpg_file_path = converterJPG_to_PDF(file_path, token, width, height)
            request.session['token'] = token
            request.session['format'] = '.pdf'
            request.session['name_file'] = uploaded_file.name

            if 'tokens' not in request.session:
                request.session['tokens'] = []
            else:
                tokens = request.session['tokens']

                if token not in tokens:
                    tokens.append(token)
                    request.session['tokens'] = tokens
            return JsonResponse(
                {
                    'redirect_url': reverse('download', kwargs={'token': token, 'format': '.pdf'}),
                }
            )
            
        else:
            return JsonResponse({'error': 'El archivo no es un JPG'}, status=404)
        
    return render(request, 'pages/services/tools/converter_jpg.html',{
        'title': 'File Converter'
    })

def compress(request):
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
            
            word_file_path = compress_to_pdf(file_path, token)
            request.session['token'] = token
            request.session['format'] = '.pdf'
            request.session['name_file'] = uploaded_file.name

            if 'tokens' not in request.session:
                request.session['tokens'] = []
            else:
                tokens = request.session['tokens']

                if token not in tokens:
                    tokens.append(token)
                    request.session['tokens'] = tokens
            return JsonResponse(
                {
                    'redirect_url': reverse('download', kwargs={'token': token, 'format': '.pdf'}),
                }
            )
            
        else:
            return JsonResponse({'error': 'El archivo no es un PDF'}, status=404)
        
    return render(request, 'pages/services/compress.html',{
        'title': 'File Compress'
    })




# Acciones en el servidor
def download(request, token=None, format=None):
    if token:
        general_name = token + format
        path_folder = os.path.join(settings.BASE_DIR, 'documents', format.split('.')[1])
        path_exists = os.path.join(path_folder, general_name)
        value = os.path.exists(path_exists)
        if value:
            if request.method == 'POST':
                data = json.loads(request.body.decode('utf-8'))
                token = data.get('token')
                format = data.get('format')
                name_file = data.get('name_file')

                file_name = token + format
                documents_folder = os.path.join(settings.BASE_DIR, 'documents', format.split('.')[1])
                file_path = os.path.join(documents_folder, file_name)

                if os.path.exists(file_path):
                    with open(file_path, 'rb') as file:
                        tokens = request.session['tokens']
                        if token not in tokens:
                            tokens.append(token)
                            request.session['tokens'] = tokens    
                        file_content = base64.b64encode(file.read()).decode('utf-8')
                        response_data = {
                            'file_name': name_file.split('.')[0] + format,
                            'file_content_base64': file_content
                        }
                        return JsonResponse(response_data)
                else:
                    return JsonResponse({"error": "El archivo no fue encontrado."}, status=404)  
                
            tokens = request.session['tokens']

            if token not in tokens:
                tokens.append(token)
                request.session['tokens'] = tokens    

            return render(request, 'pages/services/download.html',{
                'title': 'Tools to meet all your needs'
            })
        else:
            return redirect('converter')
    else:
        return redirect('converter')

def delete_file(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        token = body.get('token')

        path_folder = os.path.join(settings.BASE_DIR, 'documents')

        if 'tokens' in request.session:
            tokens = request.session['tokens']
            print('borrando archivos ......')
            print(tokens)
            try:
                deleted_files = 0
            
                # Recorre todos los archivos y subdirectorios dentro de path_folder
                for dirpath, _, filenames in os.walk(path_folder):
                    for filename in filenames:
                        # Verifica si el nombre del archivo coincide con algún token en la lista
                        for token in tokens:
                            if token in filename:
                                file_path = os.path.join(dirpath, filename)
                                os.remove(file_path)
                                deleted_files += 1
                                
                            if 'token' in request.session:
                                del request.session['token']

                            if 'format' in request.session:
                                del request.session['format']

                            if 'name_file' in request.session:
                                del request.session['name_file']
        
            except OSError as e:
                print(f"No se pudo borrar el archivo {filename}: {e}")
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
