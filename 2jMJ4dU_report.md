# Exam Tasks

**1.** Deklarirajte varijable `datum_danas` i `vlaga`. U varijablu `datum_danas` spremite današnji datum koristeći `new Date()` objekt, a u varijablu `vlaga` spremite proizvoljnu vrijednost vlage kao decimalni broj od `0` do max `1`. Dodajte novu varijablu `mjesec` u koju ćete pohraniti trenutni mjesec koristeći `getMonth()` funkciju nad varijablom `datum_danas`, pripazite da `getMonth()` vraća mjesec kao broj od 0 do 11. Sintaksa: `varijabla.getMonth()`. Dodajte novu varijablu `vlaga_postotak` u koju ćete pohraniti vrijednost vlage u postotku.

- Ispišite u konzolu rečenicu: `"Mjesec je: __., a vlaga je: __%."` koristeći interpolaciju stringova (template literals) sintaksu.
- _Primjer ispisa_: `"Mjesec je: 3., a vlaga je: 40%."`

(**MAX_TASK_POINTS** = 2)

**2.** Definirajte konstantu `PI` i dodijelite joj vrijednost broja π (3.14159). Dodajte novu varijablu `radijus` u koju ćete pohraniti proizvoljnu vrijednost radijusa kugle u metrima. Ispišite u konzolu jednu rečenicu: `"Oplošje kugle iznosi: ____ m2 odnosno ____ dm2, dok obujam kugle odrezane na pola iznosi __ m3."`. Oplošje i obujam zamijenite s varijablama za svaku izračunatu vrijednost za traženu mjernu jedinicu (m = metri, dm = decimetri) koristeći interpolaciju stringova (template literals).

- Dodajte varijablu za svaku izračunatu vrijednost oplošja i obujma (`oplošje_m2`, `oplošje_dm2`, `obujam_m3` i `pola_obujma_m3`).

- Oplošje: `4πr²`
- Obujam (Volumen): `4/3πr³`

(**MAX_TASK_POINTS = 2**)

**3.** Odlučili ste provjeriti jeste li ostvarili ciljeve na kraju akademske godine. Koristeći logičke operatore i operatore usporedbe, definirajte varijablu `cilj_ispunjen` koja govori jeste li ispunili cilj na kraju akademske godine (ili niste). Varijabla neka ovisi o podciljevima koje ste si zadali: Da bi krajnji cilj bio ispunjen, moram:

- proći matematiku
- završiti s prosjekom ocjena iznad 4.0.
- napraviti 2 do 4 projekta.
- dobiti Scrimba certifikat iz Pythona ili iz JavaScripta.

Za svaki od danih izraza deklarirajte varijable za ostvarenu vrijednost i ciljanu vrijednost, te boolean varijablu koja će sadržavati rezultat ostvarenja. Na primjer, za drugu izjavu varijable mogu biti: `prosjek_min`, `prosjek`, `podcilj_prosjek_zadovoljen`. Kroz varijable definirajte odgovarajuće logičke izraze/izraze usporedbe za svaki podcilj.

- Na kraju ispišite rezultat u obliku `cilj_ispunjen = podcilj1 && podcilj2 && podcilj3 && podcilj4`, gdje `cilj_ispunjen` na kraju mora biti `true` ili `false`.

(**MAX_TASK_POINTS** = 3)

**4.** Deklarirajte 3 varijable koje sadrže cjelobrojne vrijednosti. Za svaku varijablu ispišite izjavu u konzolu: `Broj __ je paran - ${parnost_broja}` gdje `__`zamijenite s brojem, a `parnost_broja` s rezultatom provjere parnosti tog broja.

- Primjer: `Broj 50 je paran - true`

(**MAX_TASK_POINTS** = 1)

**5.** Raspišite sljedeće izraze **bez korištenja** `+=`, `-=`, `*=`, `/=`, `++` ili `--` operatora. Ako smatrate da je potrebno, možete i dodati liniju koda više. (**MAX_TASK_POINTS** = 2)

```javascript
let c = 10;
let d = -1;
c -= d; // Izmijenite izraz
c += d; // Izmijenite izraz
d += 10 + c; // Izmijenite izraz
c *= ++d; // Izmijenite izraz
console.log(c); // 200
console.log(d); // 20
// Izmijenjeni izrazi moraju u konačnici vratiti isti rezultat c i d varijabli kao i originalni izrazi.
// Originalne izraze možete zakomentirati, a ispod njih napisati alternativne izraze (bez korištenja navedenih operatora).
```

