#!/usr/bin/env python
# coding: utf-8

# # Lecture: Trees
# 
# A tree is a _data structure_ that is like a linked list, but each item can have multiple "children" or branches.

# In[2]:


class Tree:
    def __init__(self, value, branches=()):
        self.value = value
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.value, branches_str)

    def is_leaf(self):
        return not self.branches
    
    def add_branch(self, tree):
        assert isinstance(tree, Tree)
        self.branches.append(tree)


# # Accessing Items and Creating Trees

# In[3]:


my_tree = Tree(1)


# In[4]:


my_tree


# In[5]:


my_tree.value


# In[6]:


my_tree.is_leaf()


# In[7]:


my_tree.branches


# In[8]:


company = Tree('CEO', [Tree('CTO'), Tree('COO')])


# In[9]:


company


# In[ ]:





# In[ ]:





# In[10]:


root = company.value


# In[11]:


root


# In[12]:


employees = company.branches


# In[13]:


for emp in employees:
    print(emp.value)
    print(emp.is_leaf())


# In[15]:


cto = company.branches[0]
cto.value


# In[17]:


len(company.branches)


#  # Modifying Our Trees
# 

# In[18]:


company


# In[19]:


cto


# In[20]:


cto.add_branch('Engineer')


# In[21]:


cto.add_branch(Tree('Engineer'))
cto.add_branch(Tree('Engineer'))
cto.add_branch(Tree('Engineer'))


# In[22]:


cto


# In[23]:


print(len(cto.branches))


# In[24]:


cto.is_leaf()


# In[25]:


company


# In[26]:


cto.add_branch(Tree('Product Manager'))


# In[28]:


employees # ceo.branches


# In[29]:


for emp in employees: # employees of the CEO
    print(emp.value, ':')
    print(emp.branches)
    print(emp.is_leaf())


# In[ ]:





# In[ ]:





# In[30]:


for emp in employees: # employees of the CEO
    print(emp.value, ':')
    for child in emp.branches:
        print(child.value)


# In[31]:


pm = company.branches[0].branches[3]
pm.value


# In[ ]:





# In[ ]:





# # Recursion and Iteration Through Trees

# In[44]:


big_tree = Tree(
    '1A', [
    Tree('2A', [
        Tree('3A', [
            Tree('4A', [
                Tree('5A')
            ])]),
        Tree('3B', [
            Tree('4B'), 
            Tree('4C', [
                Tree('5B', [
                    Tree('6A')
                ])
            ]),
            Tree('4D'),
            Tree('4E')
        ])
    ]),
    Tree('2B',[
        Tree('3C', [
            Tree('4F')
        ])
    ])
])


# In[45]:


big_tree


# In[46]:


def traverse(tree):
    print("Saw: " + tree.value)
    for branch in tree.branches:
        print("Saw: " + branch.value)


# In[47]:


traverse(big_tree)


# In[ ]:





# In[ ]:





# In[ ]:





# In[50]:


def traverse_recursive(tree):
    print('Saw: ' + tree.value)
    for b in tree.branches:
#         print('Processing Branch:')
        traverse_recursive(b)


# In[51]:


traverse_recursive(big_tree)


# In[ ]:





# In[ ]:





# In[53]:


def print_tree(t, indent=0):
    """Print a representation of this tree in which each label is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> company = Tree('CEO', [Tree('CTO', [Tree('Engineer'), Tree('Product Manager')]), Tree('COO')])
    >>> print_tree(company)
     CEO
     |- CTO
     | |-- Engineer
     | |-- Engineer
     | |-- Product Manager
     |- COO
    """
    print((' |' * indent)  + ('-' * indent) + ' ' + str(t.value))
    for b in t.branches:
        print_tree(b, indent + 1)


# In[54]:


print_tree(company)


# In[55]:


print_tree(big_tree)


# In[ ]:





# In[ ]:





# In[56]:


def count_nodes(t):
    """The number of leaves in tree.

    >>> count_nodes(Tree(5))
    1
    """
    if t.is_leaf():
        return 1
    else:
        return 1 + sum([count_nodes(b) for b in t.branches])


# In[57]:


print_tree(company)


# In[58]:


count_nodes(company)


# In[ ]:





# In[59]:


def leaves(tree):
    """Return a list containing the leaf labels of tree.

    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    """
    if tree.is_leaf():
        return [ tree.value ]
    else:
        # Sum with a "start=[]"
        # [1] + [2] + [3]...
        return sum([leaves(b) for b in tree.branches], [])


# In[60]:


leaves(company)


# In[61]:


leaves(big_tree)


# # Extra Ideas for things we can do with trees:

# In[ ]:


def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        fib_n = left.value + right.value
        return Tree(fib_n, [left, right])


# In[ ]:


count_nodes(fib_tree(5))


# In[ ]:


fib_tree(5)


# ### Examples of `sum` with lists...
# 
# It's a bit of a weird edge case. You don't need to know this!

# In[ ]:


sum([1,2,3], 4) # the second argument is the starting value of sum


# In[ ]:


sum([[1],[2],[3]], [4])


# In[ ]:





# In[ ]:


[1] + [2] #what happens when we sum regular lists.


# In[ ]:


leaves(company)


# In[ ]:


leaves(fib_tree(5))


# In[ ]:


fib_tree(5)


# In[ ]:





# In[ ]:


def count_leaves(t):
    """The number of leaves in tree.

    >>> count_leaves(fib_tree(5))
    8
    """
    if t.is_leaf():
        return 1
    else:
        return sum([count_leaves(b) for b in t.branches])


# In[ ]:


count_leaves(company)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


# In[ ]:


fib(4)


# In[ ]:


fib(5)


# In[ ]:


def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        fib_n = left.value + right.value
        return Tree(fib_n, [left, right])


# In[ ]:


fib_tree(4)


# In[ ]:




