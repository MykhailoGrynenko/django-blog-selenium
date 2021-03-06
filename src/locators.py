from selenium.webdriver.common.by import By


class NavigationLocators:
    home = (By.CSS_SELECTOR, 'a[href="/"]')
    about = (By.CSS_SELECTOR, 'a[href="/about/"]')
    login = (By.CSS_SELECTOR, 'a[href="/login/"]')
    register = (By.CSS_SELECTOR, 'a[href="/register/"]')
    new_post = (By.CSS_SELECTOR, 'a[href="/post/new/"]')
    profile = (By.CSS_SELECTOR, 'a[href="/profile/"]')
    logout = (By.CSS_SELECTOR, 'a[href="/logout/"]')


class LoginLocators:
    username = (By.ID, 'id_username')
    pass_login = (By.ID, 'id_password')
    button_login = (By.XPATH, '//button[text()="Login"]')
    forgot_pass = (By.CSS_SELECTOR, 'a[href="/password-reset/"]')
    sign_up_now = (By.LINK_TEXT, 'Sign Up now')
    do_you_need_account = (By.XPATH, '/html/body/main/div/div[1]/div/div/small')
    incorrect_data = (By.XPATH, '//fieldset/div[1]/ul/li')


class RegisterLocators:
    username = (By.ID, 'id_username')
    email = (By.ID, 'id_email')
    pass_register_one = (By.ID, 'id_password1')
    pass_register_two = (By.ID, 'id_password2')
    button_sign_up = (By.XPATH, '//button[text()="Sign Up"]')
    sign_in = (By.LINK_TEXT, 'Sign In')
    error_username = (By.ID, 'div_id_username')
    error_email = (By.ID, 'div_id_email')
    error_password = (By.ID, 'div_id_password2')
    valid_registration = (By.XPATH, '/html/body/main/div/div[1]/div[1]')


class ProfileLocators:
    username = (By.ID, 'id_username')
    email = (By.ID, 'id_email')
    button_update = (By.XPATH, '//button[text()="Update"]')


class NewPostLocators:
    create_title = (By.ID, 'id_title')
    crate_content = (By.ID, 'id_content')
    button_post = (By.XPATH, '//button[text()="Post"]')

    username = (By.XPATH, '/html/body/main/div/div[1]/article/div/div/a')
    time = (By.XPATH, '/html/body/main/div/div[1]/article/div/div/small')
    title = (By.XPATH, '/html/body/main/div/div[1]/article/div/h2')
    content = (By.XPATH, '/html/body/main/div/div[1]/article/div/p')
    button_update = (By.XPATH, '/html/body/main/div/div[1]/article/div/div/div/a[1]')
    button_update_confirm = (By.XPATH, '/html/body/main/div/div[1]/div/form/div/button')
    button_delete = (By.XPATH, '/html/body/main/div/div[1]/article/div/div/div/a[2]')
    button_yes_delete = (By.XPATH, '/html/body/main/div/div[1]/div/form/div/button')
    button_delete_cancel = (By.XPATH, '/html/body/main/div/div[1]/div/form/div/a')
    update_title = (By.ID, 'id_title')
    update_content = (By.ID, 'id_content')
    delete_post_text = (By.XPATH, '/html/body/main/div/div[1]/div/form/fieldset/h2')
