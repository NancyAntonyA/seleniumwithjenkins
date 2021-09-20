from Locators.locators import locatorsClass
import time
from WebActions.webactions import webActionClassOne
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

class RegistrationPage(webActionClassOne):
    def launchUrl(self,url):
        time.sleep(4)
        self.getUrl(url)

    def clickVendorLogin(self):
        time.sleep(4)
        self.click(locatorsClass.vendor_login_button)

    def clickRegisterButton(self):
        time.sleep(2)
        self.click(locatorsClass.vendor_register_button)

    def enterBasicRegistrationDetails(self,firstname,lastname,vendorname,fnsnumber,primaryemail,primaryphno,psw,cpsw,continfo):
        self.type(locatorsClass.firstname_textbox_id,firstname)
        time.sleep(1)
        self.type(locatorsClass.lastname_textbox_id, lastname)
        time.sleep(1)
        self.type(locatorsClass.vendorname_textbox_id, vendorname)
        time.sleep(1)
        self.type(locatorsClass.fns_textbox_id, fnsnumber)
        time.sleep(1)
        self.type(locatorsClass.primaryemailaddress_textbox_id, primaryemail)
        time.sleep(1)
        self.type(locatorsClass.primaryphonenumber_textbox_id, primaryphno)
        time.sleep(1)
        self.type(locatorsClass.password_textbox_id, psw)
        time.sleep(1)
        self.type(locatorsClass.confirmpassword_textbox_id, cpsw)
        time.sleep(1)
        self.type(locatorsClass.additionalcontact_textbox_id, continfo)
        time.sleep(1)

    def basicRegButton(self):
        time.sleep(2)
        self.click(locatorsClass.register_button_id)
        time.sleep(4)
    def enterPublicRegistrationDetails(self,publicemail,publicphno,publicwebsite,businessdesc,products):
        time.sleep(5)
        self.type(locatorsClass.publicemailaddress_textbox_id,publicemail)
        time.sleep(1)
        self.type(locatorsClass.publicphonenumber_textbox_id, publicphno)
        time.sleep(1)
        self.type(locatorsClass.publicwebsite_textbox_id, publicwebsite)
        time.sleep(1)
        self.type(locatorsClass.businessdesc_textbox_id, businessdesc)
        time.sleep(1)
        self.type(locatorsClass.products_textbox_id, products)
        time.sleep(1)
    def vendorimg(self,vendorPublicImg ):
        time.sleep(2)
        self.type(locatorsClass.vendorPublicImg, vendorPublicImg)

    def publicRegButton(self):
        time.sleep(2)
        self.click(locatorsClass.saveandnext_button_id)
        time.sleep(2)
    def clickCSAButton(self):
        time.sleep(8)
        self.click(locatorsClass.csa_radiobutton_id)

    def clickFarmStandButton(self):
        time.sleep(4)
        self.click(locatorsClass.farmstand_radiobutton_id)

    def clickFarmersMarketBooth(self):
        time.sleep(3)
        self.click(locatorsClass.farmersmarketbooth_radiobutton_id)

    def clickMobileMarket(self):
        time.sleep(3)
        self.click(locatorsClass.mobilemarket_radiobutton_id)
    def clickFarmerMarketManger(self):
        time.sleep(2)
        self.click(locatorsClass.farmermarket_mngr)

    def clickLocationYesButton(self):
        time.sleep(5)
        self.click(locatorsClass.locationtype_saveandnext_button_id)
    def csalocationTypeDetails(self, pickupsitename,adrs1,adrs2,zipcode,spzl_instruction):
        self.type(locatorsClass.pickupsite_textbox_id, pickupsitename)
        time.sleep(1)
        self.type(locatorsClass.adrs_1, adrs1)
        time.sleep(1)
        self.type(locatorsClass.adrs_2, adrs2)
        time.sleep(1)
        self.type(locatorsClass.zipcode_textbox_id, zipcode)
        time.sleep(1)
        self.type(locatorsClass.spzl_instruction, spzl_instruction)
        time.sleep(1)
    def starttimeMonday(self):
        time.sleep(3)
        self.choose(locatorsClass.starttimeMonday_CSA, "10:30")
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_xpath("//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[8]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/select[1]"))
        # select by select_by_visible_text() method
        sel.select_by_visible_text("10:30")
    def endtimeMonday(self):
        time.sleep(3)
        self.choose(locatorsClass.endtimeMonday_CSA, "10:30")
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_xpath("//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[8]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/select[1]"))
        # select by select_by_visible_text() method
        sel.select_by_visible_text("10:30")
    def chooseCity(self):
        time.sleep(3)
        self.choose(locatorsClass.select_citydropdown_id, "Acton")
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_xpath("//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[2]/div[3]/select[1]"))
        # select by select_by_visible_text() method
        sel.select_by_visible_text("Acton")
        time.sleep(2)

    def verifyRegistration(self):
        getTextVar = self.getText(locatorsClass.regsuccessmsg)
        return getTextVar
    def csacopy(self):
        time.sleep(4)
        self.click(locatorsClass.csa_copy)
    def addmore(self):
        time.sleep(4)
        self.click(locatorsClass.addmore)
    def remove(self):
        time.sleep(4)
        self.click(locatorsClass.remove)
    def confirmremove(self):
        time.sleep(4)
        self.click(locatorsClass.confirmremove)
    def clickmonths(self):
        time.sleep(6)
        self.click(locatorsClass.months_of_operation_june)
    def clickorder(self):
        time.sleep(6)
        self.click(locatorsClass.order_option_delivery)
    def saveCsa(self):
        time.sleep(4)
        self.click(locatorsClass.csa_saveandnext_button)
        time.sleep(4)
    def saveonlyCsa(self):
        time.sleep(4)
        self.click(locatorsClass.saveonlycsa)

    def farmstandlocationTypeDetails(self,farmstand_adrs_1,farmstand_adrs_2,farmstand_zipcode_textbox_id):
        time.sleep(1)
        self.type(locatorsClass.farmstand_adrs_1, farmstand_adrs_1)
        time.sleep(1)
        self.type(locatorsClass.farmstand_adrs_2, farmstand_adrs_2)
        time.sleep(1)
        self.type(locatorsClass.farmstand_zipcode_textbox_id, farmstand_zipcode_textbox_id)
        time.sleep(1)

    def chooseFarmStandCity(self):
        time.sleep(5)
        self.choose(locatorsClass.farmstand_select_citydropdown_id, "Acton")
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_xpath("//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[5]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[1]/div[3]/select[1]"))
        # select by select_by_visible_text() method
        sel.select_by_visible_text("Acton")
        time.sleep(2)

    def saveFarmStand(self):
        time.sleep(3)
        self.click(locatorsClass.farmstand_saveandnext_button)
        time.sleep(3)

    def choosefarmersmarketboothCity(self):
        time.sleep(7)
        self.choose(locatorsClass.farmersmarketbooth_select_citydropdown_id, "Amal's Markett")
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_xpath("//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[6]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[1]/div[1]/div[1]/select[1]"))
        # select by select_by_visible_text() method
        sel.select_by_visible_text("Amal's Markett")
        time.sleep(2)

    def saveFarmersMarketBooth(self):
        time.sleep(4)
        self.click(locatorsClass.farmersmarketbooth_saveandnext_button)
        time.sleep(4)
    def mobileMarketlocationTypeDetails(self, mobileMarkettextboxid):
        time.sleep(4)
        self.type(locatorsClass.mobileMarket_textbox_id, mobileMarkettextboxid)
        time.sleep(2)

    def choosemobileMarketCity(self):
        time.sleep(7)
        self.choose(locatorsClass.mobileMarket_select_citydropdown_id, "Abington")
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_xpath("//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[7]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[2]/div[3]/select[1]"))
        # select by select_by_visible_text() method
        sel.select_by_visible_text("Abington")
        time.sleep(2)

    def allcities(self):
        time.sleep(7)
        self.choose(locatorsClass.allcities, "All Counties and Cities")
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_xpath("//body[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/select[1]"))
        # select by select_by_visible_text() method
        sel.select_by_visible_text("All Counties and Cities")
        time.sleep(2)

    def savemobileMarket(self):
        time.sleep(4)
        self.click(locatorsClass.mobileMarket_saveandnext_button)

    def chooseFarmerMarket(self):
        time.sleep(7)
        self.choose(locatorsClass.farmermarket_mngr_market, "Acton-Boxborough Farmers' Market Booth")
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_xpath("//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[8]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[1]/div[1]/div[1]/select[1]"))
        # select by select_by_visible_text() method
        sel.select_by_visible_text("Acton-Boxborough Farmers' Market Booth")
        time.sleep(2)
    def clickFarmerMarketMangersave(self):
        time.sleep(2)
        self.click(locatorsClass.farmermarket_mngr_market_Save)
    def clickFarmerMarketMangerSpzlinst(self,farmermarket_mngr_spzlInst):
        time.sleep(2)
        self.type(locatorsClass.farmermarket_mngr_spzlInst,farmermarket_mngr_spzlInst)

    # def verifyLogin(self):
    #     getTextVar =  self.getText(locatorsClass.loginsuccessmsg)
    #     return getTextVar

