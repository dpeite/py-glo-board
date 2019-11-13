from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="py-glo-board",
    version="1.0.2",
    author="Daniel Vilar Peiteado",
    author_email="danielvilar2@gmail.com",
    description="Python client for GitKraken Glo Boards API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    maintainer="Daniel Vilar Peiteado",
    maintainer_email="danielvilar2@gmail.com",
    keywords=["gitkraken", "glo boards"],
    url="https://github.com/dpeite/py-glo-board",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=["requests"],
    project_urls={
        'Bug Reports': 'https://github.com/dpeite/py-glo-board/issues',
        'Source': 'https://github.com/dpeite/py-glo-board',
    },

)
