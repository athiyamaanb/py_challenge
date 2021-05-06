import csv

class FundingRaised(object):
    @staticmethod
    def where(options={}):
        with open("../startup_funding.csv", "rt") as csvfile:
            data = csv.reader(csvfile, delimiter=',', quotechar='"')
            csv_data = []
            for row in data:
                csv_data.append(row)

        funding = []
        if 'company_name' in options:
            result = []
            for row in csv_data:
                if row[1] == options['company_name']:
                    result.append(row)
            csv_data = result

        if 'city' in options:
            result = []
            for row in csv_data:
                if row[4] == options['city']:
                    result.append(row)
            csv_data = result

        if 'state' in options:
            result = []
            for row in csv_data:
                if row[5] == options['state']:
                    result.append(row)
            csv_data = result

        if 'round' in options:
            result = []
            for row in csv_data:
                if row[9] == options['round']:
                    result.append(row)
            csv_data = result

        output = []
        for row in csv_data:
            mapped = {}
            mapped['permalink'] = row[0]
            mapped['company_name'] = row[1]
            mapped['number_employees'] = row[2]
            mapped['category'] = row[3]
            mapped['city'] = row[4]
            mapped['state'] = row[5]
            mapped['funded_date'] = row[6]
            mapped['raised_amount'] = row[7]
            mapped['raised_currency'] = row[8]
            mapped['round'] = row[9]
            output.append(mapped)

        return output

    @staticmethod
    def find_by(options):
        with open("../startup_funding.csv", "rt") as csvfile:
            data = csv.reader(csvfile, delimiter=',', quotechar='"')
            csv_data = []
            for row in data:
                csv_data.append(row)

        for row in csv_data:
            mapped = {}

            if 'company_name' in options:
                if row[1] == options['company_name']:
                    mapped['permalink'] = row[0]
                    mapped['company_name'] = row[1]
                    mapped['number_employees'] = row[2]
                    mapped['category'] = row[3]
                    mapped['city'] = row[4]
                    mapped['state'] = row[5]
                    mapped['funded_date'] = row[6]
                    mapped['raised_amount'] = row[7]
                    mapped['raised_currency'] = row[8]
                    mapped['round'] = row[9]
                else:
                    continue

            if 'city' in options:
                if row[4] == options['city']:
                    mapped['permalink'] = row[0]
                    mapped['company_name'] = row[1]
                    mapped['number_employees'] = row[2]
                    mapped['category'] = row[3]
                    mapped['city'] = row[4]
                    mapped['state'] = row[5]
                    mapped['funded_date'] = row[6]
                    mapped['raised_amount'] = row[7]
                    mapped['raised_currency'] = row[8]
                    mapped['round'] = row[9]
                else:
                    continue

            if 'state' in options:
                if row[5] == options['state']:
                    mapped['permalink'] = row[0]
                    mapped['company_name'] = row[1]
                    mapped['number_employees'] = row[2]
                    mapped['category'] = row[3]
                    mapped['city'] = row[4]
                    mapped['state'] = row[5]
                    mapped['funded_date'] = row[6]
                    mapped['raised_amount'] = row[7]
                    mapped['raised_currency'] = row[8]
                    mapped['round'] = row[9]
                else:
                    continue

            if 'round' in options:
                if row[9] == options['round']:
                    mapped['permalink'] = row[0]
                    mapped['company_name'] = row[1]
                    mapped['number_employees'] = row[2]
                    mapped['category'] = row[3]
                    mapped['city'] = row[4]
                    mapped['state'] = row[5]
                    mapped['funded_date'] = row[6]
                    mapped['raised_amount'] = row[7]
                    mapped['raised_currency'] = row[8]
                    mapped['round'] = row[9]
                else:
                    continue

            return mapped

        raise RecordNotFound

class RecordNotFound(Exception):
    pass
