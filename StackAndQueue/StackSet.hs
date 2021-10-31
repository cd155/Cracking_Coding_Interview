{-
    Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
    Therefore, in real life, we would likely start a new stack when the previous stack 
    exceeds some threshold. 
    
    Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
    composed of several stacks and should create a new stack once the previous one 
    exceeds capacity.
    
    SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
    
    (pop () should return the same values as it would if there were just a single stack).
    
    Bonus: 
    Implement a function popAt ( int index) which performs a pop operation on 
    a specific sub-stack.

    Pre-load: 
    1   cd Cracking_Coding_Interview
    2   :l StackAndQueue/StackSet.hs
    3   :m StackAndQueue.Structure.Stack StackAndQueue.StackSet
-}

module StackAndQueue.StackSet where

import StackAndQueue.Structure.Stack

data StackSet a = Plates{
                            _stackLists :: [Stack a],
                            _threshold :: Int,
                            _counter :: Int
                        } deriving (Show)

-- Initialize: create a new Stack
makeSet :: Int -> StackSet a
makeSet t = Plates [] t 0

-- Pop: remove the top element on the stack
{-  Test:
    a = pushSet 3 (pushSet 2 (pushSet 1 (makeSet 2)))
        ##  Plates {_stackLists = [StackD [3],StackD [2,1]], 
                    _threshold = 2, _counter = 1}
    b = popSet a
        ## (Plates {_stackLists = [StackD [2,1]], 
                    _threshold = 2, _counter = 2},      Just 3)
    c = pushSet 3 (fst b)
        ##  Plates {_stackLists = [StackD [3],StackD [2,1]], 
                    _threshold = 2, _counter = 1}
    d = popSet (fst (popSet c))
        ## (Plates {_stackLists = [StackD [1]], _threshold = 2, 
                    _counter = 1},                      Just 2)
    e = popSet (fst d)
        ## (Plates {_stackLists = [], 
                    _threshold = 2, _counter = 2},      Just 1)
    f = popSet (fst e)
        ## (Plates {_stackLists = [], 
                    _threshold = 2, _counter = 0},      Nothing)
    g = pushSet 1 (fst e)
        ##  Plates {_stackLists = [StackD [1]], 
                    _threshold = 2, _counter = 1}
-}
popSet :: StackSet a -> (StackSet a, Maybe a)
popSet (Plates [] t _) = (Plates [] t 0, Nothing)
popSet (Plates xs t c)= (makeNewPlt (Plates xs t c), snd (pop topStack))
        where topStack = head xs

-- Helper function: remove empty stack from stackLists after pop
makeNewPlt :: StackSet a -> StackSet a
makeNewPlt (Plates [] t c)       = Plates [] t c
makeNewPlt (Plates (x : xs) t c)
    | isStackEmpty poppedStack     = Plates xs t t
    | otherwise                  = Plates (poppedStack : xs) t (c-1)
        where poppedStack = fst (pop x)

-- Push: insert an element at the beginning of the stack
{-  Test:
    a = pushSet 3 (pushSet 2 (pushSet 1 (makeSet 2)))
        ## Plates {_stackLists = [StackD [3],StackD [2,1]], 
                   _threshold = 2, _counter = 1}
    b = pushSet 4 a
        ## Plates {_stackLists = [StackD [4,3],StackD [2,1]], 
                   _threshold = 2, _counter = 2}
    c = pushSet 5 b
        ## Plates {_stackLists = [StackD [5],StackD [4,3],StackD [2,1]], 
                   _threshold = 2, _counter = 1}
-} 
pushSet :: a -> StackSet a -> StackSet a
pushSet a (Plates [] t _) = Plates [push a newStack] t 1
pushSet a (Plates (x : xs) t c)
    | c <  t                      = Plates (push a x : xs) t (c+1)
    | c >= t                      = Plates (push a newStack : (x : xs)) t (t-1)
    | otherwise                   = Plates (x : xs) t c

-- Peek: look up the first element of the stack
peekSet :: StackSet a -> Maybe a
peekSet (Plates [] _ _) = Nothing
peekSet (Plates (x : _) _ _) = peekStack x

-- Is Empty: check whether the stack is empty
isSetEmpty :: StackSet a -> Bool
isSetEmpty (Plates [] _ _) = True
isSetEmpty (Plates (x : _) _ _) = isStackEmpty x
