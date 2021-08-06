'''
This is for practising arrays and strings from GMs - Chapter #1
'''
import os
import random
os.system('clear')

class Solution:
    def isUnique(self, s):
        # Solution to determine string
        # has all unique characters.
        l=[False]*62
        for char in s:
            v=ord(char)-65
            if l[v]:
                return False
            l[v]=True
        return True

    def checkpermutation(self, s1, s2):
        # Solution to check if two strings are
        # permutations of each other.
        if sorted(s1)==sorted(s2):
            return True
        return False

    def replacespacewithstring(self, s):
        # Solution to replace space in string
        # with special chars.
        s=s.replace(' ', '%20')
        return s

    def palindromepermutation(self, s):
        # Solution to check if a string has
        # palindrome permutation.
        def iseven(x):
            if x%2==0:
                return True
            return False
        
        s=s.lower()
        d={}
        for c in s:
            if c != ' ':
                if c in d:
                    d[c]+=1
                else:
                    d[c]=1
        oddcount, evencount=0, 0
        for v in d.values():
            if iseven(v):
                evencount+=1
            else:
                oddcount+=1
        
        if oddcount>1: return False
        return True

    def isoneaway(self, s1, s2):
        # Solution to check if two strings
        # are one edit away.
        def oneEditReplace(s1, s2):
            diff=False
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    if diff:
                        return False
                    else:
                        diff=True
            return True

        def oneEditInsert(s1, s2):
            index1, index2=0, 0
            while index1 < len(s1) and index2 < len(s2):
                if s1[index1] != s2[index2]:
                    if index1!=index2:
                        return False
                    index2 += 1
                else:
                    index1+=1
                    index2+=1
            return True

        if len(s1)==len(s2):
            cond=oneEditReplace(s1, s2)
            return cond
        elif len(s1)+1==len(s2):
            oneEditInsert(s1, s2)
        elif len(s1)==len(s2)+1:
            oneEditInsert(s2, s1)
        return False

    def stringcompression(self, s):
        # Solution to compress a string.
        # If the size of final string same as
        # size of original string, return
        # original string.
        '''
        Time=O(n)+O(m) where n is the len of string
                       where m is the len of dict
        Space=O(m) where m is the len of dict
        '''
        initlen=len(s)
        d={}
        for char in s:
            if char in d:
                d[char]+=1
            else:
                d[char]=1
        compstr=''
        #print(d)
        for k, v in d.items():
            compstr+=str(k)+str(v)
        compstr=compstr.strip()
        finallen=len(compstr)
        if initlen==finallen: return s
        else:
            return compstr
    
    def isSubString(self, s1, s2):
        '''
        Solution to check if s2 is a rotation
        of s1.
        '''
        if len(s1)==len(s2) and len(s1)>0:
            s2s2=s2+s2
            if s1 in s2s2:
                return True
        return False

    def zeromatrix(self, rows, cols, x, y):
        '''
        Solution to check a zero matrix. If an element
        in MXN matrix is 0, it's entire row and columns
        are set to 0.
        '''
        mat=[]
        print(rows, cols, x, y)
        for i in range(rows):
            col=[]
            for j in range(cols):
                v=random.randrange(1, 9)
                #print(x)
                col.append(v)
            mat.append(col)

        # Printing original matrix 
        for i in range(rows):
            l=''
            for j in range(cols):
                l+=str(mat[i][j])+' '
            l=l.strip()
            print(l)
        print('\n')
        if x<=0 or x>rows:
            return -1
        if y<=0 or y>rows:
            return -1
        xindex, yindex=x-1, y-1
        #print(x, y, xindex, yindex)
        for i in range(rows):
            mat[i][yindex]=0
        for i in range(cols):
            mat[xindex][i]=0

        # Printing final matrix
        for i in range(rows):
            l=''
            for j in range(cols):
                l+=str(mat[i][j])+' '
            l=l.strip()
            print(l)
        print('\n')
        return

    def rotatematrix(self, rows, cols):
        '''
        Solution to rotate a sqaure matrix by 90
        degrees. Also, to rotate it in place.
        '''
        mat=[]
        for i in range(rows):
            r=[]
            for j in range(cols):
                v=random.randrange(0,9)
                r.append(v)
            mat.append(r)
        print('Initial matrix:')
        for i in range(rows):
            l=''
            for j in range(cols):
                l+=str(mat[i][j])+' '
            l=l.strip()
            print(l)
        
        # Rotating matrix by 90 degrees
        mat[:]=[[row[i] for row in mat[::-1]] for i in range(len(mat))]

        print('Rotated matrix:')
        for i in range(rows):
            l=''
            for j in range(cols):
                l+=str(mat[i][j])+' '
            l=l.strip()
            print(l)
        return


obj=Solution()

# Problem-1.1
#cond=obj.isUnique('asdfxz')
#print(cond)

# Problem-1.2
#cond=obj.checkpermutation('aasdf', 'asdxa')
#print(cond)

# Problem-1.3
#s=obj.replacespacewithstring('Today is sunny')
#print(s)

# Problem-1.4
#cond=obj.palindromepermutation('Tact Cxoa')
#print(cond)

# Problem-1.5
#cond=obj.isoneaway('pale', 'ple')
#print(cond)

# Problem-1.6
#coms=obj.stringcompression('aabbcdeee')
#print(coms)

# Problem-1.7
obj.rotatematrix(3, 3)

# Problem-1.8
#obj.zeromatrix(5, 5, 4, 3)

# Problem-1.9
#cond=obj.isSubString('waterbottle', 'terbottlewa')
#print(cond)