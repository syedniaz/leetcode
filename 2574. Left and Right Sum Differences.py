class Solution(object):
    def leftRightDifference(self, nums):
        leftSum = []
        rightSum = []
        rS = list(nums)
        rS.reverse()
        answer = []
        l = 0
        r = 0
        for i, n in enumerate(nums):
            if (i==0):
                leftSum.append(l)
                l = n
            else:
                leftSum.append(l)
                l += n
        for i, n in enumerate(rS):
            if (i==0):
                rightSum.append(r)
                r = n
            else:
                rightSum.append(r)
                r += n
        rightSum.reverse()

        for i, n in enumerate(rightSum):
            s = abs(leftSum[i]-rightSum[i])
            answer.append(s)
        
        return answer