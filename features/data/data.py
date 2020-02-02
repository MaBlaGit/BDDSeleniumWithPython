import time
_main_page_url = 'http://automationpractice.com'


def get_main_page_url():
    return _main_page_url


def random_email_generator():
    current_milli_time = lambda: int(round(time.time() * 1000))
    created_email = 'test-{}@test.com'.format(current_milli_time())
    return created_email
