from Tests.config import Test_session
import pytest
from Methods.methods import RegistrationPage
from Methods.methods import adminLoginVerify
from Methods.methods import adminLoginManageuser
from Methods.methods import adminloginManageFarmerMarket
from Methods.methods import adminloginwithwrongemailid
from Methods.methods import adminloginwithoutatSymbol
from Methods.methods import adminloginwithoutrqdfield
from Methods.methods import Registrationwithoutemailid
from Methods.methods import SearchCity
from Methods.methods import Clearsearch
from Methods.methods import adminLoginVerifywithoutcity
from Methods.methods import clickOrderOptions
from Methods.methods import clickDaysOperation
from Methods.methods import clickMonthOptions
from Methods.methods import clickOpenToday
from Methods.methods import ClickLocationTypes
from Methods.methods import commentFeatures
from Methods.methods import vendoreditFeatures
from Methods.methods import adminSearchFunctions
from Methods.methods import languagetranslationCheck
from parameterized import parameterized_class



@parameterized_class(("url","firstname","lastname","vendorname","fnsnumber","primaryemail","primaryphno","psw","cpsw","continfo","publicemail","publicphno","publicwebsite","businessdesc","products","vendorPublicImg","pickupsitename","adrs1","adrs2","zipcode","spzl_instruction","farmstand_adrs_1","farmstand_adrs_2","farmstand_zipcode_textbox_id","mobileMarkettextboxid"),[("https://massdtaiot.com/dtahip/","nancy","antony","Nancy Farms","1234567","nannnnbbananabbncyyy@kyybbba.io","9080887878","123","123","boston","nancya@kyyba.com","9080559378","www.massdtaiot.com","Sample desc","Rice","C:/Users/user/Desktop/vendorImg.jpg","Test Site","123","123","01712","Spzl instruction","one","two","01712","Mobile Market")])
# # #Valid Credentials Registration
class RegistrationClass(Test_session) :
    @pytest.mark.ts_001

    def test_valid_credentials(self):
        """
        1.launch url
        2.enter registration details
        3.verify login credential
        """
        self.tc_id = "Ts_001"
        self.tc_desc = "Verify user is able to register into the application"
        self.tc_step = "TC Start"

        registration = RegistrationPage(self.driver)

        self.tc_step = "Launch the url"
        registration.launchUrl(self.url)

        self.tc_step = "Enter the basic registration details"
        registration.clickVendorLogin()
        registration.clickRegisterButton()
        registration.enterBasicRegistrationDetails(self.firstname,self.lastname,self.vendorname,self.fnsnumber,self.primaryemail,self.primaryphno,self.psw,self.cpsw,self.continfo)
        registration.basicRegButton()
        self.tc_step = "Enter the public registration details"
        registration.enterPublicRegistrationDetails(self.publicemail,self.publicphno,self.publicwebsite,self.businessdesc,self.products)
        registration.vendorimg(self.vendorPublicImg)
        registration.publicRegButton()
        self.tc_step = "Enter the location details"
        registration.clickCSAButton()
        registration.clickFarmStandButton()
        registration.clickFarmersMarketBooth()
        registration.clickMobileMarket()
        registration.clickLocationYesButton()
        registration.csalocationTypeDetails(self.pickupsitename,self.adrs1,self.adrs2,self.zipcode,self.spzl_instruction)
        registration.chooseCity()
        registration.clickmonths()
        registration.clickorder()
        registration.starttimeMonday()
        registration.endtimeMonday()
        registration.saveCsa()
        registration.farmstandlocationTypeDetails(self.farmstand_adrs_1,self.farmstand_adrs_2,self.farmstand_zipcode_textbox_id)
        registration.chooseFarmStandCity()
        registration.saveFarmStand()
        registration.choosefarmersmarketboothCity()
        registration.saveFarmersMarketBooth()
        registration.mobileMarketlocationTypeDetails(self.mobileMarkettextboxid)
        registration.choosemobileMarketCity()
        registration.savemobileMarket()

        self.tc_step = "Verification"
        self.assertEqual(registration.verifyRegistration(),"Healthy Incentives Program (HIP)","Login Success")


# Copy these details and add more
@parameterized_class(("url","firstname","lastname","vendorname","fnsnumber","primaryemail","primaryphno","psw","cpsw","continfo","publicemail","publicphno","publicwebsite","businessdesc","products","pickupsitename","adrs1","adrs2","zipcode","spzl_instruction"),[("https://massdtaiot.com/dtahip/","nancy","antony","Nanccy Farms","1234567","nnnnancynnyyy@kyyyyybba.io","9080887878","123","123","boston","nancya@kyyba.com","9080559378","www.massdtaiot.com","Sample desc","Rice","Test Site","123","123","01712","spzl instruction")])

