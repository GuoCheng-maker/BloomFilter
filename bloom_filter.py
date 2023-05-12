import math


class BloomFilter:
    """
    布隆过滤器
    """
    def __init__(self, capacity, error_rate):
        """
        :param capacity: 容量
        :param error_rate: 误判率
        """
        self.capacity = capacity
        self.error_rate = error_rate
        self.num_bits = int(-capacity * math.log(error_rate) / (math.log(2) ** 2)) + 1
        self.num_hashes = int(self.num_bits * math.log(2) / capacity) + 1
        self.bits = [False] * self.num_bits

    def _get_hashes(self, element):
        """
        获取哈希值
        """
        hashes = []
        for i in range(self.num_hashes):
            hash_val = hash(str(element) + str(i))
            hashes.append(hash_val % self.num_bits)
        return hashes

    def add(self, element):
        """
        添加元素
        """
        hashes = self._get_hashes(element)
        for index in hashes:
            self.bits[index] = True

    def __contains__(self, element):
        """
        检查元素是否存在于布隆过滤器中
        """
        hashes = self._get_hashes(element)
        for index in hashes:
            if not self.bits[index]:
                return False
        return True
