from django.urls import path

from Online_shop.main_app.views.flowers import FlowersView, FlowersCreateView, FlowersDetailsView, FlowersEditView, \
    FlowersDeleteVies
from Online_shop.main_app.views.generic import IndexView
from Online_shop.main_app.views.jewelry import JewelryView, JewelryCreateView, JewelryDetailsView, JewelryEditView, \
    JewelryDeleteVies
from Online_shop.main_app.views.plants import PlantsView, PlantsCreateView, PlantsDetailsView, PlantsEditView, \
    PlantsDeleteVies
from Online_shop.main_app.views.quotations import QuotationCreateView
from Online_shop.main_app.views.souvenirs import SouvenirsView, SouvenirsCreateView, SouvenirsDetailsView, \
    SouvenirsEditView, SouvenirsDeleteVies

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('flowers/', FlowersView.as_view(), name='flowers'),
    path('flowers/create/', FlowersCreateView.as_view(), name='flowers create'),
    path('flowers/details/<int:pk>', FlowersDetailsView.as_view(), name='flowers details'),
    path('flowers/edit/<int:pk>', FlowersEditView.as_view(), name='flowers edit'),
    path('flowers/delete/<int:pk>', FlowersDeleteVies.as_view(), name='flowers delete'),

    path('souvenirs/', SouvenirsView.as_view(), name='souvenirs'),
    path('souvenirs/create/', SouvenirsCreateView.as_view(), name='souvenirs create'),
    path('souvenirs/details/<int:pk>', SouvenirsDetailsView.as_view(), name='souvenirs details'),
    path('souvenirs/edit/<int:pk>', SouvenirsEditView.as_view(), name='souvenirs edit'),
    path('souvenirs/delete/<int:pk>', SouvenirsDeleteVies.as_view(), name='souvenirs delete'),

    path('plants/', PlantsView.as_view(), name='plants'),
    path('plants/create/', PlantsCreateView.as_view(), name='plants create'),
    path('plants/details/<int:pk>', PlantsDetailsView.as_view(), name='plants details'),
    path('plants/edit/<int:pk>', PlantsEditView.as_view(), name='plants edit'),
    path('plants/delete/<int:pk>', PlantsDeleteVies.as_view(), name='plants delete'),

    path('jewelry/', JewelryView.as_view(), name='jewels'),
    path('jewelry/create/', JewelryCreateView.as_view(), name='jewels create'),
    path('jewelry/details/<int:pk>', JewelryDetailsView.as_view(), name='jewels details'),
    path('jewelry/edit/<int:pk>', JewelryEditView.as_view(), name='jewels edit'),
    path('jewelry/delete/<int:pk>', JewelryDeleteVies.as_view(), name='jewels delete'),

    path('quotations/', QuotationCreateView.as_view(), name='quotation create')
]
