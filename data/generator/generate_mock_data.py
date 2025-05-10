import pandas as pd
from faker import Faker


class GenerateMockData:

    def __init__(self):
        self.faker = Faker('th')
        #self.faker.add_provider('th')
    
    def person(self):
        return {
            'name': self.faker.name(),
            'address': self.faker.address(),
            'date_of_birth': self.faker.date_of_birth(),
        }

    def main(self):
        df = pd.DataFrame(
            self.person()
            for _ in range(100)
        )
        return df

if __name__ == '__main__':
    g = GenerateMockData()
    df = g.main()
    print(df)

