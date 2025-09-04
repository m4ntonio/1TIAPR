let numeroUm = 1
let stringUm = '1'
let numeroTrinta = 30
let stringTrinta = '30'
let numeroDez = 10
let stringDez = '10'

if (numeroUm == stringUm) {
  console.log('As variáveis numeroUm e stringUm tem o mesmo valor, mas tipos diferentes')
} else {
  console.log('As variáveis numeroUm e stringUm não tem o mesmo valor')
}

if (numeroTrinta === stringTrinta) {
  console.log('As variáveis numeroTrinta e stringTrinta tem o mesmo valor e mesmo tipo')
} else {
  console.log('As variáveis numeroTrinta e stringTrinta não tem o mesmo tipo')
}

if (numeroDez == stringDez) {
  console.log('As variáveis numeroDez e stringDez tem o mesmo valor, mas tipos diferentes')
} else {
  console.log('As variáveis numeroDez e stringDez não tem o mesmo valor')
}

////////////////

console.log(30 == '30')   // true   -> Faz coerção: string '30' vira número 30
console.log(30 === '30')  // false  -> Tipos diferentes (number vs string)

console.log(0 == false)   // true   -> Faz coerção: false vira 0
console.log(0 === false)  // false  -> Tipos diferentes (number vs boolean)

console.log(null == undefined)  // true   -> Regra especial da linguagem
console.log(null === undefined) // false  -> Tipos diferentes

console.log('' == 0)      // true   -> String vazia vira 0
console.log('' === 0)     // false  -> Tipos diferentes

console.log(true == 1)    // true   -> true vira 1
console.log(true === 1)   // false  -> Tipos diferentes
