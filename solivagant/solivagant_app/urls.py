from django.urls import include, path
from solivagant_app import views
 
app_name = 'solivagant_app'
 
urlpatterns = [
    path('contact_form',views.contact_form,name='contact_form'),
    path('about',views.about,name='about'),
    #Url for contact view
    path('contact',views.contact,name='contact'),
    path('contact_form_submit',views.contact_form_submit,name='contact_form_submit'),
    #Url for all_data view
    path('all_data',views.all_data,name='all_data'),
    #Url for portflio view
    path('portfolio',views.portfolio,name='portfolio'),
]