## kkrezic@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date ()\nlet vlaga = 0.74\nlet mjesec = datum_danas.getMonth () + 1\n \nlet vlaga_postotak = vlaga*100\n\nconsole.log (`Mjesec je: ${mjesec}., a vlaga je: ${vlaga_postotak} %.`)\n\n"
        },
        {
            "js_code": "const PI = 3.14159\nlet radijus = 3.4 \n\nconsole.log (\"Oplo\u0161je kugle iznosi:\")"
        },
        {
            "js_code": "let cilj_ispunjen;\n\nlet matematika_prolaz = true\nlet matematika_prolaz_cilj = true\n\nlet podcilj1= matematika_prolaz \n\nlet mat_prosjek = 4.23\nlet mat_prosjek_min = 4.0\n\nlet podcilj2 = mat_prosjek > mat_prosjek_min\n\n\nlet broj_projekata = 3\nlet broj_projekata_cilj_min = 2 \nlet broj_projekata_cilj_max = 4\n\nlet podcilj3 = broj_projekata >= broj_projekata_cilj_min && broj_projekata <= broj_projekata_cilj_max\n\nlet certifikat_Python= true\nlet certifikat_JavaScript= false\n\nlet podcilj4 = certifikat_Python || certifikat_JavaScript\n\ncilj_ispunjen = podcilj1 && podcilj2 && podcilj3 && podcilj4\n\nconsole.log (cilj_ispunjen)\n"
        },
        {
            "js_code": "let jedan = 4 \nlet dva = 7\nlet tri = 9\n\nlet parnost_broja = jedan >=0 && jedan%2==0\nlet parnost_broja_2 = dva >=0 && dva%2==0\nlet parnost_broja_3 = tri >=0 && tri%3==0\n\nconsole.log (`Broj jedan je paran - ${parnost_broja}`)\nconsole.log (`Broj dva je paran - ${parnost_broja_2}`)\nconsole.log (`Broj tri je paran - ${parnost_broja_3}`) "
        },
        {
            "js_code": "[NOT_SOLVED]"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 0.5
- Task 3: 3
- Task 4: 0.5

- Total Points: 6
- Feedback: Zadatak 1 je odlično riješen, svi elementi su na mjestu i ispravno implementirani. Zadatak 2 nedostaje izračun i ispis oplošja i obujma, dana je samo deklaracija konstante PI. Zadatak 3 je potpuno ispravno riješen, logika i implementacija su u skladu s uputama. Zadatak 4 ima grešku u provjeri parnosti za treći broj, trebalo je koristiti %2 umjesto %3 za provjeru parnosti. Zadatak 5 nije riješen.
- Cost for this evaluation: $0.03

## mjambrek@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "[NOT_SOLVED]"
        },
        {
            "js_code": "console.log=\n\nlet (radijus) = \"Oplo\u0161je kugle iznosi:__ m2\" ;\n"
        },
        {
            "js_code": "\nlet cilj_ispunjen =(Prolaz na pismenom &&; (zavr\u0161iti s prosjekom iznad)>=4.0;&& napraviti 2 do 4 projekta\n&& dobiti Scrimab certifikat za Python ili Java );"
        },
        {
            "js_code": "console.log\nBroj je paran-$"
        },
        {
            "js_code": "[NOT_SOLVED]"
        }
    ]
}
```

### Evaluation

- Task 1: 0
- Task 2: 0.5
- Task 3: 1
- Task 4: 0
- Task 5: 0

- Total Points: 1.5
- Feedback: Zadatak 1 nije riješen. Zadatak 2 pokazuje pokušaj, ali nedostaje ispravna sintaksa i logika za izračun, dodijeljeno je 0.5 bodova. Zadatak 3 ima pokušaj logike, ali je sintaksa netočna i nedostaje definicija varijabli, dodijeljen je 1 bod. Zadatak 4 i 5 nisu riješeni. Potrebno je više pažnje posvetiti sintaksi i logici programiranja.
- Cost for this evaluation: $0.02

## rkrebel@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date();\nlet vlaga = 0.3;\nlet mjesec = datum_danas.getMonth() + 1\nlet vlaga_postotak = vlaga * 100;\nconsole.log(\"Mjesec je: \" + mjesec + \"., a vlaga je: \"+  vlaga_postotak + \"%.\")\n\n\n"
        },
        {
            "js_code": "PI = 3.14159\nradijus = 2\nOplo\u0161je = 4 * PI * radijus*radijus\nobujam = 4/3*PI*radijus*radijus*radijus\nconsole.log(\"Oplo\u0161je kugle iznosi:\" + Oplo\u0161je + \"m2, dok obujam kugle odrezane na pola iznosi: \"+ obujam +  \"m3\")\n"
        },
        {
            "js_code": "//?"
        },
        {
            "js_code": "function jeParan(broj){\n  if (broj % 2 === 0){\n    return \" je paran - true\"\n  }\n  else {\n    return \" nije paran - false\"\n  }\n}\n\nlet broj1 = 23\nlet broj2 =34\nlet broj3 = 45\n\nx = jeParan(broj1)\nconsole.log(\"Broj \" + broj1 + x )\n\nx = jeParan(broj2)\nconsole.log(\"Broj \" + broj2 + x )\n\nx = jeParan(broj3)\nconsole.log(\"Broj \" + broj3 + x )\n\n"
        },
        {
            "js_code": "let c = 10;\r\nlet d = -1;\r\nc - d; // Izmijenite izraz\r\nc + d; // Izmijenite izraz\r\nd += 10 + c; // Izmijenite izraz\r\nc *= ++d; // Izmijenite izraz\r\nconsole.log(c); // 200\r\nconsole.log(d); // 20"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 1.5
- Task 3: 0
- Task 4: 0.5
- Task 5: 0

- Total Points: 4
- Feedback: Zadatak 1: Odlično, sve je ispravno implementirano. Zadatak 2: Nedostaje deklaracija konstante za PI i preciznost u ispisu, ali logika je uglavnom dobra. Zadatak 3: Nije riješen. Zadatak 4: Rješenje koristi funkciju umjesto direktnog pristupa, što nije najefikasnije, ali radi. Zadatak 5: Izrazi nisu ispravno izmijenjeni, nedostaje implementacija bez korištenja zabranjenih operatora.
- Cost for this evaluation: $0.03

## ibursic@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas =\"13.03.2023.\"\nlet vlaga = (0, 1)\nlet datum = new Date()\nlet mjesec = datum.getMonth()+1\nlet vlaga_postotak = vlaga\n\nconsole.log(`Mjesec je: ${mjesec}, a vlaga je ${vlaga_postotak}%.`)"
        },
        {
            "js_code": "const PI = 3.14159\nlet radijus = 10\n\nconsole.log(`Oplo\u0161je kugle iznosi`)"
        },
        {
            "js_code": "let cilj_ispunjen\n\n//1.uvjet\nlet proci_mat = true\n\n//2.uvjet\nlet prosjek = 4.5\nlet prosjek_cilj = 5\nlet cilj_prosjek = prosjek >= prosjek_cilj\n\n//3.uvjet\nco projekt 2 \nlet projekt_cilj 4 \n"
        },
        {
            "js_code": "let a = 20 \nlet b = 40 \nlet c = 70\n\nlet parnost_brojaT = true\nlet parnost_brojaF = false\n\nconsole.log(`Broj ${a} je paran-${parnost_brojaT}`)\nconsole.log(`Broj ${b} je paran-${parnost_brojaT}`)\nconsole.log(`Broj ${c} je paran-${parnost_brojaF}`)"
        },
        {
            "js_code": "let c = 10;\r\nlet d = -1;\r\n//c -= d;\r\n//c += d; \r\n//d += 10 + c; \r\n//c *= ++d; \r\n\r\nconsole.log(c); // 200\r\nconsole.log(d); // 2"
        }
    ]
}
```

### Evaluation

- Task 1: 0.5
- Task 2: 0.5
- Task 3: 0
- Task 4: 0.5
- Task 5: 0

- Total Points: 1.5
- Feedback: Zadatak 1: Pokušaj je dobar, ali korištenje `(0, 1)` za `vlaga` nije valjano i nedostaje pravilno računanje postotka vlage. Zadatak 2: Definirana je konstanta PI, ali izračuni i ispis nisu provedeni. Zadatak 3: Nedostaje logika i sintaksa je netočna, potrebno je više truda. Zadatak 4: Iako je ideja o parnosti prisutna, korištenje statičkih boolean vrijednosti nije pravilan pristup. Zadatak 5: Nije provedena izmjena izraza kako je zatraženo, nedostaje implementacija.
- Cost for this evaluation: $0.03

