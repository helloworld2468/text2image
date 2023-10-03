from setuptools import setup

setup(
    name='text2image',
    version='1.0.0',
    author='Soumalya Das',
    author_email='geniussantu1983@gmail.com',
    description='Use the power of AI to generate images based on your text.',
    long_description='Convert text to image using AI.',
    long_description_content_type='text/x-rst',
    packages=['text2image'],
    install_requires=[
        'requests',
    ],
    url='',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)