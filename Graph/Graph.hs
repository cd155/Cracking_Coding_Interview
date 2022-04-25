module Graph.Graph where

import Data.Set (Set, member)

newtype Graph = G (Set Vertex, Set Edge)

newtype WGraph = WG (Set Vertex,  Set WEdge)

-- Declaration: WGraphT : set ❰ set t , ❰ t, t ❱ ↔ ℝ ❱It s
newtype WGraphSet = WGS (Set (Set Vertex, Set WEdge))

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

newtype WEdge = WE ((Vertex, Vertex), Int) deriving (Eq, Ord)

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
weightOfE :: WEdge -> Int
weightOfE (WE ((_, _), x)) = x

-- | weight function for WEdge
weightOfSeqE :: [WEdge] -> Int
weightOfSeqE es = sum $ map weightOfE es

-- Declaration: isPathValid : ❰ set t, set ❰ t, t ❱ ❱ → Seq ❰ t, t ❱ → 𝔹
-- isPathValid G 𝜖
-- isPathValid ⟨V, E⟩ (e ◃ 𝜖) ≡ e ∈ E
-- isPathValid ⟨V, E⟩ (x ◃ xs) ≡ x ∈ E ∧ isPath ⟨V, E⟩ ( x ◃ xs)
isPathValid :: Graph -> [Edge] -> Bool
isPathValid _ []                 = True
isPathValid (G (_, e)) [x]    = x `member` e
isPathValid (G (v, e)) (x:xs) = x `member` e && isPath (G (v, e)) (x:xs)

isWPathValid :: WGraph -> [WEdge] -> Bool
isWPathValid _ []                 = True
isWPathValid (WG (_, e)) [x]    = x `member` e
isWPathValid (WG (v, e)) (x:xs) = x `member` e && isWPath (WG (v, e)) (x:xs)

-- findShortestPath :: WGraph -> Int
-- findShortestPath (Simple2 v e) = powerSet([])

-- Declaration: Paths : ❰ set t, set ❰ t, ℝ, t ❱ ❱ → set (Seq ❰ t, ℝ, t ❱)
-- allPaths :: WGraph -> Set [Edge]
-- allPaths (WG (v, e)) =  (WG(v, e)) `member` WGraphSet -- stop here.