class adminLoginVerify(webActionClassOne):
    def launchUrl(self,url):
        time.sleep(5)
        self.getUrl(url)

    def clickVendorLogin(self):
        time.sleep(5)
        self.click(locatorsClass.vendor_login_button)
    def enterloginDetails(self ,username,password):
        time.sleep(3)
        self.type(locatorsClass.username, username)
        time.sleep(2)
        self.type(locatorsClass.password,password)
    def clickLogin(self):
        time.sleep(5)
        self.click(locatorsClass.loginbtn)
        time.sleep(7)
    def clickvendorTab(self):
        time.sleep(7)
        self.click(locatorsClass.vendorTab)
        time.sleep(7)
    def entervendornameSearch(self,entervendornameSearch):
        time.sleep(2)
        self.type(locatorsClass.searchvendorAdmin, entervendornameSearch)
    def clickVendor(self):
        time.sleep(7)
        self.click(locatorsClass.clickVendor)
        time.sleep(7)
    def verifyVendor(self):
        time.sleep(5)
        self.click(locatorsClass.verifyVendor)
    def enterstaffDetails(self ,staffname,staffdesc):
        time.sleep(3)
        self.type(locatorsClass.staffname, staffname)
        time.sleep(2)
        self.type(locatorsClass.staffdesc,staffdesc)
    def confirmVerification(self):
        time.sleep(2)
        self.click(locatorsClass.confirmVerification)
    def allcities(self):
        time.sleep(7)
        self.choose(locatorsClass.allcities, "All Counties and Cities")
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_xpath("//body[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/select[1]"))
        # select by select_by_visible_text() method
        sel.select_by_visible_text("All Counties and Cities")
        time.sleep(2)

    def searchvendor(self):
        time.sleep(7)
        self.choose(locatorsClass.searchvendor, "Nancy Nickita Farms")
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_xpath("//body[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[7]/select[1]"))
        # select by select_by_visible_text() method
        sel.select_by_visible_text("Nancy Nickita Farms")
        time.sleep(2)

    def reloadPage(self):
        time.sleep(5)
        self.page_load(locatorsClass.allcities)

