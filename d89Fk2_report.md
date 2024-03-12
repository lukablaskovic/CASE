# Exam Tasks

**1.** Deklarirajte varijable `trenutno_vrijeme` i `temperatura`. U varijablu `trenutno_vrijeme` spremite trenutno vrijeme koristeći `new Date()` objekt, a u varijablu `temperatura` spremite proizvoljnu temperaturu kao cjelobrojnu vrijednost.
- Dodajte novu varijablu `godina` u koju ćete pohraniti godinu koristeći `getFullYear()` funkciju nad varijablom `trenutno_vrijeme`. Sintaksa: `varijabla.getFullYear()`.

- Ispišite u konzolu rečenicu: `"Godina je: ______-a, a temperatura je: ____C."` Godinu i temperaturu zamijenite s vrijednostima iz varijabli koristeći `template literals` sintaksu. Primjer ispisa: `"Godina je 2024-a, a temperatura je: 25C."`.

(MAX_TASK_POINTS = 2)

**2.** Definirajte konstantu `PI` i dodijelite joj vrijednost broja π (3.14159). Dodajte novu varijablu `radijus` u koju ćete pohraniti proizvoljnu vrijednost radijusa kruga u centimetrima. Ispišite u konzolu jednu rečenicu: `"Opseg kruga je: ____ cm odnosno ____ mm, dok je površina ____ cm2 odnosno ____ dm2"`.
Opseg i površinu zamijenite s varijablama za svaku izračunatu vrijednost za svaku mjernu jedinicu (cm = centimetri, dm = decimetri, mm = milimetri) koristeći interpolaciju stringova (template literals).
Dodajte varijablu za svaku izračunatu vrijednost opsega i površine (`opseg_cm`, `opseg_mm`, `povrsina_cm2` i `povrsina_dm2`).
(MAX_TASK_POINTS = 2)

- Opseg: `2πr`
- Površina: `π r²`

**3.** Odlučili ste provjeriti jeste li ostvarili ciljeve na kraju godine. Koristeći logičke operatore i operatore usporedbe, definirajte varijablu `cilj_ispunjen` koja govori jeste li ispunili cilj na kraju godine (ili niste). Varijabla neka ovisi o podciljevima koje ste si zadali: Da bi krajnji cilj bio ispunjen, moram:

- svaki mjesec pročitati najmanje 2 romana ili 1 knjigu.
- dnevno vježbati najmanje 30 minuta.
- uštedjeti između 100 i 200 eura mjesečno.
- naučiti svirati gitaru.

Za svaki od danih izraza deklarirajte varijable za ostvarenu vrijednost i ciljanu vrijednost, te boolean varijablu koja će sadržavati rezultat ostvarenja. Na primjer, za drugu izjavu varijable mogu biti: `vjezbanje_cilj`, `vjezbanje_ostvareno`, `vjezbanje_rezultat`.
Kroz varijable definirajte logički izraz za svaki podcilj i na kraju ispišite rezultat u obliku `cilj_ispunjen = podcilj1 && podcilj2 && podcilj3 && podcilj4`, gdje `cilj_ispunjen` na kraju mora biti `true` ili `false`.
(MAX_TASK_POINTS = 3)

**4.** Raspišite sljedeće izraze bez korištenja `+=`, `-=`, `*=`, `/=`, `++` ili `--` operatora. (MAX_TASK_POINTS = 2)

```javascript
let c = 8;
let d = 5;
c -= d; // Izmijenite izraz
c += d; // Izmijenite izraz
d += 20 + c; // Izmijenite izraz
c *= ++d; // Izmijenite izraz
console.log(c); // 272
console.log(d); // 34
// Izmijenjeni izrazi moraju u konačnici vratiti isti rezultat c i d varijabli kao i originalni izrazi.
// Originalne izraze možete zakomentirati, a ispod njih napisati alternativni izraz (bez korištenja spomenutih operatora).
```

**5.** Deklarirajte 3 varijable koje sadrže cjelobrojne vrijednosti. Za svaku varijablu ispišite izjavu u konzolu: `Broj __ je paran - ${parnost_broja}` gdje `__`zamijenite s brojem, a `parnost_broja` s rezultatom provjere parnosti tog broja.
(MAX_TASK_POINTS = 1)

