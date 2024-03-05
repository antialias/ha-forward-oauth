from setuptools import setup, find_packages

setup(
    name='ha-forward-oauth',
    version='0.1.0',
    author='Your Name',
    author_email='your_email@example.com',
    description='A ForwardAuth service integrating with Home Assistant',
    long_description=open('readme.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourgithub/ha-forward-oauth',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[
        'Flask>=2.0.1',
        'requests>=2.25.1',
        'python-dotenv>=0.19.0',
    ],
    extras_require={
        'dev': [
            'pytest>=6.2.4',
            'pytest-flask>=1.2.0',
            'requests-mock',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