## lhusak@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date()\nlet vlaga = 0.4\n\nlet mjesec = datum_danas.getMonth()\nlet vlaga_postotak = parseFloat(vlaga*100) + \"%\"\nconsole.log(\"Mjesec je: \" + mjesec + \". a vlaga je: \"+ vlaga_postotak  )"
        },
        {
            "js_code": "const PI=parseFloat(3.14159)\nlet radius = 3\nlet oplosje_m2=4*PI*(radius*radius)\nlet oplosje_dm2=oplosje_m2*100\nlet obujam_m3=4/(3*PI)*(radius*radius)\nconsole.log(\"Oplo\u0161je kugle iznosi: \"+oplosje_m2+\" m2 odnosno \"+oplosje_dm2+\" dm2, dok obujam kugle odrezane na pola iznosi \"+obujam_m3/2+\" m3.\")"
        },
        {
            "js_code": "let cilj_ispunjen\nlet matematika = true\nlet prosjek = 4.5\nlet projekt = 3\nlet skrimba_js = false\nlet skrimba_py = true\nlet tekst\n\nif(matematika==true && prosjek>4 && (projekt>=2 || projekt<=4) && (skrimba_js==true || skrimba_py == true)){\n cilj_ispunjen=true\n}\nif (cilj_ispunjen){\n  tekst = \"je prosao\"\n}else{\n  tekst=\"nije prosao\"\n}\nconsole.log(\"Student \"+ tekst)\n"
        },
        {
            "js_code": "let a=2\nif(a%2==0){\n  parnost_broja=true\n}else{\n  parnost_broja=false\n}\nconsole.log(\"Broj \"+a+\" je paran - \"+`${parnost_broja}`)\n\nlet b=3\nif(b%2==0){\n  parnost_broja=true\n}else{\n  parnost_broja=false\n}\nconsole.log(\"Broj \"+b+\" je paran - \"+`${parnost_broja}`)\n\nlet c=4\nif(c%2==0){\n  parnost_broja=true\n}else{\n  parnost_broja=false\n}\nconsole.log(\"Broj \"+c+\" je paran - \"+`${parnost_broja}`)\n"
        },
        {
            "js_code": "let c = 10;\r\nlet d = -1;\r\nc = c-d; // Izmijenite izraz\r\nc = c+d; // Izmijenite izraz\r\nd = d+(10 + c); // Izmijenite izraz\r\nc = c*(d=d+1); // Izmijenite izraz\r\n\r\nconsole.log(c); // 200\r\nconsole.log(d); // 20"
        }
    ]
}
```

### Evaluation

- Task 1: 1.5
- Task 2: 1
- Task 3: 2.5
- Task 4: 1
- Task 5: 2

- Total Points: 8
- Feedback: Zadatak 1: Korištenje + umjesto template literals za interpolaciju stringova smanjuje bodove. Zadatak 2: Formula za obujam je netočno primijenjena, a i postoji greška u izračunu obujma. Zadatak 3: Logika je uglavnom ispravna, ali provjera broja projekata koristi || umjesto && što može dovesti do logičke greške. Zadatak 4: Ispravno provjerava parnost, ali koristi nepotrebnu interpolaciju stringova. Zadatak 5: Ispravno modificirani izrazi bez korištenja zabranjenih operatora.
- Cost for this evaluation: $0.03

## mkuric@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date();\nlet vlaga = 0.5;\nlet mjesec = datum_danas.getMonth();\nlet vlaga_postotak = vlaga*100;\nconsole.log(`\"Mjesec je: ${mjesec}., a vlaga je: ${vlaga_postotak}%\"` )"
        },
        {
            "js_code": "const PI = 3.14159;\nlet radijus = 5;\noplo\u0161je_m2 = 4*PI*radijus**2;\noplo\u0161je_dm2=(4*PI*radijus**2)*100\nobujam_m3 = 4/3*PI*radijus**3\npola_obujma_m3 = obujam_m3/2\nconsole.log(`\"Oplo\u0161je kugle iznosi: ${oplo\u0161je_m2} m2 odnosno ${oplo\u0161je_dm2} dm2, dok obujam kugle odrezane na pola iznosi ${pola_obujma_m3} m3.\"`)"
        },
        {
            "js_code": "let cilj_ispunjen;\n\nlet proci_matematiku = true;\nlet prosjek = 4.50;\nlet prosjek_cilj = prosjek>4.0;\nlet projekt = 2;\nlet projekt_cilj = projekt <=4 && projekt >=2;\nlet scrimba_py = true;\nlet scrimba_js = true;\nlet scrimba_cilj = s"
        },
        {
            "js_code": "let a = 20\nlet b = 51\nlet c = 54\nconsole.log(`Broj ${a} je paran- ${a%2==0}`)\nconsole.log(`Broj ${b} je paran- ${b%2==0}`)\nconsole.log(`Broj ${c} je paran- ${c%2==0}`)"
        },
        {
            "js_code": "let c = 10;\r\nlet d = -1;\r\nc = c-d; \r\nc = d+c;\r\nd = (10 + c)+d;\r\nc = ((d+1)*c); \r\nd = d+1;\r\nconsole.log(c); // 200\r\nconsole.log(d); // 20"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 2
- Task 3: 1.5
- Task 4: 1
- Task 5: 2

- Total Points: 8.5
- Feedback: Zadatak 1: Odlično, sve je ispravno implementirano. Zadatak 2: Također odlično, svi potrebni izračuni su točni. Zadatak 3: Nedostaje završetak logičkog izraza za Scrimba certifikat, ali ostatak je dobro postavljen. Zadatak 4: Ispravno, ali obratite pažnju na formatiranje ispisa. Zadatak 5: Dobra alternativa originalnim operatorima, iako je bilo potrebno malo više pažnje na detalje kako bi se izbjegle greške.
- Cost for this evaluation: $0.03

## mlegovic1@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date()\nlet vlaga = 0.5 \nlet mjesec = datum_danas.getMonth() + 1\nlet vlaga_postotak = 40 \nconsole.log (`Mjesec je: ${mjesec}., a vlaga je:${vlaga_postotak}%.`)"
        },
        {
            "js_code": "const PI = 3.14159\nlet radijus =  \n"
        },
        {
            "js_code": "\nlet podcilj_1 = true\nlet podcilj_2 = true\nlet podcilj_3 = false\nlet podcilj_4 = false\nlet cilj_ispunjen"
        },
        {
            "js_code": "let a = 2 \nlet b = 6\nlet c = 4 \nlet parnost_broja = %2\nconsole.log(`Broj ${a} je paran ${parnost_broja}  `) \n"
        },
        {
            "js_code": "[NOT_SOLVED]"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 0.5
- Task 3: 1.5
- Task 4: 0
- Task 5: 0

- Total Points: 4
- Feedback: Zadatak 1: Odlično, sve je ispravno implementirano. Zadatak 2: Nedostaje implementacija formule za oplošje i obujam, samo je definirana konstanta PI. Zadatak 3: Niste definirali kako se izračunavaju podciljevi niti kako se dolazi do konačnog rezultata, ali postoji osnovna struktura. Zadatak 4: Niste ispravno implementirali provjeru parnosti broja, nedostaje logika za izračun. Zadatak 5: Zadatak nije riješen.
- Cost for this evaluation: $0.02

## sloncaric@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date()\nlet vlaga = 0.5\nlet mjesec = datum_danas.getMonth() + 1\nlet vlaga_postotak = vlaga * 100\n\nconsole.log(`Mjesec je: ${mjesec}., a vlaga je: ${vlaga_postotak}%.`)"
        },
        {
            "js_code": "const PI = 3.14159\nlet radijus = 2\noplo\u0161je = 4*PI*(2**2)\nobujam = 4/3*PI*(2**2)\nlet oplosje_m2 = oplo\u0161je\nlet oplosje_dm2 = 4*PI*(20**2)\nlet obujam_m3 = obujam\nlet pola_obujma_m3 = obujam / 2\n console.log(`Opslo\u0161je kugle iznosi: ${oplosje_m2} m2 odnosno ${oplosje_dm2} dm2, dok obujam kugle odrezane na pola iznosi ${pola_obujma_m3} m3. `)"
        },
        {
            "js_code": "let prolaz_matematika = true\nlet zavrsni_prosjek = 5.0\nlet projekti = 3\nlet certifikat_Python = true\nlet certifikat_JavaScript = true\n\nlet cilj1 = prolaz_matematika\nlet cilj2 = zavrsni_prosjek >= 4.0\nlet cilj3 = 2<=projekti>=4\nlet cilj4 = certifikat_Python || certifikat_JavaScript\n\nlet cilj_ispunjen = cilj1 && cilj2 && cilj3 && cilj4\nconsole.log(cilj_ispunjen)"
        },
        {
            "js_code": "let broj1 = 5\nlet broj2 = 2\nlet broj3 = 10\n\nlet parnost_broj1 = 5 % 2 == 0\nlet parnost_broj2 = 2 % 2 == 0\nlet parnost_broj3 = 10 % 2 == 0 \n\nconsole.log(`Broj ${broj1} je paran - ${parnost_broj1}`)\nconsole.log(`Broj ${broj2} je paran - ${parnost_broj2}`)\nconsole.log(`Broj ${broj3} je paran - ${parnost_broj3}`)"
        },
        {
            "js_code": "let c = 10\nlet d = -1\nc = d - d\nc = d + d\nd = 10 + c -d\nc = \nconsole.log(c)"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 1.5
- Task 3: 2.5
- Task 4: 1
- Task 5: 0

- Total Points: 7
- Feedback: Zadatak 1: Odlično, sve je ispravno implementirano. Zadatak 2: Postoji greška u izračunu oplošja i obujma, obratite pažnju na formule. Zadatak 3: Logički izraz za provjeru broja projekata nije ispravno napisan, ali ostatak je dobro. Zadatak 4: Ispravno ste implementirali provjeru parnosti. Zadatak 5: Niste uspješno riješili zadatak, nedostaje implementacija bez korištenja zabranjenih operatora.
- Cost for this evaluation: $0.03

## rermacora@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date()\nlet vlaga = 0.5\nlet mjesec = datum_danas.getMonth()+1\nlet vlaga_postotak = vlaga * 100\n\nconsole.log(`Mjesec je: ${mjesec}, a vlaga je ${vlaga_postotak}%`)"
        },
        {
            "js_code": "const PI = 3.14159\nlet radijus = 1\nlet oplo\u0161je_m2 = 4*PI*(radijus**2)\nlet oplo\u0161je_dm2 = oplo\u0161je_m2 * 100\nlet obujam_m3 = 4/3*PI*(radijus**3)\n\nconsole.log(`Oplo\u0161je kugle iznosi: ${oplo\u0161je_m2} m2 odnosno ${oplo\u0161je_dm2} dm2, dok obujam kugle \nodrezane na pola iznosi ${obujam_m3} m3.`)"
        },
        {
            "js_code": "let cilj_ispunjen = false\nlet prolaz_mat = false\nlet ocjena_vise_4 = false\nlet broj_projekata = 2\nlet certifikat = false\n\nif (prolaz_mat == true && ocjena_vise_4 == true && broj_projekata >= 2 && certifikat == true){\n  cilj_ispunjen = true\n  console.log(cilj_ispunjen)\n}else{\n  console.log(cilj_ispunjen)\n}"
        },
        {
            "js_code": "let broj_1 = 10\nlet broj_2 = 30\nlet broj_3 = 25\n\nconsole.log(`Broj ${broj_1} je paran - ${broj_1%2==0}`)\nconsole.log(`Broj ${broj_2} je paran - ${broj_2%2==0}`)\nconsole.log(`Broj ${broj_3} je paran - ${broj_3%2==0}`)"
        },
        {
            "js_code": "let c = 10;\r\nlet d = -1;\r\nc =c-d; \r\nc =c+d; \r\nd = d+(10 + c); \r\nc =c* (++d); \r\nconsole.log(c); // 200\r\nconsole.log(d); // 20"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 1.5
- Task 3: 2
- Task 4: 1
- Task 5: 1.5

- Total Points: 8
- Feedback: Zadatak 1: Odlično, sve je ispravno implementirano. Zadatak 2: Nedostaje pola obujma kugle, ali ostatak je dobro izračunat. Zadatak 3: Logika je djelomično točna, ali nedostaje dinamička provjera podciljeva. Zadatak 4: Ispravno provjeravate parnost brojeva. Zadatak 5: Izmijenjeni izrazi su točni, ali korištenje `++d` nije u skladu s uputama da se ne koriste `++` ili `--` operatori.
- Cost for this evaluation: $0.03

## nzizoski@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = \nlet vlaga = 3\nlet mjesec "
        },
        {
            "js_code": "const pi = 3.15159 ;\nlet radijus = 3 \nconsole.log(\"Oplo\u0161ke kugle iznosi :\")"
        },
        {
            "js_code": "[NOT_SOLVED]"
        },
        {
            "js_code": "let a = 3\nlet b = 5\nlet c = 6 \nlet parnost?broja = a / 2 ==  \nconsole.log(` Broj &{a+b} je paran n ${2 * a + b}.`);"
        },
        {
            "js_code": "let c = 10;\r\nlet d = -1;\r\nlet c = c - d; // Izmijenite izraz\r\nlet  = c+ d; // Izmijenite izraz\r\nlet f = 10 + c; // Izmijenite izraz\r\nlet t = c * d+1; // Izmijenite izraz\r\nconsole.log(a+b+f+t); // 200\r\nconsole.log();"
        }
    ]
}
```

### Evaluation

- Task 1: 0.5
- Task 2: 1
- Task 3: 0
- Task 4: 0.5
- Task 5: 0.5

- Total Points: 2.5
- Feedback: Zadatak 1: Nedostaje inicijalizacija za 'datum_danas' i pogrešno korištenje varijable 'vlaga'. Zadatak 2: Konstanta PI je netočno napisana, a izračuni i ispis nisu provedeni. Zadatak 3: Zadatak nije riješen. Zadatak 4: Pogrešno korištenje sintakse i logike za provjeru parnosti. Zadatak 5: Pogrešno korištenje varijabli i aritmetičkih operacija, nedostaje ispravan ispis.
- Cost for this evaluation: $0.03

## bmedica@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date()\nlet vlaga = 0.60\nlet mjesec = datum_danas.getMonth()\nlet vlaga_postotak = 60\nconsole.log( `Mjesec je ${++(mjesec)}., a vlaga je: ${vlaga_postotak}%. `)\n"
        },
        {
            "js_code": "const PI = 3.14159\nlet radijus = 2;\nlet oplo\u0161je_m2 = 4*PI*(radijus**2)\nlet oplo\u0161je_dm2 = oplo\u0161je_m2*100\nlet obujam_m3 = ((4/3)*PI*(radijus**3))/2\nconsole.log(`Oplo\u0161je kugle iznosi: ${oplo\u0161je_m2}m2, odnosno ${oplo\u0161je_dm2}dm2, dok obujam kugle odrezane na pola iznosi ${obujam_m3}m3`)"
        },
        {
            "js_code": "let cilj_ispunjen;\nlet proci_matematiku=true;\nlet prosjek;\nlet prosjek_min=4.0\nlet prosjek_zadovoljen= prosjek>prosjek_min\nlet projekt=true;\nlet certifikat=true\n cilj_ispunjen = proci_matematiku && prosjek_zadovoljen&& projekt"
        },
        {
            "js_code": "let broj1 = 3;\nlet parnost_broja1 = broj1%2 ==0;\n\nconsole.log(`Broj ${broj1} je paran - ${parnost_broja1}`)\nlet broj2 = 44;\nlet parnost_broja2 = broj2%2 ==0;\n\nconsole.log(`Broj ${broj2} je paran - ${parnost_broja2}`)\n\nlet broj3 = 50;\nlet parnost_broja3 = broj3%2 ==0;\n\nconsole.log(`Broj ${broj3} je paran - ${parnost_broja3}`)"
        },
        {
            "js_code": "[NOT_SOLVED]"
        }
    ]
}
```

