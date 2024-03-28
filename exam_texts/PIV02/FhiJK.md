# [GROUP=0]

### [TASK=1]

##### [MAX_TASK_POINTS=1]

- 0.5 POINTS: Točna provjera tipova podataka
- 0.5 POINTS: Točno napisana selekcija

Napišite funkciju `sumTriple()` koja prima dva argumenta. Funkcija treba vratiti zbroj ta dva argumenta, ali ako su argumenti jednaki, onda treba vratiti trostruki zbroj. Funkcija mora provjeriti ako su proslijeđeni argumenti brojevi, ako nisu, treba vratiti `"Argumenti nisu brojevi"`.

```javascript
console.log(sumTriple(4, 5)); // 9
console.log(sumTriple(7, 7)); // 42
console.log(sumTriple(4, "5")); // Argumenti nisu brojevi
```

### [TASK=2]

##### [MAX_TASK_POINTS=2]

- 0.5 POINTS: Točna provjera tipova podataka
- 1 POINTS: Točno napisana selekcija (if-else ili switch-case)
- 0.5 POINTS: Točno napisana slučaj za dijeljenje i default slučaj

Napišite funkciju `simpleCalculator()` koja prima tri argumenta: `broj1`, `broj2` i `operacija`. Funkcija treba provjeriti jesu li prva dva argumenta brojevi, ako nisu, treba vratiti `"Prva dva argumenta nisu brojevi".` Argument `operacija` neka bude string koji može biti `"zbrajanje"`, `"oduzimanje"`, `"mnozenje"` ili `"dijeljenje"`.

- koristeći selekciju (`if-else` ili `switch`) provjerite koja je od 4 operacije u pitanju i izvršite odgovarajuću
- ako je u pitanju operacija dijeljenja, provjerite je li drugi argument različit od 0, ako nije, vratite `"Dijeljenje s 0 nije moguće"`
- ako je proslijeđena operacija nepoznata, vratite `"Nepoznata operacija"`

### [TASK=3]

##### [MAX_TASK_POINTS=3]

- 1 POINTS: Ispravna iteracija kroz string (for, while ili do-while petlja)
- 1 POINTS: Točno napisana selekcija (traženje znaka točke)
- 1 POINTS: Točno vraćanje ekstenzije datoteke i ispis poruke ako datoteka nema ekstenziju

Napišite funkciju `getFileExtension()` koja prima string koji predstavlja puni naziv datoteke, npr. `"index.html"`, `"style.css"`, `"script.js"` itd. Funkcija treba vratiti ekstenziju datoteke (npr. `"html"`, `"css"` ili `"js"`). Ako datoteka nema ekstenziju, funkcija treba vratiti `"Datoteka nema ekstenziju"`. Zadatak riješite iteriranjem kroz znakovni niz i odgovarajućom selekcijom. **Ne smijete koristiti gotove metode nad stringovima! Možete koristiti length svojstvo.**

```javascript
console.log(getFileExtension("index.html")); // html
console.log(getFileExtension("style.css")); // css
console.log(getFileExtension("archive.tar.gz")); // gz
console.log(getFileExtension("mojastranica")); // Datoteka nema ekstenziju
```

### [TASK=4]

##### [MAX_TASK_POINTS=2]

- 0.5 POINTS: Ispravna iteracija kroz string (for, while ili do-while petlja)
- 0.5 POINTS: Točna provjera za '@' znak
- 1 POINTS: Točna provjera za '.' znak nakon '@' znaka I ispravno vraćanje rezultata

Napišite funkciju `validirajEmail()` koja prima jedan argument: `email`. Funkcija treba provjeriti je li proslijeđeni argument validna email adresa te vratiti `true` ako je validna, inače treba vratiti `false`. Funkcija mora provjeriti sadrži li email znak `@` i je li **nakon** znaka `@` prisutan znak točka `.` Ne morate provjeravati sadrži li e-mail druge nedozvoljene znakove ili više znakova `@`. Povratna vrijednost funkcije mora biti u obliku `return atSymbolFound && dotFoundAfterAtSymbol;`. Zadatak riješite iteriranjem kroz znakovni niz i odgovarajućom selekcijom. **Ne smijete koristiti gotove metode nad stringovima! Možete koristiti length svojstvo.**