class adminLoginManageuser(webActionClassOne):
    def launchUrl(self,url):
        time.sleep(4)
        self.getUrl(url)

    def clickVendorLogin(self):
        time.sleep(4)
        self.click(locatorsClass.vendor_login_button)
    def enterloginDetails(self ,username,password):
        time.sleep(2)
        self.type(locatorsClass.username, username)
        time.sleep(2)
        self.type(locatorsClass.password,password)
    def clickLogin(self):
        time.sleep(3)
        self.click(locatorsClass.loginbtn)
        time.sleep(5)
    def clickadminTab(self):
        time.sleep(4)
        self.click(locatorsClass.administration)
        time.sleep(5)
    def clickuser(self):
        time.sleep(5)
        self.click(locatorsClass.manageusers)

    def adduser(self):
        time.sleep(3)
        self.click(locatorsClass.addUser)
    def enteruserDetails(self ,userfrstname,userlastname,useremail):
        time.sleep(3)
        self.type(locatorsClass.enterfrstname, userfrstname)
        time.sleep(3)
        self.type(locatorsClass.enterlastname, userlastname)
        time.sleep(2)
        self.type(locatorsClass.enterid, useremail)

    def usersubmit(self):
        time.sleep(2)
        self.click(locatorsClass.usersubmit)
    def oksuccess(self):
        time.sleep(2)
        self.click(locatorsClass.oksuccess)

    def clickedituser(self):
        time.sleep(4)
        self.click(locatorsClass.clickedituser)



    def edituserDetails(self, editfrstname, editlastname):
        time.sleep(3)
        self.type(locatorsClass.editfrstname, editfrstname)
        time.sleep(2)
        self.type(locatorsClass.editlastname, editlastname)
        time.sleep(2)
    def userupdate(self):
        time.sleep(2)
        self.click(locatorsClass.userupdate)

    def userupdateok(self):
        time.sleep(2)
        self.click(locatorsClass.userupdateok)
    def clickdeleteuser(self):
        time.sleep(2)
        self.click(locatorsClass.clickdeleteuser)

    def clickconfirmdelete(self):
        time.sleep(2)
        self.click(locatorsClass.clickconfirmdelete)

    def okdelete(self):
        time.sleep(2)
        self.click(locatorsClass.okdelete)

class adminloginManageFarmerMarket(webActionClassOne):
    def launchUrl(self,url):
        time.sleep(4)
        self.getUrl(url)

    def clickVendorLogin(self):
        time.sleep(3)
        self.click(locatorsClass.vendor_login_button)
    def enterloginDetails(self ,username,password):
        time.sleep(2)
        self.type(locatorsClass.username, username)
        time.sleep(2)
        self.type(locatorsClass.password,password)
    def clickLogin(self):
        time.sleep(3)
        self.click(locatorsClass.loginbtn)
        time.sleep(5)
    def clickadminTab(self):
        time.sleep(3)
        self.click(locatorsClass.administration)
    def clickmanagefrmrmrkt(self):
        time.sleep(3)
        self.click(locatorsClass.managefarmermrkt)
        time.sleep(3)
    def addfrmrmrkt(self):
        time.sleep(2)
        self.click(locatorsClass.addfrmrmrkt)
    def enterfrmrmrktDetails(self ,enterfrmrmrktname,enterfrmraddress,enterfrmrmrktzipcode,enterfrmrmrktphone,enterfrmrmrktwebsite,enterfrmrmrktdesc):
        time.sleep(2)
        self.type(locatorsClass.enterfrmrmrktname, enterfrmrmrktname)
        time.sleep(2)
        self.type(locatorsClass.enterfrmraddress, enterfrmraddress)
        time.sleep(2)
        self.type(locatorsClass.enterfrmrmrktzipcode, enterfrmrmrktzipcode)
        time.sleep(2)
        self.type(locatorsClass.enterfrmrmrktphone, enterfrmrmrktphone)
        time.sleep(2)
        self.type(locatorsClass.enterfrmrmrktwebsite, enterfrmrmrktwebsite)
        time.sleep(2)
        self.type(locatorsClass.enterfrmrmrktdesc, enterfrmrmrktdesc)
    def chooseCity(self):
        time.sleep(5)
        self.choose(locatorsClass.enterfrmrmrktcity, "Abington")
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_xpath("//select[@id='city']"))
        # select by select_by_visible_text() method
        sel.select_by_visible_text("Abington")
        time.sleep(1)
    def mrktsubmit(self):
        time.sleep(2)
        self.click(locatorsClass.mrktsave)

    def entermarketnameSearch(self, entermarketnameSearch):
        time.sleep(2)
        self.type(locatorsClass.searchfarmermarketAdmin, entermarketnameSearch)

    def editmrkt(self):
        time.sleep(2)
        self.click(locatorsClass.editmrkt)

    def editmrktDetails(self, editfrmrmrktname, editmarktadrs):
        time.sleep(3)
        self.type(locatorsClass.editfrmrmrktname, editfrmrmrktname)
        time.sleep(2)
        self.type(locatorsClass.editmarktadrs, editmarktadrs)
        time.sleep(2)
    def mrktupdate(self):
        time.sleep(2)
        self.click(locatorsClass.updatefrmr)
    def clickdeletemrkt(self):
        time.sleep(5)
        self.click(locatorsClass.clickdeletefrmrmrkt)
    def clickconfirmdeletemrkt(self):
        time.sleep(2)
        self.click(locatorsClass.clickconfirmdeletemrkt)
    def importfrmrmrkt(self,importfrmrmrkts):
        time.sleep(5)
        self.type(locatorsClass.importfrmrmrkt,importfrmrmrkts)
    def exportfrmrmrkt(self):
        time.sleep(3)
        self.click(locatorsClass.exportfrmrmrkt)

