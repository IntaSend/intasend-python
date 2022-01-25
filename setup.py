from setuptools import setup

setup(
    name='intasend-python',
    packages=['intasend'],
    version='1.0.2',
    license='MIT',
    description='Official Python SDK for IntaSend Payments Gateway API',
    author='Felix Cheruiyot',
    author_email='support@intasend.com',
    url='https://github.com/IntaSend/intasend-python',
    download_url='https://github.com/IntaSend/intasend-python/archive/v_1.0.2.tar.gz',
    keywords=['payments', 'mpesa', 'card payments', 'visa',
              'mastercard', 'payments kenya', 'intasend'],
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
