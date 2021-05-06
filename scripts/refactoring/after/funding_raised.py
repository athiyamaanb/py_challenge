import csv


class FundingRaised(object):

    @staticmethod
    def get_matches(options):
        output = []
        with open("startup_funding.csv", "rt") as csvfile:
            # pandas
            data = csv.reader(csvfile, delimiter=',', quotechar='"')
            header = next(data)
            for row in data:
                match = 0
                for k, v in options.items():
                    match += 1 if row[header.index(k)] == v else 0
                if len(options.keys()) == match:
                    output.append(dict(zip(header, row)))
        return output

    @staticmethod
    def where(options={}):
        return FundingRaised.get_matches(options)

    @staticmethod
    def find_by(options):
        return FundingRaised.get_matches(options)[0]


class RecordNotFound(Exception):
    pass
