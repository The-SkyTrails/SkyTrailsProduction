
from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm,UsernameField


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))

class VisaCountryForm(forms.ModelForm):
    class Meta:
        model = VisaCountry
        fields = ['country', 'status']
    country = forms.CharField(label=("Country"),strip=False,widget=forms.TextInput(attrs={ 'class':'form-control'}))
    

class VisaCategoryForm(forms.ModelForm):
    class Meta:
        model = VisaCategory
        fields = ['visa_country_id', 'category','status','subcategory']
    visa_country_id = forms.ModelChoiceField(
        queryset=VisaCountry.objects.all(),
        
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    category = forms.CharField(label=("Category"),strip=False,widget=forms.TextInput(attrs={ 'class':'form-control'}))
    subcategory = forms.CharField(label=("SubCategory"),strip=False,widget=forms.TextInput(attrs={ 'class':'form-control'}))
   



class VisasubCategoryForm(forms.ModelForm):
    
    class Meta:
        model = VisaSubcategory
        fields = ['country_id','category_id','subcategory_name','estimate_amt','cgst','sgst','status','person']
        widgets = {'country_id':forms.Select(attrs={'class':'form-control'}),
                   'person':forms.Select(attrs={'class':'form-control selectpicker', 'multiple': 'multiple', 'data-style': 'form-control btn-default btn-outline'}),
                   'category_id':forms.Select(attrs={'class':'form-control'}),'subcategory_name':forms.Select(attrs={'class':'form-control'}),'estimate_amt':forms.NumberInput(attrs={'class':'form-control'}),'cgst':forms.NumberInput(attrs={'class':'form-control'}),'sgst':forms.NumberInput(attrs={'class':'form-control'})}
        # labels = {'country_id': 'Country','category_id':'Category','subcategory_name':'Subcategory','estimate_amt':'Estimated Amount(INR)'}
        labels = {
        'country_id': 'Country',
        'category_id': 'Category',
        'subcategory_name': 'Subcategory',
        'estimate_amt': 'Estimated Amount (INR)',
        'cgst': 'CGST (%)',
        'sgst': 'SGST (%)',
        'person':'User'
        
    }
        

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['document_name', 'document_category', 'status','document_size']
        
        widgets = {'document_name':forms.TextInput(attrs={'class':'form-control', 'Placeholder':'Document Name'}),'document_category':forms.Select(attrs={'class':'form-control'}),'document_size':forms.NumberInput(attrs={'class':'form-control','placeholder':'Document Size'})}        

class courieraddressForm(forms.ModelForm):
    class Meta:
        model = CourierAddress
        fields = ['company_name','address','landmark','city','state','zipcode','docker_no'
                  ,'sender_no','receiver_no','courier_no','receiver_address','sender_address'
                  ,'status']
        widgets = {'company_name':forms.TextInput(attrs={'class':'form-control'}),
                   'address':forms.TextInput(attrs={'class':'form-control'}),
                   'landmark':forms.TextInput(attrs={'class':'form-control'}),
                   'city':forms.TextInput(attrs={'class':'form-control'}),
                   'state':forms.TextInput(attrs={'class':'form-control'}),
                   'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
                   'docker_no':forms.TextInput(attrs={'class':'form-control'}),
                   'sender_no':forms.TextInput(attrs={'class':'form-control'}),
                   'receiver_no':forms.TextInput(attrs={'class':'form-control'}),
                   'courier_no':forms.TextInput(attrs={'class':'form-control'}),
                   'receiver_address':forms.TextInput(attrs={'class':'form-control'}),
                   'sender_address':forms.TextInput(attrs={'class':'form-control'}),
                   'status':forms.Select(attrs={'class':'form-control'})}
    
        
class CaseStatusForm(forms.ModelForm):
    class Meta:
        model = CaseStatus
        fields = ['case_status','status']
        widgets = {'case_status':forms.TextInput(attrs={'class':'form-control'})}
    
        
class FollowUpPaymentStatusForm(forms.ModelForm):
    class Meta:
        model = followuppayment_status
        fields = ['followup_status','status']
        widgets = {'followup_status':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter follow-up status'})}
    
        
class FollowUpStatusForm(forms.ModelForm):
    class Meta:
        model = followup_status
        fields = ['followup_status','status']
        widgets = {'followup_status':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter follow-up status'})}
    
        
class FollowUpTypeForm(forms.ModelForm):
    class Meta:
        model = followupType
        fields = ['followup_type','status']
        widgets = {'followup_type':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter followUp Type'})}
    
class DocumentCategoryForm(forms.ModelForm):
    class Meta:
        model = DocumentCategory
        fields = ['Document_category','status']
        widgets = {'Document_category':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Document Category'})}
    
    
class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ['currency_name','currency_rate','status']
        widgets = {'currency_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Currency Name'}),'currency_rate':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Currency Rate'})}
        
class SuccessStoriesForm(forms.ModelForm):
    class Meta:
        model = SuccessStories
        fields = ['title','description','url','image']
        widgets = {'title':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Title Name'}),'description':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Description'}),'url':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter URL'}),'image':forms.FileInput(attrs={'class':'form-control'})}
        
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title','description','publish_date','expiry_date','news_type','status']
        widgets = {'title':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Title Name'}),'description':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Description'}),'publish_date':forms.DateInput(attrs={'class':'form-control','placeholder': 'Enter Publish Date'}),'expiry_date':forms.DateInput(attrs={'class':'form-control','placeholder':'Enter Expiry Date'}),'news_type':forms.Select(attrs={'class':'form-control'})}
        
        
class OfferBannerForm(forms.ModelForm):
    class Meta:
        model = OfferBanner
        fields = ['title','url','fromdate','todate','image','status']
        widgets = {'title':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Title Name'}),'url':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter URL'}),'fromdate':forms.DateInput(attrs={'class':'form-control','placeholder': 'Enter Publish Date','type':'date'}),'todate':forms.DateInput(attrs={'class':'form-control','placeholder':'Enter Expiry Date','type':'date'}),'image':forms.FileInput(attrs={'class':'form-control'})}
        
        
