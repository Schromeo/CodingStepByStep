'''
想象一下你正在池塘边钓鱼。要钓到一条鱼，鱼饵的大小必须严格小于鱼的大小。一旦鱼被钓上，它就会被移出池塘，不能再被钓到。但是，每个鱼饵最多可以使用 3 次，之后就会耗尽。

给定两个数组 fish (池塘中鱼的大小) 和 baits (你拥有的鱼饵大小)，你的任务是返回你能钓到的最大鱼类数量。

提示： 为了计算答案，你需要充分利用每个鱼饵，从最大的鱼饵开始，到最小的鱼饵。使用每个鱼饵来钓池塘中剩下最大的鱼...
'''
def solution(fish, baits):
    fish.sort()
    baits.sort()
    catch_count = 0
    fish_idx = len(fish)-1
    for bait in reversed(baits):
        bait_uses = 0
        while fish_idx >= 0 and bait_uses < 3 and bait < fish[fish_idx]:
            catch_count += 1
            fish_idx -= 1
            bait_uses += 1
    return catch_count

fish1 = [1, 2, 3]
baits1 = [1]
print(f"示例 1: {solution(fish1, baits1)}") # 输出: 2

fish2 = [2, 2, 3, 4]
baits2 = [1]
print(f"示例 2: {solution(fish2, baits2)}") # 输出: 3

fish3 = [1, 4, 3, 2]
baits3 = [1, 1]
# 注意: .sort() 是 "in-place" 操作, 我们需要复制列表
# 否则 fish3 会被第一个 print 排序, 影响第二个
print(f"示例 3: {solution(fish3.copy(), baits3.copy())}") # 输出: 3