```javascript
console.log(validirajEmail("peroPeric@gmail.com")); // true
console.log(validirajEmail("peroPericgmail.com")); // false
console.log(validirajEmail("peroPeric@gmailcom")); // false
```

### [TASK=5]

##### [MAX_TASK_POINTS=2]

- 0.5 POINTS: Ispravan max algoritam
- 0.5 POINTS: Ispravan absolute algoritam
- 1 POINTS: Ispravan factorial algoritam

Nadopunite kôd kako bi 3 funkcijska izraza (`max`, `absolute`, `factorial`) radila ispravno.

```javascript
// [1]
const max = function (a, b) {
  // vaš kôd ovdje
};
console.log(max(10, 20)); // Output: 20

// [2]
const absolute = function (a) {
  // vaš kôd ovdje
};
console.log(absolute(-5)); // Output: 5

// [3]
// umnožak svih prirodnih brojeva manjih ili jednakih n
const factorial = function (n) {
  let result = 1;
  // vaš kôd ovdje
  return result;
};
console.log(factorial(5)); // Output: 120
```

### [TASK=6]

##### [MAX_TASK_POINTS=1]

MAX: 1 POINTS - samo za potpuno točno rješenje

**[BONUS]** Zadatak za dodatan POINTS.

- nadogradite funkciju `validirajEmail()` iz 4. zadatka tako da ćete u nju dodati podfunkciju `validateUsername(username)` koja će provjeravati sastoji li se prvi dio emaila (do znaka `@`) samo od malih slova `[a - z]` i brojeva `[0 - 9]`. Ako se sastoji, funkcija treba vratiti `true`, inače `false`. **Ne smijete koristiti gotove metode nad stringovima! Možete koristiti length svojstvo.**
- **Hint**: Leksikografska usporedba stringova

```javascript
console.log(validirajEmail("peroPeric@gmail.com")); // false
console.log(validirajEmail("pero123peric@gmail.com")); // true
console.log(validirajEmail("pero!!peric@gmail.com")); // false
```

# [GROUP=1]

### [TASK=1]

##### [MAX_TASK_POINTS=1]

- 0.5 POINTS: Točna provjera tipova podataka
- 0.5 POINTS: Točno napisana selekcija/povratna vrijednost

Napišite funkciju `isDivisible` koja prima dva argumenta. Funkcija treba provjeriti je li prvi argument djeljiv s drugim argumentom. Funkcija treba vratiti `true` ako je prvi argument djeljiv s drugim, inače treba vratiti `false`. Funkcija mora provjeriti ako su proslijeđeni argumenti brojevi, ako nisu, treba vratiti `"Argumenti nisu brojevi"`.

```javascript
console.log(isDivisible(4, 2)); // true
console.log(isDivisible(9, 3)); // true
console.log(isDivisible(15, 4)); // false
```

### [TASK=2]

##### [MAX_TASK_POINTS=2]

- 0.5 POINTS: Točna provjera tipova podataka
- 1 POINTS: Točno napisana selekcija (if-else ili switch-case)
- 0.5 POINTS: Točno napisana slučaj za dijeljenje i default slučaj

Napišite funkciju `simpleCalculator()` koja prima tri argumenta: `broj1`, `broj2` i `operacija`. Funkcija treba provjeriti jesu li prva dva argumenta brojevi, ako nisu, treba vratiti `"Prva dva argumenta nisu brojevi".` Argument `operacija` neka bude string koji može biti `"zbrajanje"`, `"oduzimanje"`, `"mnozenje"` ili `"dijeljenje"`.

- koristeći selekciju (`if-else` ili `switch`) provjerite koja je od 4 operacije u pitanju i izvršite odgovarajuću operaciju
- ako je u pitanju operacija dijeljenja, provjerite je li drugi argument različit od 0, ako nije, vratite `"Dijeljenje s 0 nije moguće"`
- ako je proslijeđena operacija nepoznata, vratite `"Nepoznata operacija"`

### [TASK=3]

##### [MAX_TASK_POINTS=3]

- 1 POINTS: Ispravna iteracija kroz string (for, while ili do-while petlja)
- 0.5 POINTS: Točna provjera tipa podataka
- 1.5 POINTS: Točno napisana selekcija/uvjet za palindrom (if-else ili switch-case)