class adminloginwithwrongemailid(webActionClassOne):
    def launchUrl(self,url):
        time.sleep(4)
        self.getUrl(url)

    def clickVendorLogin(self):
        time.sleep(5)
        self.click(locatorsClass.vendor_login_button)
    def enterloginDetails(self ,username,password):
        time.sleep(3)
        self.type(locatorsClass.username, username)
        time.sleep(2)
        self.type(locatorsClass.password,password)
    def clickLogin(self):
        time.sleep(5)
        self.click(locatorsClass.loginbtn)
        time.sleep(7)
    def verifyLogin(self):
        getTextVar =  self.getText(locatorsClass.successmsg)
        return getTextVar

class adminLoginVerifywithoutcity(webActionClassOne):
    def launchUrl(self, url):
        time.sleep(4)
        self.getUrl(url)

    def clickVendorLogin(self):
        time.sleep(5)
        self.click(locatorsClass.vendor_login_button)

    def clickRegisterButton(self):
        time.sleep(4)
        self.click(locatorsClass.vendor_register_button)

    def enterBasicRegistrationDetails(self, firstname, lastname, vendorname, fnsnumber, primaryemail, primaryphno, psw,
                                      cpsw, continfo):
        self.type(locatorsClass.firstname_textbox_id, firstname)
        time.sleep(2)
        self.type(locatorsClass.lastname_textbox_id, lastname)
        time.sleep(2)
        self.type(locatorsClass.vendorname_textbox_id, vendorname)
        time.sleep(2)
        self.type(locatorsClass.fns_textbox_id, fnsnumber)
        time.sleep(2)
        self.type(locatorsClass.primaryemailaddress_textbox_id, primaryemail)
        time.sleep(2)
        self.type(locatorsClass.primaryphonenumber_textbox_id, primaryphno)
        time.sleep(2)
        self.type(locatorsClass.password_textbox_id, psw)
        time.sleep(2)
        self.type(locatorsClass.confirmpassword_textbox_id, cpsw)
        time.sleep(2)
        self.type(locatorsClass.additionalcontact_textbox_id, continfo)
        time.sleep(2)

    def basicRegButton(self):
        time.sleep(2)
        self.click(locatorsClass.register_button_id)
        time.sleep(5)

    def enterPublicRegistrationDetails(self, publicemail, publicphno, publicwebsite, businessdesc, products):
        time.sleep(5)
        self.type(locatorsClass.publicemailaddress_textbox_id, publicemail)
        time.sleep(2)
        self.type(locatorsClass.publicphonenumber_textbox_id, publicphno)
        time.sleep(2)
        self.type(locatorsClass.publicwebsite_textbox_id, publicwebsite)
        time.sleep(2)
        self.type(locatorsClass.businessdesc_textbox_id, businessdesc)
        time.sleep(2)
        self.type(locatorsClass.products_textbox_id, products)
        time.sleep(5)

    def publicRegButton(self):
        time.sleep(2)
        self.click(locatorsClass.saveandnext_button_id)
        time.sleep(2)

    def clickCSAButton(self):
        time.sleep(10)
        self.click(locatorsClass.csa_radiobutton_id)


    def clickLocationYesButton(self):
        time.sleep(6)
        self.click(locatorsClass.locationtype_saveandnext_button_id)

    def csalocationTypeDetails(self, pickupsitename, adrs1, adrs2, zipcode):
        self.type(locatorsClass.pickupsite_textbox_id, pickupsitename)
        time.sleep(2)
        self.type(locatorsClass.adrs_1, adrs1)
        time.sleep(2)
        self.type(locatorsClass.adrs_2, adrs2)
        time.sleep(2)
        self.type(locatorsClass.zipcode_textbox_id, zipcode)
        time.sleep(2)

    def saveCsa(self):
        time.sleep(4)
        self.click(locatorsClass.csa_saveandnext_button)

