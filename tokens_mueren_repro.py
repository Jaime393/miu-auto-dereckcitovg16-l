#!/usr/bin/env python3
"""Reproduce el hecho: los tokens de Cloudflare mueren en horas, el mismo día.

Fuente primaria: repo Jaime393/miu-memoria-codex, 2026-08-29 (24 commits,
01:34:16Z -> 11:36:02Z). Tres archivos leídos por GitHub el 2026-11-09:

- ESTADO_CLOUDFLARE.md (blob 1ea6646e...) — ciclo V178, mañana.
- primeras_memorias/ESTADO_CONECTORES_2026-08-29.md (blob db611966...) — mañana.
- MEMORIA_FRANBOT_COLMENA_V183.md (blob 81c0d312...) — contiene la sección
  V185, auditoría de tokens en vivo, cabeza del repo (commit e284ad31).

Lo que se reproduce aquí es la línea de tiempo registrada en esos archivos
y en los mensajes de commit: conteos, horas y códigos. NO se re-ejecutan
llamadas a la API de Cloudflare (no hay tokens aquí, y no debe haberlos):
el hecho es lo que el propio repo escribió ese día, no una medición nueva.

Regla dura de esta semilla: ningún valor de token o clave. Solo conteos,
tipos (cfut_, cfk_, cfat_), nombres de cuenta y códigos de error (9109,
10000). Las cuentas se nombran por usuario, nunca por correo.
"""

from datetime import datetime, timezone

# --- La línea de tiempo, tal como la registran los commits (UTC) ---
# Cada entrada: (hora ISO, commit, mensaje, qué afirma)
TIMELINE = [
    ("2026-08-29T02:08:35Z", "b3d715a6",
     "V178: CF conectado (4 cuentas/151 workers) + heartbeat ALFONSO + semilla",
     "4 tokens cfut_ VALIDOS y ACTIVOS (verify -> success)"),
    ("2026-08-29T03:14:55Z", "1d81dea4",
     "V180: Global Keys OK + KV franbot-data accesible (555 claves) + oracle",
     "5 global keys VALIDAS; KV franbot-data accesible (555 claves)"),
    ("2026-08-29T03:57:11Z", "156e276a",
     "V182: credenciales validadas (CF 5/7, apis, TG 5 bots + admin_id)",
     "Ultima confirmacion de la manana: CF 5/7"),
    ("2026-08-29T11:36:02Z", "e284ad31",
     "V185: verificar tokens CF expirados silenciosamente (9109/10000)",
     "CABEZA: todos los cfk_ devuelven 9109; cfat_ devuelve 10000"),
]

# --- Los conteos de la mañana (ESTADO_CONECTORES_2026-08-29.md) ---
# 4 cuentas con workers visibles: 9 + 9 + 30 + 103.
WORKERS_POR_CUENTA = {
    "frrussell81": 9,
    "jhuarcaya938": 9,
    "dieguito.vg16": 30,
    "jaimep.viccente": 103,
}

# Global keys (MEMORIA_FRANBOT_COLMENA_V183.md, seccion Conectores):
# 5 validas por la manana, 2 ya expiradas entonces.
GLOBAL_KEYS_VALIDAS_MANANA = [
    "jaimepvicente", "jhuarcaya938", "dieguito.vg16",
    "jaimedanielmartinez75", "franchescopalacios9",
]
GLOBAL_KEYS_EXPIRADAS_MANANA = ["frrussell81", "jaimep.viccente"]

# --- Las citas textuales (V185, MEMORIA_FRANBOT_COLMENA_V183.md) ---
CITA_V185_CODIGOS = (
    'todos los global keys (cfk_) devuelven 9109 "Invalid access token" '
    "en /user/tokens/verify y /accounts. "
    'El token cfat_ devuelve 10000 "Authentication error".'
)
CITA_V185_CONCLUSION = (
    "CONCLUSIÓN: los tokens Cloudflare SÍ expiraron/revocaron "
    "silenciosamente. Cloudflare no notifica por defecto — el diagnóstico "
    'anterior ("los tokens funcionan") ya NO es válido. El estado anterior '
    'de "151 workers visibles / KV 555 claves" es UN MEMORIA de hace 1–2 '
    "días, no necesariamente en vivo."
)


