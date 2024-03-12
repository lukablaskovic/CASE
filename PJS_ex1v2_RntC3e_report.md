# Exam Tasks

**1.** Deklarirajte varijable `datum_danas` i `vlaga`. U varijablu `datum_danas` spremite datum današnjeg dana koristeći `new Date()` objekt, a u varijablu `vlaga` spremite proizvoljnu vrijednost vlage kao decimalni broj od `0` do max `1`.
- Dodajte novu varijablu `mjesec` u koju ćete pohraniti trenutni mjesec koristeći `getMonth()` funkciju nad varijablom `datum_danas`, pripazite da `getMonth()` vraća mjesec kao broj od 0 do 11. Varijablu `vlaga` pretvorite u postotak. Sintaksa: `varijabla.getMonth()`.

- Ispišite u konzolu rečenicu: `"Mjesec je: __., a vlaga je: __%."` Mjesec i vlagu zamijenite s vrijednostima iz varijabli koristeći interpolaciju stringova (template literals) sintaksu. _Primjer ispisa_: `"Mjesec je: 3., a vlaga je: 40%."`

(MAX_TASK_POINTS = 2)

**2.** Definirajte konstantu `PI` i dodijelite joj vrijednost broja π (3.14159). Dodajte novu varijablu `radijus` u koju ćete pohraniti proizvoljnu vrijednost radijusa cilindra. Dodajte i varijablu `visina` u koju ćete pohraniti proizvoljnu vrijednost visine cilindra. Ispišite u konzolu rečenice: `"Volumen cilindra je: ____ cm3, a površina iznosi ____ cm2."`.
Volumen i površinu zamijenite s izračunatim vrijednostima koristeći interpolaciju stringova (template literals). Kada to napravite, ispišite sličnu rečenicu međutim s vrijednostima u kvadratnim milimetrima (mm2)

(MAX_TASK_POINTS = 2)

- Volumen: `π r² h`
- Površina: `2 π r h + 2π r²`

**3.** Kod kuće ste s obitelji i morate odlučiti koji film pogledati, a da svi budu zadovoljni. Dosjetili ste se jednog filma, no ne možete se dogovoriti hoćete li pogledati baš taj. Koristeći logičke operatore i operatore usporedbe, definirajte varijablu `film_odabran`. Svaki od članova obitelji ima po jedan uvjet za film:

- Film mora trajati između 90 i 180 minuta.
- Film mora imati minimalno ocjenu 7.5 na IMDB-u.
- Film mora biti komedija ili akcijski film.
- Film mora biti na engleskom jeziku.

Za svaki od danih izraza deklarirajte varijable za ostvarenu vrijednost i ciljanu vrijednost, te boolean varijablu koja će sadržavati rezultat ostvarenja. Na primjer, za drugu izjavu varijable mogu biti: `min_ocjena_filma`, `ocjena_filma`, `ocjena_zadovoljena`.
Kroz varijable definirajte izraz za svaki uvjet i na kraju ispišite rezultat u obliku `film_odabran = uvjet1 && uvjet2 && uvjet3 && uvjet4`, gdje `film_odabran` mora biti `true` ili `false`.
(MAX_TASK_POINTS = 3)

**4.** Raspišite sljedeće izraze bez korištenja `+=`, `-=`, `*=`, `/=`, `++` ili `--` operatora. (MAX_TASK_POINTS = 2)

```javascript
let a = 5;
let b = 3;
b += a; // Izmijenite izraz
a -= b; // Izmijenite izraz
b += 10 + a; // Izmijenite izraz
a *= ++b; // Izmijenite izraz
console.log(a); // -48
console.log(b); // 16
// Izmijenjeni izrazi moraju u konačnici moraju vratiti isti rezultat a i b varijabli kao i originalni izrazi.
// Originalne izraze možete zakomentirati, a ispod njih napisati alternativni izraz (bez korištenja spomenutih operatora).
```

**5.** Napišite program koji uspoređuje duljinu dvije riječi i zatim ispisuje rezultat eksponencijalne operacije gdje je baza duljina dulje riječi, a eksponent duljina kraće riječi. (MAX_TASK_POINTS = 1)

