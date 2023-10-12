from setuptools import setup, find_packages
import os
import requests
from io import BytesIO
from zipfile import ZipFile

# Function to download and extract files from a GitHub release
def download_and_extract_files(url, dest_folder):
    response = requests.get(url)
    with ZipFile(BytesIO(response.content)) as zipf:
        zipf.extractall(dest_folder)

# Your package details
setup(
    name='ermodels',
    version='1.0',
    description='',
    author='Simon Oxenford',
    author_email='oxenfordsimon@gmail.com',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
)

# Define the URL to your GitHub release assets
github_release_url = 'https://github.com/simonoxen/ermodels/releases/download/v1.0/data.zip'

# Determine the destination folder for the downloaded files
dest_folder = 'ermodels/data'

# Check if the destination folder exists; create it if it doesn't
if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

# Download and extract the files
download_and_extract_files(github_release_url, dest_folder)
