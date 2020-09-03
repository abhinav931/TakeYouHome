from django import forms

GENDER_CHOICES = (('male', 'Male'),
                  ('female', 'Female'),
                  ('others', 'Others'))
REASON_CHOICES = (('student', 'Student'),
                  ('worker', 'Worker'),
                  ('others', 'Others'))
class SavingDataForm(forms.Form):
    firstName = forms.CharField(max_length = 40,
                               widget = forms.TextInput(attrs = {
                                   'name':'firstname',
                                   'type':'text'
                               })) 
    
    lastName = forms.CharField(max_length = 40,
                               widget = forms.TextInput(attrs = {
                                   'name':'firstname',
                                   'type':'text'
                               }))
    
    genderPerson = forms.CharField(widget=forms.RadioSelect(choices=GENDER_CHOICES))
    
    aadhaarNo = forms.IntegerField(max_value = 999999999999,
                                   widget = forms.NumberInput(attrs = {
                                   'name':'aadhaarno',
                               }))
    
    contactNo = forms.IntegerField(widget = forms.NumberInput(attrs = {
                                   'name':'contactno',
                               }))
    
    emailId = forms.EmailField(widget = forms.EmailInput(attrs = {
                                   'name':'email',
                               }))
    
    reasonPerson = forms.ChoiceField(choices = REASON_CHOICES,
                                     widget = forms.Select(attrs = {
                                   'name':'reason',
                               }))
    checkfirstName = forms.CharField(max_length = 40,
                               widget = forms.TextInput(attrs = {
                                   'name':'checkfirstname',
                               })) 
    
    checklastName = forms.CharField(max_length = 40,
                               widget = forms.TextInput(attrs = {
                                   'name':'checklastname',
                               }))
    checkaadhaarNo = forms.IntegerField(widget = forms.NumberInput(attrs = {
                                   'name':'checkaadhaarno',
                               }))
    
    checkcontactNo = forms.IntegerField(widget = forms.NumberInput(attrs = {
                                   'name':'checkcontactno',
                               }))
    
    checkemailId = forms.EmailField(widget = forms.EmailInput(attrs = {
                                   'name':'checkemailid',
                               }))
    
    curhouseNo = forms.IntegerField(widget = forms.NumberInput(attrs = {
                                   'name':'curhouseno',
                               }))
    
    curwardNo = forms.IntegerField(widget = forms.NumberInput(attrs = {
                                   'name':'curwardno',
                               }))
    
    curpinCode = forms.IntegerField(widget = forms.TextInput(attrs = {
                                   'name':'curpincode',
                               }))
    
    curdistrict = forms.CharField(max_length = 40,
                               widget = forms.TextInput(attrs = {
                                   'name':'curdistrict',
                               }))
    
    curState = forms.CharField(max_length = 40,
                               widget = forms.TextInput(attrs = {
                                   'name':'curstate',
                               }))
    
    perhouseNo = forms.IntegerField(widget =forms.NumberInput(attrs = {
                                   'name':'perhouseno',
                               }))
    
    perwardNo = forms.IntegerField(widget = forms.NumberInput(attrs = {
                                   'name':'perwardno',
                               }))
    
    perpinCode = forms.IntegerField(widget = forms.NumberInput(attrs = {
                                   'name':'perpincode',
                               }))
    
    perdistrict = forms.CharField(max_length = 40,
                               widget = forms.TextInput(attrs = {
                                   'name':'perdistrict',
                               }))
    
    perState = forms.CharField(max_length = 40,
                               widget = forms.TextInput(attrs = {
                                   'name':'perstate',
                               }))
    
    comments = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20, 'id':'comment', 'name':'comments'}))
                                                      

class HelpDataForm(forms.Form):
    helpdata = forms.CharField(widget=forms.Textarea(attrs={"rows":10, "cols":60}))
    
class DownloadForm(forms.Form):
    district = forms.CharField(max_length = 40,
                               widget = forms.TextInput(attrs = {
                                   'name':'districtdownload',
                                   'placeholder':'District Name',
                                   
                               }))