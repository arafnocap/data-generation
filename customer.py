import random
import names
from random_address import real_random_address
import uuid
import datetime
import pandas as pd
import helper_functions
import list_tools
import numpy as np

class Customer:
    def __init__(self, id):
        self.id = id
        self.relationship_type = random.randint(0, 3)
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
        self.marital_status = random.choice(["Single", "Married", "Divorced", "Widowed", "Separated"])
        self.us_citizen = random.randint(0, 1)
        self.phone_number = helper_functions.generate_phone_number()
        self.dob = helper_functions.generate_random_date(1940, 2000)


   


    def create_insurance_data(self, unique_number):
        """
        This method creates unique and random Auto Insurance Policy Data
        ---
        :param unique_number: int, this is the number to be given for a customer. It will help 
            generate a unique insurance policy ID.
        """
        # Generate a random number of days
        days = random.randint(60,365)
        random_days = datetime.timedelta(days=days)

        self.policy_id = "P" + str(str(uuid.uuid1()).split('-')[0] + str(unique_number))
        self.policy_type = random.choice(['Health insurance', 'Auto insurance', 'Homeowners insurance', 'Life insurance', 'Pet insurance', 'Business insurance', 'Flood insurance', 'Umbrella insurance'])
        self.policy_description = list_tools.insurance_descriptions[self.policy_type]
        self.policyholder_name = self.first_name + " " + self.last_name
        self.make_and_model = random.choice(["Ford Fusion", "Toyota Camry", "Honda Civic", "Chevrolet Malibu", "Nissan Altima"])
        self.model_year = random.randint(2000, 2022)
        self.policy_start_date = helper_functions.generate_random_date(self.model_year, 2022)
        self.policy_end_date = self.policy_start_date + random_days
        self.policy_length = (self.policy_end_date - self.policy_start_date)
        self.premium_amount = random.randint(100, 3000)
        self.estimated_coverage_total = helper_functions.get_coverage_total(self.policy_start_date,
                                        self.policy_end_date, self.premium_amount)
        self.deductible_amount = random.randrange(100, 2000, 100)
        
    
    def create_insurance_claims_data(self, unique_number):
        """
        This method creates unique and random Insurance Claims Data
        ---
        :param unique_number: int, this is the number to be given for a customer. It will help 
            generate a unique insurance claim ID.  
        """
        self.claim_id = "C" + str(str(uuid.uuid1()).split('-')[-1] + str(unique_number))
        self.claim_status = random.randint(0, 1)
        self.claim_open_date = helper_functions.random_date_between_dates(self.policy_start_date, self.policy_end_date)
        self.claim_close_date = helper_functions.random_date_between_dates(self.claim_open_date, self.policy_end_date)
        self.claim_reason = random.randint(0, 5)
        self.claim_amount = random.randint(100, 5000)
        self.policy_number = self.policy_id
        self.beneficiary_id = self.id
        self.date_of_loss = helper_functions.generate_random_date(self.policy_start_date.year, 2022)
        self.amount_claimed = random.randint(1000, 50000)
        self.amount_paid = random.randint(500, self.amount_claimed)

    def create_insurance_survey_data(self, unique_number):
        """
        This method creates unique and random Insurance Survey Data
        ---
        :param unique_number: int, this is the number to be given for a customer. It will help 
            generate a unique insurance survey ID.
        """
        self.survey_id = "S" + str(str(uuid.uuid1()).split('-')[-1] + str(unique_number))
        self.last_4_social = ''.join([str(random.randint(0, 9)) for i in range(4)])
        self.occupation = random.choice(list_tools.job_occupations)
        self.annual_income = random.randint(20000, 200000)
        self.net_worth = self.annual_income + (random.randint(-1, 4) * self.annual_income)
        self.pilot_flag = random.randint(0, 1)
        self.scuba_flag = random.randint(0, 1)
        self.auto_racing_flag = random.randint(0, 1)
        self.recreational_climbing_flag = random.randint(0, 1)
        self.felony_flag = random.randint(0, 1)
        self.dui_flag = random.randint(0, 1)
        self.suspended_license_flag = random.randint(0, 1)

    def create_marketing_data(self, campaign_data):
        self.ad_campaign_social_id = campaign_data.ad_campaign_social_id
        self.ad_campaign_initiative_id = campaign_data.ad_campaign_initiative_id
        self.ad_campaign_marketing_platform = campaign_data.ad_campaign_marketing_platform
        self.ad_campaign_impression = campaign_data.ad_campaign_impression
        self.ad_campaign_click = campaign_data.ad_campaign_click
        self.ad_campaign_updated_by = campaign_data.ad_campaign_updated_by
        self.ad_campaign_updated_time = campaign_data.ad_campaign_updated_time
        self.ad_campaign_created_by = campaign_data.ad_campaign_created_by
        self.ad_campaign_updated_time = campaign_data.ad_campaign_updated_time
        self.ad_c_display_id = campaign_data.ad_c_display_id
        self.ad_c_display_initiative_id = campaign_data.ad_c_display_initiative_id
        self.ad_c_display_host_page_url = campaign_data.ad_c_display_host_page_url
        self.ad_c_display_time_on_page = campaign_data.ad_c_display_time_on_page
        self.ad_c_display_impression = campaign_data.ad_c_display_impression
        self.ad_c_display_click = campaign_data.ad_c_display_click
        self.ad_c_display_updated_by = campaign_data.ad_c_display_updated_by
        self.ad_c_display_created_time = campaign_data.ad_c_display_created_time
        self.ad_c_display_created_by = campaign_data.ad_c_display_created_by
        self.ad_c_display_updated_time = campaign_data.ad_c_display_updated_time
        self.ad_c_email_id = campaign_data.ad_c_email_id
        self.ad_c_email_initiative_id = campaign_data.ad_c_email_initiative_id
        self.ad_c_email_service = campaign_data.ad_c_email_service
        self.ad_c_email_response = campaign_data.ad_c_email_response
        self.ad_c_email_updated_by = campaign_data.ad_c_email_updated_by
        self.ad_c_email_created_time = campaign_data.ad_c_email_created_time
        self.ad_c_email_updated_time = campaign_data.ad_c_email_updated_time
        self.ad_c_email_created_by = campaign_data.ad_c_email_created_by
        self.ad_c_direct_mail_id = campaign_data.ad_c_direct_mail_id
        self.ad_c_direct_mail_initiative_id = campaign_data.ad_c_direct_mail_initiative_id
        self.ad_c_direct_mail_mail_type = campaign_data.ad_c_direct_mail_mail_type
        self.ad_c_direct_mail_carrier = campaign_data.ad_c_direct_mail_carrier
        self.ad_c_direct_mail_tracking_id = campaign_data.ad_c_direct_mail_tracking_id
        self.ad_c_direct_mail_sent_date = campaign_data.ad_c_direct_mail_sent_date
        self.ad_c_direct_mail_delivered_date = campaign_data.ad_c_direct_mail_delivered_date
        self.ad_c_direct_mail_response = campaign_data.ad_c_direct_mail_response
        self.ad_c_direct_mail_updated_by = campaign_data.ad_c_direct_mail_updated_by
        self.ad_c_direct_mail_updated_time = campaign_data.ad_c_direct_mail_updated_time
        self.ad_c_direct_mail_created_by = campaign_data.ad_c_direct_mail_created_by
        self.ad_c_direct_mail_created_time = campaign_data.ad_c_direct_mail_created_time





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
        self.target_age_rane = random.choice(["18-24", "25-34", "35-44", "45-54", "55-64", "65+"])
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