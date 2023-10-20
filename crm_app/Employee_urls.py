from django.urls import path , include
from .EmployeeViews import *

urlpatterns = [
    
    # path('Dashboard/', TemplateView.as_view(template_name='Employee/Base/index2.html'), name='employee_dashboard'),
    path('Dashboard/', employee_dashboard.as_view(),name="employee_dashboard"),
    path('Login/', employee_login,name="employee_login"),
    
    path('AddLeads/', EmployeeEnquiryCreateView.as_view(),name="addemployee_leads"),
    path('AllLeads/', employee_leads,name="employee_leads"),
    path('emp_lead_enquiry_update/',emp_lead_enquiry_update,name="emp_lead_enquiry_update"),
    path('ViewEnquiryList/<int:id>',viewemployee_enqlist,name="viewemp_enqlist"),
    path('AcceptLeads/', employee_accept_leads,name="employee_accept_leads"),
    path('Employee/Uploaddocument/',upload_document,name="empuploaddocument"),
    path('Employee/download_document/<int:document_id>/', download_document, name='empdownload_document'),
    
    path('Employee/logout', employee_logout,name="employee_logout"),
    
    path('Employee/Employee/',add_employee,name="Employee_add_employee"),
    path('Employee/AllEmployee/',all_employee.as_view(),name="Employee_all_employee"),
    path('Employee/ViewEmployee/<int:employee_id>',view_employee.as_view(),name="Employee_view_employee"),
    path('Employee/Employe/Update/<int:pk>',employee_update,name="Employee_employee_update"),
    path('Employee/Employe/Update/Save',employee_update_save,name="Employee_employee_update_save"),
    
    path('Employee/AddAgent/',add_agent,name="Employee_add_agent"),
    path('Employee/AllAgent/',all_agent.as_view(),name="Employee_all_agent"),
    path('Employee/AgentStatus/Update/',agent_status_update,name="Employee_agent_status_update"),
    path('Employee/AgentUpdate/<int:id>',agent_update,name="empagent_update"),
    path('Employee/OutSourceAgentUpdate/<int:id>',outsourceagent_update,name="empoutsourceagent_update"),
    path('Employee/Agent/Agreement/<int:id>',agent_agreement,name="empagent_agreement"),
    path('Employee/Agent/Kyc/<int:id>',agent_kyc,name="empagent_kyc"),
    path('Employee/AllOutSourceAgent/',all_outsource_agent.as_view(),name="empall_outsource_agent"),
    path('Employee/OutsourceAgent/Agreement/<int:id>',outsourceagent_agreement,name="empoutsourceagent_agreement"),
    path('Employee/OutsourceAgent/KYC/<int:id>',outsource_kyc,name="empoutsourceagent_kyc"),
    
    path('Employee/MenuList/', MenuListView.as_view(), name='Employee_Menu_list'),
    path('Employee/AddMenu/', AddMenu.as_view(), name='Employee_add_menu'),
    path('Employee/EditMenu/<int:pk>/', EditMenuView.as_view(), name='Employee_edit_menu'),
    
    path('Employee/AddSuccessStories/', SuccessStoriesCreateView.as_view(), name='Employee_add_SuccessStories'),
    path('Employee/SuccessStoriesList/', SuccessStoriesListView.as_view(), name='Employee_SuccessStories_list'),
    path('Employee/SuccessStoriesEdit/<int:pk>', editSuccessStory.as_view(),name="Employee_editSuccessStory"),
    
    path('Employee/AddNews/', NewsCreateView.as_view(), name='Employee_add_News'),
    path('Employee/NewsList/', NewsListView.as_view(), name='Employee_News_list'),
    path('Employee/NewsEdit/<int:pk>', editNews.as_view(),name="Employee_editNews"),
    
    path('Employee/AddOfferBanner/', OfferBannerCreateView.as_view(), name='Employee_add_OfferBanner'),
    path('Employee/OfferBannerList/', OfferBannerListView.as_view(), name='Employee_OfferBanner_list'),
    path('Employee/OfferBannerEdit/<int:pk>', editOfferBanner.as_view(),name="Employee_editOfferBanner"),
    
    path('Employee/AddPackage/', PackageCreateView.as_view(), name='Employee_add_Package'),
    path('Employee/PackageList/', PackageListView.as_view(), name='Employee_Package_list'),
    path('Employee/PackageEdit/<int:pk>', editPackage.as_view(),name="Employee_editPackage"),
    
    path('Employee/AddFrontWebsiteEnquiry/', FrontWebsiteEnquiryCreateView.as_view(), name='Employee_add_FrontWebsiteEnquiry'),
    path('Employee/FrontWebsiteEnquiryList/', FrontWebsiteEnquiryListView.as_view(), name='Employee_FrontWebsiteEnquiry_list'),
    path('Employee/ViewFrontEnquiryList/<int:id>',view_frontenqlist,name="Employee_view_frontenqlist"),

    path('Employee/EnrolledApplication',enrolled_Application.as_view(),name="Employee_enroll_application"),
    path('Employee/Enrolled/AddNotes',enrolled_add_notes,name="Employee_enrolled_add_notes"),
    path('Employee/AssignAgent/',assign_agent,name="Employee_assign_agent"),
    path('Employee/AssignOutSourceAgent/',assign_outsourceagent,name="Employee_assign_outsourceagent"),
    path('Employee/assignEmployee/',assign_employee,name="Employee_assign_employee"),

    path('Employee/edit/Enrolled/Application/<int:id>',edit_enrolled_application,name="Employee_edit_enrolled_application"),
    path('Employee/Educaion/Summary/<int:id>',education_summary,name="Employee_education_summary"),
    path('Employee/Test/Score/<int:id>',test_score,name="Employee_test_score"),
    path('Employee/Test/Score/Edit/<int:id>',edit_test_score,name="Employee_edit_test_score"),
    path('Employee/Test/Score/Delete/<int:id>',delete_test_score,name="Employee_delete_test_score"),
    
    
    path('Employee/Background/Infromation/<int:id>',background_information,name="Employee_background_information"),


    path('Employee/Documents/<int:id>',documents,name="Employee_documents"),
    path('Employee/Create/Documents/<int:id>',create_documents,name="Employee_create_documents"),
    path('Employee/Timeline/<int:id>',timeline,name="Employee_timeline"),
    path('Employee/WorkExperience/<int:id>',workexperience,name="Employee_workexperience"),
    
    path('Employee/upload_to',upload_to,name="Employee_upload_to"),

    ############# visa cases ###################

    # path('Employee/ClientList',)
    path('Employee/ClientList',ClientList.as_view(),name="Employee_client_list"),
    path('Employee/UpdateCaseStatus/<int:id>',update_case_status,name="Employee_update_case_status"),


    
    # ------------------ Appointment ------------------- 

    path('Employee/ViewAppointment/<int:id>',view_appointment,name="Employee_view_appointment"),
    path('Employee/AddAppointment/<int:id>',add_appointment,name="Employee_add_appointment"),
    path('Employee/All/Appointment',all_appointment.as_view(),name="Employee_all_appointment"),


    # ---------------------- User Documents --------------- 

    path('Employee/ClientDocument',client_documents,name="Employee_client_documents"),

    path('Employee/LoginLogs',loginlog.as_view(),name="Employee_loginlog"),
    path('Employee/search_Loginlog',search_loginlog,name="Employee_search_loginlog"),
    
    path('Employee/AddDepartment/', DepartmentCreateView.as_view(), name='Employee_add_Department'),
    path('Employee/DepartmentList/', DepartmentListView.as_view(), name='Employee_Department_list'),
    path('Employee/DepartmentEdit/<int:pk>', editDepartment.as_view(),name="Employee_editDepartment"),


    path('Employee/ChangePassword',ChangePassword,name="Employee_ChangePassword"),
    
    path('Employee/handle_permissions/', handle_permissions, name='Employee_handle_permissions'),
    path('Employee/assign_permissions/', AssignRoleView, name='Employee_assign_permissions'),
    path('Employee/fetch_users/', fetch_users, name='Employee_fetch_users'),
    path('Employee/get_users_for_department/', get_users_for_department, name='Employee_get_users_for_department'),
    path('Employee/assignrolelist/', AssignRolelist,name="Employee_assignrolelist"),


    path('Employee/Addfaq/', FAQCreateView.as_view(),name="Employee_addfaq"),
    path('Employee/faqMaster/', FAQListView.as_view(),name="Employee_faqlist"),
    path('Employee/faqEdit/<int:pk>', FAQUpdateView.as_view(),name="Employee_edit_faq"),
    path('Employee/faq/delete/<int:id>/', delete_faq, name='Employee_delete_faq'),

    path('Employee/enquiryfollowup/', enquiryfollowupList.as_view(),name="Employee_enquiryfollowup"),
]