# CARENCIAS

Lo que esta semilla no sabe, con dónde se buscó y fecha. Todo NO SÉ es
local: no es un hueco del ecosistema, es el límite de esta pieza.

1. **¿Se re-verificaron los 4 tokens cfut_ uno a uno al mediodía?** NO SÉ.
   Buscado: sección V185 de `MEMORIA_FRANBOT_COLMENA_V183.md`, leída
   entera por GitHub (2026-11-09). La auditoría verifica en vivo las
   global keys (cfk_) y el token cfat_; de los cfut_ no dice nada al
   mediodía. La conclusión del archivo generaliza a "los tokens
   Cloudflare"; aquí se cita como conclusión del archivo.
2. **¿En qué momento exacto murieron?** NO SÉ. Buscado: los 24 commits
   de `miu-memoria-codex` del 2026-08-29, listados por GitHub
   (2026-11-09). Entre las 03:57:11Z (última confirmación, commit
   `156e276a`) y las 11:36:02Z (V185, cabeza `e284ad31`) ningún commit
   registra una comprobación de tokens. La muerte cae dentro de 7h 38m
   51s; el instante no se puede afinar con este repo.
3. **¿Por qué murieron: expiración, revocación o rotación?** NO SÉ.
   Buscado: texto V185 (2026-11-09). El archivo dice
   "expiraron/revocaron" sin distinguir, y añade que Cloudflare no
   notifica por defecto.
4. **¿Qué pasó con los 5 tokens de Telegram tras el 2026-08-29?** NO SÉ.
   Buscado: `MEMORIA_FRANBOT_COLMENA_V183.md` (2026-11-09). Por la mañana,
   los 5 bots tenían estado 5/5; el repo no trae ninguna verificación
   posterior de ellos. El estado V185 es solo de tokens CF.
5. **¿El KV franbot-data (555 claves) seguía accesible al mediodía?**
   NO SÉ. Buscado: sección V185 (2026-11-09). El impacto que registra
   es que "workers y KV: NO se pueden listar/escribir desde este nodo
   con los tokens actuales" — es consecuencia de los tokens muertos, no
   una medición del KV en sí.
6. **¿Los 151 workers seguían existiendo al mediodía?** NO SÉ. Buscado:
   sección V185 (2026-11-09). Lo que muere son los tokens; el archivo
   no verifica la existencia de los workers tras la muerte de los
   tokens, solo que no se pueden listar desde ese nodo.