def _ts(iso):
    return datetime.fromisoformat(iso.replace("Z", "+00:00"))


def comprobar():
    """Devuelve (ok, lista_de_lineas). ok es True solo si todo coincide."""
    lineas = []
    ok = True

    # 1. La mañana: 4 tokens cfut_ válidos y 5 global keys válidas.
    manana = TIMELINE[0][3] + " | " + TIMELINE[1][3]
    lineas.append("manana: " + manana)

    # 2. Los conteos cuadran: 9+9+30+103 = 151; 5+2 = 7.
    total_workers = sum(WORKERS_POR_CUENTA.values())
    if total_workers != 151:
        ok = False
        lineas.append("DEFECTO: workers suman %d, no 151" % total_workers)
    else:
        lineas.append("cuentas: 9+9+30+103 = 151 workers visibles")
    total_keys = len(GLOBAL_KEYS_VALIDAS_MANANA) + len(GLOBAL_KEYS_EXPIRADAS_MANANA)
    if total_keys != 7:
        ok = False
        lineas.append("DEFECTO: global keys suman %d, no 7" % total_keys)
    else:
        lineas.append("global keys: 5 validas + 2 expiradas = 7 (CF 5/7)")

    # 3. El mediodía: todos los cfk_ 9109, cfat_ 10000 (cita V185).
    if '9109 "Invalid access token"' not in CITA_V185_CODIGOS:
        ok = False
        lineas.append("DEFECTO: falta el 9109 en la cita V185")
    if '10000 "Authentication error"' not in CITA_V185_CODIGOS:
        ok = False
        lineas.append("DEFECTO: falta el 10000 en la cita V185")
    lineas.append("mediodia: todos los cfk_ -> 9109; cfat_ -> 10000")

    # 4. La ventana de muerte: vivo a las 03:57:11Z, muerto a las 11:36:02Z.
    vivo = _ts("2026-08-29T03:57:11Z")
    muerto = _ts("2026-08-29T11:36:02Z")
    ventana = muerto - vivo
    if ventana.total_seconds() != 27531:
        ok = False
        lineas.append("DEFECTO: ventana %s, no 7h38m51s" % ventana)
    else:
        lineas.append("ventana de muerte: 03:57:11Z -> 11:36:02Z = 7h38m51s")

    # 5. Mismo día: primera lectura de la mañana y verificación del mediodía.
    primera = _ts(TIMELINE[0][0])
    if primera.date() != muerto.date():
        ok = False
        lineas.append("DEFECTO: la manana y el mediodia no son el mismo dia")
    else:
        lineas.append("mismo dia: 2026-08-29 (primera lectura 02:08:35Z)")
    span = muerto - primera
    if span.total_seconds() != 34047:
        ok = False
        lineas.append("DEFECTO: span %s, no 9h27m27s" % span)
    else:
        lineas.append("span manana->mediodia: 9h27m27s")

    # 6. Orden cronológico de la línea de tiempo y cabeza = V185.
    horas = [_ts(t[0]) for t in TIMELINE]
    if horas != sorted(horas):
        ok = False
        lineas.append("DEFECTO: la linea de tiempo no esta en orden")
    if TIMELINE[-1][1] != "e284ad31":
        ok = False
        lineas.append("DEFECTO: la cabeza no es e284ad31 (V185)")
    else:
        lineas.append("cabeza: e284ad31 V185, 2026-08-29T11:36:02Z")

    return ok, lineas


if __name__ == "__main__":
    ok, lineas = comprobar()
    for linea in lineas:
        print(linea)
    print("TODO COINCIDE" if ok else "NO COINCIDE")
    raise SystemExit(0 if ok else 1)
