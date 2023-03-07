from django.shortcuts import render

from django.views import View

from application.models import Application

# Create your views here.

def index(request):
  return render(request, 'index.html')

class ApplicationView(View):
    model = Application
    template_name = 'application.html'
  
    def get(self, request):
        return render(request, 'application.html')

    def post(self, request):
        policies_accepted: bool = request.POST.get('checkbox-input', False)
        
        if policies_accepted == False:
          return render(request, 'application.html', {'error': 'You must accept the policies to submit the application.'})
      
        first_name: str = request.POST.get('first_name', ''), 
        last_name: str = request.POST.get('last_name', ''),
        school: str = request.POST.get('school', ''),
        email: str = request.POST.get('email', ''),
        # TODO: File input will be implemented.

        application: Application = Application.objects.create(full_name = f'{first_name} {last_name}', email = email, school = school)
        
        if application is None:
          return render(request, 'application.html', {'error': 'An error occurred while submitting the application.'})
        
        return render(request, 'application.html', {'success': 'Application submitted successfully.'})