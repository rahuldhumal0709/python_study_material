#[3,4,5,6,7],remain=8
#combination sum =[3,5],[4,4]

# result=[]
# def combsum(remain,comb,start):
#     if remain==0:
#         result.append(list(comb))
#         return
#     if remain<0:
#         return
#     for i in range(start,len(comb)):
#         comb.append(comb[i])
#         combsum(remain-comb[i],comb,i)
#         comb.pop
#     return result
# target=int(input("Enter your target : "))
# lst=[2,3,4,5,6]
# combsum(target,lst,0)

class Solution(object):
   def combinationSum(self, candidates, target):
      result = []
      unique={}
      candidates = list(set(candidates))
      self.solve(candidates,target,result,unique)
      return result
   def solve(self,candidates,target,result,unique,i = 0,current=[]):
      if target == 0:
         temp = [i for i in current]
         temp1 = temp
         temp.sort()
         temp = tuple(temp)
         if temp not in unique:
            unique[temp] = 1
            result.append(temp1)
         return
      if target <0:
         return
      for x in range(i,len(candidates)):
         current.append(candidates[x])
         self.solve(candidates,target-candidates[x],result,unique,i,current)
         current.pop(len(current)-1)
ob1 = Solution()
print(ob1.combinationSum([3,4,5,6],9))