Napišite funkciju `isPalindrome()` koja prima jedan argument: `string`. Funkcija treba provjeriti je li proslijeđeni argument palindrom te vratiti `true` ako je palindrom, inače treba vratiti `false`. Palindrom je riječ koja se čita isto i s lijeva na desno i s desna na lijevo. Funkcija mora provjeriti ako je proslijeđeni argument string, ako nije, treba vratiti `"Argument nije string"`. Zadatak riješite iteriranjem kroz znakovni niz i odgovarajućom selekcijom. **Ne smijete koristiti gotove metode nad stringovima! Možete koristiti length svojstvo.**

```javascript
console.log(isPalindrome("anavolimilovana")); // true
console.log(isPalindrome("hello")); // false
console.log(isPalindrome("noon")); // true
console.log(isPalindrome(12321)); // Argument nije string
```

### [TASK=4]

##### [MAX_TASK_POINTS=2]

- 0.5 POINTS: Ispravna iteracija kroz string (for, while ili do-while petlja)
- 0.5 POINTS: Točna provjera tipa podataka
- 1 POINTS: Točna provjera za minimalno 6 znakova i minimalno jedan broj

Napišite funkciju `validirajLozinku()` koja prima jedan argument: `password`. Funkcija treba provjeriti je li proslijeđeni argument validna lozinka te vratiti `true` ako je validna, inače treba vratiti `false`. Funkcija mora provjeriti sadrži li lozinka minimalno `6 znakova` i sadrži li `barem 1 broj`. Povratna vrijednost funkcije mora biti u obliku `return minBrojZnakova && sadrziBroj;` Zadatak riješite iteriranjem kroz znakovni niz i odgovarajućom selekcijom. **Ne smijete koristiti gotove metode nad stringovima! Možete koristiti length svojstvo.**

```javascript
console.log(validirajLozinku("lozinka")); // false
console.log(validirajLozinku("lozinka123")); // true
console.log(validirajLozinku("loz12")); // false
```

### [TASK=5]

##### [MAX_TASK_POINTS=2]

- 0.5 POINTS: Ispravan min algoritam
- 0.5 POINTS: Ispravan pow algoritam
- 1 POINTS: Ispravan sumUpTo algoritam

Nadopunite kôd kako bi 3 funkcijska izraza (`min`, `pow`, `sumUpTo`) radila ispravno.

```javascript
// [1]
const min = function (a, b) {
  // vaš kôd ovdje
};
console.log(min(30, 15)); // Output: 15

// [2]
const pow = function (a, b) {
  // vaš kôd ovdje
};
console.log(pow(2, 3)); // Output: 8

// [3]
// zbroj prvih n prirodnih brojeva
const sumUpTo = function (n) {
  let sum = 0;
  // vaš kôd ovdje
  return sum;
};
console.log(sumUpTo(5)); // Output: 15
```

### [TASK=6]

##### [MAX_TASK_POINTS=1]

MAX: 1 POINTS - samo za potpuno točno rješenje

**[BONUS]** Zadatak za dodatan POINTS.

- nadogradite funkciju `validirajLozinku()` iz 4. zadatka tako da ćete u nju dodati podfunkciju `containsOnlyAlphanumeric(password)` koja će provjeravati sastoji li se lozinka samo od slova `[a - z : A - Z]` i brojeva `[0 - 9]`. Ako se sastoji, funkcija treba vratiti `true`, inače `false`. **Ne smijete koristiti gotove metode nad stringovima! Možete koristiti length svojstvo.**
- **Hint**: Leksikografska usporedba stringova

```javascript
console.log(validirajLozinku("lozinka123")); // true
console.log(validirajLozinku("lozink!!!")); // false
console.log(validirajLozinku("lozinkAAAA1AAAA")); // true
console.log(validirajLozinku("123456789$$$$$$$")); // false
```

# [GROUP=2]

### [TASK=1]

##### [MAX_TASK_POINTS=1]

- 0.5 POINTS: Točna provjera tipova podataka
- 0.5 POINTS: Točno napisana selekcija

