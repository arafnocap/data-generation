from customer import Customer
import pandas as pd
import random
import helper_functions
import uuid
import datetime
from marketing import Campaigns

def create_insurance(num_records=1000, customer_output='customers.csv',
insurance_output='insurance_policies.csv', claims_output='claims.csv', 
survey_output='insurance_survey.csv'):
    """
    This function generates random auto insurance data and claims data and saves it in a specified location
    ---
    :params num_records: int, used to determine how many records the functions should generate
    :params customer_output: the location where the generated customer data file should be saved
    :params insurance_output: the location where the generated insurance data file should be saved
    :params claims_output: the location where the generated claims data file should be saved
    ---
    """
    try:
        customers = [Customer(id=i) for i in range(num_records)]
        for i, customer in enumerate(customers):
            customer.create_insurance_data(unique_number=i)
            random_number = random.randint(0, 1)
            if random_number == 1:
                customer.create_insurance_claims_data(unique_number=i)
            customer.create_insurance_survey_data(unique_number=i)
        general_customer = pd.DataFrame.from_records([s.to_dict(dict_type='customer') for s in customers])
        insurance = pd.DataFrame.from_records([s.to_dict(dict_type='insurance_policies') for s in customers])
        claims = pd.DataFrame.from_records([s.to_dict(dict_type='insurance_claims') for s in customers])
        claims = claims.dropna(subset=['claim_id'])
        surveys = pd.DataFrame.from_records([s.to_dict(dict_type='insurance_survey') for s in customers])

        general_customer.to_csv(customer_output)
        insurance.to_csv(insurance_output)
        claims.to_csv(claims_output)
        surveys.to_csv(survey_output)

        print('Data Creation Complete')
    except Exception as e:
        print(e, e.with_traceback)

#create_insurance(customer_output='customers.csv')


def create_marketing(number_campaigns, number_customers):
    campaigns = [Campaigns() for _ in range(number_campaigns)]
    for i, campaign in enumerate(campaigns):
        campaign.create_ad_campaign_social(i)
        campaign.create_ad_campaign_display(i)
        campaign.create_ad_campaign_email(i)
        campaign.create_ad_campaign_direct_mail(i)

    customers = [Customer(id=i) for i in range(number_customers)]
    for i, customer in enumerate(customers):
            customer.create_marketing_data(random.choice(campaigns))

    general_customer = pd.DataFrame.from_records([s.to_dict(dict_type='customer') for s in customers])
    ad_campaign_social = pd.DataFrame.from_records([s.to_dict(dict_type='ad_campaign_social') for s in customers])
    ad_campaign_display = pd.DataFrame.from_records([s.to_dict(dict_type='ad_campaign_display') for s in customers])
    ad_campaign_email = pd.DataFrame.from_records([s.to_dict(dict_type='ad_campaign_email') for s in customers])
    ad_campaign_direct_mail = pd.DataFrame.from_records([s.to_dict(dict_type='ad_campaign_direct_mail') for s in customers])

    general_customer.to_csv('customer.csv')
    ad_campaign_social.to_csv('ad_campaign_social.csv')
    ad_campaign_display.to_csv('ad_campaign_display.csv')
    ad_campaign_email.to_csv('ad_campaign_email.csv')
    ad_campaign_direct_mail.to_csv('ad_campaign_direct_mail.csv')

create_marketing(4, 1000)

def create_facebook_ad_report_data(number_campaigns):
    """
    This method creates unique and random Facebook Ad Campaign Report Data
    ---
    :param number_campaigns: int, this is the number of campaigns to generate data for.
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

# test1 = create_facebook_ad_report_data(250)
# print("done")


def create_google_site_report_data(number_of_days):
    """
    This method creates unique and random Google Site Analytics Report Data
    ---
    :param number_of_days: int, this is the number of days to generate data for.
    """
    start_date = helper_functions.generate_random_date(2022, 2022)
    dates = [start_date+datetime.timedelta(days=x) for x in (range(number_of_days))]

    site_data = {
        "date": [],
        "sessions": [],
        "page_views": [],
        "page_per_session": [],
        "avg_session_duration_hrs": [],
        "bounce_rate": [],
        "unique_visitors": [],
        "returning_visitors": [],
        "hours_spent_visitng": []
    }
    for date_ in dates:
        site_data["date"].append(date_)
        current_date_session = random.randint(100, 10000)
        site_data["sessions"].append(current_date_session)
        current_date_page_views = random.randint((current_date_session+10), int(current_date_session*(1 + (random.uniform(0, 1))) + 1))
        site_data["page_views"].append(current_date_page_views)
        site_data["page_per_session"].append((current_date_page_views/current_date_session))
        site_data["bounce_rate"].append(random.uniform(0, 1))
        current_date_unique_visitors = random.randint(0, (current_date_session - 50))
        site_data["unique_visitors"].append(current_date_unique_visitors)
        site_data["returning_visitors"].append(current_date_session - current_date_unique_visitors)
        current_date_hours_visited = random.uniform((current_date_session/3600), (current_date_session/3600) * (1+random.uniform(0, 2)))
        site_data["hours_spent_visitng"].append(random.randint(100, 10000))
        site_data["avg_session_duration_hrs"] = current_date_hours_visited / current_date_session

    df = pd.DataFrame(site_data)
    df = df.sort_values(["date"])
    return df

# test_2 = create_google_site_report_data(250)

# test1.to_csv('fb_generated_test.csv')

# test_2.to_csv('google_generated_test.csv')

print('done')