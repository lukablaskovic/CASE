# Exam Tasks

Tasks are as follows:

**1.** Deklarirajte tri konstante i jednu promjenjivu varijablu. Konstante neka budu vaše `ime` i `prezime` i `godina_rodenja`. Promjenjivu varijablu nazovite `trenutno_vrijeme`.
- U varijable `ime` i `prezime` pohranite svoje ime i prezime, a u varijablu `godina_rodenja` pohranite godinu rođenja kao cjelobrojnu vrijednost. U varijablu `trenutno_vrijeme` pohranite trenutno vrijeme koristeći `new Date()` objekt.
- Dodajte novu varijablu `godine` i u nju izračunajte koliko imate godina koristeći: gotovu funkciju [`getFullYear()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getFullYear) nad varijablom `trenutno_vrijeme` i varijablu `godina_rodenja`. Sintaksa je: `varijabla.getFullYear()`. Radi pojednostavljivanja, pretpostavljamo da je vaš rođendan već prošao ove godine.

Koristeći [`template literals`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals), u konzolu ispišite "Bok moje ime je __ __ i imam __ godina.".
- Deklarirajte dvije nove konstante `ime_duljina` i `prezime_duljina` u koje ćete pohraniti broj slova u vašem imenu i prezimenu koristeći funkciju [`length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length) nad varijablama `ime` i `prezime`.
- Ispišite u konzolu "Moje ime i prezime imaju __ i __ slova." koristeći `template literals`.
- Ispišite u konzolu "It is __ that my name and surname are of the same length" koristeći `template literals` i operator `"je identično"`.

Pohranite u novu varijablu `x` kvadrat zbroja varijabli `ime_duljina` i `prezime_duljina`. Rezultat zbrojite s vašom godinom rođenja inkrementiranom za 1 koristeći operator `++` ispred varijable (uočite grešku, zašto nastaje, i napravite izmjenu!) te sve skupa podijelite s `2`.
- Sve navedeno definirajte u obliku <span style="color:red">jednog izraza u jednoj liniji kȏda</span>. [MAX_TASK_POINTS=5]


**2.** Recimo da si želite definirati daily routine koji se sastoji od nekoliko ciljeva. Koristeći logičke operatore i operatore usporedbe, definirajte varijablu `daily_routine_ostvaren`, temeljem sljedećih tvrdnji. Vaš `daily_routine_ostvaren` je ispunjen ako:
- ste pročitali više od 50 stranica vaše omiljene knjige **ili** ste vježbali JavaScript barem 1 sat
- ste popili između litre i dvije litre vode
- ste vježbali minimalno 30 minuta **ili** ste prošetali minimalno 3 km
- ste naučili nešto novo
- ste se naspavali minimalno 7 sati
- ste se nasmijali

Za svaki od danih izraza deklarirajte varijable za ostvarenu vrijednost i ciljanu vrijednost, te boolean varijablu koja će sadržavati rezultat ostvarenja. Na primjer, za izraz `popiti između litre i dvije litre vode` deklarirajte varijable `unos_vode` i `ciljani_dnevni_unos_vode` te varijablu `dnevni_unos_vode_zadovoljen`.
- Definirajte varijablu `daily_routine_ostvaren` koja će sadržavati rezultat ostvarenja svih dnevnih ciljeva. [MAX_TASK_POINTS=5]


## aburic1@student.unipu.hr

### Code

```javascript
const [ime, prezime, godina_rodenja] = ['Alan', 'Burić', 2003];
var trenutno_vrijeme = new Date();
var godine = trenutno_vrijeme.getFullYear() - godina_rodenja;

console.log(`Bok moje ime je ${ime} i imam ${godine} godina.`);

const [ime_duljina, prezime_duljina] = [ime.length, prezime.length];

console.log(`Moje ime i prezime imaju ${ime_duljina} i ${prezime_duljina} slova.`);
console.log(`It is ${ime_duljina === prezime_duljina} that my name and surname are of the same length`);

var x = ((ime_duljina + prezime_duljina) ** 2 + godina_rodenja + 1) / 2;

var procitano_str = 39
var ciljani_broj_str = 50;
var procitao_50_str = procitano_str >= ciljani_broj_str;

var vjezbao_js = 1.2;
var ciljani_broj_js_vjezbi = 1;
var vjezbao_js_min_1_h = vjezbao_js >= ciljani_broj_js_vjezbi;

var unos_vode = 1.5;
var [min_unos_vode, max_unos_vode] = [1, 2];
var popio_1_2_l_vode = unos_vode >= min_unos_vode && unos_vode <= max_unos_vode;

var vjezbao = 10;
var ciljane_min_vjezbe = 30;
var vjezbao_min_30_min = vjezbao >= ciljane_min_vjezbe;

var prosetao = 4;
var prosetao_ciljano = 3;
var prosetao_min_3_km = prosetao >= prosetao_ciljano;

var naucio_nesto_novo = true;

var spavao = 5;
var spavao_min_ciljano = 7;
var spavao_min_7_h = spavao >= spavao_min_ciljano;

var nasmijao_se = true;


var daily_routine_ostvaren = (procitao_50_str || vjezbao_js_min_1_h) 
  && popio_1_2_l_vode 
  && (vjezbao_min_30_min || prosetao_min_3_km)
  && naucio_nesto_novo
  && spavao_min_7_h
  && nasmijao_se;
```

