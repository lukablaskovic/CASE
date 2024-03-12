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

## alabinjan@student.unipu.hr

### Code

```javascript
{
    "code_snippets": [
        {
            "js_code": "function sve_o_krugu(r){\n  function povrsina(r) {\n    return Math.PI * r**2;\n  }\n  \n  const opseg = opseg_f(r){\n    return 2 * Math.PI * r;\n  };\n  \n  const p = povrsina(r);\n  const o = opseg(r);\n  const zbroj = p+o;\n  \n  console.log(\"Povr\u0161ina iznosi: \" + p);\n  console.log(\"Opseg iznosi: \" + o);\n  \n  return zbroj;\n}\n\nconst zbroj = sve_o_krugu(3);\nconsole.log(\"Zbroj povr\u0161ine i opsega iznosi: \" + zbroj);"
        }
    ]
}
```

### Evaluation

- Task 1: 2
- Task 2: 1.5
- Task 3: 0
- Task 4: 0
- Task 5: 0

- Total Points: 3.5
- Feedback: Zadatak 1: Odlično, sve je ispravno implementirano. Zadatak 2: Dobra logika, ali nedostaju izračunate vrijednosti za mm i dm2, te postoji greška u deklaraciji funkcije za opseg. Zadatak 3: Nije pokušano. Zadatak 4: Nije pokušano. Zadatak 5: Nije pokušano.
- Cost for this evaluation: $0.02



# Total Cost for Evaluating krug
Total cost for running evaluations: $0.02