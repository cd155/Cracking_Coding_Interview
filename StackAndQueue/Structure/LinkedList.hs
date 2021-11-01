{-# LANGUAGE TemplateHaskell #-}

module StackAndQueue.Structure.LinkedList where

import Control.Lens
import Data.Maybe

data LinkedList a = Node{
                            _value :: Maybe a,
                            _next :: Maybe (LinkedList a)
                        } deriving (Show)
makeLenses ''LinkedList

newList :: LinkedList a
newList = Node Nothing Nothing

prepend :: a -> LinkedList a -> LinkedList a
prepend x xs = Node (Just x) (Just xs)

append :: a -> LinkedList a -> LinkedList a
append x xs
    | isNothing (xs ^. next)    = Node (Just x) (Just xs)
    | otherwise                 = Node (xs ^. value) (Just restList)
        where restList = append x (fromJust(xs ^. next))

-- not test yet
delete :: Eq a => a -> LinkedList a -> LinkedList a
delete x xs
    | isNothing (xs ^. next)    = Node (Just x) (xs ^. next)
    | x == nextValue            = Node (Just x) (xs ^. next)
    | otherwise                 = Node (xs ^. value) (Just restList)
        where nextValue = fromJust (fromJust(xs ^. next) ^. value)
              restList = delete x (fromJust(xs ^. next))
