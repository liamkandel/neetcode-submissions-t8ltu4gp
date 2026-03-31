class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        used_idxs = set()
        big_list = []
        sub_list = []
        n = len(strs)

        for i in range(n):
            if i in used_idxs: # str is already in a sublist
                continue

            used_idxs.add(i) # add current index to used_idxs
            sub_list.append(strs[i]) # starting new sublist

            for j in range(i+1,n):
                if j not in used_idxs and sorted(strs[i]) == sorted(strs[j]):
                    sub_list.append(strs[j])
                    used_idxs.add(j)

            print("sub",i,sub_list)
            big_list.append(sub_list) # add sublist to big list
            print(big_list)
            sub_list = []

        return big_list