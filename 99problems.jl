N = parse(Int32, readline())

a = N ÷ 100 * 100 - 1
b = a + 100

if N - a < b - N && a > 98
  println(a)
else
  println(b)
end