# import pytest
#
# from src.page import NewPost
# from src.locators import NewPostLocators
# from time import sleep
#
#
# def test_register_username_already_exists(driver, env_config, register, login):
#     new_post = NewPost(env_config, driver).open
#     new_post.create_post('post_title', 'post_content')
#     assert register[0] in new_post.find_element(NewPostLocators.username).text
#     sleep(5)
#     new_post.click_on_element(NewPostLocators.button_delete)
#     sleep(500)
