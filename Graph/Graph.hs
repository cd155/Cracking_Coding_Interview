module Graph.Graph where

import Data.Set (Set, member)

data Graph = Simple1{
    vertices1 :: Set Vertex,
    edges1 :: Set Edge
}

data WGraph = Simple2{
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
            deriving (Eq, Ord)

-- Declaration: WGraphT : set ❰ set t , ❰ t, t ❱ ↔ ℝ ❱
newtype Edge = E (Vertex, Vertex) deriving (Eq, Ord)

-- Declaration: WGraphT : set ❰ set t , ❰ t, t ❱ ↔ ℝ ❱
newtype WEdge = WE ((Vertex, Vertex), Float) deriving (Eq, Ord)

-- Declaration: isPath : ❰ set t, set ❰ t, t ❱ ❱ → Seq ❰ t, t ❱ → 𝔹
-- isPath G 𝜖
-- isPath G (e ◃ 𝜖)
-- (isPath G (⟨a, b⟩ ◃ ⟨c, d⟩ ◃ p)) ≡ b = c ∧ isPath G (⟨c, d⟩ ◃ p)
isPath :: Graph -> [Edge] -> Bool
isPath _ []                   = True
isPath _ [x]                  = True
isPath g (E(_, b):E(c, d):xs) = b == c && isPath g (E(c, d):xs)

-- Declaration: isPath : ❰ set t, set ❰ t, ℝ, t ❱ ❱ → Seq ❰ t, ℝ, t ❱ → 𝔹
-- isPath G 𝜖
-- isPath G (e ◃ 𝜖)
-- (isPath G (⟨a, w₁, b⟩ ◃ ⟨c, w₂, d⟩ ◃ p)) ≡ b = c ∧ isPath G (⟨c, w₂, d⟩ ◃ p))
isWPath :: WGraph -> [WEdge] -> Bool
isWPath _ []                                 = True
isWPath _ [x]                                = True
isWPath g (WE((_, b), w1):WE((c, d), w2):xs) = b == c && isWPath g (WE((c, d), w2):xs)

-- | weight function for WEdge
weight :: WEdge -> Float
weight (WE ((_, _), x)) = x

isPathValid :: Graph -> [Edge] -> Bool
isPathValid _ []                 = True
isPathValid (Simple1 _ e) [x]    = x `member` e
isPathValid (Simple1 v e) (x:xs) = isPath (Simple1 v e) (x:xs) && x `member` e

isWPathValid :: WGraph -> [WEdge] -> Bool
isWPathValid _ []                 = True
isWPathValid (Simple2 _ e) [x]    = x `member` e
isWPathValid (Simple2 v e) (x:xs) = isWPath (Simple2 v e) (x:xs) && x `member` e
