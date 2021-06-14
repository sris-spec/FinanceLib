import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

REQUIRED =['matplotlib','numpy','pandas_datareader','pandas','mypy']

setuptools.setup(
    name="FinanceLib",
    version="0.0.1",
    description='A basic python library for financial calculations and analysis with graphical representation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Chahat Mittal,Harleen Kaur,Sristhi Sahoo',
    author_email='financeLib@gmail.com',
    python_requires='>=3.7',
    url='https://github.com/sris-spec/FinanceLib.git',
    install_requires=REQUIRED,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    
)
