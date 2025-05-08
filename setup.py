from setuptools import setup, find_packages

setup(
    name="student-performance-ai",
    version="1.0.0",
    author="Sisipho Mdaka",
    description="An AI-powered system for predicting student performance.",
    packages=find_packages(exclude=["tests*", "docs*", "examples*"]),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "pytest",
        "pytest-cov"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
