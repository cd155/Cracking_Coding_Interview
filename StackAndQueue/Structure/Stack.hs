module StackAndQueue.Structure.Stack where

newtype Stack a = StackD [a] deriving (Show)  

-- Initialize: create a new Stack
newStack :: Stack a
newStack = StackD []

-- Pop: remove the top element on the stack
-- Test: pop (push "hi" (push "world" (push "!" newStack)))
pop :: Stack a -> (Stack a, Maybe a)
pop (StackD []) = (StackD [], Nothing)
pop (StackD (x : y)) = (StackD y, Just x)

-- Push: insert an element at the beginning of the stack
-- Test: push "hi" (push "world" (push "!" newStack))
push :: a -> Stack a -> Stack a
push a (StackD x) = StackD (a : x) 

-- Peek: look up the first element of the stack
-- Test: peekStack (push "world" (push "!" newStack))
peekStack :: Stack a -> Maybe a
peekStack (StackD []) = Nothing
peekStack (StackD (x : y)) = Just x

-- Is Empty: check whether the stack is empty
isStackEmpty :: Stack a -> Bool
isStackEmpty (StackD []) = True 
isStackEmpty _ = False 
