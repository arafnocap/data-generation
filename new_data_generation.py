from customer import Customer
import pandas as pd
import random
import helper_functions
import uuid

def create_auto_insurance(num_records=1000, customer_output='customers.csv', 
insurance_output='auto_insurance.csv', claims_output='auto_claims.csv'):
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
            customer.create_auto_insurance_data(unique_number=i)
            random_number = random.randint(0, 1)
            if random_number == 1:
                customer.create_insurance_claims_data(unique_number=i)
        general_customer = pd.DataFrame.from_records([s.to_dict(dict_type='customer') for s in customers])
        auto_insurance = pd.DataFrame.from_records([s.to_dict(dict_type='auto_insurance') for s in customers])
        auto_claims = pd.DataFrame.from_records([s.to_dict(dict_type='auto_claims') for s in customers])
        auto_claims = auto_claims.dropna(subset=['claim_number'])

        general_customer.to_csv(customer_output)
        auto_insurance.to_csv(insurance_output)
        auto_claims.to_csv(claims_output)

        print('Data Creation Complete')
    except Exception as e:
        print(e, e.with_traceback)

# create_auto_insurance(customer_output='customers.csv')

def create_facebook_ad_report_data(number_campaigns):
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

test = create_facebook_ad_report_data(3)
print("done")