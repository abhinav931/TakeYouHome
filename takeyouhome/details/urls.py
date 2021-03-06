from django.urls import path, include
from .import views

urlpatterns = [
    path('home/', views.HomePageView.as_view(), name = 'home'),
    path('contact/', views.ContactPageView.as_view(), name = 'contact'),
    path('details/', views.SavingData, name = 'details'),
    path('helpdata/', views.HelpData, name = 'helpdata'),
    path('districts/', views.DistrictsPageView.as_view(), name = 'districts'),
    path('takeyouhome/', views.DownloadFile, name = 'download'),
    path('Bhopal/', views.Bhopal, name='bhopal'),
    path('Raisen/', views.Raisen, name='raisen'),
    path('Rajgarh/', views.Rajgarh, name='rajgarh'),
    path('Sehore/', views.Sehore, name='sehore'),
    path('Vidisha/', views.Vidisha, name='vidisha'),
    path('Morena/', views.Morena, name='morena'),
    path('Sheopur/', views.Sheopur, name='sheopur'),
    path('Bhind/', views.Bhind, name='bhind'),
    path('Gwalior/', views.Gwalior, name='gwalior'),
    path('Ashoknagar/', views.Ashoknagar, name='ashoknagar'),
    path('Shivpuri/', views.Shivpuri, name='shivpuri'),
    path('Datia/', views.Datia, name='datia'),
    path('Guna/', views.Guna, name='guna'),
    path('Alirajpur/', views.Alirajpur,name='alirajpur'),
    path('Barwani/', views.Barwani, name='barwani'),
    path('Burhanpur/', views.Burhanpur, name='burhanpur'),
    path('Indore/', views.Indore, name='indore'),
    path('Jhabua/', views.Jhabua, name='jhabua'),
    path('Dhar/', views.Dhar, name='dhar'),
    path('Khandwa/', views.Khandwa, name='khandwa'),
    path('Khargone/', views.Khargone, name='khargone'),
    path('Balaghat/', views.Balaghat, name='balaghat'),
    path('Chhindwara/', views.Chhindwara, name='chhindwara'),
    path('Jabalpur/', views.Jabalpur, name='jabalpur'),
    path('Katni/', views.Katni, name='katni'),
    path('Mandla/', views.Mandla, name='mandla'),
    path('Narsinghpur/', views.Narsinghpur, name='narsinghpur'),
    path('Seoni/', views.Seoni, name='seoni'),
    path('Dindori/', views.Dindori, name='dindori'),
    path('Betul/', views.Betul, name='betul'),
    path('Harda/', views.Harda, name='harda'),
    path('Hoshangabad/', views.Hoshangabad, name='hoshangabad'),
    path('Rewa/', views.Rewa, name='rewa'),
    path('Satna/', views.Satna, name='satna'),
    path('Sidhi/', views.Sidhi, name='sidhi'),
    path('Singrauli/', views.Singrauli, name='singrauli'),
    path('Chhatarpur/', views.Chhatarpur, name='chhatarpur'),
    path('Damoh/', views.Damoh, name='damoh'),
    path('Panna/', views.Panna, name='panna'),
    path('Sagar/', views.Sagar, name='sagar'),
    path('Tikamgarh/', views.Tikamgarh, name='tikamgarh'),
    path('Nirwari/', views.Nirwari, name='nirwari'),
    path('Anuppur/', views.Anuppur, name='anuppur'),
    path('Shahdol/', views.Shahdol, name='shahdol'),
    path('Umaria/', views.Umaria, name='umaria'),
    path('AgarMalwa/', views.AgarMalwa, name='agarmalwa'),
    path('Dewas/', views.Dewas, name='dewas'),
    path('Mandsaur/', views.Mandsaur, name='mandsaur'),
    path('Neemuch/', views.Neemuch, name='neemuch'),
    path('Ratlam/', views.Ratlam, name='ratlam'),
    path('Shajapur/', views.Shajapur, name='shajapur'),
    path('Ujjain/', views.Ujjain, name='ujjain'),
   
]
