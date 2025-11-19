# Come Citare Lavori in Bibliografia

## Sintassi per Citazioni Inline

Per citare un singolo lavoro:
```markdown
Our first proposal is LORE presented in {% cite GMG2019 %}.
```

Per citare più lavori insieme:
```markdown
From the surveys {% cite GMR2018 BGG2021 %}, we developed...
```

## Esempio Completo di Conversione

### PRIMA (riferimenti manuali):
```markdown
From the surveys [ GMR2018 , BGG2021 ], we developed...

Our first proposal is LORE presented in [GMG2019].

We instantiated LLORE for images [GMG2019, GMM2020], time series [GMS2020]...

In [PGM2019] and [PPP2020], we addressed...
```

### DOPO (citazioni jekyll-scholar):
```markdown
From the surveys {% cite GMR2018 BGG2021 %}, we developed...

Our first proposal is LORE presented in {% cite GMG2019 %}.

We instantiated LLORE for images {% cite GMG2019 GMM2020 %}, time series {% cite GMS2020 %}...

In {% cite PGM2019 PPP2020 %}, we addressed...
```

## Aggiungere Bibliografia a Fine Sezione

Alla fine della pagina, PRIMA della sezione "Line 1 - Publications", aggiungi:

```markdown
---

## References
{% bibliography --cited %}

---
```

Questo genererà automaticamente la bibliografia di TUTTI i lavori citati nella pagina con {% cite %}.

## Alternative: Bibliografia Filtrata per Linea

Se vuoi mantenere la sezione attuale che mostra tutti i lavori della linea 1:

```markdown
---

## References (Cited Works)
{% bibliography --cited %}

---

## Line 1 - All Publications
<div class="publications">
{% bibliography --query @*[line~=1] %}
</div>
```

## Note Importanti

1. Gli ID nelle citazioni devono corrispondere agli ID nel file .bib (es: GMG2019)
2. `{% cite %}` crea riferimenti numerati o alfabetici (dipende dalla configurazione)
3. `{% bibliography --cited %}` genera solo i lavori citati con {% cite %}
4. `{% bibliography --query @*[line~=1] %}` genera tutti i lavori della linea 1

## Configurazione Style Citazioni

Nel file `_config.yml`, nella sezione `scholar:`, modifica il campo `style:` per cambiare lo stile delle citazioni.

### Stili Disponibili (Esempi)

#### 1. **APA (American Psychological Association)** - Attuale
```yaml
style: apa
```
**Nel testo:** (Guidotti et al., 2019)  
**In bibliografia:** Guidotti, R., Monreale, A., Ruggieri, S., Turini, F., Giannotti, F., & Pedreschi, D. (2019). A survey of methods for explaining black box models. *ACM Computing Surveys*, 51(5), 1-42.

---

#### 2. **IEEE (Institute of Electrical and Electronics Engineers)**
```yaml
style: ieee
```
**Nel testo:** [1]  
**In bibliografia:** [1] R. Guidotti, A. Monreale, S. Ruggieri, F. Turini, F. Giannotti, and D. Pedreschi, "A survey of methods for explaining black box models," *ACM Computing Surveys*, vol. 51, no. 5, pp. 1-42, 2019.

---

#### 3. **Chicago Author-Date**
```yaml
style: chicago-author-date
```
**Nel testo:** (Guidotti et al. 2019)  
**In bibliografia:** Guidotti, Riccardo, Anna Monreale, Salvatore Ruggieri, Franco Turini, Fosca Giannotti, and Dino Pedreschi. 2019. "A Survey of Methods for Explaining Black Box Models." *ACM Computing Surveys* 51 (5): 1–42.

---

#### 4. **Chicago Fullnote (con note a piè di pagina)**
```yaml
style: chicago-fullnote-bibliography
```
**Nel testo:** ¹  
**In bibliografia:** Guidotti, Riccardo, Anna Monreale, Salvatore Ruggieri, Franco Turini, Fosca Giannotti, and Dino Pedreschi. "A Survey of Methods for Explaining Black Box Models." *ACM Computing Surveys* 51, no. 5 (2019): 1–42.