class adminloginwithoutatSymbol(webActionClassOne):
    def launchUrl(self,url):
        time.sleep(4)
        self.getUrl(url)

    def clickVendorLogin(self):
        time.sleep(5)
        self.click(locatorsClass.vendor_login_button)
    def enterloginDetails(self ,username,password):
        time.sleep(3)
        self.type(locatorsClass.username, username)
        time.sleep(2)
        self.type(locatorsClass.password,password)
    def clickLogin(self):
        time.sleep(5)
        self.click(locatorsClass.loginbtn)

    def verifyLogin(self):
        getTextVar = self.getText(locatorsClass.successmsg)
        return getTextVar

class adminloginwithoutrqdfield(webActionClassOne):
    def launchUrl(self,url):
        time.sleep(4)
        self.getUrl(url)

    def clickVendorLogin(self):
        time.sleep(5)
        self.click(locatorsClass.vendor_login_button)
    def enterloginDetails(self ,password):
        # time.sleep(3)
        # self.type(locatorsClass.username, username)
        time.sleep(2)
        self.type(locatorsClass.password,password)
    def clickLogin(self):
        time.sleep(5)
        self.click(locatorsClass.loginbtn)
        time.sleep(7)
    def verifyLogin(self):
        getTextVar = self.getText(locatorsClass.successmsg)
        return getTextVar

class Registrationwithoutemailid(webActionClassOne):
    def launchUrl(self,url):
        time.sleep(4)
        self.getUrl(url)

    def clickVendorLogin(self):
        time.sleep(4)
        self.click(locatorsClass.vendor_login_button)

    def clickRegisterButton(self):
        time.sleep(4)
        self.click(locatorsClass.vendor_register_button)

    def enterBasicRegistrationDetails(self,firstname,lastname,vendorname,fnsnumber,primaryemail,primaryphno,psw,cpsw,continfo):
        self.type(locatorsClass.firstname_textbox_id,firstname)
        time.sleep(2)
        self.type(locatorsClass.lastname_textbox_id, lastname)
        time.sleep(2)
        self.type(locatorsClass.vendorname_textbox_id, vendorname)
        time.sleep(2)
        self.type(locatorsClass.fns_textbox_id, fnsnumber)
        time.sleep(2)
        self.type(locatorsClass.primaryemailaddress_textbox_id, primaryemail)
        time.sleep(2)
        self.type(locatorsClass.primaryphonenumber_textbox_id, primaryphno)
        time.sleep(2)
        self.type(locatorsClass.password_textbox_id, psw)
        time.sleep(2)
        self.type(locatorsClass.confirmpassword_textbox_id, cpsw)
        time.sleep(2)
        self.type(locatorsClass.additionalcontact_textbox_id, continfo)
        time.sleep(2)

    def basicRegButton(self):
        time.sleep(2)
        self.click(locatorsClass.register_button_id)
        time.sleep(5)

class SearchCity(webActionClassOne):
    def launchUrl(self,url):
        time.sleep(4)
        self.getUrl(url)

    def chooseActon(self):
        time.sleep(20)
        self.choose(locatorsClass.allcities, "Acton")
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_xpath("//body[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/select[1]"))
        # select by select_by_visible_text() method
        sel.select_by_visible_text("Acton")
        time.sleep(2)

    def chooseVendor(self):
        time.sleep(15)
        self.choose(locatorsClass.searchvendor, "Nancy Nickita Farms")
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_xpath(
            "//body[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[7]/select[1]"))
        # select by select_by_visible_text() method
        sel.select_by_visible_text("Nancy Nickita Farms")
        time.sleep(7)
    def clickmapexport(self):
        time.sleep(4)
        self.click(locatorsClass.clickmapexport)
    def sortUp(self):
        time.sleep(4)
        self.click(locatorsClass.sortUp)
    def sortDown(self):
        time.sleep(4)
        self.click(locatorsClass.sortDown)


class Clearsearch(webActionClassOne):
    def launchUrl(self,url):
        time.sleep(4)
        self.getUrl(url)

    def clickClearsearch(self):
        time.sleep(4)
        self.click(locatorsClass.clearSearch)

class ClickLocationTypes(webActionClassOne):
    def launchUrl(self,url):
        time.sleep(4)
        self.getUrl(url)
    def clickonLegend(self):
        time.sleep(4)
        self.click(locatorsClass.clickonLegend)
    def clickHIPCSALoc(self):
        time.sleep(4)
        self.click(locatorsClass.hipCsaFilter)
    def clickHIPFarmStandLoc(self):
        time.sleep(4)
        self.click(locatorsClass.hipFarmStandFilter)
    def clickHIPFarmerMarketBoothLoc(self):
        time.sleep(4)
        self.click(locatorsClass.hipMarketBoothFilter)
    def clickHIPMobileMarketLoc(self):
        time.sleep(4)
        self.click(locatorsClass.hipMobileMarketFilter)

    def clickHIPFarmerMarketLoc(self):
        time.sleep(4)
        self.click(locatorsClass.hipFarmerMarketFilter)
    def allcities(self):
        time.sleep(7)
        self.choose(locatorsClass.allcities, "All Counties and Cities")
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_xpath("//body[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/select[1]"))
        # select by select_by_visible_text() method
        sel.select_by_visible_text("All Counties and Cities")
        time.sleep(2)