## mbucaj@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "const trenutno_vrijeme = new Date();\nconst temperatura = 23;\nconst godina = trenutno_vrijeme.getFullYear();\n\nconsole.log(`Godina je : ${godina}-a, a temperatura je ${temperatura}C.`)"
        },
        {
            "js_code": "const PI = 3.14159;\nlet radius = 202;\nlet opseg = 2*PI*radius;\nlet povrsina = PI*(radius*radius);\nlet opseg_mm = opseg/100;\nlet opseg_cm = opseg\nlet povrsina_cm = povrsina\nlet povrsina_dm = povrsina/10;\nconsole.log(` Opseg kruga je- ${opseg_cm} odnosno ${opseg_mm},dok povrsina je ${povrsina_cm} odnosno ${povrsina_dm}`)"
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

- Task 1: 2
- Task 2: 1.5

- Total Points: 3.5
- Feedback: Zadatak 1: Odlično, sve je ispravno implementirano. Zadatak 2: Postoji greška u konverziji mjernih jedinica za opseg i površinu, opseg u milimetrima treba biti pomnožen s 10, a površina u decimetrima treba biti podijeljena s 100, ne s 10.
- Cost for this evaluation: $0.02

## jpejakovi@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let trenutno_vrijeme = new Date();\nlet temperatura = 24; \ngodina = trenutno_vrijeme.getFullYear();\n\nconsole.log(`Godina je ${godina}-a, a temperatura je: ${temperatura}C.`);\n"
        },
        {
            "js_code": "const PI = 3.14159;\nlet radijus = 5;\nlet opseg_kruga_cm = 2 * PI * radijus;\nlet opseg_kruga_mm = opseg_kruga_cm * 10;\nlet povr\u0161ina_cm = PI * (radijus * radijus);\nlet povr\u0161ina_dm = povr\u0161ina_cm / 10;\n\nconsole.log(`Opseg kruga je: ${opseg_kruga_cm} cm odnosno ${opseg_kruga_mm} mm, dok je povr\u0161ina ${povr\u0161ina_cm} cm2 odnosno ${povr\u0161ina_dm} dm2`);\n"
        },
        {
            "js_code": "const mjesecno_cilj = (2 || 1);\nlet mjesecno_ostvareno = (1 && 3);\nlet mjesecno = mjesecno_ostvareno > mjesecno_cilj\nconst vjezbanje_cilj = 30;\nlet vjezbanje_ostvareno = 25;\nlet vjezbanje_rezultat = vjezbanje_ostvareno > vjezbanje_cilj;\nlet u\u0161teda_postignuto = 100;\nlet u\u0161teda_cilj = (u\u0161teda_postignuto > 100 || u\u0161teda_postignuto < 200);\nlet svirati_cilj = true;\nlet svirati_ostvareno = false;\nlet svirati_rezultat = (svirati_ostvareno === true)\ncilj_ispunjen = mjesecno && vjezbanje_rezultat && u\u0161teda_cilj && svirati_rezultat;\n\nconsole.log(cilj_ispunjen);\n"
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

- Task 1: 2
- Task 2: 2
- Task 3: 1

- Total Points: 5
- Feedback: Zadatak 1: Odlično, sve je ispravno implementirano. Zadatak 2: Također odlično, svi izračuni i ispis su točni. Zadatak 3: Logika za provjeru ciljeva nije ispravno implementirana, posebno za čitanje knjiga i uštedu. Zadatak 4 i 5 nisu riješeni.
- Cost for this evaluation: $0.02

## asirol@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let trenutno_vrijeme = new Date()\nlet temperatura = 20\nlet godina = trenutno_vrijeme.getFullYear()\nconsole.log(\"Godina je: \" + godina + \"-a, a temperatura je: \" + temperatura + \"C.\")\n"
        },
        {
            "js_code": "const PI = 3.14159\nconst radijus = 2 \nlet povrsinacm = PI*(radijus**2)\nlet povrsinadm = povrsinacm*0.1\nlet opsegcm = 2*PI*radijus\nlet opsegmm = opsegcm*10\nconsole.log(\"Opseg kruga je: \" + opsegcm + \"cm odnosno \" + opsegmm + \"mm, dok je povrsina \" + povrsinacm + \"cm2 odnosno \" + povrsinadm + \"dm2.\")\n"
        },
        {
            "js_code": "let ciljromani=2 \nlet procromani=1 \nlet zadromani=procromani>=ciljromani\n\nlet ciljknjiga=1 \nlet procknjiga=1 \nlet zadknjiga=procknjiga>=ciljknjiga\n\nlet cilj1=zadknjiga || zadromani\n\nlet ciljvjezba=30\nlet vjezba=40\n\nlet cilj2=vjezba>=ciljvjezba\n\nlet ustedeno=150\n\nlet cilj3=ustedeno>=100 && ustedeno<=200\n\nlet naucenagitara=true\n\nlet cilj4=naucenagitara\n\nlet ciljispunjen = cilj1 && cilj2 && cilj3 && cilj4\n\nconsole.log(ciljispunjen)\n"
        },
        {
            "js_code": "let c = 8;\r\nlet d = 5;\r\nc = c - d; \r\nc = c + d; \r\nd = d + 20 + c; \r\nc = c*(++d); \r\nconsole.log(c);\r\nconsole.log(d); "
        },
        {
            "js_code": "const a = 22\nconst b = 9\nconst c = 80\n\nlet aparan = (a%2==0)\nlet bparan = (b%2==0)\nlet cparan = (c%2==0)\n\nconsole.log(\"Broj \" + a + \" je paran - \" +  aparan)\nconsole.log(\"Broj \" + b + \" je paran - \" +  bparan)\nconsole.log(\"Broj \" + c + \" je paran - \" +  cparan)"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 1.5
- Task 3: 3
- Task 4: 2
- Task 5: 1

- Total Points: 9.5
- Feedback: Zadatak 1: Sve je ispravno implementirano. Zadatak 2: Izračuni su točni, ali je bilo potrebno koristiti template literals za ispis. Zadatak 3: Logika i implementacija su ispravni. Zadatak 4: Ispravno su izmijenjeni izrazi bez korištenja zabranjenih operatora. Zadatak 5: Ispravno je implementirana provjera parnosti i ispis u konzolu.
- Cost for this evaluation: $0.03

## ppuljic@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let trenutno_vrijeme = new Date();\nlet temperatura = 25;\n\nlet godina = trenutno_vrijeme.getFullYear();\n\nconsole.log(`Godina je: ${godina}-a, a temperatura je: ${temperatura}C.`)\n"
        },
        {
            "js_code": "const PI = 3.14159;\nlet radijus = 5;\n\nlet opseg_cm = 2*PI*radijus;\nlet povrsina_dm2 = PI * radijus**2;\nlet opseg_mm = opseg_cm * 10;\nlet povrsina_cm2 = povrsina_dm22*10;\n\nconsole.log(`Opseg kruga je ${opseg_cm}cm odnosno ${opseg_mm}mm, dok je povr\u0161ina ${povrsina_cm2}cm2 odnosno ${povrsina_dm2}dm2`)"
        },
        {
            "js_code": "\n\nlet romani_cilj = 2;\nlet knjiga_cilj = 1;\nlet romani = 3;\nlet knjiga = 4;\nlet podcilj1 = romani  >= romani_cilj && knjiga >= knjiga_cilj;\n\nlet vjezbanje_cilj = 30;\nlet vjezbanje_ostvareno = 40;\nlet podcilj2 = vjezbanje_ostvareno >= vjezbanje_cilj;\n\nlet ustedjeti_cilj = [100, 200];\nlet ustedjeti = 150;\nlet ustedjeti_rez = true;\n\nlet nauciti_gitaru_cilj = true;\nlet nauciti_gitaru_rez = true;\n\nlet cilj_ispunjen = podcilj1 && podcilj2 && ustedjeti_rez && nauciti_gitaru_rez;\nconsole.log(cilj_ispunjen);\n"
        },
        {
            "js_code": "/* let c = 8;\r\nlet d = 5;\r\nc -= d; // Izmijenite izraz\r\nc += d; // Izmijenite izraz\r\nd += 20 + c; // Izmijenite izraz\r\nc *= ++d; // Izmijenite izraz\r\nconsole.log(c); // 272\r\nconsole.log(d); 34 */\r\nlet c = 8;\r\nlet d = 5;\r\nc = c - d;\r\nc = c + d;\r\nd=d+20+c;\r\nc=c*++d;\r\nconsole.log(c);\r\nconsole.log(d)"
        },
        {
            "js_code": "let a = 2;\nlet b = 3;\nlet c = 5;\n\n\nlet parnost_broja_a = a%=2;\n\nlet broj_a_paran = parnost_broja_a == 0;\n// isto i za b i c\nlet parnost_broja_b = b%=2;\nlet parnost_broja_c = c%=2;\n\nconsole.log(parnost_broja_a)\nconsole.log(parnost_broja_b)\nconsole.log(parnost_broja_c)\n\nconsole.log(`Broj ${a} je paran - ${broj_a_paran}`)"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 1.5
- Task 3: 3
- Task 4: 2
- Task 5: 0.5

- Total Points: 9
- Feedback: Zadatak 1: Odlično, sve je ispravno implementirano. Zadatak 2: Postoji greška u izračunu površine u dm2 i cm2, pazite na pretvorbu jedinica. Zadatak 3: Dobar pristup, ali pazite na definiciju varijabli za uštedu, trebalo je koristiti logički izraz. Zadatak 4: Ispravno rješenje, dobro koristite osnovne aritmetičke operatore. Zadatak 5: Pogrešno korištenje operatora za ostatak, trebalo je koristiti `a % 2 == 0` za provjeru parnosti.
- Cost for this evaluation: $0.03

## rstos@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let trenutno_vrijeme = new Date();\nlet temperatura = 20;\nlet godina = trenutno_vrijeme.getFullYear();\nconsole.log(\"Godina je: \" + godina + \"-a, a temperatura je \" + temperatura +\"C\")\n"
        },
        {
            "js_code": "const PI = 3.14159;\nconst radijus = 18;\nconst opseg_cm =2*PI*radijus;\nconst opseg_mm=2*PI*(radijus*10);\nconst povrsina_cm2 = PI *(radijus**2);\nconst povrsina_dm2 = PI * ((radijus/10)**2);\nconsole.log(\"Opseg kruga je \" + opseg_cm + \"cm\" + \" odnosno \" + opseg_mm + \"mm, dok je povr\u0161ina \" + povrsina_cm2 + \"cm2\" + \" odnosno \" + povrsina_dm2 + \"dm2.\" )\n"
        },
        {
            "js_code": "const citanje = 2;\nconst cilj_citanje= 1 <=2;\n\nconst vjezbanje = 15;\nconst cilj_vjezbanje = 30;\n\nconst novac = 150;\nconst cilj_novac= 100 >= 200;\n\nlet gitara = true;\nlet cilj_gitara = true;\n\n\nlet ispunjeno = citanje == cilj_citanje && vjezbanje == cilj_vjezbanje && novac== cilj_novac && gitara == cilj_gitara;\nconsole."
        },
        {
            "js_code": "let c= 8;\nlet d = 5;\n\nc= c-d;\nc= c+d;\nd=d+20+c;\nc=c*(d+1);\nconsole.log(c)\nconsole.log(d)\n"
        },
        {
            "js_code": "let a=2;\nlet b=8;\nlet c= 9;\n\n"
        }
    ]
}
```

### Evaluation

- Task 1: 1.5
- Task 2: 2
- Task 3: 1
- Task 4: 1.5
- Task 5: 0

- Total Points: 6
- Feedback: Zadatak 1: Korištena je konkatenacija umjesto template literals, što nije u skladu s uputama. Zadatak 2: Sve je ispravno izračunato i prikazano. Zadatak 3: Logički izrazi nisu pravilno definirani, a usporedba za cilj novca je netočna. Zadatak 4: Izmjene su djelomično točne, ali zadnji izraz nije ispravno prepravljen. Zadatak 5: Nema implementacije provjere parnosti i ispisivanja u konzolu.
- Cost for this evaluation: $0.03

## enedeljkovic@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
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
            "js_code": "let c = 8;\nlet d = 5;\n \nconsole.log(c - d);\nconsole.log(c + d);\nconsole.log(d + 20 + c);\nconsole.log(c * d + 1);\n"
        },
        {
            "js_code": "[NOT_SOLVED]"
        }
    ]
}
```

