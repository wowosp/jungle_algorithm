class Solution:
    def hIndex(self, citations: List[int]) -> int:
        hidx = 0
        stop = 1

        while(stop):
            count=0
            for i in range(len(citations)):
                if (citations[i]>=hidx):
                    count+=1
            if (hidx<=count):
                hidx+=1
            else:
                stop=0
    
        return hidx-1