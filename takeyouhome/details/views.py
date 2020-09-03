from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from .forms import *
from .models import *
from django.contrib import messages
import csv
import mimetypes
from django.http import HttpResponse

#JUST FOR VIEWS 

class HomePageView(TemplateView):
    template_name = 'home.html'

#class HelpPageView(TemplateView):
#    template_name = 'help.html'
    
class ContactPageView(TemplateView):
    template_name = 'contact.html'

class DistrictsPageView(TemplateView):
    template_name = 'districts.html'

class DetailPageView(TemplateView):
    template_name = 'details.html'


#SAVING DATA INTO RESPECTIVE TABLE

def SavingData(request):
    if request.method == 'POST':
        form = SavingDataForm(request.POST)
        if form.is_valid():
            
            #CHECKIING RE-ENTERED FIELDS
            
            first1 = request.POST['firstName']
            last1 = request.POST['lastName']
            aadhaar1 = request.POST['aadhaarNo']
            contact1 = request.POST['contactNo']
            email1 = request.POST['emailId']
            
            first2 = request.POST['checkfirstName']
            last2 = request.POST['checklastName']
            aadhaar2 = request.POST['checkaadhaarNo']
            contact2 = request.POST['checkcontactNo']
            email2 = request.POST['checkemailId']
            
            flag = 0
            if (first1 != first2):
                flag = 1
                messages.info(request, 'first name not matched')
            if (last1 != last2):
                flag = 1
                messages.info(request, 'last name not matched')
            if (aadhaar1 != aadhaar2):
                flag = 1
                messages.info(request, 'aadhaar no. not matched')
            if (contact1 != contact2):
                flag = 1
                messages.info(request, 'contact no. not matched')
            if (email1 != email2):
                flag = 1
                messages.info(request, 'email id not matched')
            if flag == 1:
                return render(request, 'details.html', {'form':form})
            
            obj = get_object_or_404(divisionDistrict, district_name = request.POST['curdistrict'].title())
        
            divnum = obj.div_no
            if divnum == 1:
                modelName = BhopalData
            elif divnum == 2:
                modelName = ChambalData
            elif divnum == 3:
                modelName = GwaliorData
            elif divnum == 4:
                modelName = IndoreData
            elif divnum == 5:
                modelName = JabalpurData
            elif divnum == 6:
                modelName = NarmadapuramData
            elif divnum == 7:
                modelName = RewaData
            elif divnum == 8:
                modelName = SagarData
            elif divnum == 9:
                modelName = ShahdolData
            else:
                modelName = UjjainData
            
            cur_add = 'H No. ' + str(request.POST['curhouseNo']) + ', ' 'Ward No. ' + str(request.POST['curwardNo']) + ', ' + 'district - ' + str(request.POST['curdistrict']) + ', ' + 'state - ' +str(request.POST['curState']) + ', ' + 'pincode - ' + str(request.POST['curpinCode'])
            
            per_add = 'H No. ' + str(request.POST['perhouseNo']) + ', ' 'Ward No. ' + str(request.POST['perwardNo']) + ', ' + 'district - ' + str(request.POST['perdistrict']) + ', ' + 'state - ' +str(request.POST['perState'])  + ', ' + 'pincode - ' + str(request.POST['curpinCode'])
            
            req = modelName(stucked_district = request.POST['curdistrict'].title(),
                           first_name = request.POST['firstName'].title(),
                           last_name = request.POST['lastName'].title(),
                           gender = request.POST['genderPerson'],
                           aadhaar_no = request.POST['aadhaarNo'],
                           contact_no = request.POST['contactNo'],
                           email = request.POST['emailId'],
                           reason = request.POST['reasonPerson'],
                           current_address =  cur_add,
                           permanent_address  = per_add,
                           comments = request.POST['comments']
                           )
            req.save()
            return redirect('home')
    else:
            form = SavingDataForm()
    context = {'form': form} 
    return render(request, 'details.html', context)

#SAVING HELP DATA



def HelpData(request):
    if request.method == 'POST':
        form = HelpDataForm(request.POST)
        if form.is_valid():
            req = Instructions(message = request.POST['helpdata']) 
            req.save()
            return redirect('home')
    else:
        form = HelpDataForm()
        
    context = {'form':form}
    return render(request, 'help.html', context)


##DOWNLOAD LINKS 


dist_name = None
another_context = None
def common(request, model_name, district):
    global dist_name 
    dist_name = district
    list_of_records = model_name.objects.all().filter(stucked_district = district)
    no_of_rows = len(list_of_records)
    form = DownloadForm()
    context = {'records':list_of_records, 'rows': no_of_rows, 'district':district, 'form':form}
    global another_context
    another_context = context
    return render(request, 'data.html', context)




