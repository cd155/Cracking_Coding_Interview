{-  Question:
    How would you design a stack which, in addition to push and pop, 
    has a function min which returns the minimum element? 
    Push, pop and min should all operate in 0(1) time.

    Pre-load: 
    1   cd Cracking_Coding_Interview
    2   :l StackAndQueue/StackMin.hs
    3   :m StackAndQueue.Structure.Stack StackAndQueue.StackMin
-}
module StackAndQueue.StackMin where

import StackAndQueue.Structure.Stack(Stack (StackD))
import Data.Maybe (fromJust)

-- Initialize: create a new Stack
newStackMin :: (Stack a, Maybe a)
newStackMin = (StackD [], Nothing)

-- Pop: remove the top element, return stack, first and second Min
-- 2*fromJust a - x = 2*fromJust a - (2*a - fromJust b) = b
{-
    Original Stack [10,1,5]
    a = pushMin 10 (pushMin 1 (pushMin 5 (newStackMin)))
        ## (StackD [10,-3,5],    Just 1)
    b = popMin a
        ## ((StackD [-3,5],      Just 1),  Just 10)
    c = popMin (fst b)
        ## ((StackD [5],         Just 5),  Just 1)
    d = popMin (fst c)
        ## ((StackD [],          Nothing), Just 5)
    e = popMin (fst d)
        ## ((StackD [],          Nothing), Nothing)
-}

popMin :: (Num a, Ord a) => (Stack a, Maybe a) -> ((Stack a, Maybe a), Maybe a)
popMin (StackD [], _)          = ((StackD [], Nothing), Nothing)
popMin (StackD (x : y), a)
    | null y                   = ((StackD y, Nothing), Just x)
    | x < fromJust a           = ((StackD y, Just (2*fromJust a - x)), a)
    | otherwise                = ((StackD y, a), Just x)

-- Push: insert an element, return the stack, first and second Min
{-  
    Original Stack [10,1,5]
    a = pushMin 10 (pushMin 1 (pushMin 5 (newStackMin)))
        ## (StackD [10,-3,5],    Just 1)
    pushMin (-1) a
        ## (StackD [-3,10,-3,5], Just (-1))
    pushMin 10 a
        ## (StackD [10,10,-3,5], Just 1)
-}

pushMin :: (Num a, Ord a) => a -> (Stack a, Maybe a) -> (Stack a, Maybe a)
pushMin a (StackD [], _)  = (StackD [a], Just a)
pushMin a (StackD x, b)
    | a < fromJust b      = (StackD ((2*a - fromJust b) : x), Just a)
    | otherwise           = (StackD (a : x), b)
