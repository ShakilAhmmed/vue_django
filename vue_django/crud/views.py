from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import Student
from .forms import StudentForm
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser


# Create your views here.
def home(request):
    return render(request, 'index.html')


def save(request):
    if request.method == "POST":
        # return JsonResponse({'data': request.POST.get('data[name]')})
        data = {
            'name': request.POST.get('data[name]'),
            'roll': request.POST.get('data[roll]')
        }
        form = StudentForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Successfully Added', 'status': 200, 'data': form.data})
        else:
            return JsonResponse({'message': 'Invalid', 'status': 503, 'errors': form.errors})
    else:
        all_data = Student.objects.all()
        serialized_data = StudentSerializer(all_data, many=True)
        return JsonResponse({'message': 'Success', 'status': 200, 'data': serialized_data.data}, safe=False)


def update(request):
    if request.method == "POST":
        # return JsonResponse({'data': request.POST.get('data[name]')})
        data = {
            'id': request.POST.get('data[id]'),
            'name': request.POST.get('data[name]'),
            'roll': request.POST.get('data[roll]')
        }
        get_prev = get_object_or_404(Student, pk=data.get('id'))
        form = StudentForm(data, instance=get_prev)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Successfully Updated', 'status': 200, 'data': form.data})
        else:
            return JsonResponse({'message': 'Invalid', 'status': 503, 'errors': form.errors})


def delete(request):
    if request.method == "POST":
        id = request.POST.get('id')
        delete = Student.objects.filter(pk=id).delete()
        if delete:
            return JsonResponse({'message': 'Success', 'status': 200})
        else:
            return JsonResponse({'message': 'Invalid', 'status': 503})