## nhorvat1@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "//Prvi zadatak\nlet datum_danas = new Date();\nlet vlaga = 0.7;\n\nlet mjesec = datum_danas.getMonth();\nlet postotakVlaga = vlaga * 100;\n\nlet recenica = `Mjesec je: ${mjesec}., a vlaga je: ${postotakVlaga}%.`;\n\n\nconsole.log(recenica)"
        },
        {
            "js_code": "//Drugi zadatak\nconst PI = 3.14169;\nlet radijus = 1.1;\nlet visina = 2;\n\nlet volumen = PI * radijus**2 * visina;\nlet povrsina = (2 * PI * radijus * visina) + 2 * PI * radijus**2;\n\nlet recenica = `Volumen cilindra je: ${volumen} cm3, a povr\u0161ina iznosi ${povrsina} cm2.`;\n\n//1 cm = 10 mm \nlet volumenDva = volumen / 10;\nlet povrsinaDva = povrsina / 10;\n\n\nlet recenica2 = `Volumen cilindra je: ${volumenDva} mm3, a povr\u0161ina iznosi ${povrsinaDva} mm2.`;\n\n\nconsole.log(recenica)\nconsole.log(recenica2)"
        },
        {
            "js_code": "let filmTraje = 100;\nlet ocjenaFilma = 8;\nlet zanrFilma = \"komedija\";\nlet jezikFilma = \"francuski\";\n\nlet ciljTrajanja = filmTraje >= 90 && filmTraje >= 180;\nlet ciljOcjene = ocjenaFilma >= 7.5;\nlet ciljZanra = \"komedija\" || \"akcija\";\nlet ciljJezik = \"engleski\";\n\nlet filmOdabran = ciljTrajanja && ciljOcjene && ciljZanra && ciljJezik;\n\n\nconsole.log(filmOdabran)"
        },
        {
            "js_code": "let a = 5;\r\nlet b = 3;\r\n\r\nb = b + a; // Izmijenite izraz\r\n\r\na = a - b; // Izmijenite izraz\r\n\r\nb = b + 10 + a; // Izmijenite izraz\r\n\r\na = a* ++b; // Izmijenite izraz\r\n\r\nconsole.log(a); // -48\r\nconsole.log(b); // 16"
        },
        {
            "js_code": "let prvaRijec = \"nika\";\nlet drugaRijec = \"horvat\";\n\nlet duljinaPrve = prvaRijec.length;\nlet duljinaDruge = drugaRijec.length;\n\nlet usporedba = duljinaPrve == duljinaDruge;\n\n//rezultat eksponencijalne operacije gdje je\n//baza = duljina dulje rijeci\n//eksponent = duljina krace rijec\n\nlet duljaPrva = duljinaPrve > duljinaDruge;\nlet duljaDruga = duljinaDruge > duljinaPrve;\n\nlet rezultat = duljinaPrve**duljinaDruge;\n\n\nconsole.log(usporedba)\n\nconsole.log(rezultat)"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 1.5
- Task 3: 0.5
- Task 4: 2
- Task 5: 0.5

- Total Points: 6.5
- Feedback: Zadatak 1: Odlično, sve je ispravno implementirano. Zadatak 2: Postoji greška u pretvorbi jedinica, 1 cm nije jednak 10 mm, već 1 cm3 je 1000 mm3 i 1 cm2 je 100 mm2. Zadatak 3: Logika za odabir filma nije ispravno implementirana, ciljZanra i ciljJezik nisu pravilno korišteni u usporedbi. Zadatak 4: Izmjene su ispravno implementirane i daju očekivani rezultat. Zadatak 5: Logika za određivanje baze i eksponenta nije ispravno implementirana, trebalo je usporediti duljine i koristiti ih kako je navedeno u zadatku.
- Cost for this evaluation: $0.03

## tijovanov@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date();\nlet vlaga = 0.5;\n\nvlaga *= 100;\n\nlet mjesec = datum_danas.getMonth();\n\nconsole.log(`Mjesec je: ${mjesec}., a vlaga je: ${vlaga}%.`);"
        },
        {
            "js_code": "const pi = 3.14159;\n\nlet radijus = 5;\nlet visina = 2;\n\nvolumen = pi * (radijus*radijus) * visina;\npovrsina = (2 * pi * radijus * visina) +  (2*pi * (radijus*radijus)); \n\n\nconsole.log(`Volumen cilindra je: ${volumen} cm3, a povrsina iznosi ${povrsina} cm2.`);"
        },
        {
            "js_code": "[NOT_SOLVED]"
        },
        {
            "js_code": "let a = 5;\r\nlet b = 3;\r\nb = b + a; // Izmijenite izraz\r\na = a - b; // Izmijenite izraz\r\nb = b + (10 + a); // Izmijenite izraz\r\na = a * (b = b + 1); // Izmijenite izraz\r\nconsole.log(a); // -48\r\nconsole.log(b); // 16\r\n// Izmijenjeni izrazi moraju u kona\u010dnici moraju vratiti isti rezultat a i b varijabli kao i originalni izrazi.\r\n// Originalne izraze mo\u017eete zakomentirati, a ispod njih napisati alternativni izraz (bez kori\u0161tenja spomenutih operatora).\r\n"
        },
        {
            "js_code": "let string1 = \"abraka dabra\"\nlet string2 = \"ciribu ciriba\"\n\nif(string1.length > string2.length){\n  str1 = string1.slice(0, 7);\n  str2 = string2.slice(7, 12)\n  console.log(str1 +\" \"  + str2);\n} else {\n    str1 = string2.slice(0, 7);\n  str2 = string1.slice(7, 12)\n  console.log(str2 +\" \"  + str1);\n}\n\n"
        }
    ]
}
```

### Evaluation

- Task 1: 1.5
- Task 2: 2
- Task 3: 0
- Task 4: 2
- Task 5: 0.5

- Total Points: 6
- Feedback: Zadatak 1: Dobro je, ali mjesec treba povećati za 1 da bi bio ispravan. Zadatak 2: Točno rješenje, dobro obavljeno. Zadatak 3: Nije riješeno, nema bodova. Zadatak 4: Ispravno modificirani izrazi, dobro. Zadatak 5: Niste izvršili traženu eksponencijalnu operaciju, već ste manipulirali stringovima.
- Cost for this evaluation: $0.03

## llabinjan@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas= new Date()\nlet vlaga = 0.5*100\nlet mjesec=datum_danas.getMonth()\n\n\nconsole.log(`Mjesec je:${mjesec}., a vlaga je:${vlaga}%.`)\n\n"
        },
        {
            "js_code": "const PI=3.14159\nlet radijus= 2\nlet visina=3\nconsole.log(`Volumen cilindra je:${PI*radijus**2*visina}cm3, a povr\u0161ina iznosi ${2*PI*radijus*visina+2*PI*radijus**2}cm2`)\nconsole.log(`Volumen cilindra je:${(PI*radijus**2*visina)/1000}mm2,a povr\u0161ina iznosi ${(2*PI*radijus*visina+2*PI+radijus**2)/1000}`)\n\n"
        },
        {
            "js_code": "\nlet min_trajanje=90\nlet max_trajanje=180\nlet trajanje =90\ntrajanje>=max_trajanje || trajanje<=min_trajanje\nlet film_vrsta1=\"komedija\"\nlet film_vrsta2=\"akcijski\"\nlet uvjet4=jezik==\"Engleski\"\njezik =\"Engleski\"\nlet vrsta=\"akcijski\"\nvrsta= film_vrsta1|| film_vrsta2\nlet film_odabran=uvjet4&& vrsta&&trajanje\nconsole.log(film_odabran)"
        },
        {
            "js_code": "let a=5\nlet b=3\nb=b+a\na=a-b\nb=b+(10+a)\na=a* ++b\nconsole.log(a)\nconsole.log(b)"
        },
        {
            "js_code": "let string1=\"ana\";\nlet string2 =\"emili\";\nif(string1.length>string2.length){\n  console.log(string1.length**string2.length)}\n\n  else{\n    console.log(string2.length**string1.length)}\n"
        }
    ]
}
```

### Evaluation

- Task 1: 1.5
- Task 2: 1.5
- Task 3: 1
- Task 4: 1.5
- Task 5: 1

- Total Points: 6.5
- Feedback: Zadatak 1: Vlaga nije ispravno pretvorena u postotak unutar logike programa, trebali ste pomnožiti vrijednost vlage s 100 unutar logike, a ne pri deklaraciji. Zadatak 2: Pogreška u pretvorbi jedinica za površinu u mm2, trebali ste pomnožiti cijeli izraz površine s 1000, a ne samo dio izraza. Zadatak 3: Logika za odabir filma nije potpuno ispravna, uvjeti nisu pravilno definirani i korišteni. Zadatak 4: Iako je krajnji rezultat ispravan, korištenje operatora ++ nije dozvoljeno prema zadatku. Zadatak 5: Rješenje je ispravno, ali obratite pažnju na efikasnije načine za postizanje istog rezultata.
- Cost for this evaluation: $0.03

## dkokalovi@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_dana=new Date();\nlet vlaga=0.60;\nlet mjesec=datum_dana.getMonth();\nvlaga = 0.60*100;\nconsole.log(`Mjesec je: ${datum_dana}, a vlaga je: ${vlaga}%.`)\n\n"
        },
        {
            "js_code": "const PI=3.14159\nlet radijus=5;\nlet visina=6;\nlet povrsina=2*PI*radijus*visina+2*PI*(radijus*radijus);\nlet volumen=PI*(radijus*radijus)*visina\nconsole.log(`Volumen cilindra je: ${volumen} cm3,a povr\u0161ina iznosi ${povrsina} cm2 `);"
        },
        {
            "js_code": "let=film_odabran;\n\nlet trajanje_filma 90>=180 && 90<=180;\nlet ocjena_filma 7.5>=10;\nlet naziv_filma=\"komedija\" && \"akcija\";\nlet jezik_filma=\"englesnki jezik\";\n\nlet trajanje=100;\nlet ocjena=6;\nlet naziv=\"komedija\";\nlet jezik=\"francuski jezik\";\n\nlet trajanje_filma=trajanje;\nlet ocjena=ocjena_filma;\nlet naziv=naziv_filma;\nlet jezik=jezik_filma;\n\n\nconsole.log(``)\n"
        },
        {
            "js_code": "let a=5;\nlet b=3;\n\nb=b+a;\na=b-a;\nb=a+10;\na=a*1+b;\nconsole.log(a);\nconsole.log(b);"
        },
        {
            "js_code": "let rijec=\"pas\";\nlet rijec = \"ma\u010dka\";"
        }
    ]
}
```

### Evaluation

- Task 1: 1.5
- Task 2: 2
- Task 3: 0
- Task 4: 1
- Task 5: 0

- Total Points: 4.5
- Feedback: Zadatak 1: Ispravno koristite Date objekt i pretvarate vlagu u postotak, ali ispisujete datum_dana umjesto mjeseca. Zadatak 2: Dobro ste izračunali volumen i površinu cilindra, ali niste ispisali vrijednosti u mm2. Zadatak 3: Kod nije ispravno strukturiran, logički uvjeti nisu pravilno definirani. Zadatak 4: Izmijenjeni izrazi ne vraćaju iste rezultate kao originalni izrazi. Zadatak 5: Niste uspješno implementirali zadatak, nedostaje logika za usporedbu duljina riječi i izračun eksponencijalne operacije.
- Cost for this evaluation: $0.03

## pfabijani@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas=new Date()\nlet vlaga=0.50\n\nlet mjesec=datum_danas.getMonth()\n\nconsole.log(mjesec)\n\nvlaga=vlaga*100\n\nconsole.log(vlaga)\n\nconsole.log(`Mjesec je: ${mjesec}., a vlaga je: ${vlaga}%.`)"
        },
        {
            "js_code": "const PI=3.14159\nlet radijus=4\nlet visina=2\n\nlet povrsina=2*PI*radijus*visina+2*PI*(radijus*radijus)\n\nlet volumen=PI*(radijus*radijus)*visina\n\nconsole.log(`Volumen cilindra je: ${volumen} cm3, a povr\u0161ina iznosi ${povrsina} cm2.`)"
        },
        {
            "js_code": "\n\nlet film_trajanje_moje=70\nlet film_trajanje= 90>=180 && 180<=90\nlet moja_ocjena_filma= 9.2\nlet min_ocjena_filma= 7.5\nlet zanr = \"komedija\" || \"akcija\"\nlet engleski=true\n\nlet film_trajanje_cilj=film_trajanje_moje<=film_trajanje && film_trajanje>=film_trajanje_moje\nlet cilj_ocjena=moja_ocjena_filma>=min_ocjena_filma && min_ocjena_filma<=moja_ocjena_filma\nlet zeljeni_zanr=\"komedija\"\n\nfilm_odabran=film_trajanje_cilj&&cilj_ocjena&&zeljeni_zanr&&engleski\n\nconsole.log(film_odabran)"
        },
        {
            "js_code": "let a = 5;\nlet b = 3;\n\nb=b+a;\na=a-b;\nb=b+10+a;\na=a*(++b);\nconsole.log(a);\nconsole.log(b);"
        },
        {
            "js_code": "let rijec=\"patrik\";\nlet rijec1=\"fabijanic\";\n\nduljina=rijec.length>=rijec1.length || rijec1.length<=rijec || rijec1.length>=rijec.length ||\n\n\n"
        }
    ]
}
```

