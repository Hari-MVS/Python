class Solution():
    def maxHist(self, row):
        result = []
        top_val = 0
        max_area = 0
        area = 0  
        i = 0
        while (i < len(row)):
            if (len(result) == 0) or (row[result[-1]] <= row[i]):
                result.append(i)
                i += 1
            else:
                top_val = row[result.pop()]
                area = top_val * i
 
                if (len(result)):
                    area = top_val * (i - result[-1] - 1)
                max_area = max(area, max_area)
        while (len(result)):
            top_val = row[result.pop()]
            area = top_val * i
            if (len(result)):
                area = top_val * (i - result[-1] - 1)
            max_area = max(area, max_area)
        return max_area
    def maxRectangle(self, A):
        result = self.maxHist(A[0])
        for i in range(1, len(A)):
            for j in range(len(A[i])):
                if (A[i][j]):
                    A[i][j] += A[i - 1][j]
            result = max(result, self.maxHist(A[i]))
 
        return result

A = []
m,n=[int(i) for i in input().split()]
for i in range(m):
    temp=[]
    for j in input().split():
        if j=="X":
            temp.append(1)
        else:
            temp.append(0)
    A.append(temp)
ans = Solution()
 
print(ans.maxRectangle(A))
