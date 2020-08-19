'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache = None):
    #base case
    if n < 0:
        return 0
    elif n == 0:
        return 1
        #see if the cache exists and if the el is in cache
    elif cache is not None and cache[n] > 0:
        #return previous cache value
        return cache[n]
    else:
        #create a cache if needed
        if cache is None:
            #create an empty list for cache
            cache = [0 for i in range(n+1)]
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