class clickOrderOptions(webActionClassOne):
    def launchUrl(self,url):
        time.sleep(4)
        self.getUrl(url)

    def allcities(self):
        time.sleep(5)
        self.choose(locatorsClass.allcities, "All Counties and Cities")
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_xpath("//body[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/select[1]"))
        # select by select_by_visible_text() method
        sel.select_by_visible_text("All Counties and Cities")
        time.sleep(2)

    # def clickOrderOption(self):
    #     time.sleep(7)
    #     self.choose(locatorsClass.orderOption, "Curbside pickup")
    #     # identify dropdown with Select class
    #     sel = Select(self.driver.find_element_by_xpath("//body[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/label[1]"))
    #     sel.select_by_visible_text("Curbside pickup")
    def unselectOrderOptions(self):
        time.sleep(3)
        self.click(locatorsClass.orderOption)


    def unselectOrderOption(self):
        time.sleep(1)
        self.click(locatorsClass.selectallorderOption)

class clickMonthOptions(webActionClassOne):
    def launchUrl(self,url):
        time.sleep(4)
        self.getUrl(url)

    def allcities(self):
        time.sleep(7)
        self.choose(locatorsClass.allcities, "All Counties and Cities")
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_xpath(
            "//body[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/select[1]"))
        # select by select_by_visible_text() method
        sel.select_by_visible_text("All Counties and Cities")
        time.sleep(2)

    def clickMonthOption(self):
        time.sleep(1)
        self.click(locatorsClass.monthOption)
    def unselectMonthOptions(self):
        time.sleep(1)
        self.click(locatorsClass.selectallmonthOption)

class clickDaysOperation(webActionClassOne):
    def launchUrl(self,url):
        time.sleep(4)
        self.getUrl(url)

    def allcities(self):
        time.sleep(7)
        self.choose(locatorsClass.allcities, "All Counties and Cities")
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_xpath(
            "//body[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/select[1]"))
        # select by select_by_visible_text() method
        sel.select_by_visible_text("All Counties and Cities")
        time.sleep(2)

    def clickdaysOption(self):
        time.sleep(1)
        self.click(locatorsClass.daysOption)
    def unselectdaysOption(self):
        time.sleep(1)
        self.click(locatorsClass.selectalldaysOption)

class clickOpenToday(webActionClassOne):
    def launchUrl(self,url):
        time.sleep(4)
        self.getUrl(url)

    def allcities(self):
        time.sleep(7)
        self.choose(locatorsClass.allcities, "All Counties and Cities")
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_xpath(
            "//body[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/select[1]"))
        # select by select_by_visible_text() method
        sel.select_by_visible_text("All Counties and Cities")
        time.sleep(2)

    def clickopentoday(self):
        time.sleep(1)
        self.click(locatorsClass.openToday)

class commentFeatures(webActionClassOne):
    def launchUrl(self,url):
        time.sleep(4)
        self.getUrl(url)

    def clickVendorLogin(self):
        time.sleep(5)
        self.click(locatorsClass.vendor_login_button)
    def enterloginDetails(self ,username,password):
        time.sleep(3)
        self.type(locatorsClass.username, username)
        time.sleep(2)
        self.type(locatorsClass.password,password)
    def clickLogin(self):
        time.sleep(5)
        self.click(locatorsClass.loginbtn)
        time.sleep(7)

    def clickvendorTab(self):
        time.sleep(7)
        self.click(locatorsClass.vendorTab)
        time.sleep(7)

    def clickVendor(self):
        time.sleep(7)
        self.click(locatorsClass.clickVendor)
        time.sleep(7)
    def clickAddComment(self):
        time.sleep(3)
        self.click(locatorsClass.clickAddComment)

    def entercomment(self ,entercomment):
        time.sleep(3)
        self.type(locatorsClass.enterComment, entercomment)
    def savecomment(self):
        time.sleep(3)
        self.click(locatorsClass.savecomment)
    def clickeditcomment(self):
        time.sleep(3)
        self.click(locatorsClass.clickeditcomment)

    def entereditcomment(self, entereditcomment):
        time.sleep(3)
        self.type(locatorsClass.entereditcomment, entereditcomment)

    def updatecomment(self):
        time.sleep(3)
        self.click(locatorsClass.updatecomment)
    def deletecomment(self):
        time.sleep(5)
        self.click(locatorsClass.deletecomment)

    def confirmremovecomment(self):
        time.sleep(3)
        self.click(locatorsClass.confirmremove_comment)
    def closecomment(self):
        time.sleep(3)
        self.click(locatorsClass.closecomment)

