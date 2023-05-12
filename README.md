# Bloom Filter

Bloom Filter is a Python package for implementing a simple Bloom filter, a space-efficient probabilistic data structure that is used to test whether an element is a member of a set. Bloom filters have applications in a variety of fields, including computer networks, databases, and web caching systems.

## Installation

To install Bloom Filter, simply run the following command:
    
    pip install fast-bf

## Problem
    1.Solving Redis cache penetration.
    2.During web crawling, filter out URLs that already exist in the Bloom filter and do not crawl them.
    3.For spam email filtering, judge whether the sending email address is in the Bloom blacklist, and if so, classify it as spam.
    4.When dealing with large amounts of data, check if the given data is included.
    5.This is referred to as blacklist filtering.

## Usage

Here's a simple example that demonstrates how to use the Bloom Filter:

```python3
from bloom_filter import BloomFilter

## Create a new Bloom Filter with a capacity of 1000 and an error rate of 0.1
bf = BloomFilter(1000, 0.1)

## Add some elements to the Bloom Filter
bf.add("hello")
bf.add("world")

## Check if an element is in the Bloom Filter
print("hello" in bf) # True
print("foo" in bf) # False

```
In this example, we create a new Bloom Filter with a capacity of 1000 and an error rate of 0.1. We then add the strings "hello" and "world" to the filter, and check if the strings "hello" and "foo" are members of the filter.

## Contributing
Contributions are welcome! If you would like to contribute to Bloom Filter, please fork the repository and submit a pull request.

## License
Bloom Filter is released under the MIT License.