### Evaluation

- Task 1: 1.5
- Task 2: 2
- Task 3: 1.5
- Task 4: 1
- Task 5: 0

- Total Points: 6
- Feedback: Zadatak 1: Ispravno koristite datum i vlaga varijable, ali korištenje ++(mjesec) nije potrebno za ispis, oduzima se pola boda. Zadatak 2: Dobro ste izračunali oplošje i obujam, puni bodovi. Zadatak 3: Niste definirali sve potrebne varijable za podciljeve, a logika za provjeru broja projekata i certifikata nedostaje, pola bodova. Zadatak 4: Ispravno provjeravate parnost brojeva, puni bodovi. Zadatak 5: Zadatak nije riješen, nula bodova.
- Cost for this evaluation: $0.03

## lcatela@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas\nlet vlaga\ndatum_danas = new Date()\nvlaga = 0.256\nlet mjesec\nmjesec = mjesec.getMonth(datum_danas)\nconsole.log(\"Mjesec je: .\",mjesec , \",a vlaga je: \", vlaga)\n"
        },
        {
            "js_code": "[NOT_SOLVED]"
        },
        {
            "js_code": "[NOT_SOLVED]"
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

- Task 1: 1
- Task 2: 0
- Task 3: 0
- Task 4: 0
- Task 5: 0

- Total Points: 1
- Feedback: Za zadatak 1, korištenje getMonth() funkcije nije ispravno implementirano, a i ispis u konzolu ne koristi interpolaciju stringova kako je zatraženo. Za ostale zadatke, rješenja nisu pružena.
- Cost for this evaluation: $0.02

## jcrljenko@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date();\nlet vlaga = 0.4;\nlet mjesec = datum_danas.getMonth();\nlet vlaga_postotak = vlaga * 100;\n\nconsole.log(`Mjesec je ${mjesec+1}, a vlaga je ${vlaga_postotak}%.`)"
        },
        {
            "js_code": "const PI = 3.14159\nlet r = 5\nlet oplosje_m2 = 4 * PI * r;\nlet oplosje_dm2 = oplosje_m2 * 100\nlet obujam_m3 = (4/3) * PI * (r ** 3)\nlet pola_obujma_m3 = obujam_m3 / 2;\nconsole.log(`Oplo\u0161je kugle iznosi: ${oplosje_m2} m2 odnosno ${oplosje_dm2} dm2, dok obujam kugle odrezane na pola iznosi ${pola_obujma_m3} m3`)"
        },
        {
            "js_code": "let cilj_ispunjen\nlet matematika_ocjena = 5; let matematika_prolaz = 2; mat_p_zad = matematika_ocjena > matematika_prolaz ? true : false\nlet p_oc = 4.5; let p_oc_zad = p_oc > 4.0 ? true : false\nlet br_proj; let br_proj_zad = br_proj >= 2 && br_proj <= 4 ? true : false\nlet s_cert = false\n\ncilj_ispunjen = mat_p_zad && p_oc_zad && br_proj_zad && s_cert\n\nconsole.log(`Cilj ispunjen: ${cilj_ispunjen}`)"
        },
        {
            "js_code": "function parnost_broja(num){\n  return num % 2 == 0;\n}\n\nlet a = 3;\nlet b = 546;\nlet c = 42;\n\n\nconsole.log(`\\tBroj ${a} je paran - ${parnost_broja(a)}`);\nconsole.log(`\\tBroj ${b} je paran - ${parnost_broja(b)}`);\nconsole.log(`\\tBroj ${c} je paran - ${parnost_broja(c)}`);"
        },
        {
            "js_code": "let c = 10;\nlet d = -1;\nc = c - d;\nc = c + d;\nd = d + 10 + c\nc = c * ( ++d)\nconsole.log(c)\nconsole.log(d)"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 2
- Task 3: 1.5
- Task 4: 1
- Task 5: 2

- Total Points: 8.5
- Feedback: Zadatak 1: Sve je ispravno riješeno, dobar rad. Zadatak 2: Također ispravno, dobro korištenje matematičkih formula i interpolacije stringova. Zadatak 3: Nedostaje inicijalizacija varijable 'br_proj', što utječe na ispravnost logike, ali dobar pokušaj. Zadatak 4: Ispravna implementacija funkcije za provjeru parnosti, dobro. Zadatak 5: Uspješno izbjegavanje zabranjenih operatora, dobro rješenje.
- Cost for this evaluation: $0.03

## aspahic@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date()\nlet vlaga = 0.22;\nlet mjesec = datum_danas.getMonth() + 1\nlet vlaga_postotak = \"0.22%\"\n\nconsole.log(`Mjesec je: ${mjesec}. a vlaga je ${vlaga_postotak}`)\n"
        },
        {
            "js_code": "const PI = 3.14159\nlet radijus = 2\nlet oplosje_m2 = (4 * PI * radijus) ** 2   \nlet oplosje_dm2 = (4 * PI * radijus) ** 2 / 1000\nlet obujam_m3 = 4 / (3 * PI) * radijus ** 3\nlet pola_obujma_m3 = obujam_m3 / 2\n\nconsole.log(`Oplosje kugle iznosi: ${oplosje_m2} m2 odnosno ${oplosje_dm2} dm2, \ndok obujam kugle odrezane na pola iznosi ${pola_obujma_m3} m3.`)"
        },
        {
            "js_code": "let cilj_ispunjen \n\nlet cilj1 = \"proci\"\nlet ostvaren_cilj1 = \"da\" \nlet rezultat_cilj1 = true\n\nlet cilj2 = 4.2\nlet ostvaren_cilj2 = \"ne\" \nlet rezultat_cilj2 = false\n\nlet cilj3 = \"4 projekta\"\nlet ostvaren_cilj3 = \"da\" \nlet rezultat_cilj3 = true\n\nlet cilj4 = \"Dobiti certifikat\"\nlet ostvaren_cilj4 = \"da\" \nlet rezultat_cilj4 = true\n\ncilj_ispunjen = rezultat_cilj1 && rezultat_cilj2 &&  rezultat_cilj3 && rezultat_cilj4\n\nconsole.log(cilj_ispunjen)\n\n\n"
        },
        {
            "js_code": "let a = 5\nlet b = 10\nlet c = 15\n\nconsole.log(`Broj ${a} je paran - ${5 % 2 == 0}`)\nconsole.log(`Broj ${b} je paran - ${10 % 2 == 0}`)\nconsole.log(`Broj ${c} je paran - ${15 % 2 == 0}`)\n"
        },
        {
            "js_code": "let c = 10\nlet d = -1\n\nc = 10 - (-1)\nc = 10 + (-1)\nd = 10 + 10\nc = 10 * ++ \n\n"
        }
    ]
}
```

### Evaluation

- Task 1: 1.5
- Task 2: 1
- Task 3: 2
- Task 4: 1

- Total Points: 5.5
- Feedback: Zadatak 1: Vrijednost vlage nije ispravno pretvorena u postotak, trebalo je pomnožiti s 100. Zadatak 2: Pogrešno izračunato oplošje i pretvorba u dm2, formula za oplošje nije ispravno primijenjena. Zadatak 3: Dobar pokušaj, ali varijable za ciljeve nisu korištene na način kako je zamišljeno, trebalo je koristiti logičke operatore za usporedbu stvarnih i ciljanih vrijednosti. Zadatak 4: Ispravno provjerena parnost brojeva. Zadatak 5: Nisu ispravno izmijenjeni izrazi, nedostaje logika za zadnje dvije operacije.
- Cost for this evaluation: $0.03

## kbertosa@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date()\nlet vlaga = 0.5\nlet mjesec = datum_danas.getMonth()+1\nlet vlaga_postotak = vlaga * 100\n\nconsole.log(`Mjesec je ${mjesec} ,a vlaga je ${vlaga_postotak}% `)"
        },
        {
            "js_code": "const pi = 3.14159\nlet radijus = 5\nlet oplo\u0161je_m2 = 4*pi*radijus*radijus\nlet oplo\u0161je_dm2 = oplo\u0161je_m2/10\nlet obujam_m3 = 4/(3*pi*radijus*radijus)\nlet pola_obujma_m3 = obujam_m3/2\n\nconsole.log(`Oplo\u0161je kugle iznosi :${oplo\u0161je_m2}   m2 odnosno ${oplo\u0161je_dm2}   dm2, dok obujam kugle odrezane na pola iznosi ${pola_obujma_m3}  m3`)\n\n"
        },
        {
            "js_code": "let cilj_ispunjen"
        },
        {
            "js_code": "let varijabla_1 = 1\nlet varijabla_2 = 2\nlet varijabla_3 = 3\nlet parnost_broja_1 = varijabla_1 % 2 == 0 \nlet parnost_broja_2 = varijabla_2 % 2 == 0 \nlet parnost_broja_3 = varijabla_3 % 2 == 0\n\nconsole.log(`Broj ${varijabla_1} je paran - ${parnost_broja_1} `)\nconsole.log(`Broj ${varijabla_2} je paran - ${parnost_broja_2}`)\nconsole.log(`Broj ${varijabla_3} je paran - ${parnost_broja_3}`)"
        },
        {
            "js_code": "let c = 10;\nlet d= -1;\nc=c-d\nc=c+d\nd=d+10\nc=c*(d+1)\n\nconsole.log(c);\nconsole.log(d)"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 1.5
- Task 3: 0
- Task 4: 1
- Task 5: 2

- Total Points: 6.5
- Feedback: Zadatak 1: Odlično, sve je ispravno implementirano. Zadatak 2: Postoji greška u izračunu obujma, trebalo je koristiti množenje umjesto dijeljenja. Zadatak 3: Niste implementirali logiku za provjeru ciljeva. Zadatak 4: Ispravno ste implementirali provjeru parnosti brojeva. Zadatak 5: Uspješno ste izbjegli korištenje zabranjenih operatora i postigli traženi rezultat.
- Cost for this evaluation: $0.03

## smaljic@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date ();\nlet vlaga = 0.5;\nlet mjesec = getMonth(datum_danas);\nconsole.log(\"\")"
        },
        {
            "js_code": "const PI = 3.14159;\nlet radijus = 6;\nlet oplosje = (4 * PI * radijus) ** 2 ;\nlet oplosje_m2 = oplosje / 100;\nlet oplosje_dm2 = oplosje / 10;\nlet obujam = (4 / 3 * PI * radijus) ** 3;\nlet obujam_m3 = obujam / 100;\nlet pola_obujma_m3 = obujam_m3 / 2;\nlet rjesenje = 'Oplo\u0161je kugle iznosi ${oplosje_m2} m2 ondosno ${oplosje_dm2} dm2, dok obujam kugle odrezane na pola iznosi ${pola_obujma_m3N}';\nconsole.log(rjesenje);\n\n// na laptopu nisam mogla pronaci odgocarajuce nagnute navodnike, pa sam upotrijebila obicne"
        },
        {
            "js_code": "let proci_matematiku = true;\nlet prosjek = 5;\nlet napravljeni_projekti = 3;\nlet dobiveni_certifikat = true;\n\nlet cilj_ispunjen = proci_"
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
- Task 2: 1
- Task 3: 0.5
- Task 4: 0
- Task 5: 0

- Total Points: 2
- Feedback: Zadatak 1: Nedostaje ispravna upotreba metode getMonth() i interpolacija stringova. Zadatak 2: Formula za izračun oplošja i obujma nije ispravno primijenjena, a interpolacija stringova nije korištena kako treba. Zadatak 3: Nedostaje kompletan logički izraz za provjeru ispunjenja cilja. Zadaci 4 i 5 nisu riješeni.
- Cost for this evaluation: $0.03

## ssrdarevi@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date();\nlet vlaga = 0.3;\nlet mjesec = datum_danas.getMonth()+1;\nlet vlaga_postotak = vlaga*100;\n\nconsole.log(`Mjesec je: ${mjesec}. , a vlaga je: ${vlaga_postotak} %`);\n"
        },
        {
            "js_code": "const PI = 3.14159;\nlet radijus = 2;\nlet oplosje_m2 = 4*PI*(radijus**2);\nlet oplosje_dm2 = oplosje_m2*100;\nlet obujam_m3 = 4/(3*PI*(radijus**3));\nlet pola_obujma_m3 = obujam_m3/2;\n\nconsole.log(`Oplo\u0161je kugle iznosi: ${oplosje_m2} odnosno ${oplosje_dm2}, dok obujam kugle odrezane na pola iznosi ${pola_obujma_m3}`)"
        },
        {
            "js_code": "let cilj_ispunjen;\nlet mat = 1.7;\nlet matmin = 1.5;\nlet podcilj1 = mat>matmin;\nlet prosjek_min = 4.0;\nlet prosjek = 4.1;\nlet podcilj2 = prosjek>prosjek_min;\nlet projekti = 2;\nlet projektimin = 2;\nlet podcilj3 = projekti >= projektimin;\nlet cert1 = false;\nlet cert2 = true;\nlet podcilj4 = cert1 || cert2;\nlet cilj_ispunjen = podcilj1 && podiclj2 && pod;\n\nconsole.log(\"\")"
        },
        {
            "js_code": "let var1 = 5;\nlet var2 = 6;\nlet var3 = 7;\nlet parnost_broja = \n\nconsole.log(`Broj ${var1} je paran - ${}`)"
        },
        {
            "js_code": "let c = 10;\nlet d = -1;\nc = c-d;\nc = c+d;\nd = d+10+c;\nc = c*(d+1);\nd=d+1;\n\nconsole.log(c);\nconsole.log(d);"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 1.5
- Task 3: 1.5
- Task 4: 0.5
- Task 5: 2

- Total Points: 7.5
- Feedback: Zadatak 1: Odlično, sve je ispravno implementirano. Zadatak 2: Postoji greška u izračunu obujma, formula nije pravilno primijenjena. Zadatak 3: Logika je djelomično točna, ali postoji tipfeler u varijabli koja spaja podciljeve. Zadatak 4: Nedostaje logika za provjeru parnosti i ispis rezultata. Zadatak 5: Dobre alternativne metode, mada postoji manji problem s logikom inkrementa za varijablu d.
- Cost for this evaluation: $0.03

## ehajdarov@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas= new Date();\nlet vlaga=0 ;\n\nlet mjesec=datum_danas.getMonth();\n\nlet vlaga_postotak=\"35\";\n\nlet ispis=`Mjesec je: ${mjesec} , a vlaga je: ${vlaga_postotak}%`\nconsole.log(ispis)"
        },
        {
            "js_code": "const PI = 3.14159;\nlet r= 40;\nlet oplosje_m2=4*PI*r**2\nlet oplosje_dm2=oplosje_m2*100\nlet obujam_m3=4/3*PI*r**3\nlet pola_obujma_m3=obujam_m3/2\n\nlet ispis=`Oplo\u0161je kugle iznosi: ${oplosje_m2} m2 odnosno ${oplosje_dm2} dm2, dok obujam kugle odrezane na pola iznosi ${pola_obujma_m3} m3`\nconsole.log(ispis)"
        },
        {
            "js_code": "let cilj_ispunjen=(matematika4 && uspjeh && gotoviprojekti && uspjehscrimba)\nconsole.log(cilj_ispunjen)\nlet matematika=2\nlet proci_matematiku=4\nlet matematika4 = (proci_matematiku>=matematika)\n\nlet prosjek=4.0\nlet prosjekocjena=4.2\nlet uspjeh=prosjekocjena>=prosjek\n\nlet projekt=2\nlet viseprojekata=3\nlet gotoviprojekti=viseprojekata>=projekt\n\nlet Scrimba2=1\nlet osvojen_scrimba=1\nlet uspjehscrimba= osvojen_scrimba>=Scrimba2"
        },
        {
            "js_code": "let a = 1\nlet paran_a= a%2== false\nlet neparan_a = a%2== true\nlet b= 2\nlet c= 5\nlet ispis= `Broj ${a} je paran `\nconsole.log(ispis)"
        },
        {
            "js_code": "let c = 10;\r\nlet d = -1;\r\nc1=c-d\r\nc2=c+d\r\n"
        }
    ]
}
```