Napišite funkciju `multiplyDouble()` koja prima dva argumenta. Funkcija treba vratiti umnožak ta dva argumenta, ali ako su argumenti jednaki, onda treba vratiti dvostruki umnožak. Funkcija mora provjeriti ako su proslijeđeni argumenti brojevi, ako nisu, treba vratiti `"Argumenti nisu brojevi"`.

```javascript
console.log(multiplyDouble(4, 5)); // 20
console.log(multiplyDouble(7, 7)); // 98
console.log(multiplyDouble(4, "5")); // Argumenti nisu brojevi
```

### [TASK=2]

##### [MAX_TASK_POINTS=2]

- 0.5 POINTS: Točna provjera tipova podataka
- 1 POINTS: Točno napisana selekcija (if-else ili switch-case)
- 0.5 POINTS: Točno napisan slučaj za Ružno vrijeme s visokom vlagom zraka.

Napišite funkciju `weatherForecast()` koja prima četiri argumenta: `temperatura`, `vlaga`, `oblacno`, `kisa`. Funkcija treba provjeriti jesu li argumenti `temperatura` i `vlaga` cjelobrojne vrijednosti; ako nisu, treba vratiti "Temperatura i vlaga moraju biti brojevi.". Za argumente `oblacno` i `kisa` postavite defaultne vrijednosti na `false`. Koristeći `if-else` ili `switch` selekciju, izradite kratku prognozu vremena na temelju sljedećih pravila:

- Ako je temperatura iznad 25 stupnjeva i nije oblačno, vratite string `"Vruće i sunčano vrijeme."`
- Ako je temperatura ispod 25 stupnjeva, oblačno je ali ne pada kiša, funkcija mora vratiti: `"Prohlano i oblačno vrijeme bez kiše."`
- Ako je temperatura između 15 i 25 stupnjeva, pada kiša i vlaga je preko 80%, funkcija treba vratiti: `"Ružno vrijeme s visokom vlagom zraka."`
- U svim ostalim slučajevima, funkcija treba vratiti: `"Vrijeme je promjenjivo."`

### [TASK=3]

##### [MAX_TASK_POINTS=3]

- 1 POINTS: Ispravna iteracija kroz string (for, while ili do-while petlja)
- 1 POINTS: Točno napisana selekcija (traženje znaka točke)
- 1 POINTS: Točno vraćanje ekstenzije datoteke i ispis poruke ako datoteka nema ekstenziju

Napišite funkciju `getFileExtension()` koja prima string koji predstavlja puni naziv datoteke, npr. `"index.html"`, `"style.css"`, `"script.js"` itd. Funkcija treba vratiti ekstenziju datoteke (npr. `"html"`, `"css"` ili `"js"`). Ako datoteka nema ekstenziju, funkcija treba vratiti `"Datoteka nema ekstenziju"`. Zadatak riješite iteriranjem kroz znakovni niz i odgovarajućom selekcijom. **Ne smijete koristiti gotove metode nad stringovima! Možete koristiti length svojstvo.**

```javascript
console.log(getFileExtension("index.html")); // html
console.log(getFileExtension("style.css")); // css
console.log(getFileExtension("archive.tar.gz")); // gz
console.log(getFileExtension("mojastranica")); // Datoteka nema ekstenziju
```

### [TASK=4]

##### [MAX_TASK_POINTS=2]

- 0.5 POINTS: Ispravna iteracija kroz string (for, while ili do-while petlja)
- 0.5 POINTS: Točna provjera za '@' znak
- 1 POINTS: Točna provjera za '.' znak nakon '@' znaka I ispravno vraćanje rezultata

Napišite funkciju `validirajEmail()` koja prima jedan argument: `email`. Funkcija treba provjeriti je li proslijeđeni argument validna email adresa te vratiti `true` ako je validna, inače treba vratiti `false`. Funkcija mora provjeriti sadrži li email znak `@` i je li **nakon** znaka `@` prisutan znak točka `.` Ne morate provjeravati sadrži li e-mail druge nedozvoljene znakove ili više znakova `@`. Povratna vrijednost funkcije mora biti u obliku `return atSymbolFound && dotFoundAfterAtSymbol;`. Zadatak riješite iteriranjem kroz znakovni niz i odgovarajućom selekcijom. **Ne smijete koristiti gotove metode nad stringovima! Možete koristiti length svojstvo.**

