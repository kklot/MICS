import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="micsv-knguyen", # Replace with your own username
    version="0.0.6",
    author="Kinh Nguyen",
    author_email="van-kinh.nguyen@outlook.com",
    description="Automate MICS survey downloading",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kklot/micsv",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)