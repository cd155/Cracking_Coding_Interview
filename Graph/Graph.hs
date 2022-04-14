module Graph.Graph where

import Data.Set (Set)

data Graph1 = Simple1{
    vertices1 :: Set Vertex,
    edges1 :: Set Edge
} 

data Graph2 = Simple2{
    vertices2 :: Set Vertex,
    edges2 :: Set WEdge
} 

data Vertex = One 
            | Two 
            | Three 
            | Four 
            | Five
            | Six
            | Seven
            | Eight

newtype Edge = E (Vertex, Vertex) -- Declaration: WGraphT : set ❰ set t , ❰ t, t ❱ ↔ ℝ ❱
newtype WEdge = WE ((Vertex, Vertex), Float) -- Declaration: WGraphT : set ❰ set t , ❰ t, t ❱ ↔ ℝ ❱

isPathReachable :: Graph1 -> Vertex -> Vertex -> Bool
isPathReachable g v w = False

-- | weight database for Edge
weight :: Edge -> Maybe Float
weight (E (One, Two) ) = Just 1.0
weight _ = Nothing

-- | weight function for WEdge
weight2 :: WEdge -> Maybe Float
weight2 (WE ((_, _), x) ) = Just x