```javascript
console.log(validirajEmail("peroPeric@gmail.com")); // true
console.log(validirajEmail("peroPericgmail.com")); // false
console.log(validirajEmail("peroPeric@gmailcom")); // false
```

### [TASK=5]

##### [MAX_TASK_POINTS=2]

- 0.5 POINTS: Ispravan min algoritam
- 0.5 POINTS: Ispravan absolute algoritam
- 1 POINTS: Ispravan sumUpTo algoritam

Nadopunite kôd kako bi 3 funkcijska izraza (`min`, `absolute`, `sumUpTo`) radila ispravno.

```javascript
// [1]
const min = function (a, b) {
  // vaš kôd ovdje
};
console.log(min(10, 20)); // Output: 10

// [2]
const absolute = function (a) {
  // vaš kôd ovdje
};
console.log(absolute(-5)); // Output: 5

// [3]
// zbroj prvih n prirodnih brojeva
const sumUpTo = function (n) {
  let sum = 0;
  // vaš kôd ovdje
  return sum;
};
console.log(sumUpTo(5)); // Output: 15
```

### [TASK=6]

##### [MAX_TASK_POINTS=1]

MAX: 1 POINTS - samo za potpuno točno rješenje

**[BONUS]** Zadatak za dodatan POINTS.

- nadogradite funkciju `validirajEmail()` iz 4. zadatka tako da ćete u nju dodati podfunkciju `validateUsername(username)` koja će provjeravati sastoji li se prvi dio emaila (do znaka `@`) samo od malih slova `[a - z]` i brojeva `[0 - 9]`. Ako se sastoji, funkcija treba vratiti `true`, inače `false`. **Ne smijete koristiti gotove metode nad stringovima! Možete koristiti length svojstvo.**
- **Hint**: Leksikografska usporedba stringova

```javascript
console.log(validirajEmail("peroPeric@gmail.com")); // false
console.log(validirajEmail("pero123peric@gmail.com")); // true
console.log(validirajEmail("pero!!peric@gmail.com")); // false
```

# [GROUP=3]

### [TASK=1]

##### [MAX_TASK_POINTS=1]

- 0.5 POINTS: Točna provjera tipova podataka
- 0.5 POINTS: Točno napisana selekcija/povratna vrijednost

Napišite funkciju `isNotDivisible` koja prima dva argumenta. Funkcija treba provjeriti je li prvi argument djeljiv s drugim argumentom. Funkcija treba vratiti `false` ako je prvi argument djeljiv s drugim, inače treba vratiti `true`. Funkcija mora provjeriti ako su proslijeđeni argumenti brojevi, ako nisu, treba vratiti `"Argumenti nisu brojevi"`.

```javascript
console.log(isNotDivisible(4, 2)); // false
console.log(isNotDivisible(9, 3)); // false
console.log(isNotDivisible(15, 4)); // true
```

### [TASK=2]

##### [MAX_TASK_POINTS=2]

- 0.5 POINTS: Točna provjera tipova podataka
- 1 POINTS: Točno napisana selekcija (if-else ili switch-case)
- 0.5 POINTS: Točno napisan slučaj za Ružno vrijeme s visokom vlagom zraka.

Napišite funkciju `weatherForecast()` koja prima četiri argumenta: `temperatura`, `vlaga`, `oblacno`, `kisa`. Funkcija treba provjeriti jesu li argumenti `temperatura` i `vlaga` cjelobrojne vrijednosti; ako nisu, treba vratiti "Temperatura i vlaga moraju biti brojevi.". Za argumente `oblacno` i `kisa` postavite defaultne vrijednosti na `false`. Koristeći `if-else` ili `switch` selekciju, izradite kratku prognozu vremena na temelju sljedećih pravila:

- Ako je temperatura iznad 25 stupnjeva i nije oblačno, vratite string `"Vruće i sunčano vrijeme."`
- Ako je temperatura ispod 25 stupnjeva, oblačno je ali ne pada kiša, funkcija mora vratiti: `"Prohlano i oblačno vrijeme bez kiše."`
- Ako je temperatura između 15 i 25 stupnjeva, pada kiša i vlaga je preko 80%, funkcija treba vratiti: `"Ružno vrijeme s visokom vlagom zraka."`
- U svim ostalim slučajevima, funkcija treba vratiti: `"Vrijeme je promjenjivo."`

