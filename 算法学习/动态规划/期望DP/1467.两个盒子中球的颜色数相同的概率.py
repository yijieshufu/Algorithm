import math

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        total_balls = sum(balls)
        n = total_balls // 2
        k_colors = len(balls)
        
        # 预计算总组合数（分母）
        total_cases = math.comb(total_balls, n)
        
        # DFS 状态: (当前颜色索引, A盒球数, A盒颜色数, B盒颜色数)
        # 返回值: 该状态下满足条件的组合数之和
        
        # 使用 memoization 优化（虽然本题数据规模较小，不用也可以）
        memo = {}

        def dfs(idx, count_a, distinct_a, distinct_b):
            if count_a > n: # 剪枝：A拿多了
                return 0
            
            # 同样可以判断 B 是否拿多了: 
            # 当前处理过的球总数 = sum(balls[:idx])
            # B当前的球数 = 当前处理过的球 - count_a
            # 如果 B当前的球数 > n，也可以剪枝，但这里不做复杂计算简化逻辑
            
            if idx == k_colors:
                # 只有当 A 刚好拿了 n 个球，且颜色种类相等时，才算有效
                return 1 if count_a == n and distinct_a == distinct_b else 0
            
            state = (idx, count_a, distinct_a, distinct_b)
            if state in memo:
                return memo[state]
            
            res = 0
            current_ball_count = balls[idx]
            
            # 枚举 A 拿取当前颜色的数量 x
            for x in range(current_ball_count + 1):
                # B 拿取的数量
                y = current_ball_count - x
                
                # 更新颜色种类计数
                new_distinct_a = distinct_a + (1 if x > 0 else 0)
                new_distinct_b = distinct_b + (1 if y > 0 else 0)
                
                # 计算当前分配的组合数贡献：C(total, x)
                ways = math.comb(current_ball_count, x)
                
                res += ways * dfs(idx + 1, count_a + x, new_distinct_a, new_distinct_b)
            
            memo[state] = res
            return res

        valid_cases = dfs(0, 0, 0, 0)
        return valid_cases / total_cases