class copyRegistrationDetails(Test_session):
    @pytest.mark.ts_002
    def test_copy_details(self):
        """
        1.launch url
        2.enter registration details
        3.Copy the details
        """
        self.tc_id = "Ts_002"
        self.tc_desc = "Verify the user is able to copy the location type details"
        self.tc_step = "TC Start"

        registration = RegistrationPage(self.driver)

        self.tc_step = "Launch the url"
        registration.launchUrl(self.url)

        self.tc_step = "Enter the basic registration details"
        registration.clickVendorLogin()
        registration.clickRegisterButton()
        registration.enterBasicRegistrationDetails(self.firstname, self.lastname, self.vendorname, self.fnsnumber,
                                                   self.primaryemail, self.primaryphno, self.psw, self.cpsw,
                                                   self.continfo)
        registration.basicRegButton()
        self.tc_step = "Enter the public registration details"
        registration.enterPublicRegistrationDetails(self.publicemail, self.publicphno, self.publicwebsite,
                                                    self.businessdesc, self.products)
        registration.publicRegButton()
        self.tc_step = "Enter the location details"
        registration.clickCSAButton()
        registration.clickLocationYesButton()
        registration.csalocationTypeDetails(self.pickupsitename, self.adrs1, self.adrs2, self.zipcode, self.spzl_instruction)
        registration.chooseCity()
        registration.csacopy()
        registration.addmore()
        registration.remove()
        registration.confirmremove()
        registration.saveonlyCsa()
        self.assertEqual(registration.verifyRegistration(),"Healthy Incentives Program (HIP)","Login Success")


# #Verifying vendor
@parameterized_class(("url","username","password","entervendornameSearch","staffname","staffdesc"),[("https://massdtaiot.com/dtahip/","admin@dtahip","welcome123","Nancy farms","Nancy","For verifying vendor farm")])
class adminloginVerifyVendor(Test_session):
    @pytest.mark.ts_003
    def test_verifyvendordetails(self):
        """
        1.launch url
        2.enter registration details
        3.Copy the details
        """
        self.tc_id = "Ts_003"
        self.tc_desc = "Verify the admin is able to login and verify the vendor"
        self.tc_step = "TC Start"

        login = adminLoginVerify(self.driver)

        self.tc_step = "Launch the url"
        login.launchUrl(self.url)

        self.tc_step = "Enter the login details"
        login.clickVendorLogin()
        login.enterloginDetails(self.username, self.password)
        login.clickLogin()
        login.clickvendorTab()
        login.entervendornameSearch(self.entervendornameSearch)
        login.clickVendor()
        login.verifyVendor()
        login.enterstaffDetails(self.staffname, self.staffdesc)
        login.confirmVerification()


# Manage users add , update delete
@parameterized_class(("url","username","password","userfrstname","userlastname","useremail","editfrstname","editlastname"),[("https://massdtaiot.com/dtahip/","admin@dtahip","welcome123","Nan","ant","nancya@kyyba.com","cy","tony")])
class adminloginManageUser(Test_session):
    @pytest.mark.ts_004
    def test_user_details(self):
        """
        1.launch url
        2.enter registration details
        3.Add user
        """
        self.tc_id = "Ts_004"
        self.tc_desc = "Verify the admin is able to do operation with user"
        self.tc_step = "TC Start"

        user = adminLoginManageuser(self.driver)

        self.tc_step = "Launch the url"
        user.launchUrl(self.url)

        self.tc_step = "Enter the login details"
        user.clickVendorLogin()
        user.enterloginDetails(self.username, self.password)
        user.clickLogin()
        user.clickadminTab()
        user.clickuser()
        user.adduser()
        user.enteruserDetails(self.userfrstname, self.userlastname, self.useremail)
        user.usersubmit()
        user.oksuccess()
        user.clickedituser()
        user.edituserDetails(self.editfrstname, self.editlastname)
        user.userupdate()
        user.userupdateok()
        user.clickdeleteuser()
        user.clickconfirmdelete()
        user.okdelete()

# Manage farmer markets add , update delete

@parameterized_class(("url","username","password","enterfrmrmrktname","enterfrmraddress","enterfrmrmrktzipcode","enterfrmrmrktphone","enterfrmrmrktwebsite","enterfrmrmrktdesc","entermarketnameSearch","editfrmrmrktname","editmarktadrs","importfrmrmrkts"),[("https://massdtaiot.com/dtahip/","admin@dtahip","welcome123","Nancy Antony ","123" ,"01712","9080559378" ,"www.massdta.com","Farmer Market","Nancy Antony","Market"," central street","C:/Users/user/Desktop/Farmers Market.xlsx")])
class adminloginManageFarmerMarkets(Test_session):
    @pytest.mark.ts_005
    def test_farmer_market_details(self):
        """
        1.launch url
        2.enter registration details
        3.Add farmer market
        """
        self.tc_id = "Ts_005"
        self.tc_desc = "Verify the admin is able to do operation with farmer market"
        self.tc_step = "TC Start"

        market = adminloginManageFarmerMarket(self.driver)

        self.tc_step = "Launch the url"
        market.launchUrl(self.url)

        self.tc_step = "Enter the login details"
        market.clickVendorLogin()
        market.enterloginDetails(self.username, self.password)
        market.clickLogin()
        market.clickadminTab()
        market.clickmanagefrmrmrkt()
        market.addfrmrmrkt()
        market.enterfrmrmrktDetails(self.enterfrmrmrktname, self.enterfrmraddress,self.enterfrmrmrktzipcode, self.enterfrmrmrktphone, self.enterfrmrmrktwebsite, self.enterfrmrmrktdesc)
        market.chooseCity()
        market.mrktsubmit()
        market.entermarketnameSearch(self.entermarketnameSearch)
        market.editmrkt()
        market.editmrktDetails(self.editfrmrmrktname, self.editmarktadrs)
        market.mrktupdate()
        market.clickdeletemrkt()
        market.clickconfirmdeletemrkt()
        market.exportfrmrmrkt()
        # market.importfrmrmrkt(self.importfrmrmrkts)
#
# Negative Scenarios goes here
# Login with wrong email id
@parameterized_class(("url","username","password"),[("https://massdtaiot.com/dtahip/","nancy@dtahip","welcome123")])
class adminloginwithwrongemail(Test_session):
    @pytest.mark.ts_006
    def test_wrong_emailid(self):
        """
        1.launch url
        2.Login with wrong email id

        """
        self.tc_id = "Ts_006"
        self.tc_desc = "Verify the admin is able to login with wrong email id"
        self.tc_step = "TC Start"

        incorrectlogin = adminloginwithwrongemailid(self.driver)

        self.tc_step = "Launch the url"
        incorrectlogin.launchUrl(self.url)

        self.tc_step = "Enter the login details"
        incorrectlogin.clickVendorLogin()
        incorrectlogin.enterloginDetails(self.username, self.password)
        incorrectlogin.clickLogin()
        incorrectlogin.verifyLogin()
        self.assertEqual(incorrectlogin.verifyLogin(), " DTA HIP Admin ", "Login Failed")

#Login without @ Symbol

@parameterized_class(("url","username","password"),[("https://massdtaiot.com/dtahip/","nancydtahip","welcome123")])
class adminloginwithoutatSym(Test_session):
    @pytest.mark.ts_007
    def test_without_charecter(self):
        """
        1.launch url
        2.Login without @ Symbol

        """
        self.tc_id = "Ts_007"
        self.tc_desc = "Verify the admin is able to login with wrong email id"
        self.tc_step = "TC Start"

        withoutcharacter = adminloginwithoutatSymbol(self.driver)

        self.tc_step = "Launch the url"
        withoutcharacter.launchUrl(self.url)

        self.tc_step = "Enter the login details"
        withoutcharacter.clickVendorLogin()
        withoutcharacter.enterloginDetails(self.username, self.password)
        withoutcharacter.clickLogin()
        self.assertEqual(withoutcharacter.verifyLogin(), " DTA HIP Admin ", "Login Failed")

#Login without entering required fields
@parameterized_class(("url","password"),[("https://massdtaiot.com/dtahip/","welcome123")])
class adminloginwithoutreqdfield(Test_session):
    @pytest.mark.ts_008
    def test_without_rqdfield(self):
        """
        1.launch url
        2.Login without required field

        """
        self.tc_id = "Ts_007"
        self.tc_desc = "Verify the admin is able to login without required field"
        self.tc_step = "TC Start"

        withoutcharacter = adminloginwithoutrqdfield(self.driver)

        self.tc_step = "Launch the url"
        withoutcharacter.launchUrl(self.url)

        self.tc_step = "Enter the login details"
        withoutcharacter.clickVendorLogin()
        withoutcharacter.enterloginDetails(self.password)
        withoutcharacter.clickLogin()
        self.assertEqual(withoutcharacter.verifyLogin(), " DTA HIP Admin ", "Login Failed")

#Register with existing email id
@parameterized_class(("url","firstname","lastname","vendorname","fnsnumber","primaryemail","primaryphno","psw","cpsw","continfo"),[("https://massdtaiot.com/dtahip/","nancy","antony","Nancy Farms","1234567","nancya@kyyba.com","9080887878","123","123","boston")])
class Registrationwithoutemail(Test_session) :
    @pytest.mark.ts_009

    def test_valid_credentials(self):
        """
        1.launch url
        2.enter registration details
        3.register with existing email id
        """
        self.tc_id = "Ts_009"
        self.tc_desc = "Verify user is able to register into the application with existing email id"
        self.tc_step = "TC Start"

        registration = Registrationwithoutemailid(self.driver)

        self.tc_step = "Launch the url"
        registration.launchUrl(self.url)

        self.tc_step = "Enter the basic registration details"
        registration.clickVendorLogin()
        registration.clickRegisterButton()
        registration.enterBasicRegistrationDetails(self.firstname,self.lastname,self.vendorname,self.fnsnumber,self.primaryemail,self.primaryphno,self.psw,self.cpsw,self.continfo)
        registration.basicRegButton()
        # self.assertEqual(registration.verifyReg(), "Public Info", "Registration Failed")

