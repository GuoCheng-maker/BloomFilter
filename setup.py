from setuptools import setup, find_packages

setup(
    name='fast-bf',
    version='1.1.1',
    url='https://github.com/GuoCheng-maker/bloom_filter.git',
    author='Cheng.guo',
    author_email='guocheng6868@126.com',
    description='A fast bloom filter implementation in Python',
    packages=find_packages(),
    install_requires=[
        # add any dependencies here
        # 'numpy>=1.18.1',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
