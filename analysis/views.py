from django.shortcuts import render
import pickle

from accounts.models import UserAccount
from initializer.models import visit
from labpost.models import TestItem
# Create your views here.

def analyze_liver_data(request):
    def replace(given_list, old_value, new_value):
        for ind, val in enumerate(given_list):
            if val == old_value:
                given_list[ind] = new_value

        return given_list

    attr_list = [
    'Total Billirubin',
    'Direct Bilirubin',
    'Alkaline Phosphotase',
    'Alamine_Aminotransferase',
    'Aspartate Aminotransferase',
    'Total_Protiens',
    'Albumin',
    'Albumin and Globulin_Ratio',
    ]

    attr_vals = {
    'Total Billirubin':None,
    'Direct Bilirubin':None,
    'Alkaline Phosphotase':None,
    'Alamine_Aminotransferase':None,
    'Aspartate Aminotransferase':None,
    'Total_Protiens':None,
    'Albumin':None,
    'Albumin and Globulin_Ratio':None,
    }



    load_model = pickle.load(open('final_model.sav','rb'))

    # test is a 1d array [age,gender,tb,db,alp,alt,ast,tp,alubumin,a/g]
    
    # here 55 is age of patient, 1 is sex 'Male' of patient, 14.1 = total bullirubin,  etc... Given in report 
    #Extract from required models
    test = []
    user = request.user
    age = user.get_age()
    print(age)
    if user.sex == 'male':
        sex = 1
    else:
        sex=0

    test.append(age)
    test.append(sex)

    visits = visit.objects.filter(user_id=user).order_by('-timestamp')

    print(visits)

    for visit_obj in visits:
        tests = TestItem.objects.filter(visit_id=visit_obj)

        for test_obj in tests:
            if test_obj.testName.testName in attr_list:
                if attr_vals[test_obj.testName.testName] is None:
                    attr_vals[test_obj.testName.testName] = test_obj.result

    for attr, value in attr_vals.items():
        if not value:
            return render(request,'analysis.html',{'result':'Not enough data'})        
        attr_list = replace(attr_list, attr, value)

    test = test + attr_list
    print(test)


    result = load_model.predict([test])
    


    # Display either Your are liver patient or you are not liver patient
    if(result[0]==1):
        return render(request,'analysis.html',{'result': 100})
   
    return render(request,'analysis.html',{'result':0})