class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['visa_country','visa_category','visa_subcategory','title','description','number_of_visa','amount','advance_amount','file_charges','package_expiry_date','assign_to_group']
        widgets = {'visa_country':forms.Select(attrs={'class':'form-control'}),'visa_category':forms.Select(attrs={'class':'form-control'}),'visa_subcategory':forms.Select(attrs={'class':'form-control'}),'title':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Title Name'}),'description':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Description'}),
                   'number_of_visa':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Number of Visa'}),'amount':forms.NumberInput(attrs={'class':'form-control','placeholder': 'Enter Amount'}),'advance_amount':forms.NumberInput(attrs={'class':'form-control','placeholder': 'Enter Advance Amount'}),
                   'file_charges':forms.NumberInput(attrs={'class':'form-control','placeholder': 'Enter File Charges'}),'package_expiry_date':forms.DateInput(attrs={'class':'form-control','placeholder': 'Enter Package Expiry Date','type':'date'}),'assign_to_group':forms.Select(attrs={'class':'form-control'}),}




class PackageImageForm(forms.ModelForm):
    class Meta:
        model = PackageImage
        fields = ['image']
        # widgets = {'image': forms.ClearableFileInput(attrs={'multiple': True})}

class CaseCategoryDocumentForm(forms.ModelForm):
    class Meta:
        model = CaseCategoryDocument
        fields = ['country', 'category', 'subcategory', 'document']

        widgets = {
            'country': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'subcategory': forms.Select(attrs={'class': 'form-control'}),
            'document': forms.CheckboxSelectMultiple(),  
        }

    # Queryset for the document field
        document = forms.ModelMultipleChoiceField(
            queryset=Document.objects.all(),
            required=False,  
        )

    # Include the boolean fields for document options as form fields
    # digitalphoto = forms.BooleanField(required=False)
    # passportback = forms.BooleanField(required=False)
    # passportfront = forms.BooleanField(required=False)
    # pancard = forms.BooleanField(required=False)
    # adharcard = forms.BooleanField(required=False)
    # gapmonth = forms.BooleanField(required=False)
    # experience_letter = forms.BooleanField(required=False)
    # gapyear = forms.BooleanField(required=False)
    # masterscertificate = forms.BooleanField(required=False)
    # form16 = forms.BooleanField(required=False)
    # spouse = forms.BooleanField(required=False)
    # itr = forms.BooleanField(required=False)
    # spouseworking = forms.BooleanField(required=False)
    # spouseenglish = forms.BooleanField(required=False)
    # bankbalance = forms.BooleanField(required=False)
    # itr3years = forms.BooleanField(required=False)
    # evidenceofsalary = forms.BooleanField(required=False)
    # assetsdocument = forms.BooleanField(required=False)
    # marriagecertificate = forms.BooleanField(required=False)
    # spousequalification = forms.BooleanField(required=False)
    # bankbalance6month = forms.BooleanField(required=False)
    # workexperience = forms.BooleanField(required=False)
    # applicantsbankbalance = forms.BooleanField(required=False)
    # parentbankbalance = forms.BooleanField(required=False)
    # graduation_diploma = forms.BooleanField(required=False)
    # parentsid = forms.BooleanField(required=False)
    # parentsitr = forms.BooleanField(required=False)
    # englishlanguage = forms.BooleanField(required=False)
    # studentsbank = forms.BooleanField(required=False)
    # parentbank = forms.BooleanField(required=False)
    # parentdocument = forms.BooleanField(required=False)
    # passport = forms.BooleanField(required=False)
    # idproof = forms.BooleanField(required=False)
    # certificate12th = forms.BooleanField(required=False)
    # certificate10th = forms.BooleanField(required=False)
    
