# Analisi dei File Non Utilizzati - Progetto XAI

## Riepilogo

Questo documento fornisce un'analisi dei file che NON sono utilizzati nel processo di build Jekyll del sito.

## File NON Utilizzati nella Build

### 📄 File di Documentazione (8 file)
Questi file sono esclusi dalla build ma sono **essenziali** per sviluppatori e contributori:
- `README.md`
- `FAQ.md`
- `INSTALL.md`
- `README_DEPLOYMENT.md`
- `CONTRIBUTING.md`
- `CUSTOMIZE.md`
- `CITATION_EXAMPLE.md`
- `lighthouse_results/` (risultati test prestazioni)

**Raccomandazione:** ✅ **Mantenere** - Necessari per la documentazione del progetto

### 🛠️ Script Utility (5 file)

**Script Documentati (da mantenere):**
- ✅ `create_news.ipynb` - Usato per creare news (documentato in README.md)
- ✅ `import_calendar.py` - Aggiorna pagina seminari da Google Calendar (documentato in README.md)
- ✅ `import_calendar.ipynb` - Versione debug dello script calendario (documentato in README.md)

**Script Non Documentati (da verificare):**
- ❓ `read_news.ipynb` - Non documentato nel README
- ❓ `redirect-script.sh` - Non documentato nel README

**Raccomandazione:** ✅ Mantenere gli script documentati | ⚠️ Verificare se gli altri 2 sono ancora necessari

### 📁 Directory di Output (2 directory)
- `docs/` - Directory di output della build Jekyll
- `readme_preview/` - Immagini di anteprima per la documentazione

**Raccomandazione:** ✅ **Mantenere** - Utilizzate per deployment e documentazione

## Statistiche

- **Totale file non utilizzati nella build:** 15
- **File da mantenere:** 13
- **File candidati per rimozione:** 2 (read_news.ipynb, redirect-script.sh)

## Conclusione

Il progetto è ben mantenuto con pochissimi file veramente inutilizzati. La maggior parte dei file che non sono direttamente utilizzati nella build servono per:
- 📖 Documentazione (README, FAQ, guide di installazione)
- 🔧 Gestione contenuti (script per news e calendario)
- 🚀 CI/CD e deployment
- 🖼️ Assets di documentazione

### Azione Consigliata

Si raccomanda di:
1. ✅ **Mantenere** tutti i file di documentazione
2. ✅ **Mantenere** gli script documentati (create_news.ipynb, import_calendar.py, import_calendar.ipynb)
3. ⚠️ **Verificare** se read_news.ipynb e redirect-script.sh sono ancora necessari
4. ℹ️ Se non più necessari, considerare di rimuovere solo questi 2 file

## Riferimento Completo

Per l'analisi dettagliata in inglese, consultare: `UNUSED_FILES_REPORT.md`
