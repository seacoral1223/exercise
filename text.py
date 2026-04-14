# for i in range(1,31,3):
#     print(i)

# # num=list(range(1,10000))
# # for i in num:
# #     print(i)
# # print(sum(num))
# # print()

# user_0 = {
# 			'username': 'efermi',
# 			'first': 'enrico',
# 			'last': 'fermi',
# 			}
# for key,value in user_0.items():
#     #print("\nkey:"+ key,"\nvalue:"+ value)
# 	print(key,value)


# i = 0
# num = int(input("请输入一个数字："))
# while num != 0:
# 	if num % 2 == 0:
# 		num = num/2
# 		i = i+1
# 	else:
# 		num = num-1
# 		i = i+1
# print(i)


# class Solution:
# 	def maximumWealth(self, accounts: List[List[int]]) -> int:
# 		max_wealth = 0
# 		for customer in accounts:
# 			wealth = sum(customer)
# 			if wealth > max_wealth:
# 				max_wealth = wealth
# 		return max_wealth

# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         answer = []
#         for i in range(1,n+1):
#             if i % 3 == 0 and i % 5 == 0:
#                 answer.append("FizzBuzz")
#             elif i % 3 == 0:
#                 answer.append("Fizz")
#             elif i % 5 == 0:
#                 answer.append("Buzz")
#             else:
#                 answer.append(str(i))
#         return answer

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow