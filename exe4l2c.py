nums = []
for i in range(3):
    nums.append(float(input(f"Digite o número {i+1}: ")))
nums.sort()
print(f"Menor número: {nums[0]}")
print(f"Número do meio: {nums[1]}")
print(f"Maior número: {nums[2]}")