# #Verify the vendor without providing city
@parameterized_class(("url","firstname","lastname","vendorname","fnsnumber","primaryemail","primaryphno","psw","cpsw","continfo","pickupsitename","adrs1","adrs2","zipcode","username","password"),[("https://massdtaiot.com/dtahip/","nancy","antony","Nancy Farms","1234567","nannbbananabbncyyy@kyybba.io","9080887878","123","123","boston","Test Site","123","123","01712","admin@dtahip","welcome123")])
class adminloginVerifyVendorwithoutcity(Test_session):
    @pytest.mark.ts_010
    def test_verifywithout_city(self):
        """
        1.launch url
        2.enter registration details
        3.Copy the details
        """
        self.tc_id = "Ts_010"
        self.tc_desc = "Verify the admin is able to login and verify the vendor"
        self.tc_step = "TC Start"

        registration = adminLoginVerifywithoutcity(self.driver)

        self.tc_step = "Launch the url"
        registration.launchUrl(self.url)

        self.tc_step = "Enter the login details"
        registration.clickVendorLogin()
        registration.clickRegisterButton()
        registration.enterBasicRegistrationDetails(self.firstname, self.lastname, self.vendorname, self.fnsnumber,
                                                   self.primaryemail, self.primaryphno, self.psw, self.cpsw,
                                                   self.continfo)
        registration.basicRegButton()
        self.tc_step = "Enter the public registration details"
        registration.enterPublicRegistrationDetails(self.publicemail, self.publicphno, self.publicwebsite,
                                                    self.businessdesc, self.products)
        registration.publicRegButton()
        self.tc_step = "Enter the location details"
        registration.clickCSAButton()

        registration.clickLocationYesButton()
        registration.csalocationTypeDetails(self.pickupsitename, self.adrs1, self.adrs2, self.zipcode)

        registration.saveCsa()
        login = adminLoginVerify(self.driver)

        self.tc_step = "Launch the url"
        login.launchUrl(self.url)

        self.tc_step = "Enter the login details"
        login.clickVendorLogin()
        login.enterloginDetails(self.username, self.password)
        login.clickLogin()
        login.clickvendorTab()
        login.clickVendor()
        login.verifyVendor()

# Search by city
class searchbycity(Test_session) :
    @pytest.mark.ts_011

    def test_search_city(self):
        """
        1.launch url
        2.search by city
        """
        self.tc_id = "Ts_011"
        self.tc_desc = "Verify user is able to register into the application with existing email id"
        self.tc_step = "TC Start"

        searchbycity = SearchCity(self.driver)

        self.tc_step = "Launch the url"
        searchbycity.launchUrl("https://massdtaiot.com/dtahip/")

        self.tc_step ="Search the city"
        searchbycity.chooseActon()
        # searchbycity.chooseVendor()

#Clear Search
class clearSearch(Test_session) :
    @pytest.mark.ts_012
    def test_click_clearsearch(self):
        """
        1.launch url
        2.click clear search
        """
        self.tc_id = "Ts_012"
        self.tc_desc = "Verify user is able to register into the application with existing email id"
        self.tc_step = "TC Start"

        clearSearch = Clearsearch(self.driver)

        self.tc_step = "Launch the url"
        clearSearch.launchUrl("https://massdtaiot.com/dtahip/")

        self.tc_step = "Check the clear search button"
        clearSearch.clickClearsearch()

# Location Types
class clickLocationtypes(Test_session) :
    @pytest.mark.ts_013
    def test_click_Locationtypes(self):
        """
        1.launch url
        2.Click Location Type
        """
        self.tc_id = "Ts_013"
        self.tc_desc = "Verify user is able to click Location types"
        self.tc_step = "TC Start"

        clickLocationTypes = ClickLocationTypes(self.driver)

        self.tc_step = "Launch the url"
        clickLocationTypes.launchUrl("https://massdtaiot.com/dtahip/")
        self.tc_step = "Select all cities"
        clickLocationTypes.allcities()
        self.tc_step = "Click the HIP CSA filter"
        clickLocationTypes.clickHIPCSALoc()
        clickLocationTypes.clickonLegend()
        clickLocationTypes.clickHIPFarmStandLoc()
        clickLocationTypes.clickonLegend()
        clickLocationTypes.clickHIPFarmerMarketBoothLoc()
        clickLocationTypes.clickonLegend()
        clickLocationTypes.clickHIPMobileMarketLoc()
        clickLocationTypes.clickonLegend()
        clickLocationTypes.clickHIPFarmerMarketLoc()

