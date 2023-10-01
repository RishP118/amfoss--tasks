print "Enter n: "
n = gets.chomp.to_i

if n >= 2
  for s in 2..n
    prime = true
    for i in 2..(s - 1)
      if s % i == 0
        prime = false
        break
      end
    end
    puts s if prime
  end
end
