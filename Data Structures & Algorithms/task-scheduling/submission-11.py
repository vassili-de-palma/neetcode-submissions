class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0: return len(tasks)

        frq = Counter(tasks) # O(m) CHECK
        

        h = [(-frq[x], x) for x in frq]
        heapq.heapify(h) # O(L) with L number of distinct tasks

        cdwn = deque(["IDLE"] * n, maxlen=n)

        ans = 0
        count = 0

        while count < len(tasks):
            y = cdwn.popleft()
            if not h:
                cdwn.append("IDLE")
            else:
                _, x = heapq.heappop(h)
                cdwn.append(x)
                frq[x] -= 1
                count += 1
            if y != "IDLE" and frq[y] > 0:
                heapq.heappush(h, (-frq[y], y))
            ans += 1
        return ans

            
                
           


        
        