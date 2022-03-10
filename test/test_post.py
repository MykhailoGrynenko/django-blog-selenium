import allure


from src.locators import NewPostLocators


@allure.step
def test_new_post_correct_data(register, create_post):
    assert register[0] in create_post.get_element_text(NewPostLocators.username)
    assert 'post_title' in create_post.get_element_text(NewPostLocators.title)
    assert 'post_content' in create_post.get_element_text(NewPostLocators.content)
    assert 'Update' in create_post.get_element_text(NewPostLocators.button_update)
    assert 'Delete' in create_post.get_element_text(NewPostLocators.button_delete)


@allure.step
def test_update_button(driver, create_post):
    create_post.click_on_element(NewPostLocators.button_update)
    assert 'post_title' in create_post.get_input_text(NewPostLocators.update_title)
    assert 'post_content' in create_post.get_input_text(NewPostLocators.update_content)
    assert 'Post' in create_post.get_element_text(NewPostLocators.button_update_confirm)


@allure.step
def test_update_post_only_title(create_post):
    create_post.update_post('title_updated')
    assert 'title_updated' in create_post.get_element_text(NewPostLocators.title)


@allure.step
def test_update_post_only_content(create_post):
    create_post.update_post(content='content_updated')
    assert 'content_updated' in create_post.get_element_text(NewPostLocators.content)


@allure.step
def test_update_post_both_title_and_content(create_post):
    create_post.update_post('title_updated_again', 'content_updated_again')
    assert 'title_updated_again' in create_post.get_element_text(NewPostLocators.title)
    assert 'content_updated_again' in create_post.get_element_text(NewPostLocators.content)


@allure.step
def test_delete_post(driver, create_post):
    create_post.delete_post()
    assert 'https://myamazingdjangoblog.herokuapp.com/' == driver.current_url
