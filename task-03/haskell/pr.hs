
prime::Int->Bool
prime n
  |n<=1=False
  |otherwise=not $ any (\x->n `mod` x==0)[2..(n-1)]

printp::Int->IO()
printp n=do
  mapM_ (\x->putStrLn(show x))[x|x<-[2..n], prime x]

main::IO()
main=do
  putStrLn "Enter n: "
  input<-getLine
  let n=read input::Int
  printp n
