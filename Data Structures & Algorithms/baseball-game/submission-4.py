class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        total=0
        for i in operations:
            if i.lstrip('-').isdigit():
                st.append(int(i))
            elif i=='C':
                st.pop()
            elif i=='D':
                st.append(2*st[-1])
            else:
                st.append(st[-1]+st[-2])
        while st:
            val = st.pop()
            total+=val
        return total