sumDigits :: Int -> Int
sumDigits number 
    | (number) < 10 = number
    | otherwise = (number `mod` 10) + sumDigits(number `div` 10)

lessThanTen :: Int -> Int
lessThanTen number
    | number < 10 = number
    | otherwise = lessThanTen(sumDigits(number))

higherSum :: Int -> Int -> Int
higherSum x y
    | lessThanTen(x) > lessThanTen(y) = 1
    | lessThanTen(y) > lessThanTen(x) = 2
    | otherwise = 0

main :: IO()
main = do
    x <- getLine
    y <- getLine
    putStrLn(show (higherSum (read x) (read y)))
    