class clickorderOptions(Test_session) :
    @pytest.mark.ts_014
    def test_click_orderoptions(self):
        """
        1.launch url
        2.Click order option
        """
        self.tc_id = "Ts_014"
        self.tc_desc = "Verify user is able to check order options"
        self.tc_step = "TC Start"

        clickorder = clickOrderOptions(self.driver)

        self.tc_step = "Launch the url"
        clickorder.launchUrl("https://massdtaiot.com/dtahip/")
        self.tc_step = "Select all cities"
        clickorder.allcities()
        self.tc_step = "Click the HIP CSA filter"
        clickorder.unselectOrderOptions()
        clickorder.unselectOrderOption()

class clickMonthOptionss(Test_session) :
    @pytest.mark.ts_015
    def test_click_MonthOptions(self):
        """
        1.launch url
        2.Click Location Type
        """
        self.tc_id = "Ts_015"
        self.tc_desc = "Verify user is able to click Location types"
        self.tc_step = "TC Start"

        clickLocationTypes = clickMonthOptions(self.driver)

        self.tc_step = "Launch the url"
        clickLocationTypes.launchUrl("https://massdtaiot.com/dtahip/")
        self.tc_step = "Select all cities"
        clickLocationTypes.allcities()
        self.tc_step = "Click the HIP CSA filter"
        clickLocationTypes.clickMonthOption()
        clickLocationTypes.unselectMonthOptions()

class clickDaysOperations(Test_session) :
    @pytest.mark.ts_016
    def test_click_daysOptions(self):
        """
        1.launch url
        2.Click Location Type
        """
        self.tc_id = "Ts_016"
        self.tc_desc = "Verify user is able to click Location types"
        self.tc_step = "TC Start"

        clickLocationTypes = clickDaysOperation(self.driver)

        self.tc_step = "Launch the url"
        clickLocationTypes.launchUrl("https://massdtaiot.com/dtahip/")
        self.tc_step = "Select all cities"
        clickLocationTypes.allcities()
        self.tc_step = "Click the HIP CSA filter"
        clickLocationTypes.clickdaysOption()
        clickLocationTypes.unselectdaysOption()

class clickOpenTodays(Test_session) :
    @pytest.mark.ts_017
    def test_click_OpenToday(self):
        """
        1.launch url
        2.Click Location Type
        """
        self.tc_id = "Ts_017"
        self.tc_desc = "Verify user is able to click Location types"
        self.tc_step = "TC Start"

        clickLocationTypes = clickOpenToday(self.driver)

        self.tc_step = "Launch the url"
        clickLocationTypes.launchUrl("https://massdtaiot.com/dtahip/")
        self.tc_step = "Select all cities"
        clickLocationTypes.allcities()
        self.tc_step = "Click the HIP CSA filter"
        clickLocationTypes.clickopentoday()
@parameterized_class(("url","username","password","entercomment","entereditcomment"),[("https://massdtaiot.com/dtahip/","admin@dtahip","welcome123", "Verify this ", "Vendor")])
class commentFeature(Test_session):
    @pytest.mark.ts_018
    def test_add_comment(self):
        """
        1.launch url
        2.Login as admin
        3.Go to vendor and add , edit , delete comments
        """
        self.tc_id = "Ts_018"
        self.tc_desc = "Verify the admin is able to add the comment"
        self.tc_step = "TC Start"

        comment = commentFeatures(self.driver)

        self.tc_step = "Launch the url"
        comment.launchUrl(self.url)

        self.tc_step = "Enter the login details"
        comment.clickVendorLogin()
        comment.enterloginDetails(self.username, self.password)
        comment.clickLogin()
        comment.clickvendorTab()
        comment.clickVendor()
        comment.clickAddComment()
        comment.entercomment(self.entercomment)
        comment.savecomment()
        comment.clickeditcomment()
        comment.entereditcomment(self.entereditcomment)
        comment.updatecomment()
        comment.deletecomment()
        comment.confirmremovecomment()
