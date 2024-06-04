from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'pages/home/inicio.html',{
        'title': 'All in one'
    })

def tools(request):
    return render(request, 'pages/services/tools.html',{
        'title': 'Tools to meet all your needs'
    })

def converter(request):
    return render(request, 'pages/services/converter.html',{
        'title': 'File converter'
    })

def compress(request):
    return render(request, 'pages/services/compress.html',{
        'title': 'File Compress'
    })