### Evaluation

- Task 1: 1.5
- Task 2: 2
- Task 3: 0.5
- Task 4: 1
- Task 5: 0

- Total Points: 5
- Feedback: Zadatak 1: Dobro je korištenje Date objekta i pretvorba vlage u postotak, ali mjesec se trebao povećati za 1. Zadatak 2: Ispravno izračunati volumen i površina cilindra. Zadatak 3: Logika za odabir filma je neispravna i konfuzna. Zadatak 4: Izmijenjeni izrazi ne koriste zabranjene operatore, ali krajnji rezultat nije točan. Zadatak 5: Nedostaje rješenje za usporedbu duljina riječi i izračun eksponencijalne operacije.
- Cost for this evaluation: $0.03

## dcadro@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas;\nlet vlaga;\nlet mjesec;\n\n\n"
        },
        {
            "js_code": "let PI=3.141592653589793;\nconst radius=2;\nconst visina= 3;\n\nconsole.log(\"Volumen cilindra je: \"+ (PI*(radius)**2*visina)+\" cm3, a povrsina iznosi \"+(2*PI*radius*visina+(2*PI)*(radius)**2))+\" cm2\";\n\n"
        },
        {
            "js_code": "const film_odabran;"
        },
        {
            "js_code": "[NOT_SOLVED]"
        },
        {
            "js_code": "[NOT_SOLVED]"
        }
    ]
}
```

### Evaluation

- Task 1: 0.5
- Task 2: 1.5
- Task 3: 0
- Task 4: 0
- Task 5: 0

- Total Points: 2
- Feedback: Zadatak 1: Niste implementirali logiku za dobivanje trenutnog datuma, pretvaranje vlage u postotak niti ispis u konzolu. Dodijeljeni su bodovi za trud. Zadatak 2: Imate pravilnu logiku za izračun volumena i površine cilindra, ali postoji sintaksna greška u ispisu. Zadatak 3: Niste implementirali logiku za odabir filma. Zadatak 4 i 5: Niste riješili zadatke.
- Cost for this evaluation: $0.02

## fbebek@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "const datum_danas=new Date();\nlet vlaga=0.5*100;\nlet mjesec=datum_danas.getMonth();\n\nconsole.log(`Mjesec je: ${mjesec}, a vlaga je: ${vlaga}%`);"
        },
        {
            "js_code": "const pi=3.14159;\nlet r=14;\nlet h=2;\nlet volumen=pi*(r**2)*h;\nlet povrsina=2*pi*r*h + 2*pi*(r**2);\n\nconsole.log(`Volumen cilindra je: ${volumen} cm3, a povrsina iznosi ${povrsina} cm2.`);"
        },
        {
            "js_code": "let filmtrajanje=180;\nlet trajaoje=120;\n\nlet mogucaocjena=10;\nlet pravaocjena=8.5;\n\nlet mogucfilm=\"akcija\";\nlet film=\"akcija\";\n\nlet jezikfilma=\"engleski\";\nlet jezik=\"engleski\";\n\nlet film_odabran=(trajaoje>90 && trajaoje<180) && (pravaocjena>=7.5) && (film==\"akcija\") && (jezik==\"engleski\");\n\nconsole.log(film_odabran);"
        },
        {
            "js_code": "//let a = 5;\n//let b = 3;\n//b += a; // Izmijenite izraz\n//a -= b; // Izmijenite izraz\n//b += 10 + a; // Izmijenite izraz\n//a *= ++b; // Izmijenite izraz\n//console.log(a); // -48\n//console.log(b); // 16\n\n\nlet a=5;\nlet b=3;\nb=b+a;\na=a-b;\nb=b+10+a;\na=a*++b;\nconsole.log(a);\nconsole.log(b);"
        },
        {
            "js_code": "let rijec1=\"filipa\";\nlet rijec2=\"bebek\";\nconst duljina1=rijec1.length;\nconst duljina2=rijec2.length;\nlet rezultat=duljina1**duljina2;\n\nconsole.log(`Rezultat eksponencijalne operacije: ${rezultat}`);"
        }
    ]
}
```

### Evaluation

- Task 1: 1.5
- Task 2: 2
- Task 3: 2.5
- Task 4: 1
- Task 5: 1

- Total Points: 8
- Feedback: Zadatak 1: Vlaga nije ispravno pretvorena u postotak unutar interpolacije stringa, trebalo je koristiti vlaga*100. Zadatak 2: Točno rješenje. Zadatak 3: Logika je ispravna, ali varijable za trajanje filma su nekonzistentne. Zadatak 4: Izmijenjeni izrazi su točni, ali korištenje ++b nije u skladu s uputama. Zadatak 5: Točno rješenje, ali nije uspoređena duljina riječi kako bi se odredila dulja i kraća riječ.
- Cost for this evaluation: $0.03

