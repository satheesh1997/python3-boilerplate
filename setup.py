import setuptools


with open("requirements.txt", "r") as fh:
    requirements = fh.read().split("\n")


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="python3.8.2-boilerplate",
    version="0.0.1",
    author="Author Name",
    author_email="Author Email",
    description="Boilerplate code to build project with python3.8.2 and pytest support",
    long_description=long_description,
    url="https://github.com/satheesh1997/python3.8.2-boilerplate",
    packages=[],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8.2",
)
