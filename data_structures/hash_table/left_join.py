from hash_table import HashTable as HT


def left_join(hash1, hash2):
    """Left join two hash tables."""
    one = []
    ht = HT()
    for bucket in hash1.buckets:
        if bucket:
            one.append(bucket.head.val)
    for each in one:
        key = list(each.keys())[0]
        value = list(each.values())[0]
        if hash2.buckets[hash2._hash_key(key)]:
            each[key] = value, list(hash2.buckets[hash2._hash_key(key)].head.val.values())[0]
        else:
            each[key] = value, None
        ht.set(key, each[key])
    return ht