## mholi@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date()\nlet vlaga = 0.69\n\nlet mjesec = datum_danas.getMonth()\n\nvlaga *= 100\n\nconsole.log(`Mjesec je: ${mjesec}., a vlaga je: ${vlaga}%.`)"
        },
        {
            "js_code": "const PI = 3.14159\nlet radijus = 7\nlet visina = 5\n\nconsole.log(`Volumen cilindra je: ${PI*(radijus*radijus)*visina} cm3, a povr\u0161ina iznosi ${(2*PI*radijus*visina)+(2*PI*(radijus*radijus))} cm2.`)"
        },
        {
            "js_code": "let film_odabran\n\nlet max_c_trajanje = 180\nlet min_c_trajanje = 90\nlet trajanje = 95\nlet trajanje_z = trajanje > min_c_trajanje && trajanje < max_c_trajanje\n\nlet min_ocjena = 7.5\nlet ocjena = 9.2\nlet ocjena_z = ocjena > min_ocjena\n\nlet g_c_filma = \"komedija\"\nlet g_a_filma = \"akcijski\"\nlet g_filma = \"komedija\"\nlet g_filma_z = g_filma == g_c_filma || g_filma == g_a_filma\n\nlet c_j_filma = \"engleski\"\nlet j_filma = \"engleski\"\nlet j_filma_z = j_filma == c_j_filma\n\nfilm_odabran = trajanje_z && ocjena_z && g_filma_z && j_filma_z\n\nconsole.log(film_odabran)\n\n"
        },
        {
            "js_code": "let a = 5;\r\nlet b = 3;\r\n\r\nb = b + a\r\na = a - b"
        },
        {
            "js_code": "let a = \"Luffy\"\nlet b = \"Zoro\"\n\nlet a_c = a.length\nlet b_c = b.length\n\nif (a<b){\n  console.log(b_c ** a_c)\n}\n\nif (b<a){\n  console.log(a_c ** b_c)\n}"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 2
- Task 3: 3
- Task 4: 1
- Task 5: 0.5

- Total Points: 8.5
- Feedback: Zadatak 1: Odlično, sve je ispravno implementirano. Zadatak 2: Također, sve je točno izračunato i ispravno prikazano. Zadatak 3: Svi uvjeti su pravilno definirani i logički operatori su ispravno korišteni. Zadatak 4: Nedostaje dio izraza za pravilno vraćanje istih vrijednosti za a i b. Zadatak 5: Usporedba riječi nije ispravno implementirana, trebalo je koristiti duljinu riječi, a ne same riječi za usporedbu.
- Cost for this evaluation: $0.03

## imarkovic@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date()\nlet vlaga = 0.5\nlet mjesec = datum_danas.getMonth() + 1\n\nvlaga = vlaga * 100\n\nconsole.log(`Mjesec je ${mjesec}, a vlaga je:${vlaga}`)"
        },
        {
            "js_code": "const PI = 3.14159\nlet radijus = 5\nlet visina = 7\n\nlet volumen = PI * radijus**2 * visina\nlet povrsina = 2 * PI * radijus * visina * 2 * PI * radijus**2\n\nconsole.log(`Volumen cilindra je ${volumen} cm3, a povri\u0161ina iznosi ${povrsina} cm2`)\n\nconsole.log(`Volumen cilindra je ${10 * volumen} mm3, a povri\u0161ina iznosi ${10 *povrsina} mm2`)\n"
        },
        {
            "js_code": "let trajanje_filma \ntrajanje_filma >= 90 && trajanje_filma <= 180\n\nlet ocjena\nocjena >= 7.5\n\nlet vrsta = \"akcijski\" || \"komedija\"\n\nlet film_jezik = \"engleski\""
        },
        {
            "js_code": "let a = 5\nlet b = 3\n\nb = b + a\na = a - b\nb = b + 10 + a\na = a * (b+1)\nb = b +1\n\nconsole.log(a)\nconsole.log(b)"
        },
        {
            "js_code": "let prva = \"Igor\"\nlet druga = \"Marko\"\n\n\nif( prva > druga){\n  \n}"
        }
    ]
}
```

### Evaluation

- Task 1: 1.5
- Task 2: 1
- Task 3: 0
- Task 4: 1.5
- Task 5: 0

- Total Points: 4
- Feedback: Zadatak 1: Dobro je, ali nedostaje točka iza broja mjeseca i razmak prije postotka vlage. Zadatak 2: Formula za površinu je netočna, a konverzija u mm2 nije ispravno izvedena (trebalo je koristiti faktor 1000 za volumen i 100 za površinu). Zadatak 3: Niste definirali varijable niti logičke operacije kako je zatraženo, zadatak nije riješen. Zadatak 4: Pristup je bio dobar, ali zadnji izraz za 'a' nije točno preveden, trebalo je koristiti originalnu vrijednost 'b' prije povećanja. Zadatak 5: Nema rješenja, nedostaje logika za usporedbu duljina riječi i izvođenje eksponencijalne operacije.
- Cost for this evaluation: $0.03

## dbarna@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "const datum_danas = new Date();\nlet vlaga = vlaga <\n\nlet mjesec = datum_danas.getMonth();\n\n\n\n\n\n\n"
        },
        {
            "js_code": "[NOT_SOLVED]"
        },
        {
            "js_code": "film_odabran = true;\nlet = imdb_ocjena;\nlet = vrsta_filma;\nconst = komedija;\nconst = akcija;\nconst = uvjet1;\nlet = min_ocjena_filma;\ntrajanje_filma = uvjet1  >=90  &&  <=180;\nmin_ocjena_filma = imdb_ocjena >=7.5;\nvrsta_filma = komedija || akcija;\n\n\n\n"
        },
        {
            "js_code": "[NOT_SOLVED]"
        },
        {
            "js_code": "[NOT_SOLVED]"
        }
    ]
}
```

### Evaluation

- Task 1: 0.5
- Task 2: 0
- Task 3: 1
- Task 4: 0
- Task 5: 0

- Total Points: 1.5
- Feedback: Zadatak 1: Nedostaje ispravna inicijalizacija varijable 'vlaga' i ispis u konzolu, ali pokušaj je vidljiv. Zadatak 2: Nije riješen. Zadatak 3: Postoji pokušaj definiranja varijabli i logike, ali kod nije potpun ni sintaktički ispravan. Zadatak 4: Nije riješen. Zadatak 5: Nije riješen.
- Cost for this evaluation: $0.02

## aandrijan@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date();\nlet vlaga = 0.5;\nlet mjesec = datum_danas.getMonth();\nlet vlaga_postotak = 0.5 * 100;\n\nconsole.log(`Mjesec je: ${++mjesec}, a vlaga je: ${vlaga_postotak} %.`)\n\n\n\n\n"
        },
        {
            "js_code": "const PI = 3.14159;\nlet radijus = 5;\nlet visina = 10;\nlet volumen = PI * radijus ** 2 * visina;\nlet povrsina = 2 * PI * radijus * visina + 2 * PI * radijus ** 2;\n\nconsole.log(`Volumen cilindra je: ${volumen} cm3, a povr\u0161ina iznosi ${povrsina} cm2.`);\n\nlet volumenMilimetri = volumen * 100;\nlet povrsinaMilimetri = povrsina * 10;\n\nconsole.log(`Volumen cilindra je: ${volumenMilimetri} mm3, a povr\u0161ina iznosi ${povrsinaMilimetri} mm2.`);\n"
        },
        {
            "js_code": "\n\nlet filmMinTrajanje = 90;\nlet filmMaxTrajanje = 180;\nlet filmTrajanjeOstvareno = 100;\n\nlet filmMinOcjena = 7.5;\nlet filmOcjenaOstvareno = 8.0;\n\nlet filmZanr1 = \"Komedija\";\nlet filmZanr2 = \"Akcija\";\nlet filmOdabir = \"Komedija\";\n\n\nlet filmJezik = \"Engleski\";\nlet filmJezikOdabir = \"Engleski\"\n\nlet cilj1= (filmTrajanjeOstvareno >= filmMinTrajanje) && (filmTrajanjeOstvareno <= filmMaxTrajanje);\nlet cilj2 = (filmOcjenaOstvareno >= filmMinOcjena);\nlet cilj3 = (filmOdabir === filmZanr1) || (filmOdabir === filmZanr2);\nlet cilj4 = (filmJezikOdabir === filmJezik);\n\nlet film_odabran = cilj1 && cilj2 && cilj3 && cilj4;\n\nconsole.log(film_odabran)"
        },
        {
            "js_code": "let a = 5;\r\nlet b = 3;\r\nb =b + a; // Izmijenite izraz\r\na =a - b; // Izmijenite izraz\r\nb =b + 10 + a; // Izmijenite izraz\r\na =a * (b + 1); // Izmijenite izraz\r\nconsole.log(a); // -48\r\nconsole.log(b); // 16\r\n"
        },
        {
            "js_code": "let string1 = \"Ovo je moja prva re\u010denica\";\nlet string2 = \"Ovo je moja druga re\u010denica\";\n\nlet duljinaString1 = string1.length;\nlet duljinaString2 = string2.length;\n\n"
        }
    ]
}
```

### Evaluation

- Task 1: 1.5
- Task 2: 2
- Task 3: 3
- Task 4: 2
- Task 5: 0

- Total Points: 8.5
- Feedback: Zadatak 1: Ispravno koristite Date objekt i getMonth funkciju, ali pretvorba vlage u postotak nije dinamički povezana s varijablom vlage. Zadatak 2: Dobro ste izračunali volumen i površinu, ali konverzija u milimetre nije točna. Zadatak 3: Uspješno ste implementirali logičke operatore i operatore usporedbe za odabir filma. Zadatak 4: Uspješno ste izmijenili izraze bez korištenja zabranjenih operatora. Zadatak 5: Niste dovršili zadatak, nedostaje izračun i ispis rezultata eksponencijalne operacije.
- Cost for this evaluation: $0.03

## dmihaljev@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas=new Date(11.3)\nlet vlaga=0.5\n"
        },
        {
            "js_code": "const PI=3.14159\nlet radijus=1.5\nlet visina=5.1 \nlet ispis=\"Volumen cilindra je: \" + PI*radijus*radijus*visina + \"cm3, a povrsina iznosi \" + (2*PI*radijus*visina+2*PI*radijus*radijus) + \"cm2.\"\nconsole.log(ispis)\n"
        },
        {
            "js_code": "[NOT_SOLVED]"
        },
        {
            "js_code": "let a = 5\nlet b = 3\nb = b+a \na = a-b\nb = b+10+a\nb = b+1\na = a*(b)\nconsole.log(a)\nconsole.log(b)"
        },
        {
            "js_code": "let prva=\"prva\"\nlet druga=\"druga\"\n"
        }
    ]
}
```

