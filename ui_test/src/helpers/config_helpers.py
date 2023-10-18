import os


def get_base_url():
    env = os.environ.get('ENV', 'test')
    if env.lower() == 'test':
        return 'https://automationintesting.online/'

    elif env.lower() == 'prod':
        return 'http://demostore.prod.supersqa.com/my-account/'

    else:
        raise Exception(f"Unknown environment: {env}")
