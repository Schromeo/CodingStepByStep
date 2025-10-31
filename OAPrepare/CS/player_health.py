'''
想象一个视频游戏，玩家控制一个角色闯过几个关卡。该角色拥有一个初始健康值 initialHealth，这个值会随着玩家闯关而改变。

你将获得一个整数数组 deltas，它定义了每次健康值的变化。具体来说，第 i 个关卡（0-indexed）会使角色的当前健康值改变 deltas[i]。请注意，一旦当前健康值变得小于 0，它会立即被设置为 0。同样，一旦当前健康值变得大于 100，它会立即被设置为 100。

你的任务是返回角色在闯过所有关卡后的最终健康值。
Example
For initialHealth = 12 and deltas = [-4, -12, 2, 8], the output should be 10.

Explanation: (注：你图片中的示例输出为 8，这似乎是基于其描述中的一个拼写错误 6 + 2 = 8。根据题目规则和所提供的 Java 解法，正确的逻辑和输出应该是 10。)

At the beginning, currentHealth = 12.

After level 0 (-4): currentHealth becomes 12 + (-4) = 8.

After level 1 (-12): currentHealth becomes 8 + (-12) = -4. Since this is less than 0, it gets set to 0.

After level 2 (2): currentHealth becomes 0 + 2 = 2.

After level 3 (8): currentHealth becomes 2 + 8 = 10.

The final answer is 10.
'''
def solution(initialHealth, deltas):
    current_health = initialHealth
    for d in deltas:
        current_health += d
        if current_health < 0:
            current_health = 0
        elif current_health > 100:
            current_health = 100
    return current_health

def solution_optimal(initialHealth, deltas):
    current_health = initialHealth
    
    for d in deltas:
        current_health += d
        
        # 钳位操作:
        # 1. max(0, current_health) 保证结果永远 >= 0
        # 2. min(100, ...) 保证上一步的结果永远 <= 100
        current_health = min(100, max(0, current_health))
            
    return current_health

initialHealth = 12
deltas = [-4, -12, 2, 8]
print(f"Final health: {solution(initialHealth, deltas)}") 
# 输出: Final health: 10