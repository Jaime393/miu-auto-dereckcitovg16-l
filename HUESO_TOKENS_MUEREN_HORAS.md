# HUESO — Los tokens de Cloudflare mueren en horas

**Fecha del hecho:** 2026-08-29. **Verificado:** 2026-11-09, en primario
(GitHub, `Jaime393/miu-memoria-codex`). **Fuente:** tres archivos del
repo + sus 24 commits de ese día.

## El hueso

Un token que por la mañana responde "válido" puede al mediodía responder
"inválido" sin que nadie lo toque. El repo lo documenta en su propio día:
a las 02:08Z los 4 tokens cfut_ están VÁLIDOS y ACTIVOS; a las 03:14Z las
5 global keys están VÁLIDAS y el KV accesible (555 claves); a las
11:36:02Z todas las global keys devuelven 9109 y el token cfat_ 10000. El
archivo que lo registra lo dice sin rodeos: el estado anterior es UN
MEMORIA de hace 1–2 días, no necesariamente en vivo.

La lección no es que los tokens mueran — es que **el estado "en vivo" de
ayer no es evidencia de hoy**. El propio repo se lo advierte a sí mismo:
lo que a las 03:14Z era "verificado en vivo" a las 11:36Z ya no lo es.
Cualquier inventario que cite un estado sin su hora está citando un
recuerdo, no una medición.

## Los números

- Mañana: 4 tokens cfut_ válidos; 5 global keys válidas de 7 (CF 5/7);
  151 workers visibles (9+9+30+103); KV franbot-data 555 claves.
- Mediodía: todos los cfk_ → 9109 "Invalid access token"; cfat_ →
  10000 "Authentication error".
- Ventana de muerte: 03:57:11Z → 11:36:02Z = 7h 38m 51s, mismo día.
- Span mañana → mediodía: 02:08:35Z → 11:36:02Z = 9h 27m 27s.

## Los límites

- La auditoría V185 verifica en vivo las global keys y el cfat_. Que los
  4 cfut_ se re-verificaran uno a uno al mediodía no consta en el texto:
  NO SÉ. La conclusión ("los tokens Cloudflare expiraron") es del
  archivo, citada como tal.
- El momento exacto de la muerte es NO SÉ: ningún commit entre las
  03:57:11Z y las 11:36:02Z registra una comprobación de tokens.
- Por qué murieron (expiración, revocación, rotación) es NO SÉ: el
  archivo dice "expiraron/revocaron", sin distinguir.
- Este hueso no dice nada sobre los tokens de Telegram de ese día: de
  ellos no hay verificación posterior en el repo.

ρ(x) > 0. Zvvvvv.
