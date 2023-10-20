

from django.urls import path , include
from .AdminViews import *


urlpatterns = [
    
    path('logout_user', logout_user,name="adminlogout"),
    path("Admindashboard/", TravelDashboard.as_view() , name='travel_dashboards'),

    path('Employee/',add_employee,name="add_employee"),
    path('AllEmployee/',all_employee.as_view(),name="all_employee"),
    path('ViewEmployee/<int:employee_id>',view_employee.as_view(),name="view_employee"),
    path('Employe/Update/<int:pk>',employee_update,name="employee_update"),
    path('Employe/Update/Save',employee_update_save,name="employee_update_save"),
    

    path('AddAgent/',add_agent,name="add_agent"),
    path('AllAgent/',all_agent.as_view(),name="all_agent"),

    path('AgentUpdate/<int:id>',agent_update,name="agent_update"),
    path('OutSourceAgentUpdate/<int:id>',outsourceagent_update,name="outsourceagent_update"),
    path('Agent/Agreement/<int:id>',agent_agreement,name="agent_agreement"),
    path('Agent/Kyc/<int:id>',agent_kyc,name="agent_kyc"),
    path('AllOutSourceAgent/',all_outsource_agent.as_view(),name="all_outsource_agent"),
    path('OutsourceAgent/Agreement/<int:id>',outsourceagent_agreement,name="outsourceagent_agreement"),
    path('OutsourceAgent/KYC/<int:id>',outsource_kyc,name="outsourceagent_kyc"),
    
    
    path('AgentStatus/Update/',agent_status_update,name="agent_status_update"),
    
    path('AddCountry/', add_country,name="add_country"),
    path('VisaCountryList/', visa_countrylist,name="visa_countrylist"),
    path('VisaCountryEdit/<int:id>', visa_countryedit,name="visa_countryedit"),

    path('AddCategory/', add_category,name="add_category"),
    path('CategoryList/', category_list,name="category_list"),
    path('VisaCategoryEdit/<int:id>', visa_category_edit,name="visa_category_edit"),

    path('AddSubCategory/', add_subcategory,name="add_subcategory"),
    path('SubCategoryList/', subcategory_list,name="subcategory_list"),
    path('SubCategoryEdit/<int:id>', visa_subcategory_edit,name="visa_subcategory_edit"),

    path('AddDocument/', DocumentCreateView.as_view(), name='add_document'),
    path('DocumentList/', DocumentListView.as_view(), name='document_list'),
    path('DocumentModal/', document_modal_view, name='document_modal'),
    path('UpdateDocument/<int:pk>/', DocumentUpdateView.as_view(), name='update_document'),

    path('MenuList/', MenuListView.as_view(), name='Menu_list'),
    path('AddMenu/', AddMenu.as_view(), name='add_menu'),
    path('EditMenu/<int:pk>/', EditMenuView.as_view(), name='edit_menu'),
    
    path('AddCourierAddress/', addcourieraddress.as_view(),name="addcourieraddress"),
    path('ViewCourierAddress/', viewcourieraddress_list,name="viewcourieraddress_list"),
    path('CourierAddressEdit/<int:id>', courieraddressEdit,name="courieraddressEdit"),

    path('AddCaseStatus/', addcasestatus.as_view(),name="addcasestatus"),
    path('CaseStatusMaster/', casestatuslist,name="casestatuslist"),
    path('CaseStatusEdit/<int:pk>', casestatusEdit.as_view(),name="casestatusEdit"),

    path('FollowUpPaymentStatus/', followupPaymentstatus,name="followuppaymentstatus"),
    path('AddFollowUpPaymentStatus/', addfollowupPaymentstatus.as_view(),name="addfollowupPaymentstatus"),
    path('FollowUpPaymentStatusEdit/<int:pk>', followupPaymentedit.as_view(),name="followupPaymentedit"),

    path('FollowUpStatus/', followupstatus.as_view(),name="followupstatus"),
    path('AddFollowUpStatus/', addfollowupstatus.as_view(),name="addfollowupstatus"),
    path('FollowUpEdit/<int:pk>', followupEdit.as_view(),name="followupEdit"),



    path('FollowUpType/', followuptype,name="followuptype"),
    path('AddFollowUpType/', addfollowuptype.as_view(),name="addfollowuptype"),
    path('FollowUpTypeEdit/<int:pk>', followuptype_edit.as_view(),name="followuptype_edit"),


    path('DocumentCategoryList/', DocumentCategoryList,name="DocumentCategorylist"),
    path('AddDocumentCategory/', addDocument_cat.as_view(),name="add_document_category"),
    path('DocumentCategoryEdit/<int:pk>', editDocument_cat.as_view(),name="editDocument_cat"),


    path('CurrencyMaster/', currencyMaster,name="currencyMaster"),
    path('AddCurrency/', addcurrency.as_view(),name="addcurrency"),
    path('CurrencyEdit/<int:pk>', editcurrency.as_view(),name="editcurrency"),

    path('AddEmployee/', add_employee,name="add_employee"),
    # path('view_admin/', view_admin,name="view_admin"),
    
    path('AddSuccessStories/', SuccessStoriesCreateView.as_view(), name='add_SuccessStories'),
    path('SuccessStoriesList/', SuccessStoriesListView.as_view(), name='SuccessStories_list'),
    path('SuccessStoriesEdit/<int:pk>', editSuccessStory.as_view(),name="editSuccessStory"),
    
    path('AddNews/', NewsCreateView.as_view(), name='add_News'),
    path('NewsList/', NewsListView.as_view(), name='News_list'),
    path('NewsEdit/<int:pk>', editNews.as_view(),name="editNews"),
    
    path('AddOfferBanner/', OfferBannerCreateView.as_view(), name='add_OfferBanner'),
    path('OfferBannerList/', OfferBannerListView.as_view(), name='OfferBanner_list'),
    path('OfferBannerEdit/<int:pk>', editOfferBanner.as_view(),name="editOfferBanner"),
    
    path('AddPackage/', PackageCreateView.as_view(), name='add_Package'),
    path('PackageList/', PackageListView.as_view(), name='Package_list'),
    path('PackageEdit/<int:pk>', editPackage.as_view(),name="editPackage"),
    
    path('AddCaseCategoryDocument/', CaseCategoryDocumentCreateView.as_view(), name='add_CaseCategoryDocument'),
    # path('AddCaseCategoryDocument/', CaseCategoryDocumentCreateView.as_view(), name='add_CaseCategoryDocument'),
    path('CaseCategoryDocumentList/', CaseCategoryDocumentListView.as_view(), name='CaseCategoryDocument_list'),
    path('CaseCategoryDocumentEdit/<int:pk>', editCaseCategoryDocument.as_view(),name="editCaseCategoryDocument"),
    
    path('AddFrontWebsiteEnquiry/', FrontWebsiteEnquiryCreateView.as_view(), name='add_FrontWebsiteEnquiry'),
    path('FrontWebsiteEnquiryList/', FrontWebsiteEnquiryListView.as_view(), name='FrontWebsiteEnquiry_list'),
    path('ViewFrontEnquiryList/<int:id>',view_frontenqlist,name="view_frontenqlist"),

    path('AddEnquiry/', EnquiryCreateView.as_view(), name='add_enquiry'),
    path('EnquiryList/', EnquiryListView.as_view(), name='Enquiry_list'),
    path('ViewEnquiryList/<int:id>',view_enqlist,name="view_enqlist"),
    path('AddNotes/',add_notes,name="add_notes"),
    path('AssignEnquiry/',assign_enquiry,name="assign_enquiry"),
    path('lead_enquiry/',lead_enquiry,name="lead_enquiry"),
    path('Uploaddocument/',upload_document,name="uploaddocument"),
    path('download_document/<int:document_id>/', download_document, name='download_document'),


    path('EnrolledApplication',enrolled_Application.as_view(),name="enroll_application"),
    path('Enrolled/AddNotes',enrolled_add_notes,name="enrolled_add_notes"),
    path('AssignAgent/',assign_agent,name="assign_agent"),
    path('AssignOutSourceAgent/',assign_outsourceagent,name="assign_outsourceagent"),
    path('assignEmployee/',assign_employee,name="assign_employee"),

    path('edit/Enrolled/Application/<int:id>',edit_enrolled_application,name="edit_enrolled_application"),
    path('Educaion/Summary/<int:id>',education_summary,name="education_summary"),
    path('Test/Score/<int:id>',test_score,name="test_score"),
    path('Test/Score/Edit/<int:id>',edit_test_score,name="edit_test_score"),
    path('Test/Score/Delete/<int:id>',delete_test_score,name="delete_test_score"),
    
    
    path('Background/Infromation/<int:id>',background_information,name="background_information"),


    path('Documents/<int:id>',documents,name="documents"),
    path('Create/Documents/<int:id>',create_documents,name="create_documents"),
    path('Timeline/<int:id>',timeline,name="timeline"),
    path('WorkExperience/<int:id>',workexperience,name="workexperience"),
    
    path('upload_to',upload_to,name="upload_to"),

    ############# visa cases ###################

    # path('ClientList',)
    path('ClientList',ClientList.as_view(),name="client_list"),
    path('UpdateCaseStatus/<int:id>',update_case_status,name="update_case_status"),


    
    # ------------------ Appointment ------------------- 

    path('ViewAppointment/<int:id>',view_appointment,name="view_appointment"),
    path('AddAppointment/<int:id>',add_appointment,name="add_appointment"),
    path('All/Appointment',all_appointment.as_view(),name="all_appointment"),


    # ---------------------- User Documents --------------- 

    path('ClientDocument',client_documents,name="client_documents"),

    path('LoginLogs',loginlog.as_view(),name="loginlog"),
    path('search_Loginlog',search_loginlog,name="search_loginlog"),
    
    path('AddDepartment/', DepartmentCreateView.as_view(), name='add_Department'),
    path('DepartmentList/', DepartmentListView.as_view(), name='Department_list'),
    path('DepartmentEdit/<int:pk>', editDepartment.as_view(),name="editDepartment"),


    path('ChangePassword',ChangePassword,name="ChangePassword"),
    
    path('create_group/', CreateGroupView.as_view(), name='create_group'),
    path('GroupList/', GroupListView.as_view(), name='Group_list'),
    path('GroupEdit/<int:pk>', editGroup.as_view(),name="editgroup"),
    
    
    path('handle_permissions/', handle_permissions, name='handle_permissions'),
    # path('assign_permissions/', AssignRoleView.as_view(), name='assign_permissions'),
    path('assign_permissions/', AssignRoleView, name='assign_permissions'),
    path('fetch_users/', fetch_users, name='fetch_users'),
    path('get_users_for_department/', get_users_for_department, name='get_users_for_department'),
    path('assignrolelist/', AssignRolelist,name="assignrolelist"),
    path('AssignRole/Update/<int:pk>', AssignUpdateView,name="edit_assign_role"),
    path('AssignRole/Update/Save/', AssignUpdatesave,name="AssignUpdatesave"),
    
    path('Addbranch/', addbranch.as_view(),name="addbranch"),
    path('branchMaster/', branchlist,name="branchlist"),
    
    
    
    path('branch/delete/<int:id>/', delete_branch, name='delete_branch'),
    path('group/delete/<int:id>/', delete_group, name='delete_group'),
    path('role/delete/<int:id>/', delete_role, name='delete_role'),
    path('appointment/delete/<int:id>/', delete_appointment, name='delete_appointment'),
    path('casecategorydocument/delete/<int:id>/', delete_casecategorydocument, name='delete_casecategorydocument'),
    path('package/delete/<int:id>/', delete_package, name='delete_package'),
    path('offerbanner/delete/<int:id>/', delete_offerbanner, name='delete_offerbanner'),
    path('news/delete/<int:id>/', delete_news, name='delete_news'),
    path('successstories/delete/<int:id>/', delete_successstories, name='delete_successstories'),
    path('currency/delete/<int:id>/', delete_currency, name='delete_currency'),
    path('documentcategory/delete/<int:id>/', delete_documentcategory, name='delete_documentcategory'),
    path('followuptype/delete/<int:id>/', delete_followuptype, name='delete_followuptype'),
    path('followupstatus/delete/<int:id>/', delete_followupstatus, name='delete_followupstatus'),
    path('followuppayment/delete/<int:id>/', delete_followuppayment, name='delete_followuppayment'),
    path('casestatus/delete/<int:id>/', delete_casestatus, name='delete_casestatus'),
    path('courieraddress/delete/<int:id>/', delete_courieraddress, name='delete_courieraddress'),
    path('document/delete/<int:id>/', delete_document, name='delete_document'),
    path('subcategory/delete/<int:id>/', delete_subcategory, name='delete_subcategory'),
    path('category/delete/<int:id>/', delete_category, name='delete_category'),
    path('country/delete/<int:id>/', delete_country, name='delete_country'),

    path('import/Country',import_country,name="importcountry"),
    path('import/Employee',import_employee,name="import_employee"),
    path('import/Department',import_department,name="importdepartment"),
    path('import/Branch',import_branch,name="importbranch"),
    path('import/CaseStatus',import_casestatus,name="importcasestatus"),
    path('import/PaymentStatus',import_paymentstatus,name="importpaymentstatus"),
    
    
    path('Addfaq/', FAQCreateView.as_view(),name="addfaq"),
    path('faqMaster/', FAQListView.as_view(),name="faqlist"),
    path('faqEdit/<int:pk>', FAQUpdateView.as_view(),name="edit_faq"),
    path('faq/delete/<int:id>/', delete_faq, name='delete_faq'),

    path('enquiryfollowup/', enquiryfollowupList.as_view(),name="enquiryfollowup"),
    path('enquiryfollowup/Update/<int:pk>', EnquiryFollowupUpdate.as_view(),name="Updateenquiryfollowup"),
     path('followup/delete/<int:id>/', delete_followup, name='delete_followup'),
]

