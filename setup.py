import setuptools

with open("README.md", "r", encoding="utf-8" , errors="ignore") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Chicken-Disease-Classification"
AUTHOR_USER_NAME = "Bhavya Jethwa"
SRC_REPO = "Chicken_disease_classifiction"
AUTHOR_EMAIL = "bhavyajethwa11@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for Chicken disease classification app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)