class vendoreditFeatures(webActionClassOne):
    def launchUrl(self,url):
        time.sleep(4)
        self.getUrl(url)

    def clickVendorLogin(self):
        time.sleep(4)
        self.click(locatorsClass.vendor_login_button)
    def enterloginDetails(self ,username,password):
        time.sleep(2)
        self.type(locatorsClass.username, username)
        time.sleep(2)
        self.type(locatorsClass.password,password)
    def clickLogin(self):
        time.sleep(3)
        self.click(locatorsClass.loginbtn)
        time.sleep(7)

    def clickvendorTab(self):
        time.sleep(7)
        self.click(locatorsClass.vendorTab)

    def clickVendor(self):
        time.sleep(3)
        self.click(locatorsClass.clickVendor)
    def entervendornameSearch(self,entervendornameSearch):
        time.sleep(2)
        self.type(locatorsClass.searchvendorAdmin, entervendornameSearch)

    def clickeditvendor(self):
        time.sleep(5)
        self.click(locatorsClass.editvendor)

    def entereditvendor(self,editFirstName,editLastName):
        time.sleep(3)
        self.type(locatorsClass.editFirstName, editFirstName)
        time.sleep(2)
        self.type(locatorsClass.editLastName, editLastName)

    def updatevendor(self):
        time.sleep(5)
        self.click(locatorsClass.updatevendor)
    def deletevendor(self):
        time.sleep(3)
        self.click(locatorsClass.deletevendor)
    def clickeditPrimaryEmail(self):
        time.sleep(3)
        self.click(locatorsClass.editPrimaryEmail)
    def entereditPrimaryEmail(self, primaryEmail):
        time.sleep(2)
        self.type(locatorsClass.editenterPrimaryEmail ,primaryEmail)
    def updatePrimaryEmail(self):
        time.sleep(2)
        self.click(locatorsClass.updatePrimaryEmail)
    def updatePrimaryEmailOk(self):
        time.sleep(2)
        self.click(locatorsClass.updatePrimaryEmailOk)
    def clickeditvendorlastupdatedtime(self):
        time.sleep(3)
        self.click(locatorsClass.picktimeUpdate)
    def clickpicktime(self):
        time.sleep(2)
        self.click(locatorsClass.clickpicktime)
    def picktime(self):
        time.sleep(2)
        self.click(locatorsClass.picktime)
    def picktimeapply(self):
        time.sleep(2)
        self.click(locatorsClass.picktimeapply)
    def picktimeUpdate(self):
        time.sleep(2)
        self.click(locatorsClass.editvendorupdatedtimeupdate)

    def confirmremovevendor(self):
        time.sleep(3)
        self.click(locatorsClass.confirmremovevendor)
    def confirmremovevendorok(self):
        time.sleep(3)
        self.click(locatorsClass.confirmremovevendorok)
    def selectVendor(self):
        time.sleep(3)
        self.click(locatorsClass.selectvendor)

    def activeClick(self):
        time.sleep(4)
        self.click(locatorsClass.activeVendor)
    def inactiveClick(self):
        time.sleep(3)
        self.click(locatorsClass.inactiveVendor)
    def inactiveok(self):
        time.sleep(2)
        self.click(locatorsClass.inactiveok)
    def toggleinactive(self):
        time.sleep(2)
        self.click(locatorsClass.toggleinactive)
    def toggleactive(self):
        time.sleep(10)
        self.click(locatorsClass.toggleactive)
    def toggleconfirmationyes(self):
        time.sleep(2)
        self.click(locatorsClass.toggleconfirmationyes)
    def toggleinactivevendor(self):
        time.sleep(5)
        self.click(locatorsClass.toggleinactivevendor)
    def toggleactivevendor(self):
        time.sleep(10)
        self.click(locatorsClass.toggleactivevendor)
    def vendorrefresh(self):
        time.sleep(5)
        self.click(locatorsClass.vendorrefresh)
    def exportClick(self):
        time.sleep(5)
        self.click(locatorsClass.clickexport)
    def exportverifiedVendors(self):
        time.sleep(4)
        self.click(locatorsClass.verifiedVendors)
    def exportlastupdatedTime(self):
        time.sleep(5)
        self.click(locatorsClass.lastupdatedTime)
    def exportlastlogindays(self):
        time.sleep(5)
        self.click(locatorsClass.lastlogindays)
    def viewmore(self):
        time.sleep(4)
        self.click(locatorsClass.viewmore)
    def viewmoreClose(self):
        time.sleep(4)
        self.click(locatorsClass.viewmoreClose)
    def activeCheckvendor(self):
        time.sleep(4)
        self.click(locatorsClass.activeCheckvendor)
    def verifiedCheckvendor(self):
        time.sleep(4)
        self.click(locatorsClass.verifiedCheckvendor)
    def followupvendor(self):
        time.sleep(4)
        self.click(locatorsClass.followupvendor)
    def followupvendorok(self):
        time.sleep(4)
        self.click(locatorsClass.followupvendorok)
    def vendorlocationtypes(self):
        time.sleep(4)
        self.click(locatorsClass.followupvendorok)
    def clickLoc(self):
        time.sleep(4)
        self.click(locatorsClass.clickLoc)

    def changecity(self):
        time.sleep(7)
        self.choose(locatorsClass.editloccity, "Abington")
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_xpath("//body[1]/div[5]/div[2]/div[3]/div[1]/div[2]/section[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[2]/div[3]/select[1]"))
        # select by select_by_visible_text() method
        sel.select_by_visible_text("Abington")
        time.sleep(2)
    def vendorUpdate(self):
        time.sleep(4)
        self.click(locatorsClass.vendorUpdate)
        time.sleep(4)