### Evaluation

- Task 1: 0
- Task 2: 0
- Task 3: 0
- Task 4: 0.5
- Task 5: 0

- Total Points: 0.5
- Feedback: Za zadatak 4, pokušaj je uočen, ali izrazi ne vraćaju tražene rezultate. Za ostale zadatke, potrebno je riješiti zadatke kako bi se mogli ocijeniti.
- Cost for this evaluation: $0.02

## fmilovan@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let trenutno_vrijeme = new Date();\nlet temperatura = 25; \nlet godina = trenutno_vrijeme.getFullYear();\n\nconsole.log(`Godina je: ${godina}-a, a temperatura je: ${temperatura}C.  `)"
        },
        {
            "js_code": "const \u03c0 = 3.12159;\nlet r = 3;\n\nlet opseg_cm = 2*r*\u03c0;\nlet povrsina_cm2 = \u03c0*r*r;\nlet opseg_mm = (2*r*\u03c0)*10;\nlet povrsina_dm2 = \u03c0*(r/10)*(r/10);\n\n\nconsole.log(`Opseg kruga je: ${opseg_cm}cm odnosno ${opseg_mm}mm, dok je povr\u0161ina ${povrsina_cm2}cm2 odnosno ${povrsina_dm2}dm2`)"
        },
        {
            "js_code": "[NOT_SOLVED]"
        },
        {
            "js_code": "let c = 8;\r\nlet d = 5;\r\nc += d; // Izmijenite izraz\r\nc -= d; // Izmijenite izraz\r\nd += 36 - c; // Izmijenite izraz\r\nc *= d +1; // Izmijenite izraz\r\nconsole.log(c);\r\nconsole.log(d); "
        },
        {
            "js_code": "const a=2;\nconst b=3;\nconst c=4;\n\nlet parnost_broja( a%)"
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
- Feedback: Zadatak 1: Odlično, sve je ispravno implementirano. Zadatak 2: Dobra logika, ali vrijednost PI nije točno navedena. Zadatak 3: Zadatak nije riješen. Zadatak 4: Pokušaj je vidljiv, ali izrazi ne daju traženi rezultat. Zadatak 5: Pseudokod je prisutan, ali implementacija nije ispravna.
- Cost for this evaluation: $0.02

## lstanic@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let trenutno_vrijeme = new Date();\nlet temperatura = 20;\nlet godina = trenutno_vrijeme.getFullYear();\nconsole.log(`Godina je: ${godina}-a, a temperatura je: ${temperatura}C.`)"
        },
        {
            "js_code": "const PI = 3.14159;\nlet radijus = 5;\nlet opseg_cm = 2*PI*radijus;\nlet opseg_mm = opseg_cm / 10;\nlet povrsina_cm2 = PI*(radijus)**2;\nlet povrsina_dm2 = povrsina_cm2*100;\nconsole.log(`Opseg kruga je: ${opseg_cm} cm odnosno ${opseg_mm} mm, dok je povr\u0161ina ${povrsina_cm2} cm2 odnosno ${povrsina_dm2} dm2`)"
        },
        {
            "js_code": "// 1. uvjet\nlet citanje_romana_cilj = 2;\nlet procitano_roman = 1;\nlet citanje_romana_rezultat = procitano_roman >= citanje_romana_cilj;\nlet citanje_knjige_cilj = 1;\nlet procitano_knjiga = 2;\nlet procitano_knjiga_rezultat = procitano_knjiga >= citanje_knjige_cilj;\n// 2. uvjet\nlet vjezbanje_cilj = 30;\nlet vjezbano = 20;\nlet vjezbanje_cilj_rezultat = vjezbano >= vjezbanje_cilj;\n// 3. uvjet\nlet ustedeno = 150;\nlet stednja_cilj = ustedeno >= 100 && ustedeno <= 200;\n// 4. uvjet\nlet naucio_svirati_gitaru = true;\nconst cilj_ispunjen = (citanje_romana_rezultat || procitano_knjiga_rezultat) && vjezbanje_cilj_rezultat && stednja_cilj && naucio_svirati_gitaru;\nconsole.log(cilj_ispunjen);"
        },
        {
            "js_code": "let c = 8;\nlet d = 5;\nc = c - 5;\nc = c + 5;\nd = 20 + 8;\nc = 28 + 8;\nconsole.log(c);\nconsole.log(d);"
        },
        {
            "js_code": "let a = 2;\nlet parnost_broja_a = a%2 == 0;\nconsole.log(`Broj ${a} je paran - ${parnost_broja_a}`)\nlet b = 5;\nlet parnost_broja_b = b%2 == 0;\nconsole.log(`Broj ${b} je paran - ${parnost_broja_b}`)\nlet c = 8;\nlet parnost_broja_c = c%2 == 0;\nconsole.log(`Broj ${c} je paran - ${parnost_broja_c}`)"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 1.5

- Total Points: 9
- Feedback: Zadatak 1: Odlično, sve je ispravno implementirano. Zadatak 2: Postoji greška u izračunu opsega u milimetrima, trebalo je pomnožiti s 10, a ne podijeliti. Zadatak 3: Dobar pokušaj, ali varijabla `vjezbanje_cilj_rezultat` je trebala biti `true` da bi cilj bio ispunjen. Zadatak 4: Izrazi nisu ispravno prepravljeni da bi dali tražene rezultate, posebno zadnji izraz. Zadatak 5: Sve je ispravno implementirano, dobar rad.
- Cost for this evaluation: $0.03

## arogalo@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let trenutno_vrijeme = new Date();\nlet temperatura = 17;\n\nlet godina = trenutno_vrijeme.getFullYear();\n\nconsole.log(`Godina je: ${godina}-a, a temperatura je: ${temperatura} C`);\n"
        },
        {
            "js_code": "const PI = 3.14159;\nlet radijus = 3;\n\nlet opseg_cm = 2 * PI * radijus;\nlet opseg_mm = 2 * PI * (radijus * 10);\n\nlet povrsina_cm2 = PI * radijus ** 2;\nlet povrsina_dm2 = PI * (radijus / 10) ** 2;\n\nconsole.log(`Opseg kruga je: ${opseg_cm} cm odnosno ${opseg_mm} mm, dok je povr\u0161ina ${povrsina_cm2} cm2 odnosno ${povrsina_dm2} dm2`);\n\n\n"
        },
        {
            "js_code": "let cilj_ispunjen;\n\nlet procitane_knjige = 2;\nlet procitani_romani = 1;\nlet cilj_procitanih_knjiga = 1;\nlet cilj_procitanih_romana = 2;\nlet podcilj1 = (procitani_romani >= cilj_procitanih_romana) || (procitane_knjige >= cilj_procitanih_knjiga);\n\nlet vjezba_cilj = 30;\nlet vjezba_ispunjeno = 50;\nlet podcilj2 = vjezba_ispunjeno >= vjezba_cilj;\n\nlet stednja_min = 100;\nlet stednja_max = 200;\nlet stednja = 150;\nlet podcilj3 = (stednja < stednja_max) && (stednja > stednja_min);\n\nlet nauciti_svirati_gitaru = true;\n\ncilj_ispunjen = podcilj1 && podcilj2 && podcilj3 && nauciti_svirati_gitaru;\n\nconsole.log(cilj_ispunjen);"
        },
        {
            "js_code": "let c = 8;\nlet d = 5;\n\nc = c - d;\nc = c + d;\nd = d + 20 + c;\nc = c * (d+1);\nd = d + 1;\n\nconsole.log(c);\nconsole.log(d);"
        },
        {
            "js_code": "let a = 4;\nlet b = 7;\nlet c = 12;\n\nlet parnost_broja_a = a%2 == 0;\nlet parnost_broja_b = b%2 == 0;\nlet parnost_broja_c = c%2 == 0;\n\nconsole.log(`Broj ${a} je paran - ${parnost_broja_a}`);\nconsole.log(`Broj ${b} je paran - ${parnost_broja_b}`);\nconsole.log(`Broj ${c} je paran - ${parnost_broja_c}`);"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 2
- Task 3: 2.5
- Task 4: 1.5
- Task 5: 1

- Total Points: 9
- Feedback: Zadatak 1: Savršeno, sve je ispravno implementirano. Zadatak 2: Također, sve je točno i precizno izračunato. Zadatak 3: Logika je uglavnom dobra, ali postoji greška u logičkom izrazu za štednju, trebalo bi biti >= i <= za granice. Zadatak 4: Izmjene su ispravne, ali zadnji izraz nije u potpunosti točan prema zadatku. Zadatak 5: Ispravno je, ali relativno jednostavno, stoga niži bodovi.
- Cost for this evaluation: $0.03

## jsternvuk@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let trenutno_vrijeme = new Date();\nlet temperatura = 15;\nlet godina = trenutno_vrijeme.getFullYear();\n\nconsole.log(`Godina je: ${godina}-a, a temperatura je: ${temperatura}C.`);\n"
        },
        {
            "js_code": "const PI = 3.14159;\nlet radijus = 5;\n\nconsole.log(`Opseg kruga je: ${2 * PI * radijus} cm odnosno ${PI * radijus * 20} mm, dok je povrsina ${PI * radijus ** 2} cm2 odnosno ${PI * radijus ** 2 / 100} dm2`); // Assuming da je 1dm2 = 100cm2 jer kvadrati???\n"
        },
        {
            "js_code": "const romani_cilj = 2;\nconst knjiga_cilj = 1; \nconst vjezbanje_cilj = 30;\nconst ustedjevina_donji_cilj = 100;\nconst ustedjevina_gornji_cilj = 200;\nconst gitara_cilj = true; \n\nlet romani_procitani = 0;\nlet knjige_procitane = 1;\nlet vjezbanje_ostvareno = 30;\nlet ustedeno = 150;\nlet gitara_naucena = true;\n\nlet podcilj_1 = romani_procitani >= romani_cilj || knjige_procitane >= knjiga_cilj;\nlet podcilj_2 = vjezbanje_ostvareno >= vjezbanje_cilj;\nlet podcilj_3 = ustedeno >= ustedjevina_donji_cilj && ustedeno <= ustedjevina_gornji_cilj;\nlet podcilj_4 = gitara_naucena;\n\nlet cilj_ispunjen = podcilj_1 && podcilj_2 && podcilj_3 && podcilj_4\n\nconsole.log(cilj_ispunjen)"
        },
        {
            "js_code": "let c = 8; \nlet d = 5;\nc = c - d;\nc = c + d;\nd = d + 20 + c;\nc = c * ++d;\nconsole.log(c);\nconsole.log(d);"
        },
        {
            "js_code": "let x = 1;\nlet y = 2;\nlet z = 3; \n\nconsole.log(`Broj ${x} je paran - ${x % 2 == 0}`);\nconsole.log(`Broj ${y} je paran - ${y % 2 == 0}`);\nconsole.log(`Broj ${z} je paran - ${z % 2 == 0}`);"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 1.5
- Task 3: 3
- Task 4: 1
- Task 5: 1

- Total Points: 8.5
- Feedback: Zadatak 1: Odlično, sve je ispravno implementirano. Zadatak 2: Mali problem s izračunom opsega u milimetrima, trebali ste pomnožiti rezultat s 10, a ne s 20. Zadatak 3: Sve je točno, dobro razmišljanje. Zadatak 4: Niste u potpunosti izbjegli korištenje ++ operatora. Zadatak 5: Ispravno, dobro koristite modulo operator za provjeru parnosti.
- Cost for this evaluation: $0.03

## majhorn@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let trenutno_vrijeme = new Date ();\nlet temperatura = 25;\nlet godina = trenutno_vrijeme.getFullYear();\n\nconsole.log(`Godina je: ${godina}-a, a temperatura je: ${temperatura}C.`);"
        },
        {
            "js_code": "const PI = 3.14159;\nlet radijus = 5;\nlet opseg_cm = 2 * PI * radijus;\nlet opseg_mm = opseg_cm  / 10;\n\nlet povrsina_cm = PI * (radijus ** radijus);\nlet povrsina_dm = povrsina_cm * 100;\n\nconsole.log(`Opseg kruga je: ${opseg_cm} cm odnosno ${opseg_mm}, dok je povr\u0161ina ${povrsina_cm} cm2 odnosno ${povrsina_dm} dm2`);\n\n\n"
        },
        {
            "js_code": "// cilj 1\nlet ciljano_citanje_romana = 2;\nlet ciljano_citanje_knjige = 1;\nlet ostvareno_citanje_romana = 1;\nlet ostvareno_citanje_knjige = 2;\n\nlet cilj1 = ostvareno_citanje_romana >= ciljano_citanje_romana || ostvareno_citanje_knjige === ciljano_citanje_knjige;\n\n// cilj 2\nlet ciljano_vjezbanje = 30;\nlet ostvareno_vjezbanje = 40;\n\nlet cilj2 = ostvareno_vjezbanje >= ciljano_vjezbanje;\n\n// cilj 3 \nlet ciljana_usteda = 100;\nlet ostvarena_usteda = 150;\n\nlet cilj3 = ostvarena_usteda >= ciljana_usteda && ostvarena_usteda <= 200;\n\n// cilj 4 \nlet nauciti_svirati_gitaru = true;\n\nlet cilj_ispunjen = cilj1 && cilj2 && cilj3 && nauciti_svirati_gitaru;\nconsole.log(cilj_ispunjen);"
        },
        {
            "js_code": "let c = 8;\nlet d = 5;\nc = c - d;\nc = c + d;\nd = d + 20 + c;\nc = c * ++d;\nconsole.log(c);\nconsole.log(d);"
        },
        {
            "js_code": "let a = 3;\nlet b = 5;\nlet c = 8;\nlet parnost_broja = true;\n\nif (a % 2 === 0) {\n  parnost_broja = false;\n}\n\nif (b % 2 === 0) {\n  parnost_broja = false;\n}\n\nif (c % 2 === 0) {\n  parnost_broja = true;\n}\nconsole.log(`Broj ${a} je paran - ${parnost_broja}, broj ${b} je paran - ${parnost_broja}, broj ${c} je paran - ${parnost_broja}`);"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 1
- Task 3: 3
- Task 4: 2
- Task 5: 0.5

- Total Points: 8.5
- Feedback: Zadatak 1: Odlično, sve je ispravno implementirano. Zadatak 2: Postoji greška u izračunu opsega i površine, opseg_mm treba množiti, a ne dijeliti, a površina_cm2 i površina_dm2 nisu ispravno izračunati. Zadatak 3: Sve je ispravno, logika je dobro implementirana. Zadatak 4: Ispravno je prepravljeno korištenje operatora, dobro. Zadatak 5: Provjera parnosti nije ispravno implementirana za svaku varijablu pojedinačno, parnost_broja se ne ažurira ispravno za svaki broj.
- Cost for this evaluation: $0.03

## dsambolec@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let trenutno_vrijeme = new Date();\nlet temperatura =15;\nlet godina = trenutno_vrijeme.getFullYear();\n\nconsole.log(`Godina je:  ${godina}-a, a temperatura je : ${temperatura}C.`);"
        },
        {
            "js_code": "const pi = 3.14159;\nlet radijus = 30;\nlet opseg_cm = (2*pi*radijus);\nlet opseg_mm = (opseg_cm*10);\nlet povrsina = (pi*radijus*radijus);\nlet povrsina_dm2 = (povrsina/10);\n\nconsole.log(`Opseg kruga je: ${opseg_cm} cm odnosno ${opseg_mm},dok je povrsina ${povrsina}cm2 odnosno ${povrsina_dm2} dm2`);"
        },
        {
            "js_code": "let citanje = (2 || 1);\nlet citanje_cilj = (2 || 1);\nlet citanje_rez = citanje>=citanje_cilj;\n\nlet vjezbanje= 20;\nlet vjezbanje_cilj = 30;\nlet vjezbanje_rez = vjezbanje >= vjezbanje_cilj;\n\nlet stednja = (100>200);\nlet stednja_cilj = (100>200);\nlet stednja_rez = (stednja>=stednja_cilj);\n\nlet gitara = (\"Da\");\nlet gitara_cilj = (\"Da\");\nlet gitara_rez = gitara===gitara_cilj;\n\ncilj_ispunjen =(`Citanje:  ${citanje_rez} && ${vjezbanje_rez} && ${stednja_rez} && ${gitara_rez}`);\n\nconsole.log=(cilj_ispunjen);\n"
        },
        {
            "js_code": "let c = 8;\nlet d = 5;\n\nc-=d;\nc+=d;\nd+=20;\nc*=++d;\nconsole.log(c);\nconsole.log(d);"
        },
        {
            "js_code": "let a = 4;\nlet b = 6;\nlet c = 8;\nlet parnost_broja = (a/2===2);\nlet parnost_brojab= (b/2 ===3);\nlet parnost_brojac = (c/2 ===4);\n\nconsole.log(`Broj ${a} je paran - ${parnost_broja}`);\n\nconsole.log(`Broj ${b} je paran - ${parnost_brojab}`);\n\nconsole.log(`Broj ${c} je paran - ${parnost_brojac}`);"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 2
- Task 3: 1
- Task 4: 0
- Task 5: 0.5

- Total Points: 5.5
- Feedback: Zadatak 1: Kod je ispravan, dobro koristi template literals za ispis. Zadatak 2: Ispravno izračunate vrijednosti i korištenje template literals, mala greška u ispisu površine. Zadatak 3: Logika za provjeru ciljeva nije ispravno implementirana, posebno za štednju. Zadatak 4: Niste izmijenili izraze kako je zatraženo u zadatku. Zadatak 5: Provjera parnosti nije ispravno implementirana, trebali ste koristiti operator modulo (%) za provjeru.
- Cost for this evaluation: $0.03

## lpavlic1@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "trenutno_vrijeme = new Date()\ntemperatura = 30\n\ngodina = trenutno_vrijeme.getFullYear()\n\nconsole.log(\"Godina je: \") godina (\"-a, a temperatura je: \") temperatura (\" C.\");"
        },
        {
            "js_code": "const PI = 3.14159\nconst r =  10\n\nopseg_cm = 2 * PI * r;\nopseg_mm = 2 * PI * r *10;\npovrsina_cm2 = PI * (r*r);\npovrsina_dm2 = (PI * (r*r)) /10\n\nconsole.log(\"Opseg kuga je: \" opseg_cm \" cm odnosno \" opseg_mm \" mm dok je povr\u0161ina \" povrsina_cm2 \" cm2 odnosno \" povrsina_dm2 \" dm2\");\n\n"
        },
        {
            "js_code": "cilj_ispunjen"
        },
        {
            "js_code": "let c = 8;\nlet d = 5;\n\nc = c - d;\nc = c + d;\nc = c + 20 + d;\nc = c * (d + 1);\n\nconsole.log(c);\nconsole.log(d);\n"
        },
        {
            "js_code": "a = 5\nb = 2\nc = 10\n\n\nparan_a = a/2\nif %(paran_a) == 0 then \"Paran\" else \"Neparan\";\nparan_b = a/2\nif %(paran_a) == 0 then \"Paran\" else \"Neparan\";\nparan_a = a/2\nif %(paran_a) == 0 then \"Paran\" else \"Neparan\";\n"
        }
    ]
}
```

### Evaluation

- Task 1: 0.5
- Task 2: 1.5
- Task 3: 0
- Task 4: 2
- Task 5: 0

- Total Points: 4
- Feedback: Zadatak 1: Korištenje varijabli i `Date` objekta je ispravno, ali sintaksa za ispis u konzolu nije valjana. Zadatak 2: Konstanta PI i izračuni su točni, ali sintaksa za ispis nije ispravna. Zadatak 3: Nije bilo pokušaja rješavanja. Zadatak 4: Izmjene izraza su ispravno napravljene i vraćaju očekivane rezultate. Zadatak 5: Pokušaj je napravljen, ali sintaksa i logika za provjeru parnosti nisu ispravni.
- Cost for this evaluation: $0.03

## imocilac@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "var trenutno_vrijeme = new Date()\nvar temperatura = 12\n\nvar godina = trenutno_vrijeme.getFullYear()\n\nvar ispis = `Godina je: ${godina}-a, a temperatura je: ${temperatura}C.`\n\nconsole.log(ispis)"
        },
        {
            "js_code": "const PI = 3.14159\nvar radijus = 5\n\nvar opseg_cm = 2*PI*radijus\nvar opseg_mm = (2*PI*radijus)*10\nvar povrsina_cm2 = PI*(radijus*radijus)\nvar povrsina_dm2 = (PI*(radijus*radijus))/10\n\nvar ispis = `Opseg kruga je: ${opseg_cm} cm odnosno ${opseg_mm} mm, dok je povr\u0161ina ${povrsina_cm2} \ncm2 odnosno ${povrsina_dm2} dm2.`\n\nconsole.log(ispis)"
        },
        {
            "js_code": "var cilj_ispunjen = false\n\nvar procitanih_knjiga = 0\nvar procitanih_romana = 2\nvar cilj_procitanih_knjiga= 1\nvar cilj_procitanih_romana= 2\nvar podcilj1 = procitanih_knjiga>=cilj_procitanih_knjiga || procitanih_romana>=cilj_procitanih_romana\n\nvar vjezbanje_ostvareno = 25\nvar vjezbanje_cilj = 30\nvar podcilj2 = vjezbanje_ostvareno>=vjezbanje_cilj\n\nvar ustedjeno = 128\nvar podcilj3 = ustedjeno<=200 && ustedjeno>=100\n\nvar podcilj4 = false\n\nvar cilj_ispunjen = podcilj1 && podcilj2 && podcilj3 && podcilj4\n\nconsole.log(cilj_ispunjen)"
        },
        {
            "js_code": "let c = 8;\r\nlet d = 5;\r\nc = c - d\r\nc = c + d\r\nd = d + 1 + 20 + c\r\nc = d * c\r\nconsole.log(c)\r\nconsole.log(d)"
        },
        {
            "js_code": "var broj1 = 6\nvar broj2 = 3\nvar broj3 = 11\n\nvar parnost_broja1 = broj1%2\n\nvar ispis1 =`Broj ${broj1} je paran - ${parnost_broja}`\n\nconsole.log(ispis1)\n\n\nvar ispis2 =`Broj ${broj1} je paran - ${parnost_broja}`\n\nconsole.log(ispis2)\n\nvar ispis3 =`Broj ${broj1} je paran - ${parnost_broja}`\n\nconsole.log(ispis1)\n"
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
- Feedback: Zadatak 1: Odlično, sve je ispravno implementirano. Zadatak 2: Također odlično, matematički izrazi su točno korišteni. Zadatak 3: Dobra logika, ali podcilj4 nije definiran s konkretnim uvjetima. Zadatak 4: Izmijenjeni izrazi su uglavnom točni, ali postoji greška u logici koja vodi do netočnog rezultata. Zadatak 5: Prikaz parnosti nije ispravno implementiran, i korištenje varijable 'parnost_broja' nije dosljedno, što dovodi do netočnih ispisa.
- Cost for this evaluation: $0.03

## dskrnicki@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let  trenutno_vrijeme = new Date();\n\n let temperatura = 15;\n \n  trenutno_vrijeme.getFullYear();\n \n console.log(`Godina je: ${trenutno_vrijeme}-a, a temperatura je: ${temperatura}! C.`)\n \n"
        },
        {
            "js_code": "const PI = 3.14159;\nlet radius = 15;\n\nlet opseg_cm= 2*PI*radius;\nlet opseg_mm= 2*PI*radius*10;\nlet povrsina_cm2 = PI*radius*radius;\nlet povrsina_mm2 = PI*radius*radius*10;\n\n\nconsole.log(`Opseg kruga je: ${opseg_cm} cm odnosno ${opseg_mm} mm, dok je povr\u0161ina ${povrsina_cm2} cm2 odnosno ${povrsina_mm2} dm2`)\n\n"
        },
        {
            "js_code": "let podcilj1 = true;\n\nlet podcilj2 = false;\n\nlet podcilj3 = true;\n\nlet podcilj4 = false;\n\n\n\n let cilj_ispunjen = podcilj1 && podcilj2 && podcilj3 && podcilj4;\n \n console.log(cilj_ispunjen)\n"
        },
        {
            "js_code": "let c = 8;\r\nlet d = 5;\r\nc - d = d; // Izmijenite izraz\r\nc +d = d; // Izmijenite izraz\r\nd += 20 + c; // Izmijenite izraz\r\nc *= ++d; // Izmijenite izraz\r\nconsole.log(c); // 272\r\nconsole.log(d); // 34"
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
- Task 3: 2
- Task 4: 0

- Total Points: 4.5
- Feedback: Zadatak 1: Niste ispravno pohranili godinu iz objekta trenutno_vrijeme, što rezultira ispisom neispravne godine. Zadatak 2: Pogreška u izračunu površine u dm2, trebali ste koristiti drugačiju konverziju. Zadatak 3: Dobro ste definirali logičke operatore, ali niste koristili konkretne varijable za provjeru ciljeva. Zadatak 4: Izrazi su neispravno napisani i ne mogu se izvršiti kako je navedeno.
- Cost for this evaluation: $0.03

## imikulic@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let trenutno_vrijeme;\nlet temperatura;\n\ntrenutno_vrijeme = new Date();\ntemperatura = 25;\n\nlet godina= trenutno_vrijeme.getFullYear();\n\nconsole.log(`Godina je: ${godina}-a, a temperatura je ${temperatura}C.`)"
        },
        {
            "js_code": "const PI=3.14159;\nlet radijus= 5;\n\nlet opseg_cm= 2*PI*radijus;\nlet opseg_mm=(2*PI*radijus)*10;\n\nlet povrsina_cm2= PI*(radijus**2);\nlet povrsina_dm2= (PI*(radijus**2))/10;\n\nconsole.log(`Opseg kruga je: ${opseg_cm} cm odnosno ${opseg_mm} mm, dok je povr\u0161ina ${povrsina_cm2} cm2 odnosno ${povrsina_dm2} dm2.`)"
        },
        {
            "js_code": "let cilj_ispunjen; \n\nlet procitani_romani= 1;\nlet procitane_knjige= 2;\n\nlet prvi_cilj= procitani_romani>=2 || procitane_knjige>=1;\n\nlet vjezbanje= 20;\n\nlet drugi_cilj= vjezbanje>=30;\n\nlet usteda= 120;\n\nlet treci_cilj= usteda>100 && usteda<200;\n\nlet naucila_gitaru= true;\n\nlet cetvrti_cilj= naucila_gitaru;\n\ncilj_ispunjen= prvi_cilj && drugi_cilj && treci_cilj && cetvrti_cilj;\n\nconsole."
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

- Task 1: 2
- Task 2: 2
- Task 3: 2.5

- Total Points: 6.5
- Feedback: Zadatak 1: Kod je ispravno napisan, dobro koristi template literals za ispis. Zadatak 2: Kod je točan, pravilno su izračunate vrijednosti i korištena je interpolacija stringova. Zadatak 3: Logika je uglavnom dobra, ali postoji manji problem s logikom provjere uštede (trebalo bi biti >= 100 i <= 200). Zadatak 4 i 5: Nisu riješeni, stoga ne mogu dodijeliti bodove.
- Cost for this evaluation: $0.02

## alabinjan@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let trenutno_vrijeme = new Date();\nlet temperatura = 36;\n\ngodina = trenutno_vrijeme.getFullYear();\n\nconsole.log(\"Godina je \" + godina + \" , a temperatura je \" + temperatura)"
        },
        {
            "js_code": "const PI = 3.14159;\nlet radijus = 12;\n\nopseg_cm = ((2*PI)*radijus);\nopseg_mm = (opseg_cm*10);\n\npovrsina_cm2 = ((PI) * radijus**2)\npovrsina_dm2 = ((PI * (radijus*0.1)))\n\nconsole.log(\"Opseg kruga je: \" + opseg_cm + \" cm odnosno \" + opseg_mm +\" mm, dok je povr\u0161ina \" + povrsina_cm2 +\" cm2 odnosno \" + povrsina_dm2 + \" dm2. \")"
        },
        {
            "js_code": "let ciljano_citanje_2_romana = false;\nlet ostvareno_citanje_2_romana = true\nlet ciljano_citanje_1_knjige = false;\nlet ostvareno_citanje_1_knjige = true;\nlet ciljano_citanje = ostvareno_citanje_2_romana || ostvareno_citanje_1_knjige;\nlet ciljano_vjezbanje = 30;\nlet ostvareno_vjezbanje = 35;\nlet minimalna_ciljana_usteda = 100;\nlet maksimalna_ciljana_usteda = 200;\nlet ostvarena_usteda = 199;\nlet naucena_ciljana_gitara = true;\n\n\nlet ostvareno_citanje = ciljano_citanje;\nlet usteda_ostvarena =   maksimalna_ciljana_usteda > minimalna_ciljana_usteda;\nlet ostvarena_vjezba = ostvareno_vjezbanje>ciljano_vjezbanje;\nlet naucena_gitara = naucena_ciljana_gitara;\n\ncilj_ispunjen = ostvareno_citanje && usteda_ostvarena && ostvarena_vjezba && naucena_ciljana_gitara;\n"
        },
        {
            "js_code": "let c = 8;\r\nlet d = 5;\r\n//c -= d; // Izmijenite izraz\r\nc = c-d;\r\n// c += d; // Izmijenite izraz\r\nc = c+d;\r\n//d += 20 + c; // Izmijenite izraz\r\nd = d + 20 + c;\r\n//c *= ++d; // Izmijenite izraz\r\nc = c* (1+d)\r\nconsole.log(c); // 272\r\nconsole.log(d); // 34"
        },
        {
            "js_code": "let broj1 = 1;\nlet broj2 = 2;\nlet broj3 = 3;\nparnost_broja1 = broj1 % 2 == 0;\nparnost_broja2 = broj2 % 2 == 0;\nparnost_broja3 = broj3 % 2 == 0;\n\nconsole.log('Broj ' + broj1 + ' je paran - ' + parnost_broja1 );\nconsole.log('Broj ' + broj2 + ' je paran - ' + parnost_broja2 );\nconsole.log('Broj ' + broj3 + ' je paran - ' + parnost_broja3 );"
        }
    ]
}
```

