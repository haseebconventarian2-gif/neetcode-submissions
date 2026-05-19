class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        Total_Counts={};

        for num in nums:
           Total_Counts[num]=1+Total_Counts.get(num , 0)

        num_sorted=sorted(Total_Counts.items(), key =lambda x:x[1], reverse=True)


        result=[];
        for num,count in num_sorted:
          result.append(num)

          if len(result)==k:
            break

        return result
        