### Evaluation

- Task 1: 1
- Task 2: 1.5
- Task 3: 0
- Task 4: 1.5
- Task 5: 0.5

- Total Points: 4.5
- Feedback: Zadatak 1: Nedostaje pretvorba vlage u postotke i ispis trenutnog mjeseca s pravilnim indeksom. Zadatak 2: Ispis je točan, ali nedostaje pretvorba u kvadratne milimetre. Zadatak 3: Zadatak nije riješen. Zadatak 4: Izmjene su uglavnom točne, ali postoji greška u logici koja ne daje točan rezultat kao originalni kod. Zadatak 5: Nedostaje logika za usporedbu duljina riječi i izvođenje eksponencijalne operacije.
- Cost for this evaluation: $0.02

## aburic1@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date();\nlet vlaga = 0.59;\nlet mjesec = datum_danas.getMonth() + 1;\n\nvlaga *= 100;\n\nconsole.log(`Mjesec je ${mjesec}., a vlaga je: ${vlaga}%.`);"
        },
        {
            "js_code": "let PI = 3.14159;\nlet radijus = 5;\nlet visina = 2;\n\nconsole.log(`Volumen cilindra je: ${PI * (radijus ** 2) * visina} cm3, a povr\u0161ina iznosi ${2 * PI * radijus * (visina + radijus)} cm2.`)"
        },
        {
            "js_code": "let trajanje_filma = 153;\nlet ocjena_filma = 6.8;\nlet komedija = true;\nlet akcijski = false;\nlet film_na_engleskome = true;\n\nlet min_ocjena_filma = 7.5;\nlet min_trajanje = 90;\nlet max_trajanje = 180;\n\nlet uvjet1 = trajanje_filma >= min_trajanje && trajanje_filma <= max_trajanje;\nlet uvjet2 = ocjena_filma >= min_ocjena_filma;\nlet uvjet3 = komedija || akcijski;\n\nlet film_odabran = uvjet1 && uvjet2 && uvjet3 && film_na_engleskome;"
        },
        {
            "js_code": "let a = 5;\nlet b = 3;\n\nb = b + a;\na = a - b;\nb = b + 10 + a;\nb = b + 1;\na = a * b;\n\nconsole.log(a);\nconsole.log(b);"
        },
        {
            "js_code": "let rijec1 = \"Rije\u010d\";\nlet rijec2 = \"Kreativno\";\n\nlet kraca = rijec1.length > rijec2.length ? rijec2.length : rijec1.length;\nlet dulja = rijec1.length + rijec2.length - kraca;\n\nconsole.log(kraca ** dulja);"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 2
- Task 3: 2.5
- Task 4: 1.5
- Task 5: 0.5

- Total Points: 8.5
- Feedback: Zadatak 1: Sve je ispravno riješeno, dobar rad. Zadatak 2: Ispravno rješenje, dobro korištenje matematičkih operacija i interpolacije stringova. Zadatak 3: Logika je uglavnom dobra, ali ocjena filma ne zadovoljava uvjet, stoga je rezultat malo previsok. Zadatak 4: Izmijenjeni izrazi ne vraćaju točno iste rezultate zbog greške u logici s inkrementom. Zadatak 5: Pokušaj je vidljiv, ali korištena logika za određivanje duljine riječi nije ispravna, rezultat operacije nije točan.
- Cost for this evaluation: $0.03

## mgalavic@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date();\nlet vlaga = 0.5;\nlet mjesec = datum_danas.getMonth();\n\nconsole.log(\"Mjece je: ${mjesec}, )\nconsole.log(datum_danas);\n\n"
        },
        {
            "js_code": "const PI = 3.141;\nlet radijus; \nlet visina;\n\nlet volumen = PI * (radijus) **2 * visina;\nlet povrsina = 2 * PI * radijus * visina + 2*PI * (radijus) **2;\nconsole.log('Volument cilindra je: ${volumen}, a povrsina iznosi: ${povrsina}cm2.');"
        },
        {
            "js_code": "var film_odabran;\nvar min_ocjena_filma = 2;\nvar ocjena_filma;\nvar ocjena_zadovoljena;\nvar trajanje = 100;\nvar film = \"akcija\";\nvar jezik = \"engleski\";\nvar film_odabran = (trajanje >= 90 && trajanje <= 180) && (min_ocjena_filma = 7.5) && (film = \"akcija\") && (jezik =\"engleski\");\nconsole.log(film_odabran);"
        },
        {
            "js_code": "let a = 5;\nlet b = 3;\nb = b + a;\na = a - b;\nb = 10 + a + b;\na = 1+b * a;\nconsole.log(a);\nconsole.log(b);"
        },
        {
            "js_code": "[NOT_SOLVED]"
        }
    ]
}
```

### Evaluation

- Task 1: 1
- Task 2: 1.5
- Task 3: 1
- Task 4: 1.5
- Task 5: 0

- Total Points: 5
- Feedback: Zadatak 1: Nedostaje ispravna interpolacija stringova i pretvorba vlage u postotke. Zadatak 2: Konstanta PI ima netočnu vrijednost, a interpolacija stringova nije ispravno implementirana. Zadatak 3: Korištenje operatora dodjele umjesto usporedbe rezultira uvijek istinitim izrazima, što nije logično. Zadatak 4: Izmijenjeni izrazi ne vraćaju točne vrijednosti za a i b varijable. Zadatak 5: Zadatak nije riješen.
- Cost for this evaluation: $0.02

## icacic@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "\r\n// script.js\r\nlet datum_danas;\r\nnew Date(datum_danas)\r\nlet vlaga = 1;\r\nfunction showMessage() {\r\nconsole.log(\"Hello World!\");\r\n}"
        },
        {
            "js_code": "[NOT_SOLVED]"
        },
        {
            "js_code": "let film_odabran;\r\nlet ciljaniBrojStranica = 200;\r\n\r\nlet uvjet1;\r\nuvjet1 <= 180;\r\nuvjet1 => 90;\r\nlet uvjet2;\r\nuvjet2 => 7.5;\r\nlet uvjet3;\r\n"
        },
        {
            "js_code": "[NOT_SOLVED]"
        },
        {
            "js_code": "const x = Number.MAX_SAFE_INTEGER + 1;\r\nconst y = Number.MAX_SAFE_INTEGER + 2;\r\n\r\nconsole.log(Number.MAX_SAFE_INTEGER);"
        }
    ]
}
```

