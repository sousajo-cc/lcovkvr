import setuptools

setuptools.setup(
    name='lcovkv',
    version='0.1.0',
    maintainer='Jorge Pinto Sousa',
    maintainer_email='jorge.pinto.sousa@protonmail.com',
    description='A Flask kv service to store lcov values for a commit hash',
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask_restful'
    ],
    extras_require={
        'test': [
            'pytest',
            'pytest-cov',
        ],
    },
)
