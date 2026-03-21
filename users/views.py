from django.shortcuts import render, redirect  # trimite un fisier HTML in browser, redirect #sa trimti userul pe alta pagina
from .forms import RegisterForm
from django.contrib.auth import login

# Create your views here.
def register(request):
    if request.method == 'POST': #POST adica trimite datele catre server
        form = RegisterForm(request.POST) #cream formularul cu date (username, parola)

        if form.is_valid(): #validare formulare
            user = form.save() #salvare user
            login(request, user) #autentificare dupa ce si-a facut cont
            return redirect("/")
    else: #cand pagina este doar deschisa, cand nu este pe POST, ci pe GET, adica userul doar a deschis pagina
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})
