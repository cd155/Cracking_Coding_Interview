{-
    How would you design a stack which, in addition to push and pop, 
    has a function min which returns the minimum element? 
    Push, pop and min should all operate in 0(1) time.
-}
module StacksAndQueues.StackMin where

import StacksAndQueues.Structure.Stack(Stack (StackD))
import Data.Maybe (fromJust)

-- Pop: remove the top element on the stack
-- Test: pop (push "hi" (push "world" (push "!" newStack)))
popMin :: (Ord a) => (Stack a, Maybe a, Maybe a) -> Maybe (Stack a, Maybe a, Maybe a)
popMin (StackD _, Nothing, Nothing)    = Nothing
popMin (StackD (x : y), a, Nothing)     = Just (StackD y, Nothing, Nothing)
popMin (StackD (x : y), a, b)
    | x <= fromJust a                   = Just (StackD y, Just x , a)
    | x > fromJust a && x <= fromJust b = Just (StackD y, a , Just x)
    | otherwise                         = Just (StackD y, a, b)
-- popMin (_, _, _)                     = Nothing

-- Push: insert an element at the beginning of the stack
-- Test: push "hi" (push "world" (push "!" newStack))
pushMin :: (Ord a) => a -> (Stack a, Maybe a, Maybe a) -> Maybe (Stack a, a, Maybe a)
pushMin a (StackD x, Nothing, Nothing) = Just (StackD (a : x), a, Nothing)
pushMin a (StackD x, b, Nothing)       = Just (StackD (a : x), min a (fromJust b), Just (max a (fromJust b)))
pushMin a (StackD x, b, c)             
    | a <= fromJust b                  = Just (StackD (a : x), a, b)
    | a > fromJust b && a <= fromJust c = Just (StackD (a : x), fromJust b, Just a)
    | otherwise                        = Just (StackD (a : x), fromJust b, c)
