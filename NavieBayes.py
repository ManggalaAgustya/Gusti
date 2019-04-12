import csv
import random
import math


with open('TrainsetTugas1ML.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    TrainSet = []
    Id = []
    age = []
    workclass = []
    education = []
    marital_status = []
    occupation = []
    relationship = []
    hours_per_week = []
    income = []
    Yes = []
    No = []

    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            age.append([row[1],row[8]])
            workclass.append([row[2],row[8]])
            education.append([row[3],row[8]])
            marital_status.append([row[4],row[8]])
            occupation.append([row[5], row[8]])
            relationship.append([row[6], row[8]])
            hours_per_week.append([row[7], row[8]])
            income.append((row[8], row[8]))

with open('TestsetTugas1ML.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    TestSet = []

    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            TestSet.append([str(row[1]),str(row[2]),str(row[3]), str(row[4]), str(row[5]),str(row[6]), str(row[7])])

Income_X_morethan50 = 0
Income_X_lessthan50 = 0
Income_Y_morethan50 = 0
Income_Y_lessthan50 = 0
Income_Z_morethan50 = 0
Income_Z_lessthan50 = 0

for P in range(0,len(age)):
    if age[P][0] == 'young' and age[P][1] == '>50K':
        Income_X_morethan50 = Income_X_morethan50 + 1
    elif age[P][0] == 'young' and age[P][1] == '<=50K':
        Income_X_lessthan50 = Income_X_lessthan50 + 1
    if age[P][0] == 'adult' and age[P][1] == '>50K':
        Income_Y_morethan50 = Income_Y_morethan50 + 1
    elif age[P][0] == 'adult' and age[P][1] == '<=50K':
        Income_Y_lessthan50 = Income_Y_lessthan50 + 1
    if age[P][0] == 'old' and age[P][1] == '>50K':
        Income_Z_morethan50 = Income_Z_morethan50 + 1
    elif age[P][0] == 'old' and age[P][1] == '<=50K':
        Income_Z_lessthan50 = Income_Z_lessthan50 + 1

Income_morethan50 = 0
Income_lessthan50 = 0

for P in range(0,len(age)):
    if age[P][1] == '>50K':
        Income_morethan50 = Income_morethan50 + 1
    elif age[P][1] == '<=50K':
        Income_lessthan50 = Income_lessthan50 + 1

Income_YoungMore = Income_X_morethan50/Income_morethan50
Income_YoungLess = Income_X_lessthan50/Income_lessthan50
Income_AdultMore = Income_Y_morethan50/Income_morethan50
Income_AdultLess = Income_Y_lessthan50/Income_lessthan50
Income_OldMore = Income_Z_morethan50/Income_morethan50
Income_OldLess = Income_Z_lessthan50/Income_lessthan50

PrivateMore = 0
PrivateLess = 0
Local_govMore = 0
Local_govLess = 0
Self_emp_not_incMore = 0
Self_emp_not_incLess = 0

for P in range(0,len(workclass)):
    if workclass[P][0] == 'Private' and workclass[P][1] == '>50K':
        PrivateMore = PrivateMore + 1
    elif workclass[P][0] == 'Private' and workclass[P][1] == '<=50K':
        PrivateLess = PrivateLess + 1
    if workclass[P][0] == 'Local-gov' and workclass[P][1] == '>50K':
        Local_govMore = Local_govMore + 1
    elif workclass[P][0] == 'Local-gov' and workclass[P][1] == '<=50K':
        Local_govLess = Local_govLess + 1
    if workclass[P][0] == 'Self-emp-not-inc' and workclass[P][1] == '>50K':
        Self_emp_not_incMore = Self_emp_not_incMore + 1
    elif workclass[P][0] == 'Self-emp-not-inc' and workclass[P][1] == '<=50K':
        Self_emp_not_incLess = Self_emp_not_incLess + 1

Income_PrivateMore = PrivateMore/Income_morethan50
Income_Privateless = PrivateLess/Income_lessthan50
Income_Local_govMore = Local_govMore/Income_morethan50
Income_Local_govLess = Local_govLess/Income_lessthan50
Income_Self_emp_not_incMore = Self_emp_not_incMore/Income_morethan50
Income_Self_emp_not_incless = Self_emp_not_incLess/Income_lessthan50

Some_CollegeMore = 0
Some_CollegeLess = 0
BachelorsMore = 0
BachelorsLess = 0
HS_gradMore = 0
HS_gradLess = 0

for P in range(0,len(education)):
    if education[P][0] == 'Some-college' and education[P][1] == '>50K':
        Some_CollegeMore = Some_CollegeMore + 1
    elif education[P][0] == 'Some-college' and education[P][1] == '<=50K':
        Some_CollegeLess = Some_CollegeLess + 1
    if education[P][0] == 'Bachelors' and education[P][1] == '>50K':
        BachelorsMore = BachelorsMore + 1
    elif education[P][0] == 'Bachelors' and education[P][1] == '<=50K':
        BachelorsLess = BachelorsLess + 1
    if education[P][0] == 'HS-grad' and education[P][1] == '>50K':
        HS_gradMore = HS_gradMore + 1
    elif education[P][0] == 'HS-grad' and education[P][1] == '<=50K':
        HS_gradLess = HS_gradLess + 1

Income_Some_CollegeMore = Some_CollegeMore/Income_morethan50
Income_Some_CollegeLess = Some_CollegeLess/Income_lessthan50
Income_BachelorsMore = BachelorsMore/Income_morethan50
Income_BachelorsLess = BachelorsLess/Income_lessthan50
Income_HS_gradMore = HS_gradMore/Income_morethan50
Income_HS_gradLess = HS_gradLess/Income_lessthan50


Married_CivSpouseMore = 0
Married_CivSpouseLess = 0
Never_MarriedMore = 0
Never_MarriedLess = 0
DivorcedMore = 0
DivorcedLess = 0

for P in range(0,len(marital_status)):
    if marital_status[P][0] == 'Married-civ-spouse' and marital_status[P][1] == '>50K':
        Married_CivSpouseMore = Married_CivSpouseMore + 1
    elif marital_status[P][0] == 'Married-civ-spouse' and marital_status[P][1] == '<=50K':
        Married_CivSpouseLess = Married_CivSpouseLess + 1
    if marital_status[P][0] == 'Never-married' and marital_status[P][1] == '>50K':
        Never_MarriedMore = Never_MarriedMore + 1
    elif marital_status[P][0] == 'Never-married' and marital_status[P][1] == '<=50K':
        Never_MarriedLess = Never_MarriedLess + 1
    if marital_status[P][0] == 'Divorced' and marital_status[P][1] == '>50K':
        DivorcedMore = DivorcedMore + 1
    elif marital_status[P][0] == 'Divorced' and marital_status[P][1] == '<=50K':
        DivorcedLess = DivorcedLess + 1

Income_Married_CivSpouseMore = Married_CivSpouseMore/Income_morethan50
Income_Married_CivSpouseLess = Married_CivSpouseLess/Income_lessthan50
Income_Never_MarriedMore = Never_MarriedMore/Income_morethan50
Income_Never_MarriedLess = Never_MarriedLess/Income_lessthan50
Income_DivorcedMore = DivorcedMore/Income_morethan50
Income_DivorcedLess = DivorcedLess/Income_lessthan50

Prof_SpecialityMore = 0
Prof_SpecialityLess = 0
Craft_RepairMore = 0
Craft_RepairLess = 0
Exec_ManagerialMore = 0
Exec_ManagerialLess = 0

for P in range(0,len(occupation)):
    if occupation[P][0] == 'Prof-specialty' and occupation[P][1] == '>50K':
        Prof_SpecialityMore = Prof_SpecialityMore + 1
    elif occupation[P][0] == 'Prof-specialty' and occupation[P][1] == '<=50K':
        Prof_SpecialityLess = Prof_SpecialityLess + 1
    if occupation[P][0] == 'Craft-repair' and occupation[P][1] == '>50K':
        Craft_RepairMore = Craft_RepairLess + 1
    elif occupation[P][0] == 'Craft-repair' and occupation[P][1] == '<=50K':
        Craft_RepairLess = Craft_RepairLess + 1
    if occupation[P][0] == 'Exec-managerial' and occupation[P][1] == '>50K':
        Exec_ManagerialMore = Exec_ManagerialMore + 1
    elif occupation[P][0] == 'Exec-managerial' and occupation[P][1] == '<=50K':
        Exec_ManagerialLess = Exec_ManagerialLess + 1

Income_Prof_SpecialityMore = Prof_SpecialityMore/Income_morethan50
Income_Prof_SpecialityLess = Prof_SpecialityLess/Income_lessthan50
Income_Craft_RepairMore = Craft_RepairMore/Income_morethan50
Income_Craft_RepairLess = Craft_RepairLess/Income_lessthan50
Income_Exec_ManagerialMore = Exec_ManagerialMore/Income_morethan50
Income_Exex_ManagerialLess = Exec_ManagerialLess/Income_lessthan50

HusbandMore = 0
HusbandLess = 0
Not_In_FamilyMore = 0
Not_In_FamilyLess = 0
Own_ChildMore = 0
Own_ChildLess = 0

for P in range(0,len(relationship)):
    if relationship[P][0] == 'Husband' and relationship[P][1] == '>50K':
        HusbandMore = HusbandMore + 1
    elif relationship[P][0] == 'Husband' and relationship[P][1] == '<=50K':
        HusbandLess = HusbandLess + 1
    if relationship[P][0] == 'Not-in-family' and relationship[P][1] == '>50K':
        Not_In_FamilyMore = Not_In_FamilyMore + 1
    elif relationship[P][0] == 'Not-in_family' and relationship[P][1] == '<=50K':
        Not_In_FamilyLess = Not_In_FamilyLess + 1
    if relationship[P][0] == 'Own-child' and relationship[P][1] == '>50K':
        Own_ChildMore = Own_ChildMore + 1
    elif relationship[P][0] == 'Own-child' and relationship[P][1] == '<=50K':
        Own_ChildLess = Own_ChildLess + 1

Income_HusbandMore = HusbandMore/Income_morethan50
Income_HusbandLess = HusbandLess/Income_lessthan50
Income_Not_In_FamilyMore = Not_In_FamilyMore/Income_morethan50
Income_Not_In_FamilyLess = Not_In_FamilyLess/Income_lessthan50
Income_Own_ChildMore = Own_ChildMore/Income_morethan50
Income_Own_ChildLess = Own_ChildLess/Income_lessthan50

NormalMore = 0
NormalLess = 0
LowMore = 0
LowLess = 0
ManyMore = 0
ManyLess = 0

for P in range(0,len(hours_per_week)):
    if hours_per_week[P][0] == 'normal' and hours_per_week[P][1] == '>50K':
        NormalMore = NormalMore + 1
    elif hours_per_week[P][0] == 'normal' and hours_per_week[P][1] == '<=50K':
        NormalLess = NormalLess + 1
    if hours_per_week[P][0] == 'low' and hours_per_week[P][1] == '>50K':
        LowMore = LowMore + 1
    elif hours_per_week[P][0] == 'low' and hours_per_week[P][1] == '<=50K':
        LowLess = LowLess + 1
    if hours_per_week[P][0] == 'many' and hours_per_week[P][1] == '>50K':
        ManyMore = ManyMore + 1
    elif hours_per_week[P][0] == 'many' and hours_per_week[P][1] == '<=50K':
        ManyLess = ManyLess + 1

Income_NormalMore = NormalMore/Income_morethan50
Income_NormalLess = NormalLess/Income_lessthan50
Income_LowMore = LowMore/Income_morethan50
Income_LowLess = LowLess/Income_lessthan50
Income_ManyMore = ManyMore/Income_morethan50
Income_ManyLess = ManyLess/Income_lessthan50

def getPredictions(data, TestsetTugas1ML):
    predictions = []
    for P in range(len(TestsetTugas1ML)):
        result = predict(data, TestsetTugas1ML[P])
        predictions.append(result)
    return predictions

with open('TebakanTugas1.csv', 'w', newline="") as new_file:
    csv_writer = csv.writer(new_file,delimiter=' ')
    for P in range(0, len(TestSet)):
        if TestSet[P][0] == 'young':
            Yes = Income_X_morethan50 * 1
            No = Income_X_lessthan50 * 1
        elif TestSet[P][0] == 'adult':
            Yes = Income_Y_morethan50 * 1
            No = Income_Y_lessthan50 * 1
        elif TestSet[P][0] == 'old':
            Yes = Income_Z_morethan50 * 1
            No = Income_Z_lessthan50 * 1

        if TestSet[P][1] == 'Private':
            Yes = Yes * Income_PrivateMore
            No = No * Income_Privateless
        elif TestSet[P][1] == 'Local-gov':
            Yes = Yes * Income_Local_govMore
            No = No * Income_Local_govLess
        elif TestSet[P][1] == 'Self-emp-not-inc':
            Yes = Yes * Income_Self_emp_not_incMore
            No = No * Income_Self_emp_not_incless

        if TestSet[P][2] == 'HS-grad':
            Yes = Yes * Income_HS_gradMore
            No = No * Income_HS_gradLess
        elif TestSet[P][2] == 'Bachelors':
            Yes = Yes * Income_BachelorsMore
            No = No * Income_BachelorsLess
        elif TestSet[P][2] == 'Some-college':
            Yes = Yes * Income_Some_CollegeMore
            No = No * Income_Some_CollegeLess

        if TestSet[P][3] == 'Married':
            Yes = Yes * Income_Married_CivSpouseMore
            No = No * Income_Married_CivSpouseLess
        elif TestSet[P][3] == 'Never-married':
            Yes = Yes * Income_Never_MarriedMore
            No = No * Income_Never_MarriedLess
        elif TestSet[P][3] == 'Divorced':
            Yes = Yes * Income_DivorcedMore
            No = No * Income_DivorcedLess

        if TestSet[P][4] == 'Prof-specialty':
            Yes = Yes * Income_Prof_SpecialityMore
            No = No * Income_Prof_SpecialityLess
        elif TestSet[P][4] == 'Craft-repair':
            Yes = Yes * Income_Craft_RepairMore
            No = No * Income_Craft_RepairLess
        elif TestSet[P][4] == 'Exec-managerial':
            Yes = Yes * Income_Exec_ManagerialMore
            No = No * Income_Exex_ManagerialLess

        if TestSet[P][5] == 'Husband':
            Yes = Yes * Income_HusbandMore
            No = No * Income_HusbandLess
        elif TestSet[P][5] == 'Not-in-family':
            Yes = Yes * Income_Not_In_FamilyMore
            No = No * Income_Not_In_FamilyLess
        elif TestSet[P][5] == 'Own-child':
            Yes = Yes * Income_Own_ChildMore
            No = No * Income_Own_ChildLess

        if TestSet[P][6] == 'low':
            Yes = Yes * Income_LowMore
            No = No * Income_LowLess
        elif TestSet[P][6] == 'normal':
            Yes = Yes * Income_NormalMore
            No = No * Income_NormalLess
        elif TestSet[P][6] == 'many':
            Yes = Yes * Income_ManyMore
            No = No * Income_ManyLess

        if Yes < No :
            Income = '<=50K'
        elif Yes > No :
            Income = '>50K'
        csv_writer.writerow(Income)

print("ResultSaved")
print("TebakanTugas1.csv")