### Evaluation

- Task 1: 4.5
- Task 2: 4
- Total Points: 8.5
- Feedback: Zadatak 1: Dobro obavljeno, ali postoji greška u izračunu varijable x gdje je trebalo koristiti godina_rodenja++ nakon što se izračuna kvadrat zbroja. Zadatak 2: Logika je uglavnom dobra, ali varijabla procitao_50_str nije ispravno definirana jer koristi pogrešan operator usporedbe za postizanje cilja čitanja više od 50 stranica.
- Cost for this evaluation: $0.02

## alabinjan@student.unipu.hr

### Code

```javascript
const ciljane_stranice = 50;
const ciljani_JS = 1;
const minimalna_ciljana_kolicina_vode = 1;
const maksimalna_ciljana_kolicina_vode = 2;
const ciljano_vrijeme_vjezbe = 30;
const ciljana_setnja  =3;
const cilj_novo_ucenje = true;
const cilj_spavanje = 7;
const smijanje = true;

const ostvaren_broj_stranica = 55;
const ostvaren_JS = 2;
const ostvarena_voda = 1.9;
const ostvarena_vjezba = 35;
const ostvarena_setnja = 4;
const ostvareno_ucenje = true;
const ostvareno_spavanje = 9;
const ostvareno_smijanje = true;

const ispunjene_stranice = ostvaren_broj_stranica >= ciljane_stranice;
const ispunjeni_JS = ostvaren_JS >=ciljani_JS;
const ispunjena_voda = ostvarena_voda >minimalna_ciljana_kolicina_vode && ostvarena_voda <maksimalna_ciljana_kolicina_vode;
const ispunjena_vjezba = ciljano_vrijeme_vjezbe < ostvarena_vjezba;
const ispunjena_setnja = ciljana_setnja < ostvarena_setnja;
const ispunjeno_ucenje = true;
const ispunjeno_spavanje = cilj_spavanje < ostvareno_spavanje;
const ispunjeno_smijanje = true;


const daily_routine_ostvaren = (ispunjene_stranice || ispunjeni_JS)&& ispunjena_voda && (ispunjena_vjezba||ostvarena_setnja) && ispunjeno_ucenje && ispunjeno_spavanje && ispunjeno_smijanje
console.log(daily_routine_ostvaren)

```

### Evaluation

- Task 1: 0
- Task 2: 4.5
- Total Points: 4.5
- Feedback: Zadatak 1: Niste pružili kod za ocjenjivanje. Zadatak 2: Logika je uglavnom ispravna, ali postoji greška u provjeri ispunjenosti uvjeta za vodu; trebali ste koristiti >= i <= za minimalnu i maksimalnu količinu vode. Također, korištenje 'ostvarena_setnja' u logičkom izrazu bez usporedbe je greška.
- Cost for this evaluation: $0.02

## arogalo@student.unipu.hr

### Code

```javascript
const ime = "Ana";
const prezime = "Rogalo";
const godina_rođenja = 2004;
let trenutno_vrijeme = new Date();
trenutno_vrijeme = trenutno_vrijeme.getFullYear()
  
let godine = trenutno_vrijeme - godina_rođenja;



```

### Evaluation

- Task 1: 2.5
- Task 2: 0
- Total Points: 2.5
- Feedback: Za prvi zadatak, student je ispravno deklarirao konstante i varijable te izračunao godine, ali nije ispunio sve navedene zahtjeve, poput ispisa u konzolu i izračuna s varijablom x. Drugi zadatak nije riješen jer kod za njega nije priložen.
- Cost for this evaluation: $0.02

