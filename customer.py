import random
import names
from random_address import real_random_address
import uuid
import datetime
import pandas as pd

class Customer:
    def __init__(self, id):
        self.customer_id = id
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
        # Desired format of the string
        date_format = "%Y-%m-%d"

        # Generate a random number of days
        days = random.randint(60,365)
        random_days = datetime.timedelta(days=days)

        self.policy_number = "P" + str(str(uuid.uuid1()).split('-')[0] + str(unique_number))
        self.policyholder_name = self.first_name + " " + self.last_name
        self.make_and_model = random.choice(["Ford Fusion", "Toyota Camry", "Honda Civic", "Chevrolet Malibu", "Nissan Altima"])
        self.model_year = random.randint(2000, 2022)
        self.policy_start_date = datetime.datetime.strptime(str(random.randint(self.model_year, 2022)) + "-" + str(random.randint(1, 12)) + "-" + str(random.randint(1, 28)), date_format)
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
        self.date_of_loss = str(random.randint(2000, 2020)) + "-" + str(random.randint(1, 12)) + "-" + str(random.randint(1, 28))
        self.amount_claimed = random.randint(1000, 50000)
        self.amount_paid = random.randint(500, self.amount_claimed)

    

    def to_dict(self, dict_type='customer'):
        """
        This method converts the customer class to a dictionary.
        ---
        input params
        :param dict_type: str, this parameter tells the method what information to output 
            in the dictionary
        
        """

        attributes_to_output = ['customer_id', 'first_name', 'last_name', 'address_line_1', 'address_line_2',
            'address_city', 'address_state', 'address_zipcode', 'address_lat', 'address_lng',
            'gender', 'race']

        if dict_type=='customer':
            return dict(filter(lambda item: item[0] in attributes_to_output, self.__dict__.items()))

        elif dict_type=='auto_insurance':
            attributes_to_output = ['customer_id', 'policy_number', 'make_and_model', 'model_year',
                'policy_start_date', 'policy_end_date']
            return dict(filter(lambda item: item[0] in attributes_to_output, self.__dict__.items()))

        elif dict_type=='auto_claims':
            attributes_to_output = ['customer_id', 'claim_number', 'policy_number', 'date_of_loss',
                'amount_claimed', 'amount_paid']
            return dict(filter(lambda item: item[0] in attributes_to_output, self.__dict__.items()))



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