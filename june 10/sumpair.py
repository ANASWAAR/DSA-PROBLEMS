n, target = map(int, input().split())
a = list(map(int, input().split()))
st = set()
for i in range(n):
    req = target - a[i]
    if req in st:
        print("TRUE")
        break
    st.add(a[i])
else:
    print("FALSE")