from django.shortcuts import render
from .forms import LoanForm
from .models import LoanApplication


def home(request):
    return render(request, 'core/index.html')


def apply_loan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the data to your database!
            return render(request, 'core/success.html')
    else:
        form = LoanForm()
    return render(request, 'core/apply.html', {'form': form})


def check_status(request):
    applications = None
    email = request.GET.get('email')
    if email:
        applications = LoanApplication.objects.filter(email=email)
    return render(request, 'core/status.html', {'applications': applications})
