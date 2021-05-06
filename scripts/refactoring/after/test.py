import unittest
from funding_raised import FundingRaised

KEYS = ['permalink', 'company_name', 'number_employees', 'category', 'city', 'state', 'funded_date', 'raised_amount', 'raised_currency', 'round']

class TestWhere(unittest.TestCase):

    def test_where_with_company_name(self):
        self.assertEqual(len(FundingRaised.where({'company_name': 'Facebook'})), 7)

    def test_where_with_company_name_returns_correct_keys(self):
        row = FundingRaised.where({'company_name': 'Facebook'})[0]
        values = ['facebook', 'Facebook', '450', 'web', 'Palo Alto', 'CA', '1-Sep-04', '500000', 'USD', 'angel']
        for i in range(len(KEYS)):
            self.assertEqual(row[KEYS[i]], values[i])

    def test_where_with_city(self):
        self.assertEqual(len(FundingRaised.where({'city': 'Tempe'})), 3)

    def test_where_with_state(self):
        self.assertEqual(len(FundingRaised.where({'state': 'CA'})), 873)



    def test_where_with_round(self):
        self.assertEqual(len(FundingRaised.where({'round': 'a'})), 582)

    def test_where_company_name_does_not_exist(self):
        self.assertEqual(len(FundingRaised.where({'company_name': 'NotFacebook'})), 0)

    def test_where_with_company_and_round(self):
        print(FundingRaised.where({'company_name': 'Facebook', 'round': 'a'}))
        self.assertEqual(len(FundingRaised.where({'company_name': 'Facebook', 'round': 'a'})), 1)


class TestFindBy(unittest.TestCase):

    def test_find_by_with_company_name(self):
        row = FundingRaised.find_by({'company_name': 'Facebook'})
        print(row)
        values = ['facebook', 'Facebook', '450', 'web', 'Palo Alto', 'CA', '1-Sep-04', '500000', 'USD', 'angel']
        for i in range(len(KEYS)):
            self.assertEqual(row[KEYS[i]], values[i])

    def test_find_by_with_state(self):
        row = FundingRaised.find_by({'state': 'CA'})
        print(row)
        values = ['digg', 'Digg', '60', 'web', 'San Francisco', 'CA', '1-Dec-06', '8500000', 'USD', 'b']
        for i in range(len(KEYS)):
            self.assertEqual(row[KEYS[i]], values[i])

    def test_find_by_with_company_name_and_round(self):
        row = FundingRaised.find_by({'company_name': 'Facebook', 'round': 'a'})
        values = ['facebook', 'Facebook', '450', 'web', 'Palo Alto', 'CA', '1-May-05', '12700000', 'USD', 'a']
        for i in range(len(KEYS)):
            self.assertEqual(row[KEYS[i]], values[i])

#class TestExtraCredit(unittest.TestCase):
#
#    def test_where_allows_chaining(self):
#         self.assertEqual(len(FundingRaised.where(company_name: 'Facebook').where(round: 'a').size)), 1)

if __name__ == '__main__':
    unittest.main()
