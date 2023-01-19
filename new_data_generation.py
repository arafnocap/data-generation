from customer import Customer
import pandas as pd
import random

def create_auto_insurance(num_records=1000, customer_output='customers.csv', 
insurance_output='auto_insurance.csv', claims_output='auto_claims.csv'):
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

    return 'Data Creation Complete'

create_auto_insurance()

print('done')