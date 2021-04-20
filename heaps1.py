import heapq
x = [5, 2, 8, 1, 6, 7, 4, 9]

heapq.heapify(x)
print(x)
heapq.heappush(x, 0)
print(x)
print(heapq.heappop(x))
print(x)
print(heapq.heappushpop(x, 5))
print(x)
print(heapq.nlargest(4, x))
print(heapq.nsmallest(4, x))