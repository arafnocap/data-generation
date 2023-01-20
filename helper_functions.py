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

def to_dict(dictionary, dict_type='customer'):
        """
        This method converts the customer class to a dictionary.
        ---
        input params
        :param dict_type: str, this parameter tells the method what information to output 
            in the dictionary
        
        """

        attributes_to_output = ['id', 'first_name', 'last_name', 'address_line_1', 'address_line_2',
            'address_city', 'address_state', 'address_zipcode', 'address_lat', 'address_lng',
            'gender', 'race']

        if dict_type=='customer':
            return dict(filter(lambda item: item[0] in attributes_to_output, dictionary))

        elif dict_type=='auto_insurance':
            attributes_to_output = ['id', 'policy_number', 'make_and_model', 'model_year',
                'policy_start_date', 'policy_end_date']
            return dict(filter(lambda item: item[0] in attributes_to_output, dictionary))

        elif dict_type=='auto_claims':
            attributes_to_output = ['id', 'claim_number', 'policy_number', 'date_of_loss',
                'amount_claimed', 'amount_paid']
            return dict(filter(lambda item: item[0] in attributes_to_output, dictionary))

        elif dict_type=='fb_marketing':
            attributes_to_output = ['id', 'ad_id', 'ad_name', 'impressions', 'clicks', 'spend', 'date',
            'campaign_name', 'target_age_range', 'target_gender', 'target_location', 'ad_format',
            'call_to_action', 'result']
            return dict(filter(lambda item: item[0] in attributes_to_output, dictionary))