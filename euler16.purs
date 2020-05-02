module Main where

import Prelude
import Data.BigInt (BigInt)
import Data.BigInt as BI
import Data.Char.Unicode (digitToInt)
import Data.Foldable (sum)
import Data.Function (on)
import Data.Maybe (Maybe, maybe)
import Data.String.CodeUnits (toCharArray)
import Data.Traversable (traverse)
import Effect (Effect)
import Effect.Console (logShow)

powerDigitSum :: Int -> Int -> Int
powerDigitSum m n = sumDigits $ pow m n
  where
  sumDigits :: BigInt -> Int
  sumDigits = maybe 0 sum <<< stringToInts <<< BI.toString

  stringToInts :: String -> Maybe (Array Int)
  stringToInts = traverse digitToInt <<< toCharArray

  pow :: Int -> Int -> BigInt
  pow = BI.pow `on` BI.fromInt

main :: Effect Unit
main = do
  logShow $ powerDigitSum 2 1000
