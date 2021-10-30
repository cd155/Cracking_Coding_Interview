module StackAndQueue.Structure.Queue where

newtype Queue a = QueueD [a] deriving (Show)  

-- Initialize: create a new Queue
newQueue :: Queue a
newQueue = QueueD []

-- Add: add an element at the end of the queue
-- Test: add "!" (add "world" (add "hi" newQueue))
add :: a -> Queue a -> Queue a
add a (QueueD x) = QueueD (x ++ [a])

-- Remove: remove an element at the top of the queue
-- Test: remove (add "!" (add "world" (add "hi" newQueue)))
remove :: Queue a -> (Queue a, Maybe a)
remove (QueueD []) = (QueueD [], Nothing)
remove (QueueD (x : y)) = (QueueD y, Just x)

-- Peek: check the first of element in the queue
-- Test: peekQueue (add "!" (add "world" newQueue))
peekQueue :: Queue a -> Maybe a
peekQueue (QueueD []) = Nothing
peekQueue (QueueD (x : _)) = Just x

-- Is Empty: check the queue whether it is empty
isQueueEmpty :: Queue a -> Bool
isQueueEmpty (QueueD []) = True 
isQueueEmpty _ = False
