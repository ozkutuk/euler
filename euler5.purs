module Main where

import Prelude
import Data.Foldable (fold, foldl, product)
import Data.Function (on)
import Data.HashMap (HashMap, empty, insertWith, toArrayBy, unionWith)
import Data.List (fromFoldable, List(..), (:))
import Data.NonEmpty (NonEmpty, foldl1)
import Data.Unfoldable (replicate)
import Data.Unfoldable1 (range)
import Effect (Effect)
import Effect.Console (logShow)

factorize :: Int -> List Int
factorize 1 = Nil

factorize n = go n 2
  where
  go n x = case n `mod` x of
    0 -> x : factorize (n / x)
    _ -> go n (x + 1)

countFactors :: List Int -> HashMap Int Int
countFactors = foldl increment empty

increment :: HashMap Int Int -> Int -> HashMap Int Int
increment m x = insertWith (\v _ -> v + 1) x 1 m

nLcm :: NonEmpty List (List Int) -> List Int
nLcm xs = foldl1 twoLcm xs

twoLcm :: List Int -> List Int -> List Int
twoLcm x y = fold <<< fromFoldable <<< toArrayBy (flip replicate) $ commonFactors x y

commonFactors :: List Int -> List Int -> HashMap Int Int
commonFactors = unionWith max `on` countFactors

firstEvenlyDivisible :: Int -> Int
firstEvenlyDivisible = product <<< nLcm <<< map factorize <<< range 2

main :: Effect Unit
main = do
  logShow $ firstEvenlyDivisible 20
