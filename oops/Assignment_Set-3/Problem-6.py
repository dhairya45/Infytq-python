class Applicant:
    __application_dict={'A':0, 'B':0, 'C':0}
    __applicant_id_count=1000
    
    def __init__(self, applicant_name):
        self.__applicant_name=applicant_name
        self.__job_band=""
        self.__applicant_id=0
        
    def get_applicant_name(self):
        return self.__applicant_name
        
    def get_job_band(self):
        return self.__job_band
    
    def get_applicant_id(self):
        return self.__applicant_id
    
    @staticmethod
    def get_application_dict():
        return Applicant.__application_dict
        
    def generate_applicant_id(self):
        if Applicant.__applicant_id_count is None:
            Applicant.__applicant_id_count=1000
            Applicant.__applicant_id_count+=1
            self.__applicant_id=Applicant.__applicant_id_count
        else:
            Applicant.__applicant_id_count+=1
            self.__applicant_id=Applicant.__applicant_id_count
            
    def apply_for_job(self, job_band):
        if Applicant.__application_dict[job_band]>=5:
            return -1
        else:
            Applicant.__application_dict[job_band]+=1
            self.generate_applicant_id()
            self.__job_band=job_band
            
x=Applicant('x')
x.apply_for_job('A')
y=Applicant('y')
y.apply_for_job('A')
z=Applicant('z')
z.apply_for_job('A')
print(z.get_applicant_id()) 