---

#### 5. **MLA (Modern Language Association)**
```yaml
style: modern-language-association
```
**Nel testo:** (Guidotti et al.)  
**In bibliografia:** Guidotti, Riccardo, et al. "A Survey of Methods for Explaining Black Box Models." *ACM Computing Surveys*, vol. 51, no. 5, 2019, pp. 1-42.

---

#### 6. **Nature**
```yaml
style: nature
```
**Nel testo:** ¹  
**In bibliografia:** 1. Guidotti, R. *et al.* A survey of methods for explaining black box models. *ACM Comput. Surv.* **51**, 1–42 (2019).

---

#### 7. **Science**
```yaml
style: science
```
**Nel testo:** (1)  
**In bibliografia:** 1. R. Guidotti, A. Monreale, S. Ruggieri, F. Turini, F. Giannotti, D. Pedreschi, A survey of methods for explaining black box models. *ACM Comput. Surv.* **51**, 1-42 (2019).

---

#### 8. **Harvard**
```yaml
style: harvard-cite-them-right
```
**Nel testo:** (Guidotti et al., 2019)  
**In bibliografia:** Guidotti, R., Monreale, A., Ruggieri, S., Turini, F., Giannotti, F. and Pedreschi, D. (2019) 'A survey of methods for explaining black box models', *ACM Computing Surveys*, 51(5), pp. 1-42.

---

#### 9. **Vancouver (Medicina)**
```yaml
style: vancouver
```
**Nel testo:** (1)  
**In bibliografia:** 1. Guidotti R, Monreale A, Ruggieri S, Turini F, Giannotti F, Pedreschi D. A survey of methods for explaining black box models. ACM Comput Surv. 2019;51(5):1-42.

---

#### 10. **ACM (Association for Computing Machinery)**
```yaml
style: association-for-computing-machinery
```
**Nel testo:** [Guidotti et al. 2019]  
**In bibliografia:** Riccardo Guidotti, Anna Monreale, Salvatore Ruggieri, Franco Turini, Fosca Giannotti, and Dino Pedreschi. 2019. A survey of methods for explaining black box models. *ACM Comput. Surv.* 51, 5 (2019), 1–42.

---

#### 11. **Springer Basic (Author-Year)**
```yaml
style: springer-basic-author-date
```
**Nel testo:** (Guidotti et al. 2019)  
**In bibliografia:** Guidotti R, Monreale A, Ruggieri S, Turini F, Giannotti F, Pedreschi D (2019) A survey of methods for explaining black box models. ACM Comput Surv 51(5):1–42

---

#### 12. **Elsevier Harvard**
```yaml
style: elsevier-harvard
```
**Nel testo:** (Guidotti et al., 2019)  
**In bibliografia:** Guidotti, R., Monreale, A., Ruggieri, S., Turini, F., Giannotti, F., Pedreschi, D., 2019. A survey of methods for explaining black box models. ACM Comput. Surv. 51, 1–42.

---

### Come Cambiare Stile

Nel file `_config.yml`, cerca la sezione:
```yaml
scholar:
  last_name: [Einstein]
  first_name: [Albert, A.]
  
  style: apa  # <-- CAMBIA QUI
  locale: en
```

Sostituisci `apa` con uno degli stili sopra elencati.

### Altri Stili Popolari

- `apa-6th-edition` - APA 6th edition
- `apa-7th-edition` - APA 7th edition (più recente)
- `chicago-note-bibliography` - Chicago con note
- `ieee-with-url` - IEEE con URL inclusi
- `cell` - Stile Cell (biologia)
- `american-medical-association` - AMA (medicina)
- `american-chemical-society` - ACS (chimica)
- `american-physics-society` - APS (fisica)

### Repository Completo Stili CSL

Tutti gli stili sono disponibili su: **https://github.com/citation-style-language/styles**

Puoi cercare uno stile specifico per la tua disciplina o journal.
