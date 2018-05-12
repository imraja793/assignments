from django.shortcuts import render
from rest_framework.decorators import api_view

from .models import AddExpense




@api_view(['POST'])
def home(request):
   form = AddExpense(**request.data)
        form.save()
    return render(request, 'based/expense.html', {'form': form})