def DownloadFile(request):
    # fill these variables with real values
    if request.method == 'POST': 
            dist = request.POST['district'].title()
            if dist_name != dist:
                messages.info(request, 'Enter correct district')
                return render(request, 'data.html', another_context)
            obj = get_object_or_404(divisionDistrict, district_name = dist)

            divnum = obj.div_no
            if divnum == 1:
                        modelName = BhopalData
            elif divnum == 2:
                        modelName = ChambalData
            elif divnum == 3:
                        modelName = GwaliorData
            elif divnum == 4:
                        modelName = IndoreData
            elif divnum == 5:
                        modelName = JabalpurData
            elif divnum == 6:
                        modelName = NarmadapuramData
            elif divnum == 7:
                        modelName = RewaData
            elif divnum == 8:
                        modelName = SagarData
            elif divnum == 9:
                        modelName = ShahdolData
            else:
                        modelName = UjjainData
            list_of_records = modelName.objects.all().filter(stucked_district = dist.title())
            if len(list_of_records) > 0:
                with open('data_of_district.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['Current District', 'First Name', 'LastName', 'Gender', 'Aadhaar No.', 'Contact No.', 'E-mail', 'Current Address', 'Permanent Address', 'Reason', 'Comments'])
                    for rec in list_of_records:
                        writer.writerow([rec.stucked_district, rec.first_name, rec.last_name, rec.gender, rec.aadhaar_no, rec.contact_no, rec.email, rec.current_address, rec.permanent_address, rec.reason, rec.comments])
                fl_path = 'data_of_district.csv'
                filename = 'data_of_district.csv'

                fl = open(fl_path, 'r')
                mime_type, _ = mimetypes.guess_type(fl_path)
                response = HttpResponse(fl, content_type=mime_type)
                response['Content-Disposition'] = "attachment; filename=%s" % filename
                return response
            else:
                messages.info(request, 'No data: Can\'t download an empty file')
                return render(request, 'data.html')

#HANDLING DATA PAGE

    


 #division1
    
    
    
    
def Bhopal(request):
    return common(request, BhopalData, 'Bhopal')

def Raisen(request):
    return common(request, BhopalData, 'Raisen')

def Rajgarh(request):
    return common(request, BhopalData, 'Rajgarh')

def Sehore(request):
    return common(request, BhopalData, 'Sehore')

def Vidisha(request):
    return common(request, BhopalData, 'Vidisha')


#division2
def Morena(request):
    return common(request, ChambalData, 'Morena')

def Sheopur(request):
    return common(request, ChambalData, 'Sheopur')

def Bhind(request):
    return common(request, ChambalData, 'Bhind')


#division3
def Gwalior(request):
     return common(request, GwaliorData, 'Gwalior')

def Ashoknagar(request):
    return common(request, GwaliorData, 'Ashoknagar')

def Shivpuri(request):
     return common(request, GwaliorData, 'Shivpuri')

def Datia(request):
    return common(request, GwaliorData, 'Datia')

def Guna(request):
     return common(request, GwaliorData, 'Guna')


#division4
def Alirajpur(request):
    return common(request, IndoreData, 'Alirajpur')

def Barwani(request):
    return common(request, IndoreData, 'Barwani')

def Burhanpur(request):
    return common(request, IndoreData, 'Burhanpur')

def Indore(request):
    return common(request, IndoreData, 'Indore')

def Dhar(request):
    return common(request, IndoreData, 'Dhar')

def Jhabua(request):
    return common(request, IndoreData, 'Jhabua')

def Khandwa(request):
    return common(request, IndoreData, 'Khandwa')

def Khargone(request):
    return common(request, IndoreData, 'Khargone')


#division5
def Balaghat(request):
    return common(request, JabalpurData, 'Balaghat')

def Chhindwara(request):
    return common(request, JabalpurData, 'Chhindwara')

def Katni(request):
    return common(request, JabalpurData, 'Katni')

def Jabalpur(request):
    return common(request, JabalpurData, 'Jabalpur')

def Mandla(request):
    return common(request, JabalpurData, 'Mandla')

def Narsinghpur(request):
    return common(request, JabalpurData, 'Narsinghpur')

def Seoni(request):
    return common(request, JabalpurData, 'Seoni')

def Dindori(request):
    return common(request, JabalpurData, 'Dindori')


#division6
def Betul(request):
    return common(request, NarmadapuramData, 'Betul')

def Harda(request):
    return common(request, NarmadapuramData, 'Harda')

def Hoshangabad(request):
    return common(request, NarmadapuramData, 'Hoshangabad')


#division7
def Rewa(request):
    return common(request, RewaData, 'Rewa')

def Satna(request):
    return common(request, RewaData, 'Satna')

def Sidhi(request):
    return common(request, RewaData, 'Sidhi')

def Singrauli(request):
    common(request, RewaData, 'Singrauli')

#division8
def Chhatarpur(request):
    return common(request, SagarData, 'Chhatarpur')

def Damoh(request):
    return common(request, SagarData, 'Damoh')

def Panna(request):
    return common(request, SagarData, 'Panna')

def Sagar(request):
    return common(request, SagarData, 'Sagar')

def Tikamgarh(request):
    return common(request, SagarData, 'Tikamgarh')

def Nirwari(request):
    return common(request, SagarData, 'Nirwari')

#division9
def Anuppur(request):
    return common(request, ShahdolData, 'Anuppur')

def Shahdol(request):
    return common(request, ShahdolData, 'Shahdol')

def Umaria(request):
    return common(request, ShahdolData, 'Umaria')

#division10
def AgarMalwa(request):
    return common(request, UjjainData, 'AgarMalwa')

def Dewas(request):
    return common(request, UjjainData, 'Dewas')

def Mandsaur(request):
    return common(request, UjjainData, 'Mandsaur')

def Ratlam(request):
    return common(request, UjjainData, 'Ratlam')

def Shajapur(request):
    return  common(request, UjjainData, 'Shajapur')

def Ujjain(request):
    return common(request, UjjainData, 'Ujjain')

def Neemuch(request):
    return common(request, UjjainData, 'Neemuch')


