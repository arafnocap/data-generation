import random
import names
from random_address import real_random_address
import uuid
import datetime
import pandas as pd
import helper_functions

class Marketing:
    def __init__(self, company_name):
        self.company_name = company_name

    def create_facebook_ad_report_data(self, number_campaigns):
        """
        This method creates unique and random Facebook Ad Campaign Report Data
        ---
        :param unique_number: int, this is the number to be given for a customer. It will help 
            generate a unique auto insurance claim ID.
        """
        ad_data = {
        "ad_id": [],
        # "ad_name": [],
        "ad_impressions": [],
        "clicks": [],
        "spend": [],
        "date": [],
        "campaign_name": [],
        "target_age_range": [],
        "target_gender": []
        #, "location": [],
        # "ad_format": [],
        # "action": [],
        # "result": []
    }
        ad_ids = [str(uuid.uuid4()).split('-')[-1] for x in range(number_campaigns)]
        for i in range(number_campaigns):
            for ad_id in ad_ids:
                for age_range in ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"]:
                    for gender in ["Male", "Female", "Other"]: 
                        # for location in list_of_locations:
                            # for ad_format in ["Carousel", "Single Image", "Video"]:
                                # for action in ["Learn More", "Sign Up", "Shop Now"]:
                                    # for result in ["Completed", "Not Completed", "Failed"]:
                        ad_data["ad_id"].append(ad_id)
                        # ad_data["ad_name"].append("Ad " + current_ad_id)
                        current_ad_impressions = random.randint(1000, 100000)
                        ad_data["ad_impressions"].append(current_ad_impressions)
                        ad_data["clicks"].append(random.randint(0, (current_ad_impressions - 100)))
                        ad_data["spend"].append(round(random.uniform(10, 1000), 2))
                        ad_data["date"].append(helper_functions.generate_random_date(2021, 2022))
                        ad_data["campaign_name"].append("Campaign " + str(i))
                        ad_data["target_age_range"].append(age_range)
                        ad_data["target_gender"].append(gender)
                        # ad_data["location"] = location
                        # ad_data["ad_format"] = ad_format
                        # ad_data["action"] = action
                        # ad_data["result"] = result
        df = pd.DataFrame(ad_data)
        df.groupby(["ad_id", "target_age_range", "target_gender"])
        df = df.sort_values(["target_age_range"])
        return df
    
class Campaigns:
    def __init__(self):
        pass
    
    def create_ad_campaign_social(self, unique_number):
        self.ad_campaign_social_id = "ACSI" + str(str(uuid.uuid1()).split('-')[-1] + str(unique_number))
        self.ad_campaign_initiative_id = "IN" + str(str(uuid.uuid1()).split('-')[-1] + str(unique_number))
        self.ad_campaign_marketing_platform = random.choice(['Facebook', 'Instagram', 'Twitter', 'Snapchat', 'TikTok'])
        self.ad_campaign_impression = random.randint(0, 1)
        self.ad_campaign_click = random.randint(0, 1)
        self.ad_campaign_updated_by = "User"
        self.ad_campaign_created_time = helper_functions.generate_random_date(2020, 2022) + datetime.timedelta(days=random.randint(0, 10))
        self.ad_campaign_created_by = "User"
        self.ad_campaign_updated_time = self.ad_campaign_created_time + datetime.timedelta(days=random.randint(0, 10))

    def create_ad_campaign_display(self, unique_number):
        self.ad_c_display_id = "ACDI" + str(str(uuid.uuid1()).split('-')[-1] + str(unique_number))
        self.ad_c_display_initiative_id = "IN" + str(str(uuid.uuid1()).split('-')[-1] + str(unique_number))
        self.ad_c_display_host_page_url = random.choice(['Facebook.com', 'Instagram.com', 'Twitter.com', 'Snapchat.com', 'TikTok.com'])
        self.ad_c_display_time_on_page = random.randint(0, 20000)
        self.ad_c_display_impression = random.randint(0, 1)
        self.ad_c_display_click = random.randint(0, 1)
        self.ad_c_display_updated_by = "User"
        self.ad_c_display_created_time = helper_functions.generate_random_date(2020, 2022)
        self.ad_c_display_created_by = "User"
        self.ad_c_display_updated_time = self.ad_c_display_created_time + + datetime.timedelta(days=random.randint(0, 10))

    def create_ad_campaign_email(self, unique_number):
        self.ad_c_email_id = "ACEI" + str(str(uuid.uuid1()).split('-')[-1] + str(unique_number))
        self.ad_c_email_initiative_id = "IN" + str(str(uuid.uuid1()).split('-')[-1] + str(unique_number))
        self.ad_c_email_service = random.choice(['gmail', 'yahoo', 'hotmail', 'aol', 'proton'])
        self.ad_c_email_response = random.randint(0, 1)
        self.ad_c_email_updated_by = "User"
        self.ad_c_email_created_time = helper_functions.generate_random_date(2020, 2022)
        self.ad_c_email_updated_time = self.ad_c_email_created_time + datetime.timedelta(days=random.randint(0, 10))
        self.ad_c_email_created_by = "User"

    def create_ad_campaign_direct_mail(self, unique_number):
        self.ad_c_direct_mail_id = "ACEI" + str(str(uuid.uuid1()).split('-')[-1] + str(unique_number))
        self.ad_c_direct_mail_initiative_id = "IN" + str(str(uuid.uuid1()).split('-')[-1] + str(unique_number))
        self.ad_c_direct_mail_mail_type = random.choice(['letter', 'package'])
        self.ad_c_direct_mail_carrier = random.choice(['USPS', 'UPS', 'Amazon', 'DHL', 'FedEx'])
        self.ad_c_direct_mail_tracking_id = "tid_" + str(str(uuid.uuid1()).split('-')[-1] + str(unique_number))
        self.ad_c_direct_mail_sent_date = helper_functions.generate_random_date(2020, 2022)
        self.ad_c_direct_mail_delivered_date = helper_functions.generate_random_date(2020, 2022) + datetime.timedelta(days=random.randint(0, 10))
        self.ad_c_direct_mail_response = random.randint(0, 1)
        self.ad_c_direct_mail_updated_by = "User"
        self.ad_c_direct_mail_updated_time = self.ad_c_direct_mail_delivered_date + datetime.timedelta(days=random.randint(0, 10))
        self.ad_c_direct_mail_created_by = "User"
        self.ad_c_direct_mail_created_time = self.ad_campaign_updated_time