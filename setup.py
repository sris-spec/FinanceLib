import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

REQUIRED =['matplotlib','numpy','pandas_datareader','pandas','mypy']


setuptools.setup(
    name="FinanceLib",
    version="0.0.1",
    description='A python library that consists of modules for different types of financial calculations and analysis.',
    long_description= long_description,
    long_description_content_type='text/markdown',
    author='Chahat Mittal,Harleen Kaur,Sristhi Sahoo',
    author_email='financeLib027@gmail.com',
    python_requires='>=3.7',
    url='https://github.com/sris-spec/FinanceLib.git',
    install_requires=REQUIRED,
    license='MIT',
    keywords =['python', 'Finance with python', 'interest', 'analysis', 'general banking' , 'visualising finance','stock','yahoo finance'],
    classifiers=[
        "Development Status :: 1 - Developing",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        'License :: OSI Approved :: MIT License',
        
    ],
    
)