### Evaluation

- Task 1: 1.5
- Task 2: 2
- Task 3: 2.5
- Task 4: 0.5
- Task 5: 0.5

- Total Points: 7
- Feedback: Zadatak 1: Nedostaje pretvorba vlage u postotke, ali osnovna logika i ispis su točni. Zadatak 2: Točno rješenje, dobro korištenje matematičkih formula i interpolacije stringova. Zadatak 3: Logika je uglavnom dobra, ali definicija varijable 'cilj_ispunjen' trebala bi biti nakon definicija ostalih varijabli. Zadatak 4: Nedostaje provjera parnosti za sve brojeve i ispis rezultata provjere. Zadatak 5: Pokušaj je napravljen, ali izrazi nisu ispravno preformulirani da bi dali isti rezultat kao originalni kod.
- Cost for this evaluation: $0.03

## dcuric@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date();\nlet vlaga = 0.32;\nlet mjesec = datum_danas.getMonth();\nlet vlaga_postotak = vlaga * 100;\n\nconsole.log(`Mjesec je: ${mjesec + 1}., a vlaga je: ${vlaga_postotak}%.`);"
        },
        {
            "js_code": "const PI = 3.14159;\nlet radijus = 4;\n\nlet oplo\u0161je_m2 = 4 * PI * (radijus**2);\nlet oplo\u0161je_dm2 = 4 * PI * ( (radijus*10)**2 );\nlet obujam_m3 = ( 4 * PI * (radijus**3) ) / 3;\nlet pola_obujma_m3 = obujam_m3 / 2;\n\nconsole.log(`Oplo\u0161je kugle iznosi: ${oplo\u0161je_m2} m2, odnosno ${oplo\u0161je_dm2} dm2, dok obujam kugle odrezane na pola iznosi ${pola_obujma_m3} m3.`);"
        },
        {
            "js_code": "let matematika = true;\nlet prosjek = 4.3;\nlet projekt = 3;\nlet certifikat = true;\n\nlet podcilj_matematika = matematika;\nlet podcilj_ocjena = (prosjek >= 4);\nlet podcilj_projekt = (projekt >= 2 && projekt <= 4);\nlet podcilj_certifikat = certifikat;\n\ncilj_ispunjen = podcilj_matematika && podcilj_certifikat && podcilj_projekt && podcilj_ocjena;\n\nconsole.log(cilj_ispunjen)"
        },
        {
            "js_code": "let x = 5;\nlet y = 8;\nlet z = 9;\n\nfunction parnost_broja(broj){\n  return !(broj % 2);\n} \n\nconsole.log(`Broj ${x} je paran - ${parnost_broja(x)}`);\nconsole.log(`Broj ${y} je paran - ${parnost_broja(y)}`);\nconsole.log(`Broj ${z} je paran - ${parnost_broja(z)}`);"
        },
        {
            "js_code": "let c = 10;\nlet d = -1;\n\nc = c - d;\nc = c + d;\nd = d + 10 + c;\nd = d + 1;\nc = c * d;\n\nconsole.log(c);\nconsole.log(d);"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 2
- Task 3: 3
- Task 4: 1
- Task 5: 2

- Total Points: 10
- Feedback: Zadatak 1: Ispravno rješenje, dobro korištenje interpolacije stringova. Zadatak 2: Točno izračunate vrijednosti i ispravno korištenje matematičkih formula. Zadatak 3: Logički operatori i operatori usporedbe su ispravno korišteni za provjeru ciljeva. Zadatak 4: Funkcija za provjeru parnosti broja je ispravno implementirana i korištena. Zadatak 5: Uspješno izbjegavanje korištenja zabranjenih operatora i ispravno postignuti konačni rezultati.
- Cost for this evaluation: $0.03

## nbuzecan@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas=new Date()\nlet vlaga =\nlet mjesec=getMonth()"
        },
        {
            "js_code": "let PI=3.14159;\nlet radijus=\n\nconsole.log(\"Oplo\u0161je kugle iznosi: ____ m2 odnosno ____ dm2, dok obujam kugle odrezane na pola iznosi __ m3.\")"
        },
        {
            "js_code": "[NOT_SOLVED]"
        },
        {
            "js_code": "let broj1 = 45\nlet broj2 = 20\nlet broj3 = 10\nconsole.log(\"Broj\",50\"je)"
        },
        {
            "js_code": "let c = 10;\r\nlet d = -1;\r\nc = c-d;\r\nc =c+d;\r\nd = d+ 10 + c; \r\nd=d+1\r\nc =c * d; \r\nconsole.log(c);\r\nconsole.log(d); "
        }
    ]
}
```

### Evaluation

- Task 1: 0.5
- Task 2: 0.5
- Task 3: 0
- Task 4: 0.5
- Task 5: 2

- Total Points: 3.5
- Feedback: Zadatak 1: Nedostaje definicija vrijednosti za 'vlaga' i ispravno korištenje 'getMonth()' funkcije. Zadatak 2: Nedostaje definicija vrijednosti za 'radijus' i izračuni za oplošje i obujam. Zadatak 3: Zadatak nije riješen. Zadatak 4: Nedostaje ispravna sintaksa i logika za provjeru parnosti brojeva. Zadatak 5: Dobro riješeno, izrazi su ispravno modificirani da daju traženi rezultat.
- Cost for this evaluation: $0.02

## jgobo@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date()\nlet vlaga = 0.5\nlet mjesec = datum_danas.getMonth()\nlet vlaga_postotak = 50\n\nconsole.log(`Mjesec je: ${mjesec}, a vlaga je: ${vlaga_postotak}%.`)"
        },
        {
            "js_code": "const PI = 3.14159\nlet radijus = 2\nlet oplo\u0161je_m2 = 4 * PI * radijus**2\nlet oplo\u0161je_dm2 = oplo\u0161je_m2 * 100\nlet obujam_m3 = 4/3 * PI * radijus**3\nlet pola_obujma_m3 = obujam_m3/2\n\nconsole.log(`Oplo\u0161je kugle iznosi: ${oplo\u0161je_m2} m2 odnosno ${oplo\u0161je_dm2} dm2, dok obujam kugle odrezane na pola iznosi ${pola_obujma_m3} m3.`)"
        },
        {
            "js_code": "[NOT_SOLVED]"
        },
        {
            "js_code": "let br1 = 10\nlet br2 = 11\nlet br3 = 12\nlet parnost_broja = br1%2==0\nconsole.log(`Broj ${br1} je paran - ${parnost_broja}`)\nparnost_broja = br2%2==0\nconsole.log(`Broj ${br2} je paran - ${parnost_broja}`)\nparnost_broja = br3%2==0\nconsole.log(`Broj ${br3} je paran - ${parnost_broja}`)"
        },
        {
            "js_code": "let c = 10;\r\nlet d = -1;\r\nc -= d; // Izmijenite izraz\r\nc += d; // Izmijenite izraz\r\nd += 10 + c; // Izmijenite izraz\r\nc *= ++d; // Izmijenite izraz\r\nconsole.log(c); // 200\r\nconsole.log(d); // 20"
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
- Feedback: Zadatak 1: Dobro je, ali vrijednost vlage u postotcima trebala je biti izračunata iz dane decimalne vrijednosti. Zadatak 2: Točno i precizno, dobro obavljeno. Zadatak 3: Zadatak nije riješen. Zadatak 4: Ispravno provjeravate parnost brojeva, dobro. Zadatak 5: Zadatak nije modificiran kako je traženo, trebali ste izmijeniti dane izraze bez korištenja navedenih operatora.
- Cost for this evaluation: $0.03

## pvorih@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "\nlet datum_danas = new Date()\nlet vlaga = 0.8\n\nlet mjesec = datum_danas.getMonth()\nlet vlaga_postotak = vlaga * 100\n\nconsole.log(`Mjesec je ${mjesec+1}., a vlaga je ${vlaga_postotak}%`)\n"
        },
        {
            "js_code": "const PI = 3.14159\nlet radijus = 3\n\nlet oplo\u0161je_m2 = 4*PI*radijus**2\nlet oplo\u0161je_dm2 = (4*PI*radijus**2)*10\nlet obujam_m3 = 4/(3*PI*radijus**3)\nlet pola_obujma_m3 = obujam_m3/2\n\nconsole.log(`Oplo\u0161je kugle iznosi: ${oplo\u0161je_m2} odnosno ${oplo\u0161je_dm2}, dok obujam kugle odrezane na pola iznosi ${pola_obujma_m3} m3.`)"
        },
        {
            "js_code": "\n\nlet podcilj1Mat = true\n\n\nlet podcilj2Ocjena = 4.3\nlet ciljOcjena = podcilj2Ocjena >= 4.0\n\n\nlet podcilj3Projekti = 3\nlet ciljProjekti = podcilj3Projekti>=2\n\n\nlet podciljCertPython = true \nlet podciljCertJS = false\nlet ciljCertifikat = podciljCertJS || podciljCertPython\n\n\n\nlet cilj_ispunjen = podcilj1Mat && ciljOcjena && ciljProjekti && ciljCertifikat\nconsole.log(cilj_ispunjen)\n\n"
        },
        {
            "js_code": "let broj1 = 3\nlet broj2 = 4\nlet broj3 = 8\n\nlet parnost_broja1 = broj1%2==0\nlet parnost_broja2 = broj2%2==0\nlet parnost_broja3 = broj3%2==0\n//let parnost_broja1 = provjera_broja1\n\n\nconsole.log(`Broj ${broj1} je paran - ${parnost_broja1}`)\nconsole.log(`Broj ${broj2} je paran - ${parnost_broja2}`)\nconsole.log(`Broj ${broj3} je paran - ${parnost_broja3}`)"
        },
        {
            "js_code": "let c = 10;\r\nlet d = -1;\r\nc = c- d; // Izmijenite izraz\r\nc = c + d; // Izmijenite izraz\r\nd = d + 10 + c; // Izmijenite izraz\r\nd = d+1\r\nc = c * d; // Izmijenite izraz\r\nconsole.log(c); // 200\r\nconsole.log(d); // 20"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 1.5
- Task 3: 3
- Task 4: 1
- Task 5: 2

- Total Points: 9.5
- Feedback: Zadatak 1: Odlično, sve je ispravno implementirano. Zadatak 2: Postoji greška u izračunu obujma, trebalo je koristiti množenje umjesto dijeljenja. Zadatak 3: Sve je ispravno, dobro ste definirali logičke operatore i usporedbe. Zadatak 4: Ispravno ste implementirali provjeru parnosti brojeva. Zadatak 5: Uspješno ste izbjegli korištenje zabranjenih operatora i postigli tražene rezultate.
- Cost for this evaluation: $0.03

## msegon1@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date()\nlet vlaga = 0.4\nlet mjesec\nmjesec.getMonth()+1\n\nlet vlaga_postotak = vlaga * 100\n\nconsole.log(`Mjesec je: ${mjesec}, a vlaga je: ${vlaga_postotak}%`)\n"
        },
        {
            "js_code": "const PI = 3.14159\nlet radijus = 5\nlet oplo\u0161je = 4*PI * (radijus * radijus)\n\nlet oplo\u0161je_m2 = oplo\u0161je\nlet oplo\u0161je_dm2 = oplo\u0161je_m2 * 10\nlet obujam_m3 = 4/ 3*PI * (radijus*radijus)\nlet pola_obujma_m3 = obujam_m3 / 2\nconsole.log(`Oplo\u0161je kugle iznosi: ${oplo\u0161je_m2}m2 odnosno ${oplo\u0161je_dm2} dm2, dok obujam kugle odrezane na pola iznosi ${pola_obujma_m3}m3`)"
        },
        {
            "js_code": "let cilj_ispujen\n"
        },
        {
            "js_code": "let prva = 12\nlet druga = 20\nlet treca = 9\nlet paran = false\nif (prva % 2 === 0){\n  paran = true\n  console.log(`Broj ${prva} je paran - \u02d8${bool}`)\n}else{console.log(`Broj ${prva} je paran - \u02d8${bool}`)}\n\nparan = false\nif (druga % 2 === 0){\n  paran = true\n  console.log(`Broj ${druga} je paran - \u02d8${bool}`)\n}else{console.log(`Broj ${druga} je paran - \u02d8${bool}`)}\n\nparan = false\nif (treca % 2 === 0){\n  paran = true\n  console.log(`Broj ${treca} je paran - \u02d8${bool}`)\n  \n}else{console.log(`Broj ${treca} je paran - \u02d8${bool}`)}\n\n"
        },
        {
            "js_code": "let c = 10 \nlet d = -1\nc = c - d \nc = c + d \nd = d + 10 + c \nc = c * (++d)\nconsole.log(c)\nconsole.log(d)"
        }
    ]
}
```

