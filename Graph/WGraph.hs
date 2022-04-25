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

type Path v = [v]
type Weight = Int

isPath :: WGraph -> Path Vertex -> Bool
isPath g [] = False
isPath g p = all (isEdge g) (pairs p)

pairs :: [a] -> [(a, a)]
pairs [] = []
pairs [x] = []
pairs (x1:x2:xs) = (x1, x2): pairs (x2:xs)

isEdge :: WGraph -> (Vertex,Vertex) -> Bool
isEdge g e = e `Map.member` wEdges g

-- totalWeight :: WGraph -> Path Vertex -> Weight
-- totalWeight g p = Map.foldrWithKey f 0 (wEdges g)
--   where f (x, y) w ks = 0 + k:ks
--         path = pairs p