### Evaluation

- Task 1: 1.5
- Task 2: 1.5
- Task 3: 2
- Task 4: 2
- Task 5: 1

- Total Points: 8
- Feedback: Zadatak 1: Nedostaje upotreba template literals za ispis u konzolu. Zadatak 2: Pogreška u izračunu površine u dm2, trebalo je koristiti pretvorbu radijusa u decimetre prije kvadriranja. Zadatak 3: Logika za ostvarenje ciljeva je djelomično točna, ali usporedba za uštedu nije ispravno implementirana. Zadatak 4: Izmjene izraza su točne, ali postoji greška u zadnjem izrazu, trebalo je koristiti d+1 umjesto 1+d. Zadatak 5: Točno je implementirana provjera parnosti, ali bi bilo bolje koristiti template literals za ispis.
- Cost for this evaluation: $0.03

## gmijatov1@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let trenutno_vrijeme = new Date();\nlet temperatura = 26;\n\nlet godina = trenutno_vrijeme.getFullYear();\n\n\n\nconsole.log(`Godina je: ${godina}, a temperatura je: ${temperatura}C.`)\n"
        },
        {
            "js_code": "const PI = 3.14159;\nconst radijus = 34;\n\nlet opseg_cm = ((PI **2))*radijus;\nconsole.log(opseg_cm);\nlet povrsina_cm = (PI*(radijus **2));\nconsole.log (povrsina_cm);\n\nlet opseg_mm = (opseg_cm **10);\nlet povrsina_cm2 = (povrsina_cm ** povrsina_cm);\nlet povrsina_dm2 = (povrsina_cm2 *10);\n\nconsole.log(`Opseg kruga je: ${opseg_cm} cm odnosno ${opseg_mm}, dok je povr\u0161ina ${povrsina_cm2} odnosno ${povrsina_dm2} dm2`)"
        },
        {
            "js_code": "let procitano = 3;\nconst procitano_cilj = 3;\n\nlet vjezbanje = 20;\nconst vjezbanje_cilj = 30;\n\nlet usteda = 150;\nconst usteda_cilj = (usteda <= 200 && usteda >= 100);\n\nlet sviranje = true;\n\nlet vjezbanje_ostvareno = (vjezbanje >= 30);\n\n"
        },
        {
            "js_code": "let c = 8;\nlet d = 5;\n\nlet  \n\nconsole.log(c);\nconsole.log(d);"
        },
        {
            "js_code": "let broj = 2;\n"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 0.5

- Total Points: 2.5
- Feedback: Zadatak 1: Odlično, sve je ispravno implementirano. Zadatak 2: Formula za opseg nije ispravno primijenjena, a izračuni za pretvorbu mjernih jedinica su netočni. Zadatak 3: Niste dovršili logiku za provjeru ciljeva, nedostaje konačna provjera i ispis. Zadatak 4: Niste implementirali tražene izmjene. Zadatak 5: Niste dovršili zadatak, nedostaje logika za provjeru parnosti i ispis za svaku varijablu.
- Cost for this evaluation: $0.02

## gnadal@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let trenutno_vrijeme = new Date();\nlet temperatura = 25;\n\ngodina = trenutno_vrijeme.getFullYear();\n\nconsole.log(\"Godina je : \" + godina +  \"-a , a temperatura je:\" + temperatura + \"C\");\nconsole.log(`Godina je : ${godina}-a , a temperatura je: ${temperatura} C`);"
        },
        {
            "js_code": "const = PI = 3.14159;\nlet radijus = 6;\n\nlet opseg = 2 * PI * radijus;\nlet povrsina = PI * radijus **2;\n\nlet opseg_centim = opseg;\nlet opseg_centim = opseg *\u00b810;\nlet povrsina_cm2 = povrsina;\nlet povrsina_dm2= povrsina /10;\n\nconole.log(\"opseg\")"
        },
        {
            "js_code": "let cilj_procitati_romana = 2;\nlet cilj_procitati_knjigu = 1;\nlet cilj_vjezbati = 30;\nlet cilj_ustedjeti_min = 100;\nlet cilj_ustedjeti_max = 200;\nlet cilj_svirati_gitaru = true;\n\nlet procitati_romana = 3;\nlet procitati_knjigu = 2;\nlet vjezbati = 50;\nlet ustedjeti = 150;\nlet svirati_gitaru = true;\n\nlet ostavreno_procitati_romana = procitati_romana >= cilj_procitati_romana;\nlet ostavreno_procitati_knjigu = procitati_knjigu >= cilj_procitati_knjigu;\nlet ostavreno_vjezbati = vjezbati > cilj_vjezbati;\nlet ostavreno_ustedjeti = ustedjeti >= cilj_ustedjeti_min && ustedjeti <= cilj_ustedjeti_max;\nlet ostavreno_svirati_gitaru = svirati_gitaru === cilj_svirati_gitaru;\n\nlet cilj_ispunjen  = ostavreno_procitati_romana && ostavreno_procitati_knjigu\n&& ostavreno_vjezbati && ostavreno_ustedjeti && ostavreno_svirati_gitaru;\n\nconsole.log(`cilj je ${cilj_ispunjen} znaci ispunjen`);\n\n\n"
        },
        {
            "js_code": "let c = 8;\nlet d = 5;\nc = c - d;\nc = c + d;\nc = c * d;\nd_ce_biti = 6;\nconsole.log(c);\nconsole.log(d);\n"
        },
        {
            "js_code": "let a = 2;\nlet b = 3;\nlet c = 4;"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 1
- Task 3: 2.5
- Task 4: 1
- Task 5: 0

- Total Points: 6.5
- Feedback: Zadatak 1: Odlično, korištenje template literals sintakse je ispravno. Zadatak 2: Postoji nekoliko grešaka, uključujući ponovnu deklaraciju varijable i tipfeler u ispisu. Zadatak 3: Logika je dobro razrađena, ali obratite pažnju na tipfeler u ispisu. Zadatak 4: Izmijenjeni izrazi nisu u potpunosti točni, nedostaje pravilna implementacija za zadnji izraz. Zadatak 5: Nema implementacije za provjeru parnosti brojeva i ispis u konzolu.
- Cost for this evaluation: $0.03

## iplese@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let trenutno_vrijeme= new Date();\nlet temperatura= 15;\nlet godina= trenutno_vrijeme.getFullYear();\nconsole.log(`Godina je: ${godina}, a temperatura je: ${temperatura}C `);\n\n\n"
        },
        {
            "js_code": "const PI=3.14159;\nlet radijus=8;\n\nlet opseg_cm= 2*radijus*PI;\nlet opseg_mm= opseg_cm * 10;\n\nlet povrsina_cm2= PI*radijus**2;\nlet povrsina_dm2= povrsina_cm2 / 10;\n\nconsole.log(`Opseg kruga je: ${opseg_mm} mm, dok je povr\u0161ina ${povrsina_cm2}  cm2 odnosno ${povrsina_dm2} dm2`);"
        },
        {
            "js_code": "[NOT_SOLVED]"
        },
        {
            "js_code": "let c= 8;\nlet d= 5;\n\nd=c-d;\nd=c+d;\nc=d+20;\nd=c* ++d;\n\nconsole.log(c);\nconsole.log(d);"
        },
        {
            "js_code": "let a= 8;\nlet b= 6;\nlet c=7;\n\nlet parnost_broja(){\n  if (a%2==0)\n  return true;\n  \n  else\n  return false;\n}\n  \nconsole.log(parnost_broja);\n\n//console.log(`Broj ${a} je paran ${parnost_broja} .`)"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 2
- Task 3: 0
- Task 4: 0.5
- Task 5: 0.5

- Total Points: 5
- Feedback: Zadatak 1: Odlično, sve je ispravno implementirano. Zadatak 2: Također odlično, matematički izrazi su točno implementirani. Zadatak 3: Nije riješeno, stoga nema bodova. Zadatak 4: Izmijenjeni izrazi ne vraćaju ispravne rezultate, postoji pokušaj rješavanja. Zadatak 5: Pokušaj je napravljen, ali funkcija nije ispravno definirana niti korištena za provjeru parnosti svih triju brojeva.
- Cost for this evaluation: $0.02

## mudovici1@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "let trenutno_vrijeme = new Date();\nlet temperatura = 21;\n\nlet godina = trenutno_vrijeme.getFullYear();\n\nconsole.log(`Godina je: ${godina}-a, a teperatura je: ${temperatura}C`);"
        },
        {
            "js_code": "const PI = 3.14159;\nlet radijus = 4;\n\nlet opseg = 2 * PI * radijus;\nlet povrsina = PI * radijus**2;\n\nlet opseg_cm = opseg;\nlet opseg_mm = opseg * 10;\nlet povrsina_cm2 = povrsina;\nlet povrsina_dm2 = povrsina / 10;\n\nconsole.log(`Opseg kruga je: ${opseg_cm} cm odnosno ${opseg_mm} mm, dok je povrsina ${povrsina_cm2} cm2 odnosno ${povrsina_dm2} dm2`);\n"
        },
        {
            "js_code": "let vjezbanje_cilj = 30;\nlet vejzbanje_ostvarneo = 60;\nBoolean vjezbanje_rezultat;\n\nif (vjezbanje_ostvaerno >= vjezbanje_cilj){\n  vjezbanje_rezultat = true;\n}\n\n\n\n\n"
        },
        {
            "js_code": "let c = 8;\nlet d = 5;\nc = c - d;\nc = c + d;\nd = d + 20 + c;\nc = c * ++d;\nconsole.log(c);\nconsole.log(d);"
        },
        {
            "js_code": "let a = 2;\nlet b = 13;\nlet c = 17;\nlet parnost_broja;\n\n  if (a % 2 == 0){\n    parnost_broja = \"paran\";\n  }\n  if ( a % 2 != 0){\n    parnost_broja = \"neparan\";\n  }\n\nconsole.log(`Broj ${a} je ${parnost_broja}`)\n\n  if (b % 2 == 0){\n    parnost_broja = \"paran\";\n  }\n  if (b % 2 != 0){\n    parnost_broja = \"neparan\";\n  }\n  \n  console.log(`Broj ${b} je ${parnost_broja}`)\n  \n  if (c % 2 == 0){\n    parnost_broja = \"paran\";\n  }\n  if (c % 2 != 0){\n    parnost_broja = \"neparan\";\n  }\n  \n  console.log(`Broj ${c} je ${parnost_broja}`)"
        }
    ]
}
```

### Evaluation

- Task 1: 1.5
- Task 2: 2
- Task 3: 0.5
- Task 4: 2
- Task 5: 0.5

- Total Points: 6.5
- Feedback: Zadatak 1: Mali tipfeler u ispisu ('teperatura' umjesto 'temperatura'), ali logika je ispravna. Zadatak 2: Ispravno i precizno izračunati i ispisani opseg i površina kruga. Zadatak 3: Nedovršena logika i tipfeleri u imenima varijabli, nisu definirani svi potrebni elementi za provjeru cilja. Zadatak 4: Ispravno prevedeni izrazi bez korištenja zabranjenih operatora, dobro. Zadatak 5: Logika za provjeru parnosti je ispravna, ali nedostaje optimizacija koda (ponavljanje koda za svaku varijablu umjesto korištenja funkcije ili petlje).
- Cost for this evaluation: $0.03



# Total Cost for Evaluating d89Fk2
Total cost for running evaluations: $0.55