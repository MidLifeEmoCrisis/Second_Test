from django.shortcuts import render

def front_page(request):
    return render(request, 'First_Project/Templates/front_page.html')
