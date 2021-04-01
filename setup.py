import setuptools

with open("README.md", "r") as readme_file:

    long_description = readme_file.read()

setuptools.setup(

    name="SnS_SampleProject",

    version="0.1.0",

    author="<AlexanderBlair>",

    author_email="alexander.blair.dev@gmail.com",

    description="<SampleProject Package>",

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="<https://github.com/SnSation/SampleProject>",

    license='MIT',

    packages=setuptools.find_packages('src'),

    package_dir={'': 'src'},

    classifiers=[

        "Programming Language :: Python :: 3",

        "Operating System :: OS Independent",

    ],

    python_requires='>=3.6',

)