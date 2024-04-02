import setuptools

# to publish project as a pypi package or local package
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text_Summarizer"
AUTHOR_USER_NAME = "hisanamuhammed"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "hisanamuhammed01@gmail.com"

# Setting up local package, it will get installed every folder under src which has init file

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python app for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)