### [TASK=3]

##### [MAX_TASK_POINTS=3]

- 1 POINTS: Ispravna iteracija kroz string (for, while ili do-while petlja)
- 0.5 POINTS: Točna provjera tipa podataka
- 1.5 POINTS: Točno napisana selekcija/uvjet za palindrom (if-else ili switch-case)

Napišite funkciju `isPalindrome()` koja prima jedan argument: `string`. Funkcija treba provjeriti je li proslijeđeni argument palindrom te vratiti `true` ako je palindrom, inače treba vratiti `false`. Palindrom je riječ koja se čita isto i s lijeva na desno i s desna na lijevo. Funkcija mora provjeriti ako je proslijeđeni argument string, ako nije, treba vratiti `"Argument nije string"`. Zadatak riješite iteriranjem kroz znakovni niz i odgovarajućom selekcijom. **Ne smijete koristiti gotove metode nad stringovima! Možete koristiti length svojstvo.**

```javascript
console.log(isPalindrome("anavolimilovana")); // true
console.log(isPalindrome("hello")); // false
console.log(isPalindrome("noon")); // true
console.log(isPalindrome(12321)); // Argument nije string
```

### [TASK=4]

##### [MAX_TASK_POINTS=2]

- 0.5 POINTS: Ispravna iteracija kroz string (for, while ili do-while petlja)
- 0.5 POINTS: Točna provjera tipa podataka
- 1 POINTS: Točna provjera za minimalno 6 znakova i minimalno jedan broj

Napišite funkciju `validirajLozinku()` koja prima jedan argument: `password`. Funkcija treba provjeriti je li proslijeđeni argument validna lozinka te vratiti `true` ako je validna, inače treba vratiti `false`. Funkcija mora provjeriti sadrži li lozinka minimalno `6 znakova` i sadrži li `barem 1 broj`. Povratna vrijednost funkcije mora biti u obliku `return minBrojZnakova && sadrziBroj;` Zadatak riješite iteriranjem kroz znakovni niz i odgovarajućom selekcijom. **Ne smijete koristiti gotove metode nad stringovima! Možete koristiti length svojstvo.**

```javascript
console.log(validirajLozinku("lozinka")); // false
console.log(validirajLozinku("lozinka123")); // true
console.log(validirajLozinku("loz12")); // false
```

### [TASK=5]

##### [MAX_TASK_POINTS=2]

- 0.5 POINTS: Ispravan max algoritam
- 0.5 POINTS: Ispravan pow algoritam
- 1 POINTS: Ispravan factorial algoritam

Nadopunite kôd kako bi 3 funkcijska izraza (`max`, `pow`, `factorial`) radila ispravno.

```javascript
// [1]
const max = function (a, b) {
  // vaš kôd ovdje
};
console.log(max(10, 20)); // Output: 20

// [2]
const pow = function (a, b) {
  // vaš kôd ovdje
};
console.log(pow(2, 3)); // Output: 8

// [3]
// umnožak svih prirodnih brojeva manjih ili jednakih n
const factorial = function (n) {
  let result = 1;
  // vaš kôd ovdje
  return result;
};
console.log(factorial(5)); // Output: 120
```

### [TASK=6]

##### [MAX_TASK_POINTS=1]

MAX: 1 POINTS - samo za potpuno točno rješenje

**[BONUS]** Zadatak za dodatan POINTS.

- nadogradite funkciju `validirajLozinku()` iz 4. zadatka tako da ćete u nju dodati podfunkciju `containsOnlyAlphanumeric(password)` koja će provjeravati sastoji li se lozinka samo od slova `[a - z : A - Z]` i brojeva `[0 - 9]`. Ako se sastoji, funkcija treba vratiti `true`, inače `false`. **Ne smijete koristiti gotove metode nad stringovima! Možete koristiti length svojstvo.**
- **Hint**: Leksikografska usporedba stringova

```javascript
console.log(validirajLozinku("lozinka123")); // true
console.log(validirajLozinku("lozink!!!")); // false
console.log(validirajLozinku("lozinkAAAA1AAAA")); // true
console.log(validirajLozinku("123456789$$$$$$$")); // false
```