class FrontWebsiteEnquiryForm(forms.ModelForm):
    class Meta:
        model = FrontWebsiteEnquiry      
        fields = ['name','email','phone','country_name','category_name','message','image','appointment_date']   
        # exclude = ['last_updated_by','last_updated_on','type']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Id'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'country_name': forms.Select(attrs={'class': 'form-control'}),
            'category_name': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Let us know your enquiry'}),
            'image':forms.FileInput(attrs={'class':'form-control'}), 
            'appointment_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select Appointment Date', 'type': 'date'}), 
        }
        
        
class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['email','contact','Salutation','FirstName','LastName','Dob','Gender','Country','passport_no','Visa_country','Visa_category'
                  ,'Visa_subcategory','Visa_type','Package','Source','Reference']
        widgets = {
            'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email Id'}),
            'contact' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Contact No'}),
            'Salutation' : forms.Select(attrs={'class':'form-control'}),
            'FirstName' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
            'LastName' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),
            'Dob' : forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'Gender' : forms.Select(attrs={'class':'form-control'}),
            'Country': forms.Select(attrs={'class':'form-control'}),
            'Visa_country' : forms.Select(attrs={'class':'form-control'}),
            'Visa_category' : forms.Select(attrs={'class':'form-control'}),
            'Visa_subcategory' : forms.Select(attrs={'class':'form-control'}),
            'Visa_type' : forms.Select(attrs={'class':'form-control'}),
            'Package' : forms.Select(attrs={'class':'form-control'}),
            'Source' : forms.Select(attrs={'class':'form-control','placeholder':'Enter Source Name'}),
            'Reference' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Reference Name'}),
            'passport_no' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Passport Number'}),
        }
        
        
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name','status']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Role Name'}),
            
        }



class EmployeeForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, label="First Name")
    class Meta:
        model = Employee
        
        fields = ['users','department','branch','group','contact_no','country','state','City','Address','zipcode','status','file','first_name']

   
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['users'].widget = forms.HiddenInput()  # Hide the users field
            self.fields['department'].widget.attrs['onchange'] = 'loadUsers()'

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['group_name','group_member']
        widgets = {
                'group_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Group Name'}),
                
            }
    group_member = forms.ModelMultipleChoiceField(
        queryset=CustomUser.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )     
    
# class CustomSelectWidget(forms.Widget):
#     def render(self, name, value, attrs=None, choices=()):
#         html = f"""
#             <div class="form-group">
#                 <label class="control-label mb-10">{name}</label>
#                 <select class="selectpicker" multiple data-style="form-control btn-default btn-outline" name="{name}">
#         """

#         for choice in choices:
#             selected = 'selected' if choice[0] in value else ''
#             html += f'<option value="{choice[0]}" {selected}>{choice[1]}</option>'

#         html += """
#                 </select>
#             </div>
#         """

#         return html
    
class AssignRole(forms.ModelForm):
    class Meta:
        model = AssignRoles
        fields = ['menu_name','department','employee']
        widgets = {
            'employee':forms.Select(attrs={'class':'form-control'}),
            # 'employee':forms.Select(attrs={'class':'form-control','multiple': 'multiple','data-style': 'form-control'}),
            'menu_name': forms.Select(attrs={'class': 'form-control selectpicker', 'multiple': 'multiple', 'data-style': 'form-control btn-default btn-outline'}),
            'department': forms.Select(attrs={'class': 'form-control', 'onchange': 'console.log("Department changed to: " + this.value);'}),

        }

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name']
        
        widgets = {'name':forms.Select(attrs={'class':'form-control', 'Placeholder':'Document Name'})}        
        

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['branch_name','status','branch_source']
        widgets = {'branch_name':forms.TextInput(attrs={'class':'form-control'}),
                   'branch_source':forms.Select(attrs={'class':'form-control'}),}
        
        
class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question','answer']
        widgets = {'question':forms.Textarea(attrs={'class':'form-control'}),
            'answer':forms.Textarea(attrs={'class':'form-control'})
        }


class FollowUpForm(forms.ModelForm):
    class Meta:
        model = FollowUp
        fields = ['title', 'description', 'follow_up_status', 'priority', 'calendar', 'time', 'remark']
        
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Title'}),
            'description' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Description'}),
            'follow_up_status' : forms.Select(attrs={'class':'form-control'}),
            'calendar': forms.DateInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Date','type':'date'}),
            'time': forms.TimeInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Time','type':'time'}),
            'remark' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Remark'}),
        }