'''
CodewritingYour task is to implement a simplified inventory tracking system for a large retail store.1You are given a transaction log, 
where each log item corresponds to one of three transaction types: supply, sell, or return. 
Log items are provided in the following format:2["supply", "<item name>", "<count>", "<price>"] - 
the store receives <count> units of <item name>, and each item costs <price>.
3["sell", "<item name>", "<count>"] 
- the store sells <count> units of <item name>. If the specified item is available at different prices, the cheapest ones should be sold first. 
It is guaranteed that the store will always have enough items to satisfy all sell transactions.
4["return", "<item name>", "<count>", "<sell price>", "<new price>"] - the store takes back <count> units of <item name>. 
It is guaranteed that the store has sold at least <count> units of <item name> previously at price <sell price>, which were not returned yet. 
The returned items can be added back to inventory and sold later at price <new price>.
5The tracking system should return the revenue from all sell transactions after processing the entire transaction log. Specifically, return an array representing the amount of money the store received from each sell transaction.6Note: You are not expected to provide the most optimal solution, but a solution with time complexity n7ot worse than $O(\text{logs.length}^2)$ will fit within the execution time limit.ExampleForlogs = [
    ["supply", "item1", "2", "100"],
    ["supply", "item2", "3", "60"],
    ["sell", "item1", "1"],
    ["sell", "item1", "1"],
    ["sell", "item2", "2"],
    ["return", "item2", "1", "60", "40"],
    ["sell", "item2", "1"],
    ["sell", "item2", "1"]
]
the output should besolution(logs) = [100, 100, 120, 40, 60]

你的任务是为一家大型零售商店实现一个简化的库存跟踪系统。
你将获得一个交易日志（logs），其中每个日志项对应三种交易类型之一：supply (供应)、sell (销售) 或 return (退货)。
日志项按以下格式提供：["supply", "<商品名称>", "<数量>", "<价格>"] - 商店收到 <数量> 个 <商品名称>，每个商品的成本（进价）为 <价格>。
["sell", "<商品名称>", "<数量>"] - 商店售出 <数量> 个 <商品名称>。
如果该商品有不同价格的库存，应首先出售价格最低的。题目保证商店始终有足够的商品来满足所有 sell 交易。
["return", "<商品名称>", "<数量>", "<售出价格>", "<新价格>"] - 商店收回 <数量> 个 <商品名称>。
题目保证商店之前曾以 <售出价格> 售出了至少 <数量> 个该商品，并且这些商品尚未被退回。退回的商品将以 <新价格> 重新添加到库存中，以便将来出售。
该跟踪系统应在处理完整个交易日志后，返回所有 sell 交易产生的收入。
具体来说，返回一个数组，表示商店从每笔 sell 交易中获得的金额。
注意： 你不需要提供最优解，但时间复杂度不差于 $O(\text{logs.length}^2)$ 的解决方案将在执行时间限制内通过。

'''
import heapq
def solution(logs):
    inventory = {}
    result = []

    for log in logs:
        type = log[0]
        item = log[1]

        if type == 'supply':
            count = int(log[2])
            price = int(log[3])
            if item not in inventory:
                inventory[item] = []
            heapq.heappush(inventory[item], (price, count))
        
        elif type == "sell":
            count = int(log[2])
            total = 0
            while count > 0:
                price, availability = heapq.heappop(inventory[item])
                sell_count = min(count, availability)
                total += sell_count * price
                if availability > sell_count:
                    heapq.heappush(inventory[item], (price, availability - sell_count))
                count -= sell_count
            result.append(total)

        elif type == 'return':
            count = int(log[2])
            new_price = int(log[4])
            if item not in inventory:
                inventory[item] = []
            heapq.heappush(inventory[item], (new_price, count))
    return result        

print(solution([["supply", "item1", "2", "100"],
    ["supply", "item2", "3", "60"],
    ["sell", "item1", "1"],
    ["sell", "item1", "1"],
    ["sell", "item2", "2"],
    ["return", "item2", "1", "60", "40"],
    ["sell", "item2", "1"],
    ["sell", "item2", "1"]
]))
