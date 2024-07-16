from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail 

from .models import AvlTest, OrderModel, Doctor


# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request,'patient/index.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request,'patient/about.html')

class Order(View):
    def get(self, request, *args, **kwargs):
        
        #get every item
        available_tests = AvlTest.objects.all()

        context = {'available_tests': available_tests}

        #render the template
        return render(request,'patient/order.html', context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        street = request.POST.get('street')
        pin_code = request.POST.get('pin_code')
        date = request.POST.get('date')

        order_items = {
            'items' : []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            avltest = AvlTest.objects.get(pk__contains=int(item))
            test_data = {
                            'id': avltest.pk,
                            'name': avltest.name,
                            'price': avltest.price
                        }

            order_items['items'].append(test_data)

            price = 0
            item_ids = []

        for item in order_items ['items']: 
            price += item['price'] 
            item_ids.append(item['id'])

        order = OrderModel.objects.create(
            price = price,
            name = name,
            email = email,
            phone = phone,
            street = street,
            pin_code = pin_code,
            date = date)
        
        order.items.add(*item_ids)

        body = (f'''
            Hello {name}!

            Thank You for choosing Us!
            Trust you are in sound health.
            
            The diagnostic center will connect with you on {phone} 
            to confirm the appointment. 
            
            Eat Apples and Stay Healthy!
            ''')

        send_mail(
            'Appointment Scheduled',
            body,
            'example@example.com', 
            [email], 
            fail_silently=False
        )
        
        context = {
            'items': order_items['items'],
            'price': price
            }
        print(order)
        # return render(request, 'patient/order_confirmation.html', context)

        #return redirect('Order-Confirmation', pk=order.pk)

        return render(request, 'patient/order_pay_confirmation.html')



class OrderConfirmation(View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get (pk=pk)

        context = {
            'pk': order.pk,
            'items': order.items,
            'price': order.price,
        }
        return render(request, 'patient/order_confirmation.html', context)
    

    def post(self, request, pk, *args, **kwargs):
        print(request.body)


class OrderPayConfirmation (View):
    def get(self, request, *args, **kwargs) :
        return render (request, 'customer/order_pay_confirmation.html')

class Doctor(View):
    def get(self, request, *args, **kwargs):
        
        #get every item
        available_tests = AvlTest.objects.all()

        context = {'available_tests': available_tests}

        #render the template
        return render(request,'patient/order.html', context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        street = request.POST.get('street')
        pin_code = request.POST.get('pin_code')
        date = request.POST.get('date')

        order_items = {
            'items' : []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            avltest = AvlTest.objects.get(pk__contains=int(item))
            test_data = {
                            'id': avltest.pk,
                            'name': avltest.name,
                            'price': avltest.price
                        }

            order_items['items'].append(test_data)

            price = 0
            item_ids = []


        order = Doctor.objects.create(
            price = price,
            name = name,
            email = email,
            phone = phone,
            street = street,
            pin_code = pin_code,
            date = date)
        
        order.items.add(*item_ids)

        body = (f'''
            Hello {name}!

            Thank You for choosing Us!
            Trust you are in sound health.
            
            The diagnostic center will connect with you on {phone} 
            to confirm the appointment. 
            
            Eat Apples and Stay Healthy!
            ''')

        send_mail(
            'Appointment Scheduled',
            body,
            'example@example.com', 
            [email], 
            fail_silently=False
        )
        
        context = {
            'items': order_items['items'],
            'price': price
            }
        # return render(request, 'patient/order_confirmation.html', context)

        #return redirect('Order-Confirmation', pk=order.pk)

        return render(request, 'patient/order_pay_confirmation.html')