### Evaluation

- Task 1: 0.5
- Task 2: 0
- Task 3: 0.5
- Task 4: 0

- Total Points: 1
- Feedback: Zadatak 1: Pokušaj je vidljiv, ali korištenje new Date() nije ispravno implementirano, a vlaga nije pretvorena u postotak. Zadatak 2: Nije riješeno. Zadatak 3: Pokušaj je napravljen, ali logika i sintaksa nisu ispravno primijenjeni. Zadatak 4: Nije riješeno. Zadatak 5: Korištenje Number.MAX_SAFE_INTEGER nije relevantno za zadatak.
- Cost for this evaluation: $0.02

## kbazina@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas\nlet vlaga\ndatum_danas = new Date()\nvlaga = 0.5\nlet mjesec = datum_danas.getMonth()\nvlaga=vlaga*100\nconsole.log(`MJesec je: ${mjesec+1}. a vlaga je: ${vlaga}%`)"
        },
        {
            "js_code": "const PI = 3.14159\nlet radijus = 2 \nlet visina = 2 \nlet viina = 3 \nconsole.log(`Volumen cilindra je: ${PI*(radijus**2)*visina} cm3 a povrsina iznosi ${2*PI*radijus*visina + (2*PI*(radijus**2))} cm2`)\nconsole.log(`Volumen cilindra je: ${(PI*(radijus**2)*visina)*1000} mm3 a povrsina iznosi ${(2*PI*radijus*visina + (2*PI*(radijus**2)))*100} mm2`)"
        },
        {
            "js_code": "let film_odabran\nlet min_ocjena_filma, ocjena_filma, ocjena_zadovoljena\nlet min_trajanje, max_trajanje, trajanje, trajanje_zadovoljeno\nlet zanr, znar_ciljani, zanr_zadovoljen\nlet jezik, jezik_ciljani, jezik_zadovoljen\nzanr_ciljani=[\"komedija\", \"akcija\"]\nzanr=\"akcija\"\nocjena_filma=5\nmin_ocjena_filma=7.5\n\nocjena_zadovoljena=(ocjena_filma>=7.5)\ntrajanje_zadovoljeno=(trajanje<max_trajanje && trajanje>min_trajanje)\nzanr_zadovoljen=(zanr_ciljani.includes(zanr))\njezik_zadovoljen=(jezik_ciljani===jezik)\nfilm_odabran=(ocjena_zadovoljena&&trajanje_zadovoljeno&&zanr_zadovoljen&&jezik_zadovoljen)\n"
        },
        {
            "js_code": "let a = 5\nlet b =3 \n//b+=a \nb=b+a\n//a-=b \na=a-b\n//b+=10 + a \nb=b+(10+a)\na=a*(b=b+1)\nconsole.log(a)\nconsole.log(b)\n"
        },
        {
            "js_code": "let string1 = \"karlo\"\nlet string2 = \"bazina\"\nif(string1.length>string2.length){\n  console.log(`${string1.length**string2.length}`)\n}\nelse{\n  console.log(`${string2.length**string1.length}`)\n}"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 1.5
- Task 3: 2
- Task 4: 2
- Task 5: 1

- Total Points: 8.5
- Feedback: Zadatak 1: Odlično, sve je ispravno implementirano. Zadatak 2: Postoji greška u imenovanju varijable ('viina'), ali logika i izračuni su uglavnom točni. Zadatak 3: Niste inicijalizirali sve potrebne varijable za usporedbu, što utječe na ispravnost koda. Zadatak 4: Ispravno ste izmijenili izraze bez korištenja zabranjenih operatora, dobro. Zadatak 5: Uspješno ste implementirali logiku za usporedbu duljina stringova i izračun eksponencijalne operacije.
- Cost for this evaluation: $0.03

## tmikasino@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas=new Date();\nlet vlaga=0.7;\nconsole.log(datum_danas);\n\nlet mjesec= datum_danas.getMonth() + 1;\nvlaga=vlaga*100;\nconsole.log(mjesec);\n\nconsole.log(`Mjesec je: ${mjesec}., a vlaga je: ${vlaga}%.`)\n"
        },
        {
            "js_code": "const PI=3.14159;\nlet radijus=6;\nlet visina=4;\nconsole.log(`Volumen cilindra je: ${PI*radijus**2*visina} cm3, a povr\u0161ina iznosi ${2*PI*visina*radijus+PI*2*radijus**2} cm2.`)\nconsole.log(`Volumen cilindra je: ${PI*radijus**2*visina} cm3, a povr\u0161ina iznosi ${(2*PI*visina*radijus+PI*2*radijus**2)*100} mm2.`)\n"
        },
        {
            "js_code": "\nlet trajanje_filma=120;\nlet trajanje_filma_cilj= trajanje_filma>=90 && trajanje_filma<=180;\n\nlet ocjena_filma=9;\nlet ocjena_filma_cilj= ocjena_filma>= 7.5;\n\nlet zanr_filma=\"komedija\";\nlet zanr_filma_cilj =\"komedija\" || \"akcijski\";\n\nlet jezik_filma=\"eng\";\nlet jezik_filma_cilj=\"eng\";\n\n\nlet film_odabran= trajanje_filma_cilj && ocjena_filma_cilj && (zanr_filma_cilj=== zanr_filma) && (jezik_filma_cilj===jezik_filma);\nconsole.log(film_odabran);\n"
        },
        {
            "js_code": "let a = 5;\r\nlet b = 3;\r\nb += a; // Izmijenite izraz\r\na -= b; // Izmijenite izraz\r\nb += 10 + a; // Izmijenite izraz\r\na *= ++b; // Izmijenite izraz\r\nconsole.log(a); // -48\r\nconsole.log(b); // 16"
        },
        {
            "js_code": "let rijec1=\"tomas\";\nlet rijec2=\"lenovo\";\n\nlet duljina1=rijec1.length;\nlet duljina2=rijec2.length;\n\nlet rezultat;\n\nif duljina1>duljina2  rezultat=duljina1**duljina2;\n\nconsole.log()"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 1.5
- Task 3: 1
- Task 4: 0
- Task 5: 0.5

- Total Points: 5
- Feedback: Zadatak 1: Odlično, sve je ispravno implementirano. Zadatak 2: Dobro, ali konverzija u mm2 nije ispravno izračunata. Zadatak 3: Postoji greška u logici za žanr filma, trebali ste koristiti operator || za usporedbu vrijednosti varijable sa dva moguća žanra. Zadatak 4: Zadatak nije riješen prema uputama, nisu korištene alternative za +=, -=, *=, /= operatore. Zadatak 5: Postoji pokušaj, ali sintaksa if naredbe nije ispravna i nedostaje ispis rezultata.
- Cost for this evaluation: $0.03

## mcekada1@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date()\nlet vlaga = [0,1]\n\nlet mjesec = datum_danas.getMonth()\n\nlet postotak_vlaga =  1 * 10\n\nconsole.log(`Mjesec je:${mjesec}.,a vlaga je: ${postotak_vlaga}%`)\n\n"
        },
        {
            "js_code": "const PI= 3.14159\nlet radijus = 4 \nlet visina = 8 \n\nlet volumen = PI*radijus**2 * visina\nlet povrsina = 2* PI * radijus * visina + 2*PI * radijus**2 \n\nconsole.log(`Volumen silindra je:${volumen}cm3,a povrsina iznosi ${povrsina}cm2`)\n\nlet volumen_mm2 = volumen * 1000\nlet povrsina_mm2 = povrsina * 100\n\nconsole.log(`Volumen silindra je:${volumen_mm2}cm3,a povrsina iznosi ${povrsina_mm2}cm2`)"
        },
        {
            "js_code": "let cilj_vrijeme_trajanja = [90,180]\nlet trajanje_filma = 95\n\nlet cilj_ocjena = 7.5 \nlet ocjena = 9\n\nlet cilj_kategorija1 = \"komedija\"\nlet cilj_kategorija2 = \"akcijski\"\nlet kategorija = \"komedija\"\n\nlet cilj_jezik = \"engleski\"\nlet jezik = \"engleski\"\n\nlet film_vrijeme_trajanja =trajanje_filma>= 90 && trajanje_filma <= 180\nlet film_ocjena = ocjena>=cilj_ocjena\nlet film_kategorija = kategorija ==  cilj_kategorija1 ||  kategorija ==  cilj_kategorija2\nlet film_jezik = jezik == cilj_jezik\n\nfilm_odabran = film_vrijeme_trajanja &&  film_ocjena && film_kategorija && film_jezik\n\nconsole.log(film_odabran)"
        },
        {
            "js_code": "let a = 5;\nlet b = 3;\nb = b + a;\na = a - b ;\nb = b + 10+ a ;\na = a * (++b);\nconsole.log(a); \nconsole.log(b); "
        },
        {
            "js_code": "let prva_rijec = \"ime\"\nlet druga_rijec = \"prezime\"\nlet duljina_prva_rijec = prva_rijec.length \nlet duljina_druga_rijec = druga_rijec.length\n\nconsole.log(`${duljina_druga_rijec > duljina_prva_rijec}`)\nconsole.log(`${duljina_druga_rijec ** duljina_prva_rijec}`)\n\n\n"
        }
    ]
}
```

### Evaluation

- Task 1: 1
- Task 2: 1.5
- Task 3: 2.5
- Task 4: 1
- Task 5: 0.5

- Total Points: 6.5
- Feedback: Zadatak 1: Nedostaje pretvorba vlage u postotak na ispravan način. Zadatak 2: Ispis za mm2 je netočan, trebalo je koristiti mm3 za volumen. Zadatak 3: Dobro riješeno, ali pripazite na čitljivost koda. Zadatak 4: Izmijenjeni izrazi ne vraćaju točne vrijednosti kao originalni kod. Zadatak 5: Niste koristili eksponencijalnu operaciju za ispis rezultata.
- Cost for this evaluation: $0.03

## flukes@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date(\"11.03.2023\")\nlet vlaga = 1\nlet mjesec = datum_danas\n\nconsole.log(datum_danas)"
        },
        {
            "js_code": "[NOT_SOLVED]"
        },
        {
            "js_code": "\nlet minOcjenaFilma\nlet OcjenaFilma\nlet ocjena\nlet zanr\nlet jezik"
        },
        {
            "js_code": "[NOT_SOLVED]"
        },
        {
            "js_code": "let prvaRijec = \"rijec\"\nlet drugaRijec = \"rjecica\"\n\n\nif (prvaRijec.lenght > drugaRijec .lenght){\n  let result = Math.pow (prvarijec.lenght, drugaRijec)\n  console.log(\"\")\n}\n\n"
        }
    ]
}
```

