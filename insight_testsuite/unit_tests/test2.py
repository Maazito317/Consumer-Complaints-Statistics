import unittest
from src.complaints_count import process_complaints

class TestProcess(unittest.TestCase):
    def setUp(self):
        self.output = []
        self.entry1 = [['2019-09-24', 'Debt collection','I do not know',	'Attempts to collect debt not owed', 	'Debt is not yours', 	'transworld systems inc. is trying to collect a debt that is not mine, not owed and is inaccurate.','', 'TRANSWORLD SYSTEMS INC' 	,'FL', 	'335XX', 		'Consent provided', 	'Web', 	'2019-09-24', 	'Closed with explanation', 	'Yes', 	'N/A', 	'3384392'],
        ['2019-09-19' 	,'Credit reporting, credit repair services, or other personal consumer reports', 	'Credit reporting' 	,'Incorrect information on your report '	,'Information belongs to someone else ','Company has responded to the consumer and the CFPB and chooses not to provide a public response ','Experian Information Solutions Inc.','PA','15206','Consent not provided','Web','2019-09-20','Closed with non-monetary relief','Yes','N/A','3379500'],
        ['2019-11-20',"Credit reporting, credit repair services, or other personal consumer reports",'Credit reporting','Incorrect information on your report','Account information incorrect,I would like the credit bureau to correct my XXXX XXXX XXXX XXXX balance. My correct balance is XXXX','Company has responded to the consumer and the CFPB and chooses not to provide a public response',"TRANSUNION INTERMEDIATE HOLDINGS, INC.",'TX','77004','','Consent provided','Web','2019-11-20','Closed with explanation','Yes','N/A','3444592'],
        ['2019-10-24',"Credit reporting, credit repair services, or other personal consumer reports",'Credit reporting','Incorrect information on your report','Information belongs to someone else','','Company has responded to the consumer and the CFPB and chooses not to provide a public response',"TRANSUNION INTERMEDIATE HOLDINGS, INC.",'CA','925XX','','Other','Web','2019-10-24','Closed with explanation','Yes','N/A','3416481'],
        ['2020-01-06',"Credit reporting, credit repair services, or other personal consumer reports",'Credit reporting','Incorrect information on your report','Information belongs to someone else','','','Experian Information Solutions Inc.','CA,92532','','N/A','Email','2020-01-06','In progress','Yes','N/A','3486776']]

    def test_func(self):
        self.output = process_complaints(self.entry1)
        test = [['credit reporting, credit repair services, or other personal consumer reports', '2019', 2, 3, 66], ['credit reporting, credit repair services, or other personal consumer reports', '2020', 1, 1, 100], ['debt collection', '2019', 1, 1, 100]]
        self.assertEqual(self.output, test)


if __name__=='__main__':
    unittest.main()
