
console.log("=== PEGADINHAS DO '==' NO JAVASCRIPT (com explicação) ===\n")

let casos2 = [
  ["0", false],
  ["1", true],
  ["0", ""],
  ["0", "0"],
  ["''", false],
  ["null", undefined],
  ["[]", false],
  ["[]", "![]"],
  ["[]", "''"],
  ["[]", 0],
  ["[1]", "'1'"],
  ["['']", "''"],
  ["['1']", 1],
  ["['1']", true],
  ["['0']", false],
  ["{}", "'[object Object]'"]
]

for (let [a, b] of casos2) {
  let valA = eval(a)
  let valB = eval(b)
  let resSolta = valA == valB
  let resEstrita = valA === valB

  let coer = ''
  if (resSolta && typeof valA !== typeof valB) coer = `(coerção: ${typeof valB} → ${typeof valA})`
  if (!resSolta && typeof valA !== typeof valB) coer = `(tipos diferentes)`

  console.log(`${a} == ${b}  → == ${resSolta} ${coer} | === ${resEstrita}`)
}

