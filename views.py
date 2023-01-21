from django.shortcuts import render
from .models import MyModel

def my_view(request):
    my_model_data = MyModel.objects.all()
    return render(request, 'template.html', {'data': my_model_data})