# Edit vendor
@parameterized_class(("url","username","password","editFirstName","editLastName", "primaryEmail"),[("https://massdtaiot.com/dtahip/","admin@dtahip","welcome123","y","s","m")])
class vendorEditFeature(Test_session):
    @pytest.mark.ts_019
    def test_editVendor(self):
        """
        1.launch url
        2.Login as admin

        3.Go to vendor and edit and update vendors
        """
        self.tc_id = "019"
        self.tc_desc = "Verify the admin is able to edit and update delete the vendor"
        self.tc_step = "TC Start"

        vendoredit = vendoreditFeatures(self.driver)

        self.tc_step = "Launch the url"
        vendoredit.launchUrl(self.url)

        self.tc_step = "Enter the login details"
        vendoredit.clickVendorLogin()
        vendoredit.enterloginDetails(self.username, self.password)
        vendoredit.clickLogin()
        vendoredit.clickvendorTab()
        vendoredit.clickVendor()
        vendoredit.clickeditvendor()
        vendoredit.entereditvendor(self.editFirstName,self.editLastName)
        vendoredit.updatevendor()
        vendoredit.clickvendorTab()
        vendoredit.clickeditPrimaryEmail()
        vendoredit.entereditPrimaryEmail(self.primaryEmail)
        vendoredit.updatePrimaryEmail()
        vendoredit.updatePrimaryEmailOk()
        vendoredit.clickeditvendorlastupdatedtime()
        vendoredit.clickpicktime()
        vendoredit.picktime()
        vendoredit.picktimeapply()
        vendoredit.picktimeUpdate()
        # vendoredit.deletevendor()
        # vendoredit.confirmremovevendor()
        # vendoredit.confirmremovevendorok()
        vendoredit.viewmore()
        vendoredit.viewmoreClose()
        vendoredit.activeCheckvendor()
        vendoredit.verifiedCheckvendor()
        vendoredit.followupvendor()
        vendoredit.followupvendorok()


# #
# # Active and inactive list of vendors
# @parameterized_class(("url","username","password","entervendornameSearch"),[("https://massdtaiot.com/dtahip/","admin@dtahip","welcome123","Merlin Antony Farms")])
# class vendoractiveInactivelist(Test_session):
#     @pytest.mark.ts_020
#     def test_vendorStatus(self):
#         """
#         1.launch url
#         2.Login as admin
#         3.Check active and inactive list of vendors
#         """
#         self.tc_id = "020"
#         self.tc_desc = "Verify the admin is able to check active and inactive list of vendors"
#         self.tc_step = "TC Start"
#
#         vendoredit = vendoreditFeatures(self.driver)
#
#         self.tc_step = "Launch the url"
#         vendoredit.launchUrl(self.url)
#
#         self.tc_step = "Enter the login details"
#         vendoredit.clickVendorLogin()
#         vendoredit.enterloginDetails(self.username, self.password)
#         vendoredit.clickLogin()
#         vendoredit.clickvendorTab()
#         vendoredit.entervendornameSearch(self.entervendornameSearch)
#         vendoredit.selectVendor()
#         vendoredit.inactiveClick()
#         vendoredit.inactiveok()
#         vendoredit.entervendornameSearch(self.entervendornameSearch)
#         vendoredit.selectVendor()
#         vendoredit.activeClick()
#         vendoredit.inactiveok()
#         vendoredit.entervendornameSearch(self.entervendornameSearch)
#         vendoredit.clickVendor()
#         vendoredit.toggleinactive()
#         vendoredit.toggleconfirmationyes()
#         vendoredit.toggleactive()
#         vendoredit.toggleconfirmationyes()
#         vendoredit.clickvendorTab()
#         vendoredit.entervendornameSearch(self.entervendornameSearch)
#         vendoredit.toggleinactivevendor()
#         vendoredit.toggleactivevendor()
#
# # Export
# @parameterized_class(("url","username","password"),[("https://massdtaiot.com/dtahip/","admin@dtahip","welcome123")])
# class vendorexportcheck(Test_session):
#     @pytest.mark.ts_021
#     def test_editVendor(self):
#         """
#         1.launch url
#         2.Login as admin
#
#         3.Go to vendor and edit and update vendors
#         """
#         self.tc_id = "021"
#         self.tc_desc = "Verify the admin is able to export 3 types of export"
#         self.tc_step = "TC Start"
#
#         vendoredit = vendoreditFeatures(self.driver)
#
#         self.tc_step = "Launch the url"
#         vendoredit.launchUrl(self.url)
#
#         self.tc_step = "Enter the login details"
#         vendoredit.clickVendorLogin()
#         vendoredit.enterloginDetails(self.username, self.password)
#         vendoredit.clickLogin()
#         vendoredit.clickvendorTab()
#         vendoredit.exportClick()
#         vendoredit.exportverifiedVendors()
#         vendoredit.vendorrefresh()
#         vendoredit.exportClick()
#         vendoredit.exportlastupdatedTime()
#         vendoredit.vendorrefresh()
#         vendoredit.exportClick()
#         vendoredit.exportlastlogindays()
#         vendoredit.vendorrefresh()

