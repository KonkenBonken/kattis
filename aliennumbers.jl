cases = readlines()[2:end]

for (caseNum, case) in enumerate(cases)
  ali, src, trg = split(case)

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

  res = string("")

  for i in reslen-1:-1:0
    div = num ÷ length(trg)^i + 1
    num %= length(trg)^i
    res *= string(trg[div])
  end

  println("Case #", caseNum, ": ", res)
end