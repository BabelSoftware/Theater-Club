from django.shortcuts import render

from django.views import View

from application.models import Application

# Create your views here.

def index(request):
  return render(request, 'index.html')

def clubs(request):
  return render(request, 'clubs.html')
class ApplicationView(View):
    model = Application
    template_name = 'application.html'
  
    def get(self, request):
        return render(request, 'application.html')

    def post(self, request):
        policies_accepted: bool = request.POST.get('checkbox-input', False)
        
        if policies_accepted == False:
          return render(request, 'application.html', {'error': 'You must accept the policies to submit the application.'})
      
        first_name: str = request.POST['first-name'] 
        last_name: str = request.POST['last-name']
        school: str = request.POST['school']
        email: str = request.POST['email']
        # TODO: File input will be implemented.

        if not first_name or not last_name or not school or not email: 
          return render(request, 'application.html', {'error': 'An error occured while getting the form data.'})

        application: Application = Application.objects.create(full_name = f'{first_name} {last_name}', email = email, school = school)
        
        if application is None:
          return render(request, 'application.html', {'error': 'An error occurred while submitting the application.'})
        
      
        application.save()
        print('An application created succesfully.')

        return render(request, 'application.html', {'success': 'Application submitted successfully.'})
