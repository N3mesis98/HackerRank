#!/usr/bin/python3

if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        original = list(input())
        original.reverse()
        last_index = [None for j in range(26)]
        
        j=0
        for char in original:
            index = None
            for k in range(ord(char)-ord("a")+1, 26):
                index = last_index[k]
                if index != None:
                    break
            else:
                last_index[ord(char)-ord("a")] = j
                
            if index != None:
                original[j], original[index] = original[index], original[j]
                left = original[j:]
                left.reverse()
                right = sorted(original[:j])
                print("".join(left+right))
                break
            
            j+=1
        else:
            print("no answer")