class adminSearchFunctions(webActionClassOne):
    def launchUrl(self,url):
        time.sleep(4)
        self.getUrl(url)

    def clickVendorLogin(self):
        time.sleep(5)
        self.click(locatorsClass.vendor_login_button)
    def enterloginDetails(self ,username,password):
        time.sleep(3)
        self.type(locatorsClass.username, username)
        time.sleep(2)
        self.type(locatorsClass.password,password)
    def clickLogin(self):
        time.sleep(5)
        self.click(locatorsClass.loginbtn)
        time.sleep(7)
    def clickvendorTab(self):
        time.sleep(5)
        self.click(locatorsClass.vendorTab)
        time.sleep(7)
    def entervendornameSearch(self,entervendornameSearch):
        time.sleep(2)
        self.type(locatorsClass.searchvendorAdmin, entervendornameSearch)
    def entervendorfnsSearch(self,entervendorfnsSearch):
        time.sleep(2)
        self.type(locatorsClass.searchvendorAdmin, entervendorfnsSearch)
    def entervendormobileSearch(self,entervendormobileSearch):
        time.sleep(2)
        self.type(locatorsClass.searchvendorAdmin, entervendormobileSearch)
    def entervendoremailSearch(self,entervendormobileSearch):
        time.sleep(2)
        self.type(locatorsClass.searchvendorAdmin, entervendormobileSearch)
    def entervendorfnameSearch(self,entervendormobileSearch):
        time.sleep(2)
        self.type(locatorsClass.searchvendorAdmin, entervendormobileSearch)
    def entervendorlnameSearch(self,entervendormobileSearch):
        time.sleep(2)
        self.type(locatorsClass.searchvendorAdmin, entervendormobileSearch)

    def clickadminTab(self):
        time.sleep(5)
        self.click(locatorsClass.administration)
        time.sleep(7)

    def clickuser(self):
        time.sleep(3)
        self.click(locatorsClass.manageusers)
        time.sleep(5)
    def clickmanagefrmrmrkt(self):
        time.sleep(3)
        self.click(locatorsClass.managefarmermrkt)
        time.sleep(5)
    def importfrmrmrkt(self,importfrmrmrkt):
        time.sleep(3)
        self.type(locatorsClass.importfrmrmrkt ,importfrmrmrkt)
    def exportfrmrmrkt(self):
        time.sleep(3)
        self.click(locatorsClass.exportfrmrmrkt)
    def entermarketnameSearch(self,entermarketnameSearch):
        time.sleep(2)
        self.type(locatorsClass.searchfarmermarketAdmin, entermarketnameSearch)
    def enterusernameSearch(self,enterusernameSearch):
        time.sleep(2)
        self.type(locatorsClass.searchuserAdmin, enterusernameSearch)

    def clickLogoutTab(self):
        time.sleep(5)
        self.click(locatorsClass.clickLogoutTab)
    def clickLogout(self):
        time.sleep(5)
        self.click(locatorsClass.clickLogout)
    def vendorrefresh(self):
        time.sleep(5)
        self.click(locatorsClass.vendorrefresh)
    def userrefresh(self):
        time.sleep(5)
        self.click(locatorsClass.userrefresh)
    def marketrefresh(self):
        time.sleep(5)
        self.click(locatorsClass.marketrefresh)
    def clickaudit(self):
        time.sleep(5)
        self.click(locatorsClass.clickAudit)
    def chooseLoginLogs(self):
        time.sleep(7)
        self.choose(locatorsClass.chooseLoginLogs, "Login Logs")
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_id("logType"))
        # select by select_by_visible_text() method
        sel.select_by_visible_text("Login Logs")
        time.sleep(2)




class languagetranslationCheck(webActionClassOne):
    def launchUrl(self,url):
        time.sleep(4)
        self.getUrl(url)
    def clickHipVendors(self):
        time.sleep(2)
        self.click(locatorsClass.findhipvendors)

    def choosePortuguese(self):
        time.sleep(7)
        self.choose(locatorsClass.languageSelection, "Portuguese")
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_id("langSelection"))
        # select by select_by_visible_text() method
        sel.select_by_visible_text("Portuguese")
        time.sleep(2)
    def chooseChinese(self):
        time.sleep(8)
        self.choose(locatorsClass.languageSelection, "chinês")
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_id("langSelection"))
        # select by select_by_visible_text() method
        sel.select_by_visible_text("chinês")
        time.sleep(2)
    def chooseSpanish(self):
        time.sleep(8)
        self.choose(locatorsClass.languageSelection,"西班牙语")
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_id("langSelection"))
        # select by select_by_visible_text() method
        sel.select_by_visible_text("西班牙语")
        time.sleep(2)

    def chooseVietnamese(self):
        time.sleep(8)
        self.choose(locatorsClass.languageSelection,"vietnamita")
        # identify dropdown with Select class
        sel = Select(self.driver.find_element_by_id("langSelection"))
        # select by select_by_visible_text() method
        sel.select_by_visible_text("vietnamita")
        time.sleep(2)





# python -m pytest --html=report.html Tests/


# py.test --excelreport=report.xls