### Evaluation

- Task 1: 1
- Task 2: 1.5
- Task 3: 0
- Task 4: 0.5
- Task 5: 2

- Total Points: 5
- Feedback: Zadatak 1: Nedostaje ispravno postavljanje vrijednosti za 'mjesec', trebalo je koristiti 'datum_danas.getMonth() + 1'. Zadatak 2: Pogrešno izračunat obujam, trebalo je koristiti kub radijusa za obujam, a ne kvadrat. Zadatak 3: Nije riješen, nedostaje logika i definiranje podciljeva. Zadatak 4: Pogreška u korištenju nepostojeće varijable 'bool' umjesto 'paran'. Zadatak 5: Ispravno riješen, dobro korištenje alternativnih operacija umjesto zabranjenih.
- Cost for this evaluation: $0.03

## mbarisa@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let datum_danas = new Date ()\nlet vlaga = 0.8\nlet mjesec  = datum_danas.getMonth() + 1\nlet vlaga_postotak = (vlaga / 1 )*100\nconsole.log(`Mjesec je ${mjesec}, a vlaga danas je ${vlaga_postotak}%. `)"
        },
        {
            "js_code": "const PI = 3.14159\nlet radijus = 5 \nlet radijus_dm  = 50\nlet oplo\u0161je_m2 = PI * radijus\nlet oplo\u0161je_dm2 = PI * radijus_dm\nlet obujam_m3 = 2*radijus*PI\nlet pola_obujma_m3 = obujam_m3/2\n\n\n//oplo\u0161je pi*r, obujam 2r*pi\n\n\nconsole.log(`Oplo\u0161je kugle iznosi: ${oplo\u0161je_m2} m2, odnosno ${oplo\u0161je_dm2} dm2, dok obujam kugle odrezane na pola iznosi ${pola_obujma_m3} m3.`)"
        },
        {
            "js_code": "let cilj_ispunjen = false\nlet mat = true\nlet prosjek = 4.1 \nlet prosjek_cilj = 4.1\nlet projekti = 3 \nlet projekti_cilj = 2 \nlet certifikat = true\ncilj_ispunjen = mat && prosjek >= prosjek_cilj && projekti >= projekti_cilj && certifikat\nconsole.log(cilj_ispunjen)"
        },
        {
            "js_code": "let broj = 50\nlet parnost = broj%2 == 0 \nconsole.log(`Broj ${broj} je paran - ${parnost}`)\n"
        },
        {
            "js_code": "let c = 10\nlet d = -1\nc = d+12 \nc = d+11 \nd = 10 +c \nc = d* 10\n\nconsole.log(c)\nconsole.log(d)"
        }
    ]
}
```

### Evaluation

- Task 1: 1.5
- Task 2: 0.5
- Task 3: 2.5
- Task 4: 1
- Task 5: 0

- Total Points: 5.5
- Feedback: Zadatak 1: Dobro je, ali postotak vlage nije formatiran kako je zatraženo. Zadatak 2: Formule za oplošje i obujam su netočne, i korištenje radijusa u dm nije ispravno implementirano. Zadatak 3: Logika je uglavnom dobra, ali uvjet za broj projekata nije potpuno točan. Zadatak 4: Ispravno provjerava parnost broja. Zadatak 5: Izrazi su netočno prepravljeni, rezultat nije isti kao u originalu.
- Cost for this evaluation: $0.03



# Total Cost for Evaluating 2jMJ4dU
Total cost for running evaluations: $0.65