## asirol@student.unipu.hr

### Code

```javascript
const ime = 'Anastazija';
const prezime = 'Širol';
const godina_rodenja = 2003;
let trenutno_vrijeme = new Date();
trenutno_vrijeme = trenutno_vrijeme.getFullYear();
let godine = trenutno_vrijeme - godina_rodenja;

console.log("Bok moje ime je " + ime + " i imam " + godine + " godinu.")

const ime_duljina = ime.length;
const prezime_duljina=prezime.length;

console.log("Moje ime i prezime imaju " + (ime_duljina + prezime_duljina) + " slova.");

let jednako = ime_duljina==prezime_duljina;

console.log("It is " + jednako + " that my name and surname are of the same length");

let x = (((ime_duljina+prezime_duljina)**2)+(godina_rodenja+1))/2;

// ++ godina_rodenja izbacuje grešku jer je to konstantna varijabla i ne može se mijenjati

console.log(x);


let broj_procitanih_stranica_knjige = 30;
let ciljani_broj_stranica=50;
let stranice=broj_procitanih_stranica_knjige>=ciljani_broj_stranica;
let broj_sati_vjezbanja_JavaScripta = 2;
let ciljani_broj_sati = 1;
let ostvareni_broj_sati=broj_sati_vjezbanja_JavaScripta>=ciljani_broj_sati;
let cilj_1 = broj_procitanih_stranica_knjige>=ciljani_broj_stranica || broj_sati_vjezbanja_JavaScripta>=ciljani_broj_sati;

let popijene_litre_vode = 2;
let ciljane_litre_min=1;
let ciljane_litre_max=2;
let cilj_2 = popijene_litre_vode >= ciljane_litre_min && popijene_litre_vode <=ciljane_litre_max;

let broj_sati_vjezbanja = 15;
let ciljano=30;
let prosetani_km = 4;
let ciljani_km=3;
let cilj_3 = broj_sati_vjezbanja>=ciljano || prosetani_km >=ciljani_km;

let nauceno=true;
let ciljano_nauceno=true;
let cilj_4=nauceno==ciljano_nauceno;

let broj_sati_sna=8;
let ciljani_broj_sati_sna=7;
let cilj_5=broj_sati_sna>=ciljani_broj_sati_sna;

let osmijeh=true;
let ciljani_osmijeh=true;
let cilje_6=osmijeh==ciljani_osmijeh;

let daily_routine_ostvaren = cilj_1 && cilj_2 && cilj_3 && cilj_4 && cilj_5 && cilje_6;

console.log(daily_routine_ostvaren);

```

### Evaluation

- Task 1: 4
- Task 2: 4.5
- Total Points: 8.5
- Feedback: Zadatak 1: Dobro je obavljeno, ali korištenje + umjesto template literals smanjuje bodove. Također, greška s inkrementiranjem konstante je dobro uočena, ali izračun nije u jednoj liniji. Zadatak 2: Logika je uglavnom dobra, ali deklaracija varijabli za ciljane vrijednosti i ostvarene vrijednosti nije potpuno u skladu s uputama. Dobar pokušaj i dobro razumijevanje logičkih operatora.
- Cost for this evaluation: $0.03

## aspahic@student.unipu.hr

### Code

```javascript
const ime = "Adis"
const prezime = "Spahic"
let godina_rodenja = 2004
let trenutno_vrijeme = new Date()

let godine = trenutno_vrijeme.getFullYear() - godina_rodenja

console.log(`Bok moje ime je ${ime} i imam ${godine} godina.`)

const ime_duljina = ime.length
const prezime_duljina = prezime.length

console.log(`Moje ime i prezime imaju ${ime_duljina} i ${prezime_duljina} slova.`)

console.log(`It is ${ime.length == prezime.length} that my name and surname are of the same lenth`)

let x = (ime_duljina ** 2 + prezime_duljina ** 2) + (++godina_rodenja) / 2
console.log(x)

```

### Evaluation

- Task 1: 4
- Task 2: 0
- Total Points: 4
- Feedback: Zadatak 1: Dobro je obavljeno deklariranje konstanti i varijabli te ispis u konzolu, ali izračun varijable x nije u jednom izrazu niti je ispravno riješen problem s inkrementom. Zadatak 2: Nije priložen kod za drugi zadatak, stoga ne mogu dodijeliti bodove.
- Cost for this evaluation: $0.02



# Total Cost for Evaluating a_new_hope
Total cost for running evaluations: $0.11