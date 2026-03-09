# 求面积和：红矩形不被黑矩形覆盖的部分，结果 mod 114514
# 扫描线 + 线段树（维护 cntR/cntB/有效长度 len）

import sys
import bisect

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))

    ev = []
    Y_list = []
    for _ in range(n):
        x1, y1, x2, y2 = [int(next(it)) for _ in range(4)]
        ev.append((x1, y1, y2, 1, 1))
        ev.append((x2, y1, y2, 1, -1))
        Y_list.extend([y1, y2])
    for _ in range(m):
        x1, y1, x2, y2 = [int(next(it)) for _ in range(4)]
        ev.append((x1, y1, y2, 2, 1))
        ev.append((x2, y1, y2, 2, -1))
        Y_list.extend([y1, y2])

    Y = sorted(list(set(Y_list)))
    Y.insert(0, 0)
    K = len(Y) - 1
    if K <= 0:
        print(0)
        return

    def get_L(y1):
        return bisect.bisect_left(Y, y1)
    def get_R(y2):
        return bisect.bisect_right(Y, y2) - 1

    ev.sort(key=lambda e: (e[0], e[1], e[2], e[3], e[4]))

    MOD = 114514
    size = 4 * (K + 2)
    sR = [0] * size
    sB = [0] * size
    le = [0] * size

    def pushup(idx, l, r):
        if sB[idx] > 0:
            le[idx] = 0
        elif sR[idx] > 0:
            le[idx] = Y[r + 1] - Y[l]
        else:
            if l == r:
                le[idx] = 0
            else:
                le[idx] = le[idx * 2] + le[idx * 2 + 1]

    def update(idx, l, r, L, R, val, color):
        if L <= l and r <= R:
            if color == 1:
                sR[idx] += val
            else:
                sB[idx] += val
            pushup(idx, l, r)
            return
        mid = (l + r) // 2
        if L <= mid:
            update(idx * 2, l, mid, L, R, val, color)
        if R > mid:
            update(idx * 2 + 1, mid + 1, r, L, R, val, color)
        pushup(idx, l, r)

    num_seg = K - 1
    if num_seg < 1:
        print(0)
        return

    ans = 0
    last_x = ev[0][0]
    for x, y1, y2, color, val in ev:
        ans = (ans + le[1] * (x - last_x)) % MOD
        L_idx = get_L(y1)
        R_idx = get_R(y2)
        L_idx = max(1, min(L_idx, num_seg))
        R_idx = min(R_idx, num_seg)
        if L_idx <= R_idx:
            update(1, 1, num_seg, L_idx, R_idx, val, color)
        last_x = x

    print(ans % MOD)

if __name__ == "__main__":
    main()
