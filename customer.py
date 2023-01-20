import random
import names
from random_address import real_random_address
import uuid
import datetime
import pandas as pd
import helper_functions

class Customer:
    def __init__(self, id):
        self.id = id
        self.first_name = names.get_first_name()
        self.last_name = names.get_last_name()
        address = real_random_address()
        self.address_line_1 = address['address1']
        self.address_line_2 = address['address2']
        try:
            self.address_city = address['city']
        except:
            self.address_city = ''
        self.address_state = address['state']
        self.address_zipcode = address['postalCode']
        self.address_lat = address['coordinates']['lat']
        self.address_lng = address['coordinates']['lng']
        self.gender = random.randint(0, 1)
        self.race = random.randint(0, 4)

    def create_auto_insurance_data(self, unique_number):
        """
        This method creates unique and random Auto Insurance Policy Data
        ---
        :param unique_number: int, this is the number to be given for a customer. It will help 
            generate a unique auto insurance policy ID.

        """
        # Generate a random number of days
        days = random.randint(60,365)
        random_days = datetime.timedelta(days=days)

        self.policy_number = "P" + str(str(uuid.uuid1()).split('-')[0] + str(unique_number))
        self.policyholder_name = self.first_name + " " + self.last_name
        self.make_and_model = random.choice(["Ford Fusion", "Toyota Camry", "Honda Civic", "Chevrolet Malibu", "Nissan Altima"])
        self.model_year = random.randint(2000, 2022)
        self.policy_start_date = helper_functions.generate_random_date(self.model_year, 2022)
        self.policy_end_date = self.policy_start_date + random_days
    
    def create_insurance_claims_data(self, unique_number):
        """
        This method creates unique and random Auto Insurance Claims Data
        ---
        :param unique_number: int, this is the number to be given for a customer. It will help 
            generate a unique auto insurance claim ID.
        
        """
        self.claim_number = "C" + str(str(uuid.uuid1()).split('-')[-1] + str(unique_number))
        self.policy_number = self.policy_number
        self.date_of_loss = helper_functions.generate_random_date(self.policy_start_date.year, 2022)
        self.amount_claimed = random.randint(1000, 50000)
        self.amount_paid = random.randint(500, self.amount_claimed)

    def create_facebook_ad_report_data(self, unique_number):
        """
        This method creates unique and random Facebook Ad Campaign Report Data
        ---
        :param unique_number: int, this is the number to be given for a customer. It will help 
            generate a unique auto insurance claim ID.
        """
        self.ad_id = str(str(uuid.uuid1()).split('-')[-1] + str(unique_number))
        self.ad_name = "Ad " + str(self.ad_id)
        self.impressions = random.randint(1000, 100000)
        self.clicks = random.randint(0, (self.impressions - 100))
        self.spend = round(random.uniform(10, 1000), 2)
        self.date = helper_functions.generate_random_date(2021, 2022)
        self.campaign_name = "Campaign " + str(self.ad_id)
        self.target_age_range = random.choice(["18-24", "25-34", "35-44", "45-54", "55-64", "65+"])
        self.target_gender = random.choice(["Male", "Female", "All"])
        self.target_location = "Location " + str(random.randint(1, 1000))
        self.ad_format = random.choice(["Carousel", "Single Image", "Video"])
        self.call_to_action = random.choice(["Learn More", "Sign Up", "Shop Now"])
        self.result = random.choice(["Completed", "Not Completed", "Failed"])

    

    def to_dict(self, dict_type='customer'):
        """
        This method converts the customer class to a dictionary.
        ---
        input params
        :param dict_type: str, this parameter tells the method what information to output 
            in the dictionary
        """
        return helper_functions.to_dict(self.__dict__.items(), dict_type)

       


# test = Customer()

# test.create_auto_insurance_data(1)
# test_2 = Customer()
# test.create_auto_insurance_data(1)

# test_2.create_auto_insurance_data(1)

# import pandas as pd

# test_list = [test, test_2]


# # dict(filter(lambda item: item[0] in list_to_keep, test_dict.items()))

# test_dict = test.to_dict(dict_type='auto_insurance')

# # test_df = [s.to_dict(dict_type='auto_insurance') for s in test_list_2]

# df = pd.DataFrame.from_records([s.to_dict(dict_type='auto_insurance') for s in test_list])

# print(df)
# print(test.policy_number)