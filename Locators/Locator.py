class Create_account:
    button_Signin_xpath = '//a[@class="login"]'
    textbox_emailcreate_id = "email_create"
    button_Createanaccount = "SubmitCreate"


class create_successaccount:
    button_Sign_xpath = '//a[@class="login"]'
    button_Createanaccount = "SubmitCreate"
    textbox_email = "email"
    textbox_password = "passwd"
    button_signin = "SubmitLogin"


class newsletter:
    textbox_newsletter_xpath = "//input[@id='newsletter-input']"
    button_newsletter = '//button[@name="submitNewsletter"]'


class contactUs:


    button_ContactUs = '//*[@id="contact-link"]/a'
    subject = "id_contact"
    order_reference_id = 'id_order'
    Email_address_id = "email"
    textboxt_attach_file_id = 'fileUpload'
    send_id = 'submitMessage'
    textbox_message_id = 'message'


class changebuy:

    button_addtocard1 = "//ul[@id='homefeatured']//div[@class='button-container']//a[@data-id-product='1']"
    button_addtocard2 = "//ul[@id='homefeatured']//div[@class='button-container']//a[@data-id-product='2']"
    button_addtocard3 = "//ul[@id='homefeatured']//div[@class='button-container']//a[@data-id-product='3']"
    button_addtocard4 = "//ul[@id='homefeatured']//div[@class='button-container']//a[@data-id-product='4']"
    button_addtocard5 = "//ul[@id='homefeatured']//div[@class='button-container']//a[@data-id-product='5']"
    button_continue_shopping = '//*[@class="continue btn btn-default button exclusive-medium"]'
    button_proceedtocheckout = '//a[@class="btn btn-default button button-medium"]'


class contactus:
    button_ContactUs = '//*[@id="contact-link"]/a'
    subject = "id_contact"
    order_reference_id = 'id_order'
    Email_address_id = "email"
    textboxt_attach_file_id = 'fileUpload'
    send_id = 'submitMessage'
    # file_xpath = ('C:\Users\New folder\xpath.txt')
    textbox_message_id = 'message'


class Chitietsanpham:
    img1 = '//*[@id="homefeatured"]/li[1]/div'
    product_xpath = '//*[@id="bigpic"]'


class write_a_comment():
    button_Signin_xpath = '//*[@class="header_user_info"]'
    textboxt_email_address = '//*[@id="email"]'
    textbox_password = '//*[@id="passwd"]'
    button_signin_register = '//*[@id="SubmitLogin"]'
    img_logo = '//*[@id="header_logo"]/a/img'
    img1 = '//*[@id="homefeatured"]/li[1]/div'
    button_write_a_review = '//a[@class="open-comment-form"]'
    textboxt_title_id = 'comment_title'
    text_comment = '//*[@id="content"]'
    button_send = '//*[@id="submitNewMessage"]'


class share_to_tweet:
    image2 = '//*[@id="homefeatured"]/li[2]/div'
    button_tweet = "//button[normalize-space()='Tweet']"
    textbox_username_tweet = "//button[normalize-space()='Tweet']"
    textbox_password_tweet = "//div[@class='css-1dbjc4n r-13qz1uu']//form"


class send_to_friend:
    img2 = '//*[@id="homefeatured"]/li[2]/div'
    button_send_to_friend = '//*[@id="send_friend_button"]'
    textbox_friendname = '//*[@id="friend_name"]'
    textbox_email_address = '//*[@id="friend_email"]'
    button_send = '//*[@id="sendEmail"]'

class Searchall:
    textboxt_search = '//*[@id="search_query_top"]'
    button_search = '//*[@id="searchbox"]/button'
    price_product = '//*[@id="center_column"]/ul/li[1]/div/div[2]/div[1]/span[1]'
    product = '//*[@id="index"]/div[2]/ul/li'