### Evaluation

- Task 1: 0.5
- Task 2: 0
- Task 3: 0.5
- Task 4: 0
- Task 5: 0

- Total Points: 1
- Feedback: Zadatak 1: Pokušaj je napravljen, ali nedostaje ispravno korištenje getMonth() funkcije i pretvorba vlage u postotak. Zadatak 2: Nije riješen. Zadatak 3: Napravljen je početni pokušaj definiranja varijabli, ali nedostaje logika i ispis. Zadatak 4: Nije riješen. Zadatak 5: Pokušaj je napravljen, ali postoje greške u sintaksi i logici, te je korištena pogrešna metoda za dobivanje duljine riječi ('lenght' umjesto 'length').
- Cost for this evaluation: $0.02

## mcekada@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date()\nlet vlaga = [0,1]\n\nlet mjesec = datum_danas.getMonth()\n\nlet postotak_vlage = 1 * 100\n\nconsole.log(`Mjesec je: ${mjesec}.,a vlaga je: ${postotak_vlage}%`)"
        },
        {
            "js_code": "const PI =  3.14159;\nlet radijus = 4\nlet visina = 8\n\nlet volumen = PI * radijus**2 * visina\nlet povrsina = 2*PI*radijus*visina + 2*PI*radijus**2\n\nconsole.log(`Volumen cilindra je:${volumen}cm3,a povrsina iznosi \u02d8${povrsina}cm2`)\n\nlet volumen_mm = volumen * 1000\nlet povrsina_mm = povrsina*100\n\nconsole.log(`Volumen cilindra je:${volumen_mm}mm2,a povrsina iznosi \u02d8${povrsina_mm}mm2`)"
        },
        {
            "js_code": "let cilj_trajanje_filma = [90,180]\nlet trajanje_filma = 100\n\nlet cilj_ocijena = 7.5\nlet ocijena = 8  \n\nlet cilj_film_kategorija= \"Komedija\"\nlet kategorija = `komedija`\nlet cilj_film_kategorija2= `akcijski`\n\n\nlet cilj_jezik = `engleski`\nlet jezik = `engleski`\n\nlet konacno_trajanje = trajanje_filma >= 90 && trajanje_filma <= 180\nlet konacna_ocijena = ocijena >= cilj_ocijena\nlet konacna_kategorija = kategorija == cilj_film_kategorija || kategorija == cilj_film_kategorija2\nlet konacan_jezik = jezik == cilj_jezik\n\nlet film_odabran = konacno_trajanje && konacna_ocijena && konacna_kategorija && konacan_jezik\n\nconsole.log(film_odabran)"
        },
        {
            "js_code": "let a = 5;\nlet b = 3;\nb = b + a\na = a - b  \nb = b + 10 + a  \na = a * (++b)\nconsole.log(a)\nconsole.log(b)\n\n"
        },
        {
            "js_code": "\nlet prva_rijec = `Monika`\nlet druga_rijec = `cekada`\nconst prva_rijec_duljina = prva_rijec.lenght\nconst druga_rijec_duljina = druga_rijec.lenght\n\n\nconsole.log(`prva i druga rijec imaju ${prva_rijec_duljina} i ${druga_rijec_duljina}`)\n\nconsole.log(`imaju istu duljinu: &{prva_rijec_duljina == druga_rijec_duljina }`)"
        }
    ]
}
```

### Evaluation

- Task 1: 1.5
- Task 2: 2
- Task 3: 3
- Task 4: 1.5
- Task 5: 0

- Total Points: 8
- Feedback: Zadatak 1: Ispravno koristite Date objekt i getMonth(), ali pretvorba vlage u postotak nije dinamički povezana s varijablom vlage. Zadatak 2: Dobro ste izračunali volumen i površinu cilindra te prilagodili jedinice, ali obratite pažnju na formatiranje ispisa. Zadatak 3: Uspješno ste implementirali logiku za odabir filma koristeći zadane uvjete. Zadatak 4: Ispravno ste izmijenili izraze bez korištenja zabranjenih operatora, ali postoji greška u logici koja ne utječe na konačni rezultat. Zadatak 5: Niste uspješno implementirali logiku za usporedbu duljina riječi i izračun eksponencijalne operacije, primijetite grešku u tipkanju ('lenght' umjesto 'length').
- Cost for this evaluation: $0.03

## mdamijanj@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas=new Date();\nlet vlaga=0.5;\nlet mjesec=datum_danas.getMonth();\nconsole.log(`Mjesec je: ${mjesec}., a vlaga je: ${vlaga}%.`);\n\n\n\n"
        },
        {
            "js_code": "const PI=3.14159;\nlet radijus=3;\nlet visina =5;\nconsole.log(`Volumen cilindra je: ${PI*radijus**2 * visina}cm3, a povr\u0161ina iznosi ${2 PI *radijus *visina + 2PI *radijus**2}`)\n"
        },
        {
            "js_code": "let trajanje_filma=110;\nconst cilj_trajanja_filma_zadovoljen=trajanje_filma>=90 && trajanje_filma<=180; \n\n\nlet film_ocijena=8;\nconst min_film_ocijena=7.5;\nconst film_ocijena_zadovoljen=film_ocijena>=min_film_ocijena\n\nlet film_zanr=\"komedija\";\nconst cilj_film_zanr_zadovoljen=film_zanr===\"komedija\" || film_zanr===\"akcija\";\n\nlet film_jezik=\"engleski\";\nconst cilj_film_jezik=\"engleski\";\nconst film_jezik_zadovoljen=film_jezik===cilj_film_jezik;\n\nconst film_odabran=cilj_trajanja_filma_zadovoljen && film_ocijena_zadovoljen && cilj_film_zanr_zadovoljen && film_jezik_zadovoljen;"
        },
        {
            "js_code": "let a = 5;\r\nlet b = 3;\r\nb=b+a;\r\na=a-b;\r\nb=b+10+a;\r\na=a*(b+1);\r\nb=b+1\r\nconsole.log(a); \r\nconsole.log(b);"
        },
        {
            "js_code": "let a=\"Marko\";\nlet b=\"Dami\";\n\nlet duljina_ime=a.length;\n\n"
        }
    ]
}
```

