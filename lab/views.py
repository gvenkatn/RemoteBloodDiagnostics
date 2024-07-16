from django.shortcuts import render
from django.views import View 
from patient.models import OrderModel
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils.timezone import datetime
from django.views.generic.edit import FormView
from django.http import HttpResponse
from forms import UploadFileForm


# Create your views here.
class Dashboard(UserPassesTestMixin, LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        today = datetime.today()
        
        orders = OrderModel.objects.filter(
            created_on__year=today.year, 
            created_on__month=today.month,
            created_on__day=today.day)
        
        total_revenue = 0
        for order in orders:
            total_revenue += order.price

        context = {
            'orders' : orders,
            'total_revenue' : total_revenue,
            'total_orders' : len(orders)
        }

        return render(request, 'lab/dashboard.html', context)
    
    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()

class OrderDetails(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get (pk=pk)
        context = {
            'order': order
        }
        return render (request, 'lab/order-details.html', context)
    
    def test_func(self) :
        return self.request.user.groups.filter(name='Staff').exists()

def upload_file(request):
    if request.method == 'POST' :
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES['file']
        return HttpResponse("The name of uploaded file is" + str(file))
    else:
        form = UploadFileForm()
    return render (request, 'lab/order-details.html', {'form': form})