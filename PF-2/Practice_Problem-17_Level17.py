#lex_auth_0127136112798105601178    

""" get_train_name(train_no)

        This function accepts the train number and returns the dict which contains the details of the train.

get_trains_for_day(day_of_run)

       This function accepts a day and returns the list of numbers of the trains running on that day.

get_total_fare(train_no,passenger_dict)

       This function accepts train_no and a dictionary of passenger details. The passenger_dict is of the following format:
       passenger_dict={ “sleeper”:5, “ac”,1 }
       This function returns the total fare based on the passenger details and train number.
       
 """


train_list=[
{"train_no":16453,"name":"Prasanti Express","from":"SBC","to":"BBS","days_of_run":['Mo','We','Th'],"sleeper_fare":600,"ac_fare": 987},
{"train_no":25627,"name":"Karnataka Express","from":"SBC","to":"DEC","days_of_run":['Su','Tu'],"sleeper_fare":1600,"ac_fare": 2500},
{"train_no":22642,"name":"Trivandrum SF Express","from":"VSKP","to":"TVM","days_of_run":['Mo','Tu','We','Th','Fr','Sa'],"sleeper_fare":800,"ac_fare": 1256},
{"train_no":22905,"name":"Okha Howrah Express","from":"ST","to":"KOAA","days_of_run":['We','Sa'],"sleeper_fare":987,"ac_fare": 2879}]

def get_train_name (train_no):
    for x in train_list:
        if train_no==x["train_no"]:
            return x
    return "Invalid Train_no"
            
def get_trains_for_day(day_of_run):
    l=[]
    for x in train_list:
        if day_of_run in x["days_of_run"]:
            l.append(x["train_no"])
    if len(l)==0:
        return "Invalid day"
    else:
        return l
        
    
    
def get_total_fare(train_no,passenger_dict):
    for x in train_list:
        if train_no==x["train_no"]:
            return (passenger_dict["sleeper"]*x["sleeper_fare"]+passenger_dict["ac"]*x["ac_fare"])
            
    
print(get_train_name(22642))
print(get_trains_for_day("Mo"))
print(get_total_fare(25627,{"sleeper":10, "ac":10}))