### Evaluation

- Task 1: 1.5
- Task 2: 1
- Task 3: 3
- Task 4: 1.5
- Task 5: 0

- Total Points: 7
- Feedback: Zadatak 1: Nedostaje pretvorba vlage u postotak. Zadatak 2: Nedostaje množenje s 1000 za mm2 i sintaksna greška s operatorom množenja. Zadatak 3: Svi uvjeti su ispravno definirani i logika je točna. Zadatak 4: Izmjene su djelomično točne, ali krajnji rezultat nije ispravan zbog pogreške u logici. Zadatak 5: Nema rješenja za usporedbu duljina riječi i izvođenje eksponencijalne operacije.
- Cost for this evaluation: $0.03

## fmarecic@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date();\nconst vlaga = 0.43;\n\nlet mjesec = datum_danas.getMonth();\n\nconsole.log(`Mjesec je ${mjesec+1}, a vlaga je ${vlaga*100}%`)\n"
        },
        {
            "js_code": "const pi = 3.14159;\n\nlet radijus = 5;\nlet visina = 12;\n\nlet volumen = (pi*radijus**2*visina)\nlet povrsina = (2*pi*radijus*visina + 2*pi*radijus**2)\n\nconsole.log(volumen + \" cm3\")\nconsole.log(povrsina + \" cm2\")\n"
        },
        {
            "js_code": "let film_odabran;\n\nlet film_trajanje = 160;\nlet ocjena = 6.2;\nlet vrsta = \"komedija\";\nlet jezik = \"engleski\";\n\nlet trajanje_zeljeno = (film_trajanje >= 90 && film_trajanje <=180)\nlet ocjena_zadovoljena = (ocjena >= 7.5)\nlet vrsta_zeljeno = (vrsta == \"komedija\" || vrsta==\"akcijski\")\nlet jezik_zeljeno = (jezik == \"engleski\")\n\nfilm_odabran = (trajanje_zeljeno && ocjena_zadovoljena && vrsta_zeljeno && jezik_zeljeno)\n"
        },
        {
            "js_code": "let a = 5;\nlet b = 3;\n\nb = b+a;\na = a-b;\nb = b+10+a;\na = a*++b;\nconsole.log(a);\nconsole.log(b);\n"
        },
        {
            "js_code": "let rijec1, rijec2;\n\nrijec1 = \"nekarijec\"\nrijec2 = \"da\"\n\nlet b = rijec1.length;\nlet e = rijec2.length;\n\nconsole.log(b**e);\n"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 1.5
- Task 3: 2.5
- Task 4: 1
- Task 5: 1

- Total Points: 8
- Feedback: Zadatak 1: Odlično, sve je ispravno implementirano. Zadatak 2: Nedostaje ispis vrijednosti u kvadratnim milimetrima, ali osnovna logika je točna. Zadatak 3: Logika je uglavnom dobra, ali ocjena filma ne zadovoljava uvjet, stoga nije potpuno točno. Zadatak 4: Izmijenjeni izrazi nisu u potpunosti ispravni, posebno kod množenja. Zadatak 5: Dobar pristup, ali provjerite uvijek rubne slučajeve i kompleksnije primjere.
- Cost for this evaluation: $0.03

## ldizdarev@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas  = new Date ();\n\nlet vlaga = 0.9;\n\nlet mjesec = get Month (datum_danas);\n"
        },
        {
            "js_code": "const PI =3.14159;\nlet radijus = 5;\n\nlet visina = 2;\n\nlet volumen = PI*radijus*radijus*visina;\nlet povrsina = 2*PI*radijus*visina+2*PI*radijus*radijus;\n\nconsole.log(\"Volumen cilindra je:\");\nconsole.log (volumen) (\"cm3\")\n"
        },
        {
            "js_code": "let film_odabran;\n\n"
        },
        {
            "js_code": "let a = 5;\nlet b = 3;\nb =b + a; // Izmijenite izraz\na =a - b; // Izmijenite izraz\nb =b + 10 + a; // Izmijenite izraz\na = a * ++b; // Izmijenite izraz\nconsole.log(a); // -48\nconsole.log(b); // 16"
        },
        {
            "js_code": "[NOT_SOLVED]"
        }
    ]
}
```

### Evaluation

- Task 1: 0.5
- Task 2: 1.5
- Task 3: 0
- Task 4: 1.5
- Task 5: 0

- Total Points: 3.5
- Feedback: Zadatak 1: Pokušaj je dobar, ali postoji sintaksna greška u pozivu funkcije getMonth i pretvaranju vlage u postotak nije izvršeno. Zadatak 2: Izračuni su točni, ali ispis u konzolu nije pravilno formatiran. Zadatak 3: Nije riješen, potrebno je definirati logiku za odabir filma. Zadatak 4: Dobro je prilagođen kod bez korištenja zabranjenih operatora, ali postoji greška u logici koja ne dovodi do ispravnih konačnih vrijednosti. Zadatak 5: Zadatak nije riješen.
- Cost for this evaluation: $0.02

## bvujica@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "const datum_danas=new date()\nconst vlaga=0.5\nlet mjesec=datum_danas.getMonth();\n\n\n"
        },
        {
            "js_code": "const PI=3.14159;\nradijus=20;\nvisina=10\nconsole.log(\"volumen cilindra je: \"+(PI*(radijus**2)*visina)+\" cm3, a povr\u0161ina iznosi \"+(2*PI*radijus*visina+2*PI*radijus**2));\nconsole.log(\"`volumen cilindra je:`\")"
        },
        {
            "js_code": "film_odbrana;\nfilm_traje=95;\ntrajamje_filma=film_traje>=90 && film_traje<=180;\n\nocjena=8;\nmin_ocjena_filma=ocjena>=7.5;\n"
        },
        {
            "js_code": "[NOT_SOLVED]"
        },
        {
            "js_code": "[NOT_SOLVED]"
        }
    ]
}
```

### Evaluation

- Task 1: 1.5
- Task 2: 1.5
- Task 3: 1
- Task 4: 0
- Task 5: 0

- Total Points: 4
- Feedback: Zadatak 1: Nedostaje pretvorba vlage u postotke i ispis u konzolu. Zadatak 2: Ispis u kvadratnim milimetrima nije realiziran. Zadatak 3: Nedostaje definicija varijable 'film_odabran' i provjera svih uvjeta. Zadatak 4 i 5: Nisu riješeni.
- Cost for this evaluation: $0.02



# Total Cost for Evaluating PJS_ex1v2_RntC3e
Total cost for running evaluations: $0.63