import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="skyscrapers_ivddorrka",
    version="0.0.1",
    author="Daria Kuzmina",
    author_email="darya.kuzmina@ucu.edu.ua",
    description="Project checks whether there's a winning combination on the board ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ivddorrka/first_ex_lab1.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8'
)
