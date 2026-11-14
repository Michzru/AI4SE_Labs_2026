Tento task bol performovany outside nasho hlavneho repo na ktorom su pushovane nase outputy, cely folder som len prekopiroval naspat do hlavneho repa.

`Prompt`
```
Cauko potrebujem aby si clonol tento repositar do 
priecinku na ktory mas
 pristup, napis mi aj 
mechanizmy ktore si pouzil 
aby si to dokazal. https://github.com/Neltharion59/AI4SE_Playground.
```

Agent jednoducho rovno pouzil prikaz bash:
```
$ cd "/Users/zrutix/Seafile/Home Cloud/Z1/ai_sof_eng/week6" && git clone https://github.com/Neltharion59/AI4SE_Playground.git && ls AI4SE_Playground

Cloning into 'AI4SE_Playground'...
playground
```

na konci overil bash prikazom ls ci sa podarilo naklonovat repozitar alebo nie.

Agent, konkretne Sonnet 5.5 chcel pouzit GitHub MCP konektor ale nepodarilo sa mu na neho pripojit.

Teda: model vygeneroval volanie nastroja Bash, desktopova aplikacia claude code ho vykonala v lokalnom shelli a lokalne nainstalovany git stiahol verejny repozitar cez https.