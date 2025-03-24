from setuptools import setup, find_packages

setup(
    name="xaif",
    version="0.3.4",
    author="DEBELA",
    author_email="dabookoo@gmail.com",
    description="xaif package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/arg-tech/xaif",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
