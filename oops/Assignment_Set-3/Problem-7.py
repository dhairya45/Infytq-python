#lex_auth_012751886858420224260
"""
Care hospital management wants to calculate the charge of lab tests done by its patients.
Class Description:
LabTestRepository class:

list_of_hospital_lab_test_ids: Static list which contains the list of test ids of lab tests available in the hospital

list_of_lab_test_charge: Static list which contains the charge of the lab tests available in the hospital

The above two lists have one-to-one correspondence

get_test_charge(lab_test_id): Accept a lab test id and return the corresponding lab test charge. If lab test id is invalid, return -1

 

Patient class:

list_of_lab_test_ids: Instance variable which contains the list of test ids of lab tests done by the patient

calculate_lab_test_charge(): Calculate total charge of the lab tests done by the patient

Calculate total lab test charge based on test charge of each lab test done by the patient

If any lab test id provided by the patient is invalid, consider its charge to be 0

Initialize attribute, lab_test_charge with the total lab test charge

Note: Perform case sensitive string comparison  

For testing:

Create objects of Patient class

Invoke calculate_lab_test_charge() on Patient object

Display patient name, patient id, test ids of lab tests done by the patient and total lab test charge
"""

class Patient:
    def __init__(self,patient_id,patient_name,list_of_lab_test_ids):
        self.__patient_id=patient_id
        self.__patient_name=patient_name
        self.__list_of_lab_test_ids=list_of_lab_test_ids
        self.__lab_test_charge=0
    def get_patient_id(self):
        return self.__patient_id
    def get_patient_name(self):
        return self.__patient_name
    def get_list_of_lab_test_ids(self):
        return self.__list_of_lab_test_ids
    def get_lab_test_charge(self):
        return self.__lab_test_charge
    def calculate_lab_test_charge(self):
        charge=0
        for i in self.__list_of_lab_test_ids:
            x=LabTestRepository.get_test_charge(i)
            if x!=-1:
                charge+=x
        
        self.__lab_test_charge=charge    

class LabTestRepository:
    __list_of_hospital_lab_test_ids=["L101","L102","L103","L104"]
    __list_of_lab_test_charge=[2020,1750.50,5700,1320.50]
    @staticmethod
    def get_test_charge(lab_test_id):
        if lab_test_id in LabTestRepository.__list_of_hospital_lab_test_ids:
            for i,j in zip(LabTestRepository.__list_of_hospital_lab_test_ids,LabTestRepository.__list_of_lab_test_charge):
                if i==lab_test_id:
                    return j
    
            return -1
        else:
            return -1

lab_test_list1=["L101","L103","L104",'L105']
patient1=Patient(1010,"Sam",lab_test_list1)
patient1.calculate_lab_test_charge()
print("Patient id:",patient1.get_patient_id(),"\nPatient name:",patient1.get_patient_name(),"\nPatient's test ids:",patient1.get_list_of_lab_test_ids(), "\nTotal lab test charge:",patient1.get_lab_test_charge())\

