from setuptools import setup

long_description = None
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="gitchk",
    packages=["gitchk"],
    version="1.3.1",
    license="MIT",
    description="Manage multiple git repos from one place",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/noluminagency-cloud/gitchk",
    platforms=["linux", "osx", "win32"],
    keywords=["git", "manage multiple repositories", "cui", "command-line"],
    author="Davey Mars",

    entry_points={"console_scripts": ["gitchk = gitchk.__main__:main"]},
    python_requires=">=3.14",
    install_requires=["argcomplete"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Version Control :: Git",
        "Topic :: Terminals",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3.14",

    ],
    include_package_data=True,
)
