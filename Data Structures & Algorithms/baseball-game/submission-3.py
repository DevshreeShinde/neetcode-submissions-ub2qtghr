class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        total=0
        for i in operations:
            if i.lstrip('-').isdigit():
                st.append(int(i))
            if i=='C':
                st.pop()
            if i=='D':
                st.append(2*st[-1])
            if i=='+':
                st.append(st[-1]+st[-2])
        while st:
            val = st.pop()
            total+=val
        return total