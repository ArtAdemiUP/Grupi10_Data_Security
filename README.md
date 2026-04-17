# Grupi10_Data_Security
# 🔐 Beale Cipher Implementation

Ky projekt është realizuar në kuadër të lëndës **Siguria e të Dhënave**. Ai implementon algoritmin e njohur si **Beale Cipher** (Shifra e Beale-it), i cili shfrytëzon një dokument teksti (`.txt`) si çelës për enkriptimin dhe dekriptimin e mesazheve.

## 📖 Rreth Projektit
Beale Cipher është një formë e "Shifrës së Librit". Siguria e tij bazohet në një tekst burimor të gjatë. Çdo shkronjë e mesazhit sekret zëvendësohet me numrin rendor të një fjale në libër që fillon me atë shkronjë.

### Karakteristikat:
* **Homophonic Substitution:** E njëjta shkronjë mund të kodohet me numra të ndryshëm, duke e bërë rezistent ndaj analizës së frekuencës.
* **Dynamic Key:** Çelësi (libri) mund të ndërrohet lehtësisht duke zëvendësuar skedarin `libri.txt`.
* **Clean Code:** Kodi është i ndarë në module logjike për menaxhim më të lehtë.
