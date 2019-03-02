from distutils.core import setup

setup(
        name='stock_price_app',
        version='0.1',
        description='A stock price API built with Django REST framework',
        author='Friedrich Dunne',
        author_email='dunneff@tcd.ie',
        url='https://github.com/dunneff/stock-price-app',
        packages=find_packages(),
        install_requires=[
            'Django==2.1.7',
            'djangorestframework==3.9.1',
            'pytz==2018.9',
            ]
        )
