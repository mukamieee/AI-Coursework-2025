def solution(A):
    # Implement your solution here
    def count(arr, N):
        s = set()
        for i in range(N):
            s.add(abs(arr[i]))
        return len(s)

    N = len(A)
    return count(A, N)
