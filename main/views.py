from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'application': 'Boon Beauty Store',
        'name' : 'Chelsea Angelica',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)