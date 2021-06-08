from setuptools import setup

setup(
    name='intasend-python',
    packages=['intasend'],
    version='0.1',
    license='MIT',
    description='Official Python SDK for IntaSend Payments Gateway API',
    author='Felix Cheruiyot',
    author_email='support@intasend.com',
    url='https://github.com/IntaSend/intasend-python',
    download_url='https://github.com/IntaSend/intasend-python/archive/v_01.tar.gz',
    keywords=['payments', 'mpesa', 'card payments',
              'payments kenya', 'intasend'],
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
