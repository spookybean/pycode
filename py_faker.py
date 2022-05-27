from faker import Faker
from pprint import pp


fake = Faker('it_IT')

pp({
    'name': fake.name(),
    'address': fake.address(),
    'ipv4': fake.ipv4_public(),
    'company': fake.company(),
    'email': fake.company_email(),
    'phone': fake.phone_number(),
    'country': fake.country(),
    'job': fake.job()
})