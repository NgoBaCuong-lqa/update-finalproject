import unittest
import HtmlTestRunner

from pom.test.test_changebuy import Changebuys
from pom.test.test_contactus import Contactus
from pom.test.test_createaccount import createaccount
from pom.test.test_createsucess_account import create_successsaccount
from pom.test.test_sendtofriend import sendtofriend
from pom.test.test_search import Searchs
from pom.test.test_newsletter import Letter
from pom.test.test_write_a_comment import Writeacomment
from pom.test.test_kiemtraviewlarge import TestChiTietSanPham
from pom.test.test_sharetotweet import share_to_tweet

tc1 = unittest.TestLoader().loadTestsFromTestCase(Changebuys)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Contactus)
tc3 = unittest.TestLoader().loadTestsFromTestCase(createaccount)
tc4 = unittest.TestLoader().loadTestsFromTestCase(create_successsaccount)
tc5 = unittest.TestLoader().loadTestsFromTestCase(sendtofriend)
tc6 = unittest.TestLoader().loadTestsFromTestCase(Searchs)
tc7 = unittest.TestLoader().loadTestsFromTestCase(Letter)
tc8 = unittest.TestLoader().loadTestsFromTestCase(Writeacomment)
tc9 = unittest.TestLoader().loadTestsFromTestCase(TestChiTietSanPham)
tc10 = unittest.TestLoader().loadTestsFromTestCase(share_to_tweet)

sanityTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5, tc6, tc7, tc8, tc9, tc10])

unittest.TextTestRunner().run(sanityTestSuite)
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output=r'C:\Users\Admin\PycharmProjects\UpdateFinalproject\test_report', combine_reports=True,
        report_name="Test Report"))
