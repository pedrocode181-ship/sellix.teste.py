from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    senha_user = None

    if request.method == 'POST':
        senha_user = request.POST.get('senha')

    if senha_user in ['1234', 'pedro']:
        return redirect('pagina principal')

    return render(request, 'core/index.html')

def principal(request):
    return render(request, 'core/principal.html')