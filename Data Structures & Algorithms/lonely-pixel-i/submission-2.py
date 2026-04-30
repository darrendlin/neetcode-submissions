import collections
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        b_cols = collections.defaultdict(list)
        bad_rows = set()

        for r in range(len(picture)):
            added = 0
            for c in range(len(picture[0])):
                if picture[r][c] == 'B':
                    added += 1
                    b_cols[c].append(r)
            if added > 1:
                bad_rows.add(r)
        print(b_cols)
        alone = 0
        for col in b_cols:
            if len(b_cols[col]) == 1 and b_cols[col][0] not in bad_rows:
                alone += 1
        return alone
                