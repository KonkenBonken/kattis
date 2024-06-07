for caseNum in 1:parse(UInt8, readline())
  ali, src, trg = split(readline())

  num = 0

  for (i, c) in enumerate(ali[end:-1:1])
    num += (findfirst(c, src) - 1) * length(src)^(i - 1)
  end

  reslen = 0

  for i in 0:10^10
    if num < length(trg)^i
      reslen = i
      break
    end
  end

  res = ""

  for i in reslen-1:-1:0
    div = num ÷ length(trg)^i + 1
    num %= length(trg)^i
    res *= trg[div]
  end

  println("Case #", caseNum, ": ", res)
end