class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return res


# machine1

# machine2


"""
planning

ascii?
for temp intermediate string, need to concatenate not append each c

encode
what steps are req'd to encode?
iterate over each str in strs
iterate over each c in each str
add each c to new array/queue
new str will be just a string 
(but how to keep each word/string separate (delimiter) so can decode later?)
(use length of each str to delimit?)
instantiate 2 arrays?
if so, could combine into dict

decode
if instantiate 2 arrays as dict
use get_item() or index using key
and reassemble into orig strs
and return strs

T: O(n) for iteration over each c in str, O(m) for each str in strs; so O(n+m)
S: do we need to create any ds? maybe an intermediate queue? O(n)

handle edge cases
empty strs
"""