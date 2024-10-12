from setuptools import setup, find_packages

# Full setup configuration
setup(
    name="onyxmod",  # The name of your library
    version="0.1.0",  # Version number of your library
    packages=find_packages(),  # Automatically find and include all Python packages
    description="A private library of reusable widgets",  # Short description of your library
    long_description=open('README.md').read(),  # Load the content from the README.md for detailed description
    long_description_content_type='text/markdown',  # Specify that the long description is in Markdown format
    url="https://github.com/opiumonyxtech/onyxmod",  # Link to your repository (optional)
    author="Jae",  # Your name or username
    install_requires=[
        'customtkinter'  # External dependency used in your code
    ],
)