#Whole search in admin side
# @parameterized_class(("url","username","password","entervendornameSearch","entervendorfnsSearch","entervendormobileSearch","entervendoremailSearch","entervendorfnameSearch","entervendorlnameSearch","entermarketnameSearch","enterusernameSearch","enteruseremailSearch"),[("https://massdtaiot.com/dtahip/","admin@dtahip","welcome123","Nancy farms","1234567","9080559378","nancya@kyyba.com","nancy","antony","Alex","nancy","nancya@boodskap.io")])
# class wholeSearch(Test_session):
#     @pytest.mark.ts_022
#     def test_adminwholeSearchFunction(self):
#         """
#         1.launch url
#         2.Login as admin
#         3.Check whether all search is working
#         """
#         self.tc_id = "022"
#         self.tc_desc = "Verify the admin is able to search"
#         self.tc_step = "TC Start"
#
#         search = adminSearchFunctions(self.driver)
#
#         self.tc_step = "Launch the url"
#         search.launchUrl(self.url)
#
#         self.tc_step = "Enter the login details"
#         search.clickVendorLogin()
#         search.enterloginDetails(self.username, self.password)
#         search.clickLogin()
#         search.clickvendorTab()
#         search.entervendornameSearch(self.entervendornameSearch)
#         search.vendorrefresh()
#         search.entervendorfnsSearch(self.entervendorfnsSearch)
#         search.vendorrefresh()
#         search.entervendormobileSearch(self.entervendormobileSearch)
#         search.vendorrefresh()
#         search.entervendoremailSearch(self.entervendoremailSearch)
#         search.vendorrefresh()
#         search.entervendorfnameSearch(self.entervendorfnameSearch)
#         search.vendorrefresh()
#         search.entervendorlnameSearch(self.entervendorlnameSearch)
#         search.vendorrefresh()
#         search.clickadminTab()
#         search.clickmanagefrmrmrkt()
#         search.marketrefresh()
#         search.entermarketnameSearch(self.entermarketnameSearch)
#         search.clickadminTab()
#         search.clickuser()
#         search.enterusernameSearch(self.enterusernameSearch)
#         search.clickLogoutTab()
#         search.clickLogout()
#
# # Login via registered user
# @parameterized_class(("url","username","password"),[("https://massdtaiot.com/dtahip/","nancya@kyyba.com","welcome123")])
# class loginviaregisteredvendor(Test_session):
#     @pytest.mark.ts_023
#     def test_without_charecter(self):
#         """
#         1.launch url
#         2.Login with registered vendor
#
#         """
#         self.tc_id = "Ts_023"
#         self.tc_desc = "Verify the vendor is able to login"
#         self.tc_step = "TC Start"
#
#         withoutcharacter = adminloginwithoutatSymbol(self.driver)
#
#         self.tc_step = "Launch the url"
#         withoutcharacter.launchUrl(self.url)
#
#         self.tc_step = "Enter the login details"
#         withoutcharacter.clickVendorLogin()
#         withoutcharacter.enterloginDetails(self.username, self.password)
#         withoutcharacter.clickLogin()
#
#
# # Language check
# @parameterized_class(("url"),[("https://massdtaiot.com")])
# class languageCheck(Test_session):
#     @pytest.mark.ts_024
#     def test_language(self):
#         """
#         1.launch url
#         2.Login with registered vendor
#
#         """
#         self.tc_id = "Ts_024"
#         self.tc_desc = "Verify the vendor is able to login"
#         self.tc_step = "TC Start"
#
#         languageCheck = languagetranslationCheck(self.driver)
#
#         self.tc_step = "Launch the url"
#         languageCheck.launchUrl("https://massdtaiot.com")
#
#         languageCheck.clickHipVendors()
#         languageCheck.choosePortuguese()
#         languageCheck.chooseChinese()
#         languageCheck.chooseSpanish()
#         languageCheck.chooseVietnamese()
#
#
# # Search by vendor
# class searchbyVendor(Test_session) :
#     @pytest.mark.ts_025
#
#     def test_search_vendor(self):
#         """
#         1.launch url
#         2.search by city
#         """
#         self.tc_id = "Ts_025"
#         self.tc_desc = "Verify user is able to register into the application with existing email id"
#         self.tc_step = "TC Start"
#
#         searchbyVendor = SearchCity(self.driver)
#
#         self.tc_step = "Launch the url"
#         searchbyVendor.launchUrl("https://massdtaiot.com/dtahip/")
#
#         self.tc_step ="Search the vendor"
#         searchbyVendor.chooseActon()
#         searchbyVendor.chooseVendor()
#
# # Export and sorting in map page
# class exportandSort(Test_session) :
#     @pytest.mark.ts_026
#
#     def test_map_export(self):
#         """
#         1.launch url
#         2.search by city
#         """
#         self.tc_id = "Ts_026"
#         self.tc_desc = "Verify user is able to register into the application with existing email id"
#         self.tc_step = "TC Start"
#
#         searchbyVendor = SearchCity(self.driver)
#
#         self.tc_step = "Launch the url"
#         searchbyVendor.launchUrl("https://massdtaiot.com/dtahip/")
#
#         self.tc_step ="Search the vendor"
#         searchbyVendor.chooseActon()
#         searchbyVendor.clickmapexport()
#         searchbyVendor.sortUp()
#         searchbyVendor.sortDown()
#
# @parameterized_class(("url","username","password","entervendornameSearch","editFirstName","editLastName", "primaryEmail"),[("https://massdtaiot.com/dtahip/","admin@dtahip","welcome123","nancy farm","y","s","m")])
# class vendorLocEditFeature(Test_session):
#     @pytest.mark.ts_027
#     def test_LocEditFeature(self):
#         """
#         1.launch url
#         2.Login as admin
#
#         3.Go to vendor and edit and update vendors
#         """
#         self.tc_id = "027"
#         self.tc_desc = "Verify the admin is able to edit and update delete the vendor"
#         self.tc_step = "TC Start"
#
#         vendoredit = vendoreditFeatures(self.driver)
#
#         self.tc_step = "Launch the url"
#         vendoredit.launchUrl(self.url)
#
#         self.tc_step = "Enter the login details"
#         vendoredit.clickVendorLogin()
#         vendoredit.enterloginDetails(self.username, self.password)
#         vendoredit.clickLogin()
#         vendoredit.clickvendorTab()
#         vendoredit.entervendornameSearch(self.entervendornameSearch)
#         vendoredit.clickVendor()
#         vendoredit.clickeditvendor()
#         vendoredit.entereditvendor(self.editFirstName,self.editLastName)
#         vendoredit.updatevendor()
#         vendoredit.clickvendorTab()
#         vendoredit.entervendornameSearch(self.entervendornameSearch)
#         vendoredit.clickVendor()
#         vendoredit.clickLoc()
#         vendoredit.changecity()
#         vendoredit.vendorUpdate()
# #
# @parameterized_class(("url","firstname","lastname","vendorname","fnsnumber","primaryemail","primaryphno","psw","cpsw","continfo","publicemail","publicphno","publicwebsite","businessdesc","products","vendorPublicImg","farmermarket_mngr_spzlInst"),[("https://massdtaiot.com/dtahip/","nancy","antony","Nancy Farms","1234567","nannnbbananabbncyyy@kyybbba.io","9080887878","123","123","boston","nancya@kyyba.com","9080559378","www.massdtaiot.com","Sample desc","Rice","C:/Users/user/Desktop/vendorImg.jpg","Test instruction")])
# # #Farmer market Registration
# class FarmerMarketRegistrationClass(Test_session) :
#     @pytest.mark.ts_028
#     def test_farmers_market(self):
#         """
#         1.launch url
#         2.enter registration details
#         3.verify login credential
#         """
#         self.tc_id = "Ts_028"
#         self.tc_desc = "Verify market manager is able to register into the application"
#         self.tc_step = "TC Start"
#
#         registration = RegistrationPage(self.driver)
#
#         self.tc_step = "Launch the url"
#         registration.launchUrl(self.url)
#
#         self.tc_step = "Enter the basic registration details"
#         registration.clickVendorLogin()
#         registration.clickRegisterButton()
#         registration.enterBasicRegistrationDetails(self.firstname,self.lastname,self.vendorname,self.fnsnumber,self.primaryemail,self.primaryphno,self.psw,self.cpsw,self.continfo)
#         registration.basicRegButton()
#         self.tc_step = "Enter the public registration details"
#         registration.enterPublicRegistrationDetails(self.publicemail,self.publicphno,self.publicwebsite,self.businessdesc,self.products)
#         registration.vendorimg(self.vendorPublicImg)
#         registration.publicRegButton()
#         self.tc_step = "Enter the location details"
#         registration.clickFarmerMarketManger()
#         registration.clickLocationYesButton()
#         registration.clickFarmerMarketMangerSpzlinst(self.farmermarket_mngr_spzlInst)
#         registration.clickFarmerMarketMangersave()
#         registration.chooseFarmerMarket()
#         registration.clickFarmerMarketMangersave()
#         self.tc_step = "Verification"
#         self.assertEqual(registration.verifyRegistration(),"Healthy Incentives Program (HIP)","Login Success")
#
#
# @parameterized_class(("url","username","password"),[("https://massdtaiot.com/dtahip/","admin@dtahip","welcome123")])
# class wholeauditLogs(Test_session):
#     @pytest.mark.ts_029
#     def test_adminauditFunction(self):
#         """
#         1.launch url
#         2.Login as admin
#         3.Check whether all audit page functionality working
#         """
#         self.tc_id = "022"
#         self.tc_desc = "Verify the admin is able to "
#         self.tc_step = "TC Start"
#
#         auditlogs = adminSearchFunctions(self.driver)
#
#         self.tc_step = "Launch the url"
#         auditlogs.launchUrl(self.url)
#
#         self.tc_step = "Enter the login details"
#         auditlogs.clickVendorLogin()
#         auditlogs.enterloginDetails(self.username, self.password)
#         auditlogs.clickLogin()
#         auditlogs.clickadminTab()
#         auditlogs.clickaudit()
#         auditlogs.chooseLoginLogs()
#         auditlogs.clickLogoutTab()
#         auditlogs.clickLogout()
#
#
