for caseNum in 1:parse(UInt8, readline())
  ali, src, trg = split(readline())

  num = reduce((tot, (i, c)) -> tot + (findfirst(c, src) - 1) * length(src)^(i - 1), enumerate(ali[end:-1:1]); init=0)
  reslen = findfirst(i -> num < length(trg)^(i + 1), 0:94)

  function digit(i)
    div = num ÷ length(trg)^i + 1
    num %= length(trg)^i
    return trg[div]
  end

  res = reduce(*, map(digit, reslen-1:-1:0))

  println("Case #", caseNum, ": ", res)
end