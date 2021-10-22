module Structure.Stack where

newtype Stack a = StackD [a] deriving (Show)  

-- Initialize: create a new Stack
-- Test: a = new
new :: Stack a
new = StackD []

-- Pop: remove the top element on the stack
-- Test: pop (push ("hi") (push ("world") (push ("!") new)))
pop :: Stack a -> Maybe (Stack a)
pop (StackD []) = Nothing 
pop (StackD (_ : y)) = Just (StackD y)

-- Push: insert an element at the beginning of the stack
-- Test: push ("hi") (push ("world") (push ("!") new))
push :: a -> Stack a -> Stack a
push a (StackD x) = StackD (a : x) 

-- Peek: look up the first element of the stack
-- Test: peek (push ("world") (push ("!") new))
peek :: Stack a -> Maybe a
peek (StackD []) = Nothing
peek (StackD (x : y)) = Just x

-- Is Empty: check whether the stack is empty
isEmpty :: Stack a -> Bool
isEmpty (StackD []) = True 
isEmpty _ = False 
