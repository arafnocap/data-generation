import datetime
import random


def generate_random_date(min_year:int, max_year:int):
    """
    This function generates a random date- and returns it in a string format
    :params min_year: int, this is the minimum year your date can be generated until
    :params max_year: int, this is the maximum year your date can be generated until
    "returns: A random date as a string in the following format YYYY-MM-DD
    """
    date_format = "%Y-%m-%d"
    return datetime.datetime.strptime(str(random.randint(min_year, max_year)) + "-" + str(random.randint(1, 12)) + "-" + str(random.randint(1, 28)), date_format)


def random_date_between_dates(start_date, end_date):
    """
    Generates a random date between two given dates.
    :params start_date: date, this is the start date your generated date should be in between
    :params end_date: date, this is the end date your generated date should be in between
    "returns: A random date as a string in the following format YYYY-MM-DD
    """
    date_format = "%Y-%m-%d"
    delta = end_date - start_date
    random_days = random.randrange(delta.days)
    random_date = start_date + datetime.timedelta(days=random_days)
    return datetime.datetime.strptime(str(random_date.year) + "-" + str(random_date.month) + "-" + str(random_date.day), date_format) 

def get_coverage_total(start_date, end_date, estimated_monthly_payment):
    """
    This function calculates the estimated insurance coverage total
    :params start_date: datetime, this is the start date of the insurance plan
    :params end: datetime, this is the end date of the insurance plan
    :params estimated_monthly_payment: float, this is the estimated monthly payment of the plan
    "returns: A random date as a string in the following format YYYY-MM-DD
    """
    date_delta = start_date - end_date
    days = date_delta.days

    daily_payment = estimated_monthly_payment / 30

    return round(-1 * (days * daily_payment), 2)

def generate_phone_number():
    """
    This function will generate a fake phone number
    "returns: A 10-digit phone numebr as a string
    """
    phone_number = [str(random.randint(0, 9)) for i in range(10)]
    while len(phone_number) < 10:
        phone_number.append(random.randint(0,9))
    
    return "".join(phone_number)
    

def to_dict(dictionary, dict_type='customer'):
        """
        This method converts the customer class to a dictionary.
        ---
        input params
        :param dict_type: str, this parameter tells the method what information to output 
            in the dictionary
        
        """

        attributes_to_output = ['id', 'relationship_type', 'first_name', 'last_name', 'address_line_1', 'address_line_2',
            'address_city', 'address_state', 'address_zipcode', 'address_lat', 'address_lng',
            'gender', 'race', 'marital_status', 'us_citizen', 'phone_number', 'dob']

        if dict_type=='customer':
            return dict(filter(lambda item: item[0] in attributes_to_output, dictionary))

        elif dict_type=='insurance_policies':
            attributes_to_output = ['policy_id', 'policy_type', 'policy_description', 'policyholder_name',
                'policy_start_date', 'policy_end_date', 'policy_length', 'premium_amount', 'deductible_amount',
                'estimated_coverage_total']
            return dict(filter(lambda item: item[0] in attributes_to_output, dictionary))

        elif dict_type=='insurance_claims':
            attributes_to_output = ['claim_id', 'claim_status', 'claim_open_date', 'claim_close_date', 'claim_reason', 'claim_amount', 'policy_number', 
                                    'beneficiary_id', 'date_of_loss', 'amount_claimed', 'amount_paid']
            return dict(filter(lambda item: item[0] in attributes_to_output, dictionary))
        
        elif dict_type == 'insurance_survey':
            attributes_to_output = ['id', 'survey_id', 'first_name', 'last_name', 'address_line_1', 'address_line_2',
            'address_city', 'address_state', 'address_zipcode', 'us_citizen', 'last_4_social', 
            'marital_status', 'gender', 'dob', 'occupation', 'annual_income', 'net_worth', 'pilot_flag', 'scuba_flag', 
            'auto_racing_flag', 'recreational_climbing_flag', 'felony_flag', 'dui_flag', 
            'suspended_license_flag']
            return dict(filter(lambda item: item[0] in attributes_to_output, dictionary))


        elif dict_type=='fb_marketing':
            attributes_to_output = ['id', 'ad_id', 'ad_name', 'impressions', 'clicks', 'spend', 'date',
            'campaign_name', 'target_age_range', 'target_gender', 'target_location', 'ad_format',
            'call_to_action', 'result']
            return dict(filter(lambda item: item[0] in attributes_to_output, dictionary))
        
        elif dict_type=='ad_campaign_social':
            attributes_to_output = ['ad_campaign_social_id', 'ad_campaign_initiative_id', 'ad_campaign_impression', 'ad_campaign_click', 'ad_campaign_updated_by',
            'ad_campaign_updated_time', 'ad_campaign_created_by', 'ad_campaign_updated_time']
            return dict(filter(lambda item: item[0] in attributes_to_output, dictionary))
        
        elif dict_type=='ad_campaign_display':
            attributes_to_output = ['ad_c_display_id', 'ad_c_display_initiative_id', 'ad_c_display_host_page_url', 'ad_c_display_time_on_page', 'ad_c_display_impression',
            'ad_c_display_click', 'ad_c_display_updated_by', 'ad_c_display_created_time', 'ad_c_display_created_by', 'ad_c_display_updated_time']
            return dict(filter(lambda item: item[0] in attributes_to_output, dictionary))
        
        elif dict_type=='ad_campaign_email':
            attributes_to_output = ['ad_c_email_id', 'ad_c_email_initiative_id', 'ad_c_email_service', 'ad_c_email_response', 'ad_c_email_updated_by',
            'ad_c_email_created_time', 'ad_c_email_updated_time', 'ad_c_email_created_by']
            return dict(filter(lambda item: item[0] in attributes_to_output, dictionary))
        
        elif dict_type=='ad_campaign_direct_mail':
            attributes_to_output = ['ad_c_direct_mail_id', 'ad_c_direct_mail_initiative_id', 'ad_c_direct_mail_mail_type', 'ad_c_direct_mail_carrier', 'ad_c_direct_mail_tracking_id',
            'ad_c_direct_mail_sent_date', 'ad_c_direct_mail_delivered_date', 'ad_c_direct_mail_response', 'ad_c_direct_mail_updated_by', 'ad_c_direct_mail_updated_time',
            'ad_c_direct_mail_created_by', 'ad_c_direct_mail_created_time']
            return dict(filter(lambda item: item[0] in attributes_to_output, dictionary))
        
