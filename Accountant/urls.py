from django.urls import path
from . import views

urlpatterns = [
    path('purchasebill/', views.purchasebill, name='purchasebill'),
    path('displaypurchasebill/', views.displaypurchasebill, name='displaypurchasebill'),
    path('displaypurchasebill1/', views.displaypurchasebill1, name='displaypurchasebill1'),
    path('salesbill/', views.salesbill, name='salesbill'),
    path('display-inventory/', views.display_inventory, name='display_inventory'),

    path('make_payment/', views.make_payment, name='make_payment'),
    path('payment_success/', views.payment_success, name='payment_success'),

    path('submitPaymentReceived/',views.submitPaymentReceived),
    path('payment-paid/',views.payment_paid, name='payment_paid'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('displaysalesbill/', views.displaysalesbill, name='displaysalesbill'),
    path('displaysalesbill1/', views.displaysalesbill1, name='displaysalesbill1'),
    path('paymentreceived/', views.paymentreceived, name='paymentreceived'),
    path('paymentpaid/', views.paymentpaid, name='paymentpaid'),
    path('miscelleneousexpanse/', views.Misc, name='Misc'),
    path('creditors/', views.creditors, name='creditors'),
    path('debtors/', views.debtors, name='debtors'),
]