from setuptools import setup

setup(
    name='intasend-python',
    packages=['intasend'],
    version='1.0.6',
    license='MIT',
    description='Official Python SDK for IntaSend Payments Gateway API',
    readme='README.md',
    author='Felix Cheruiyot',
    author_email='support@intasend.com',
    url='https://github.com/IntaSend/intasend-python',
    download_url='https://github.com/IntaSend/intasend-python/archive/v_1.0.6.tar.gz',
    keywords=['payments', 'mpesa', 'mpesa api', 'card payments', 'visa',
              'mastercard', 'payments kenya', 'intasend', 'airtime',],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ]
)
