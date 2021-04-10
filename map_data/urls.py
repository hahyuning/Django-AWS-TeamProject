from django.contrib import admin
from django.urls import path

import map_data.views

urlpatterns = [
    path('theme1/',map_data.views.Culture,name='culture'),
    path('theme2/',map_data.views.Health_welfare,name='health_welfare'),
    path('theme3/',map_data.views.Facility,name='facility'),
    path('theme4/',map_data.views.Education,name='education'),
    path('theme5/',map_data.views.Population,name='population'),
    path('theme6/',map_data.views.Traffic,name='traffic'),
    path('theme7/',map_data.views.Environment,name='environment'),
    path('theme1/theme1/',map_data.views.Museum,name='museum'),
    path('theme1/theme2/',map_data.views.Concert_hall,name='concert_hall'),
    path('theme1/theme3/',map_data.views.Theaters ,name='theaters'),
    path('theme2/theme1/',map_data.views.General_hospital,name='general_hospital'),
    path('theme2/theme2/',map_data.views.Hospital ,name='hospital'),
    path('theme2/theme3/',map_data.views.Pharmacy ,name='pharmacy'),
    path('theme2/theme4/',map_data.views.Dentist ,name='dentist'),
    path('theme2/theme5/',map_data.views.Total_hospital,name='total_hospital'),
    path('theme3/theme1/',map_data.views.Library,name='library'),
    path('theme3/theme2/',map_data.views.Sports_facility,name='sports_facility'),
    path('theme3/theme3/',map_data.views.Park,name='park'),
    path('theme4/theme1/',map_data.views.Kindergarden,name='kindergarden'),
    path('theme4/theme2/',map_data.views.Elementary,name='elementary'),
    path('theme4/theme3/',map_data.views.Middle,name='middle'),
    path('theme4/theme4/',map_data.views.High,name='high'),
    path('theme6/theme1/',map_data.views.Number_of_registered_cars,name='number_of_registered_cars'),
    path('theme6/theme2/',map_data.views.Number_of_parking,name='number_of_parking'),
    path('theme6/theme3/',map_data.views.Bus_satisfaction,name='bus_satisfaction'),
    path('theme6/theme4/',map_data.views.Subway_satisfaction,name='subway_satisfaction'),
    path('theme6/theme5/',map_data.views.Taxi_satisfaction,name='taxi_satisfaction'),
    path('theme7/theme1/',map_data.views.Garbage_discharge,name='garbage_discharge'),
    path('theme7/theme2/',map_data.views.Satisfaction_with_using_green_space,name='satisfaction_with_using_green_space'),
    path('theme7/theme3/',map_data.views.Fine_dust,name='fine_dust'),
    path('theme7/theme4/',map_data.views.Environmental_complaints,name='environmental_complaints'),
    path('theme7/theme5/',map_data.views.Noise_related_complaints,name='noise_related_complaints'),
]


