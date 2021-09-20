# username = "//input[@name='userName']"
from selenium.webdriver.common.by import By
class locatorsClass (object) :
    findhipvendors = (By.XPATH,"//body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/p[2]/a[1]")
    vendor_login_button = (By.XPATH,"//a[@data-toggle='modal']")
    vendor_register_button = (By.XPATH,"//a[normalize-space()='Register']")
    firstname_textbox_id = (By.XPATH,"//input[@id='firstName']")
    lastname_textbox_id = (By.XPATH,"//input[@id='lastName']")
    vendorname_textbox_id = (By.XPATH,"//input[@id='farmVendorName']")
    fns_textbox_id = (By.XPATH,"/html[1]/body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/div[1]/input[1]")
    primaryemailaddress_textbox_id = (By.XPATH,"//input[@id='primaryEmailID']")
    primaryphonenumber_textbox_id = (By.XPATH,"//input[@id='primaryPhoneNumber']")
    password_textbox_id = (By.XPATH,"//input[@id='vendorPassword']")
    confirmpassword_textbox_id = (By.XPATH,"//input[@id='confirmPassword']")
    additionalcontact_textbox_id = (By.XPATH,"//textarea[@id='additionalContactInfo']")
    register_button_id = (By.XPATH,"//body/div[5]/div[1]/div[1]/div[2]/div[2]/section[1]/div[3]/form[1]/div[1]/div[1]/div[1]/button[1]")
    publicemailaddress_textbox_id = (By.XPATH,"//input[@id='infoEmailID']")
    publicphonenumber_textbox_id = (By.XPATH,"//input[@id='infoPhoneNumber']")
    publicwebsite_textbox_id = (By.XPATH,"//input[@id='infoWebsite']")
    businessdesc_textbox_id = (By.XPATH,"//textarea[@id='business_desc']")
    vendorPublicImg = (By.ID, "infoPhoto")
    products_textbox_id = (By.XPATH,"//textarea[@id='infoProductDescription']")
    saveandnext_button_id = (By.XPATH,"/html[1]/body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[2]/div[3]/div[1]/div[1]/div[1]/button[1]")
    csa_radiobutton_id = (By.XPATH,"/html[1]/body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]")
    farmstand_radiobutton_id = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/label[1]")
    farmersmarketbooth_radiobutton_id = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/label[1]")
    mobilemarket_radiobutton_id = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[3]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/label[1]")
    farmermarket_mngr = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[3]/div[2]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/label[1]")
    locationtype_saveandnext_button_id = (By.XPATH,"//button[@id='hipProgramNextBtn']")

    # CSA Pickupsite locators

    pickupsite_textbox_id = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[1]/div[1]/input[1]")
    adrs_1 = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[2]/div[1]/input[1]")
    adrs_2 = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[2]/div[2]/input[1]")
    select_citydropdown_id = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[2]/div[3]/select[1]")
    zipcode_textbox_id = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[2]/div[5]/input[1]")
    months_of_operation_june = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[7]/div[1]/div[1]/div[1]/ul[1]/li[6]/div[1]/input[1]")
    spzl_instruction = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[4]/div[1]/div[1]/textarea[1]")
    order_option_delivery = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[7]/div[2]/div[1]/input[1]")
    starttimeMonday_CSA = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[8]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/select[1]")
    endtimeMonday_CSA = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[8]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/select[1]")
    csa_copy = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[2]")
    addmore = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/span[2]")
    remove = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[4]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]")
    confirmremove = (By.XPATH, "//body[1]/div[7]/div[1]/div[3]/button[1]")
    saveonlycsa = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[4]/div[3]/div[1]/div[1]/div[1]/button[1]")
    csa_saveandnext_button = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[4]/div[3]/div[1]/div[1]/div[1]/button[2]")

    # Farmstand locators

    farmstand_adrs_1 = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[5]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[1]/div[1]/input[1]")
    farmstand_adrs_2 = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[5]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[1]/div[2]/input[1]")
    farmstand_select_citydropdown_id = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[5]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[1]/div[3]/select[1]")
    farmstand_zipcode_textbox_id = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[5]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[1]/div[5]/input[1]")
    farmstand_months_of_operation = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[5]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[6]/div[1]/div[1]/div[1]/ul[1]/li[7]/div[1]/input[1]")
    farmstand_order_option = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[5]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[6]/div[2]/div[2]/input[1]")
    farmstand_saveandnext_button = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[5]/div[3]/div[1]/div[1]/div[1]/button[2]")

    # Farmers Market Booth locators

    farmersmarketbooth_select_citydropdown_id = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[6]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[1]/div[1]/div[1]/select[1]")
    farmersmarketbooth_months_of_operation = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[6]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[7]/div[1]/div[1]/div[1]/ul[1]/li[5]/div[1]/label[1]")
    farmersmarketbooth_order_option = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[6]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[7]/div[2]/div[5]/label[1]")
    farmersmarketbooth_saveandnext_button = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[6]/div[3]/div[1]/div[1]/div[1]/button[2]")

    # Mobile Market Booth locators

    mobileMarket_textbox_id = (By.XPATH,"/html[1]/body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[7]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[1]/div[1]/input[1]")
    mobileMarket_select_citydropdown_id = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[7]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[2]/div[3]/select[1]")
    mobileMarket_months_of_operation = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[7]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[7]/div[1]/div[1]/div[1]/ul[1]/li[5]/div[1]/label[1]")
    mobileMarket_order_option = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[7]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[7]/div[2]/div[4]/label[1]")
    mobileMarket_saveandnext_button = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[7]/div[3]/div[1]/div[1]/div[1]/button[1]")

    #Farmer Market Manager Locators

    farmermarket_mngr_market = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[8]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[1]/div[1]/div[1]/select[1]")
    farmermarket_mngr_market_Save = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[8]/div[3]/div[1]/div[1]/div[1]/button[1]")
    farmermarket_mngr_spzlInst = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[8]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[4]/div[1]/div[1]/textarea[1]")
    #AdminLogin
    username = (By.ID, "username")
    password = (By.ID, "password")
    loginbtn = (By.XPATH, "//button[@type='submit']")
    regsuccessmsg = (By.XPATH, "//body[1]/div[1]/nav[1]/div[1]/a[1]/span[1]")
    successmsg = (By.XPATH, "//body[1]/div[1]/nav[1]/div[2]/ul[1]/li[4]/a[1]")
    succmsg = (By.XPATH,"//body[1]/div[5]/div[1]/div[1]/div[2]/div[2]/section[2]/div[1]/div[1]/div[1]/h4[1]")
    vendorTab = (By.XPATH, "//body[1]/div[1]/nav[1]/div[2]/ul[1]/li[2]/a[1]")
    viewmore = (By.XPATH, "/html[1]/body[1]/div[5]/div[1]/u[1]")
    viewmoreClose = (By.XPATH, "//body[1]/div[10]/div[1]/div[1]/div[1]/button[1]")
    clickVendor = (By.XPATH, "//body[1]/div[5]/div[4]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/div[1]/div[1]/a[1]")
    verifyVendor = (By.XPATH, "//body[1]/div[5]/div[1]/div[2]/button[1]")
    editPrimaryEmail = (By.XPATH, "//body[1]/div[5]/div[4]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/div[1]/div[2]/button[1]")
    editenterPrimaryEmail = (By.XPATH, "//body[1]/div[8]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
    updatePrimaryEmail = (By.XPATH, "//body[1]/div[8]/div[1]/div[1]/form[1]/div[2]/button[1]")
    updatePrimaryEmailOk = (By.XPATH, "//body[1]/div[15]/div[1]/div[3]/button[1]")
    editvendor = (By.XPATH, "//body[1]/div[5]/div[2]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]")
    editFirstName = (By.XPATH, "//body[1]/div[5]/div[2]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[4]/div[1]/input[1]")
    editLastName = (By.XPATH, "//body[1]/div[5]/div[2]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[4]/div[2]/input[1]")
    updatevendor = (By.XPATH, "//body[1]/div[5]/div[2]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]")
    deletevendor = (By.XPATH, "//body[1]/div[5]/div[4]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[9]/button[1]")
    confirmremovevendor = (By.XPATH, "//body[1]/div[13]/div[1]/div[3]/button[1]")
    confirmremovevendorok = (By.XPATH, "//body[1]/div[13]/div[1]/div[3]/button[1]")
    picktimeUpdate = (By.XPATH, "//body[1]/div[5]/div[4]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[7]/div[1]/div[2]/button[1]")
    clickpicktime = (By.XPATH, "//body[1]/div[9]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]/i[1]")
    picktime = (By.CLASS_NAME, "today")
    picktimeapply = (By.XPATH, "//body[1]/div[14]/div[4]/button[2]")
    editvendorupdatedtimeupdate = (By.XPATH,"//body[1]/div[9]/div[1]/div[1]/form[1]/div[2]/button[1]")
    selectvendor = (By.XPATH, "//body[1]/div[5]/div[4]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/input[1]")
    activeVendor = (By.XPATH, "//body[1]/div[5]/div[4]/div[1]/div[1]/button[1]")
    inactiveVendor = (By.XPATH, "//body[1]/div[5]/div[4]/div[1]/div[1]/button[2]")
    inactiveok = (By.XPATH, "//body[1]/div[13]/div[1]/div[3]/button[1]")
    toggleinactive = (By.XPATH, "//body[1]/div[5]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/label[2]")
    toggleactive = (By.XPATH, "//body[1]/div[5]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/label[2]")
    toggleconfirmationyes = (By.XPATH, "//body[1]/div[12]/div[1]/div[3]/button[1]")
    toggleinactivevendor = (By.XPATH, "//body[1]/div[5]/div[4]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[6]/div[1]/label[1]")
    toggleactivevendor = (By.XPATH, "//body[1]/div[5]/div[4]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[6]/div[1]/label[1]")
    clickexport = (By.XPATH, "//body[1]/div[5]/div[2]/div[3]/div[1]/div[1]/button[1]")
    verifiedVendors = (By.XPATH, "//body[1]/div[5]/div[2]/div[3]/div[1]/div[1]/div[1]/a[1]")
    lastupdatedTime = (By.XPATH, "//body[1]/div[5]/div[2]/div[3]/div[1]/div[1]/div[1]/a[2]")
    lastlogindays = (By.XPATH, "//body[1]/div[5]/div[2]/div[3]/div[1]/div[1]/div[1]/a[3]")
    # verifyVendorwithoutcity = (By.XPATH, "//body[1]/div[5]/div[1]/div[2]/button[1]")
    staffname = (By.ID, "staff_email")
    staffdesc = (By.ID, "staff_note")
    confirmVerification = (By.XPATH, "//button[@class='btn btnModal btnSubmit btn-primary']")
    allcities = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/select[1]")
    searchvendor = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[7]/select[1]")
    followupvendor = (By.XPATH, "//body[1]/div[5]/div[4]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[9]/button[4]")
    activeCheckvendor = (By.ID  , "isActive")
    verifiedCheckvendor = (By.ID, "isVerified")
    followupvendorok = (By.XPATH, "//body[1]/div[9]/div[1]/div[1]/div[3]/button[1]")
    clickLoc = (By.XPATH, "//body[1]/div[5]/div[2]/div[3]/div[1]/div[1]/ul[1]/li[2]/a[1]")
    editloccity = (By.XPATH, "//body[1]/div[5]/div[2]/div[3]/div[1]/div[2]/section[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/fieldset[1]/div[2]/div[3]/select[1]")
    vendorUpdate = (By.XPATH, "//body[1]/div[5]/div[2]/div[3]/div[1]/div[2]/section[2]/div[3]/div[1]/div[1]/div[1]/button[1]")
#Manage Users
    administration = (By.XPATH,"//body[1]/div[1]/nav[1]/div[2]/ul[1]/li[3]/a[1]")
    manageusers = (By.XPATH, "//body[1]/div[1]/nav[1]/div[2]/ul[1]/li[3]/div[1]/a[1]")
    addUser = (By.XPATH, "//body[1]/div[5]/div[1]/div[2]/button[1]")
    enterfrstname = (By.ID, "firstName")
    enterlastname = (By.ID, "lastName")
    enterid = (By.ID, "emailId")
    usersubmit = (By.XPATH, "//body[1]/div[6]/div[1]/div[1]/form[1]/div[2]/button[1]")
    oksuccess = (By.XPATH, "//body[1]/div[8]/div[1]/div[3]/button[1]")
    clickedituser = (By.XPATH, "//body[1]/div[5]/div[2]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[7]/button[1]/i[1]")
    editfrstname = (By.ID, "firstName")
    editlastname = (By.ID, "lastName")
    userupdate = (By.XPATH, "//body[1]/div[6]/div[1]/div[1]/form[1]/div[2]/button[1]")
    userupdateok = (By.XPATH,"//body[1]/div[8]/div[1]/div[3]/button[1]")
    clickdeleteuser = (By.XPATH, "//body[1]/div[5]/div[2]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[7]/button[2]")
    clickconfirmdelete = (By.XPATH, "//body[1]/div[8]/div[1]/div[3]/button[1]")
    okdelete = (By.XPATH, "//body[1]/div[8]/div[1]/div[3]/button[1]")
    # Manage FarmerMarket
    managefarmermrkt = (By.XPATH, "//a[normalize-space()='Manage Farmer Markets']")
    addfrmrmrkt = (By.XPATH, "//button[@aria-label='button'][normalize-space()='Add']")
    enterfrmrmrktname = (By.XPATH, "//input[@id='location_name']")
    enterfrmraddress = (By.XPATH, "//input[@id='address']")
    enterfrmrmrktcity = (By.XPATH, "//select[@id='city']")
    enterfrmrmrktzipcode = (By.XPATH, "//input[@id='zip']")
    enterfrmrmrktphone = (By.XPATH, "//input[@id='phone']")
    enterfrmrmrktwebsite = (By.XPATH, "//input[@id='website']")
    enterfrmrmrktdesc = (By.XPATH, "//textarea[@id='description']")
    mrktsave = (By.XPATH, "//button[@type='submit']")
    editmrkt = (By.XPATH, "//body[1]/div[5]/div[2]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[4]/td[5]/button[1]")
    editfrmrmrktname = (By.XPATH, "//input[@id='location_name']")
    editmarktadrs = (By.XPATH, "//input[@id='address']")
    updatefrmr = (By.XPATH, "//button[@type='submit']")
    clickdeletefrmrmrkt = (By.XPATH, "//body[1]/div[5]/div[2]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[6]/td[5]/button[2]")
    clickconfirmdeletemrkt = (By.XPATH, "//body[1]/div[8]/div[1]/div[3]/button[1]")
    importfrmrmrkt = (By.XPATH, "//body[1]/div[5]/div[1]/div[2]/a[1]/i[1]")
    exportfrmrmrkt = (By.XPATH, "//body[1]/div[5]/div[1]/div[2]/a[2]/span[1]/u[1]")

    #Audit Logs
    clickAudit = (By.XPATH, "//body[1]/div[1]/nav[1]/div[2]/ul[1]/li[3]/div[1]/a[4]")
    chooseLoginLogs = (By.ID, "logType")



    #Map Page
    clearSearch = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/div[1]/div[2]/button[1]")
    clickonLegend = (By.XPATH, "//body[1]/div[5]/div[2]/div[1]/div[1]/div[5]/div[1]/p[2]/i[1]")
    hipCsaFilter = (By.XPATH, "//body[1]/div[5]/div[2]/div[1]/div[1]/div[5]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]/ul[1]/li[1]")
    hipFarmStandFilter = (By.XPATH, "//body[1]/div[5]/div[2]/div[1]/div[1]/div[5]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]/ul[1]/li[2]")
    hipMarketBoothFilter = (By.XPATH, "//body[1]/div[5]/div[2]/div[1]/div[1]/div[5]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]/ul[1]/li[3]")
    hipFarmerMarketFilter = (By.XPATH, "//body[1]/div[5]/div[2]/div[1]/div[1]/div[5]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]/ul[1]/li[4]")
    hipMobileMarketFilter = (By.XPATH, "//body[1]/div[5]/div[2]/div[1]/div[1]/div[5]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]/ul[1]/li[5]")
    orderOption = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/label[1]")
    monthOption = (By.ID, "operationMonth_inputCount")
    daysOption = (By.ID, "operationDay_inputCount")
    openToday = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[8]/div[1]/div[1]/input[1]")
    selectallorderOption = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/div[2]/span[1]/label[1]")
    selectallmonthOption = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[5]/div[1]/div[2]/span[1]/label[1]/input[1]")
    selectalldaysOption = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[6]/div[1]/div[2]/span[1]/label[1]/span[1]")
    languageSelection =  (By.ID, "langSelection")
    clickmapexport = (By.XPATH, "//body[1]/div[5]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/a[1]/small[1]/u[1]")
    sortUp = (By.ID, "upArrow")
    sortDown = (By.ID, "downArrow")

    #Comment features
    clickAddComment = (By.ID, "addComment")
    enterComment = (By.ID, "private_comment")
    savecomment = (By.XPATH, "//body[1]/div[9]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/button[1]")
    clickeditcomment = (By.XPATH, "//body[1]/div[9]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[3]/span[1]/i[1]")
    entereditcomment = (By.XPATH, "//body[1]/div[9]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/textarea[1]")
    updatecomment = (By.XPATH, "//body[1]/div[9]/div[1]/div[1]/form[1]/div[1]/div[2]/div[2]/button[2]")
    deletecomment = (By.XPATH, "//body[1]/div[9]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[3]/span[2]/i[1]")
    confirmremove_comment = (By.XPATH, "//body[1]/div[13]/div[1]/div[3]/button[1]")
    closecomment = (By.XPATH, "//body[1]/div[9]/div[1]/div[1]/div[1]/button[1]")

    #Search in admin functionality
    searchvendorAdmin = (By.XPATH, "//body[1]/div[5]/div[4]/div[1]/div[2]/div[1]/div[2]/div[1]/label[1]/input[1]")
    searchuserAdmin = (By.XPATH, "//body[1]/div[5]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/label[1]/input[1]")
    searchfarmermarketAdmin = (By.XPATH, "//body[1]/div[5]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/label[1]/input[1]")
    clickLogoutTab = (By.XPATH, "//body[1]/div[1]/nav[1]/div[2]/ul[1]/li[4]/a[1]")
    clickLogout = (By.XPATH, "//body[1]/div[1]/nav[1]/div[2]/ul[1]/li[4]/div[1]/a[1]")

    #Refresh for Vendor , User , Market
    vendorrefresh = (By.XPATH, "//body[1]/div[5]/div[2]/div[3]/button[1]")
    userrefresh = (By.XPATH, "//body[1]/div[5]/div[1]/div[2]/button[2]")
    marketrefresh = (By.XPATH, "//body[1]/div[5]/div[1]/div[2]/button[2]")