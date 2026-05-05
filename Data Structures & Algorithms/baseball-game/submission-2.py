class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        total=0
        for i in operations:
            if i.lstrip('-').isdigit():
                st.append(int(i))
            elif i.isalpha():
                if i=='C':
                    st.pop()
                if i=='D':
                    a = st.pop()
                    st.append(a)
                    st.append(2*a)
            else:
                a = st.pop()
                b = st.pop()
                if i=="+":
                    c=a+b
                st.append(b)
                st.append(a)
                st.append(c)
        while st:
            val = st.pop()
            total+=val
        return total