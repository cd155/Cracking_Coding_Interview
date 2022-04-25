module Graph.WGraph where

import Data.Set (Set, member)
import Data.Map (Map)
import qualified Data.Map as Map

data WGraph = WGraph{
    wVertices :: Set Vertex,
    wEdges :: Map (Vertex, Vertex) Weight
}

isWGraph :: WGraph -> Bool
isWGraph g = Map.foldrWithKey f True (wEdges g)
  where f (x, y) w acc = x `member` wVertices g && y `member` wVertices g

data Vertex = One
            | Two
            | Three
            | Four
            | Five
            | Six
            | Seven
            | Eight
            deriving (Eq, Ord)

type Path v = [(v, v)]
type Weight = Int

isPath :: WGraph -> Path Vertex -> Bool
isPath g p = all (isEdge g) (pairs p) 

-- how to deal with a broken path? 
-- broken path valid path at first couple seq, but not all seq
pairs :: Path Vertex -> Path Vertex
pairs [] = []
pairs [x] = [x]
pairs ((x1, y1): (x2, y2):xs) = 
  if y1 == x2 
    then 
    (x1, y1): pairs((x2, y2):xs) 
    else []

-- pairs :: [a] -> [(a, a)]
-- pairs _ =  

isEdge :: WGraph -> (Vertex,Vertex) -> Bool
isEdge g e = e `Map.member` wEdges g
