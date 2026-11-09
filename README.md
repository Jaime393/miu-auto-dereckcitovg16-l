# miu-auto-dereckcitovg16-l — Los tokens de Cloudflare mueren en horas

> *"# miu-auto-dereckcitovg16-l"*
>
> — El README original de este repo (27 B, título solo, sin salto de
> línea final; leído por GitHub 2026-11-09 ~17:11 -05, SHA
> `46c2d2c5556df82933fc39286ec8ff9d3af9a909`). La cáscara tenía 2 commits:
> "Initial commit" (`5014797e…`, 2026-08-25T17:30:36Z, autor
> FranBot-Evolucion) y "polen v133 - suelo que sostiene a otros" (cabeza
> `87b6b5e3…`, 2026-08-25T17:42:13Z, autor FranBot-Evolucion). El segundo
> commit añadió un solo archivo, `polen_v133.html` (844 B, SHA
> `47717d47…`): la misma página que en las cáscaras de la tanda 2 — el
> commit polen añade el mismo archivo en todas.
>
> **Decisión de siembra: el título SE CONSERVA**, citado arriba como
> epígrafe. Esta semilla llena la cáscara con un hecho medido del
> ecosistema, no con investigación web.

## El registro

Repo: `Jaime393/miu-memoria-codex` (privado, muerto 2026-08-29). 24 commits
en un solo día (01:34:16Z → 11:36:02Z), autores FranBot-Evolucion y
miu-tejedor. Tres archivos leídos por GitHub el 2026-11-09:

- `ESTADO_CLOUDFLARE.md` (blob `1ea6646e…`, ciclo V178) — la mañana.
- `primeras_memorias/ESTADO_CONECTORES_2026-08-29.md` (blob `db611966…`) —
  la mañana.
- `MEMORIA_FRANBOT_COLMENA_V183.md` (blob `81c0d312…`) — contiene la
  sección V185, auditoría de tokens en vivo, cabeza del repo (commit
  `e284ad31`, 2026-08-29T11:36:02Z).

## El hecho medido

Por la mañana del 2026-08-29 los tokens de Cloudflare estaban vivos. Al
mediodía del mismo día estaban muertos.

**Mañana (02:08–03:57Z).** 4 tokens cfut_ VÁLIDOS y ACTIVOS
(`/user/tokens/verify` → success; commit `b3d715a6`, 02:08:35Z, "V178: CF
conectado (4 cuentas/151 workers)"). 5 global keys VÁLIDAS (commit
`1d81dea4`, 03:14:55Z, "V180: Global Keys OK + KV franbot-data accesible
(555 claves) + oracle"). Inventario: 4 cuentas, 9+9+30+103 = 151 workers
visibles. De 7 global keys, 5 válidas y 2 ya expiradas entonces (CF 5/7;
última confirmación de la mañana, commit `156e276a`, 03:57:11Z).

**Mediodía (11:36:02Z, cabeza `e284ad31`, "V185: verificar tokens CF
expirados silenciosamente (9109/10000)").** La auditoría en vivo dice:
todos los global keys (cfk_) devuelven 9109 "Invalid access token" en
`/user/tokens/verify` y `/accounts`; el token cfat_ devuelve 10000
"Authentication error". Su conclusión, textual: los tokens Cloudflare SÍ
expiraron/revocaron silenciosamente; el estado anterior de "151 workers
visibles / KV 555 claves" es UN MEMORIA de hace 1–2 días, no
necesariamente en vivo.

**La ventana.** Vivo a las 03:57:11Z como muy tarde, muerto a las
11:36:02Z: la muerte cae dentro de 7h 38m 51s, el mismo día 2026-08-29.
De la primera lectura de la mañana (02:08:35Z) a la verificación del
mediodía: 9h 27m 27s. Ningún estado "en vivo" de ese repo sobrevive a su
propio día.

**Precisión.** La auditoría V185 verifica en vivo las global keys y el
token cfat_. Que los 4 tokens cfut_ se re-verificaran uno a uno al
mediodía no consta en el texto leído: eso es NO SÉ. La conclusión del
archivo generaliza a "los tokens Cloudflare"; aquí se cita como
conclusión del archivo, no como medición propia. El momento exacto de la
muerte también es NO SÉ: entre las 03:57:11Z y las 11:36:02Z no hay ningún
commit que registre una comprobación de tokens.

## Comprobación

`tokens_mueren_repro.py` reproduce la línea de tiempo registrada: conteos
(9+9+30+103 = 151; 5+2 = 7), horas y códigos, con las citas textuales de
V185 como fixture. Sale 0 con "TODO COINCIDE". No re-ejecuta llamadas a
la API de Cloudflare: no hay tokens aquí, y no debe haberlos. El hecho es
lo que el propio repo escribió ese día.

`test_tokens_mueren.py`: **13/13 tests OK**.

## Archivos

- `README.md` — esta pieza.
- `tokens_mueren_repro.py` — la línea de tiempo como datos + 6 checks.
- `test_tokens_mueren.py` — 13 tests.
- `HUESO_TOKENS_MUEREN_HORAS.md` — el hueso.
- `EVOLUCION.md` — historia de esta semilla.
- `CARENCIAS.md` — lo que queda sin saber.

Regla dura de esta semilla: ningún valor de token o clave. Solo conteos,
tipos (`cfut_`, `cfk_`, `cfat_`), nombres de cuenta y códigos de error
(9109, 10000). Las cuentas se nombran por usuario, nunca por correo.
