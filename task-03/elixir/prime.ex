defmodule Prime do
  def prime(1), do: false
  def prime(2), do: true
  def prime(n) when n > 2, do: prime(n, 2)

  defp prime(n, i) when i*i>n, do: true
  defp prime(n, i) when rem(n, i) == 0, do: false
  defp prime(n, i) do
    prime(n, i+1)
  end

  def print_primes(n) when n >= 2 do
    for j<- 2..n, prime(j) do
      IO.puts(j)
    end
  end
end

IO.puts("Enter n:")
input = IO.gets("")
n = String.trim(input) |> String.to_integer()

if n >= 2 do
  Prime.print_primes(n)
end
