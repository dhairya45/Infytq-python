"""
Care hospital wants to know the medical speciality visited by the maximum number of patients. Assume that the patient id of the patient along with the medical speciality visited by the patient is stored in a list. The details of the medical specialities are stored in a dictionary as follows:
{
"P":"Pediatrics",
"O":"Orthopedics",
"E":"ENT
} 

Write a function to find the medical speciality visited by the maximum number of patients and return the name of the speciality.
"""


def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    input=[0,0,0]
    for i in patient_medical_speciality_list:
        if i =='P' or i=='p':
            input[0]+=1
        elif i=='O' or i=='o':
            input[1]+=1
        elif i=='E' or i=='e':
            input[2]+=1
    if input[0] > input[1] and input[0]>input[2]:
        speciality=medical_speciality['P']
    elif input[1] > input[2] and input[1]>input[0]:
        speciality=medical_speciality['O']
    elif input[2] > input[1] and input[2]>input[0]:
        speciality=medical_speciality['E']
        

    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'O',302, 'O' ,305, 'E' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
