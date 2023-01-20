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