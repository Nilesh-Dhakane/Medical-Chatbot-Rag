from setuptools import setup, find_packages

with open("requirements.txt") as file:
    requirements = file.read().splitlines()


setup(
    name="Medical-Chatbot-RAG",
    version="0.1",
    author="Nilesh Dhakane",
    packages=find_packages(),
    install_requires = requirements,
    python_requires=">=3.7"
)