from setuptools import setup, find_packages
import add_gitignore

setup(
    name="add_gitignore",
    version="0.9.0",
    author="fanny vieira",
    author_email="fannyvieira082@gmail.com",
    packages=find_packages(),
    license='MIT License',
    url="https://github.com/FannyVieira/add-gitignore",
    entry_points={
        'console_scripts': [
            'add-gitignore=add_gitignore:command_line_runner',
        ]
    },
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'requests',
    ],
    description="Generate Gitignore rules basing on GitHub's templates collection."
)
