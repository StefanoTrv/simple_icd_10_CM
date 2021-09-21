import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple_icd_10_cm",
    version="1.1.2",
    author="Stefano Travasci",
    author_email="stefanotravasci@gmail.com",
    description="A simple python library for ICD-10-CM codes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/StefanoTrv/simple_icd_10_CM",
    packages=setuptools.find_packages(),
    package_dir={'simple_icd_10_cm': 'simple_icd_10_cm'},
    package_data={'simple_icd_10_cm': ['data/*']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    keywords='ICD-10-CM ICD-10 icd 10 CM codes clinical modification',
)