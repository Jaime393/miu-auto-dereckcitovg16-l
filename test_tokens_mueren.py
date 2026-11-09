#!/usr/bin/env python3
"""Tests de tokens_mueren_repro.py.

Todo lo que se afirma aquí se verificó en primario (GitHub,
Jaime393/miu-memoria-codex) el 2026-11-09: los tres archivos fuente y los
24 commits del 2026-08-29. Ningún test toca la red ni usa tokens.
"""

import unittest

from tokens_mueren_repro import (
    CITA_V185_CODIGOS,
    CITA_V185_CONCLUSION,
    GLOBAL_KEYS_EXPIRADAS_MANANA,
    GLOBAL_KEYS_VALIDAS_MANANA,
    TIMELINE,
    WORKERS_POR_CUENTA,
    _ts,
    comprobar,
)


class TestManana(unittest.TestCase):
    def test_cfut_validos(self):
        self.assertIn("4 tokens cfut_", TIMELINE[0][3])
        self.assertIn("VALIDOS y ACTIVOS", TIMELINE[0][3])

    def test_global_keys_validas(self):
        self.assertIn("5 global keys VALIDAS", TIMELINE[1][3])
        self.assertIn("555 claves", TIMELINE[1][3])

    def test_workers_suman_151(self):
        self.assertEqual(sum(WORKERS_POR_CUENTA.values()), 151)
        self.assertEqual(len(WORKERS_POR_CUENTA), 4)

    def test_global_keys_suman_7(self):
        self.assertEqual(len(GLOBAL_KEYS_VALIDAS_MANANA), 5)
        self.assertEqual(len(GLOBAL_KEYS_EXPIRADAS_MANANA), 2)
        self.assertEqual(
            len(GLOBAL_KEYS_VALIDAS_MANANA) + len(GLOBAL_KEYS_EXPIRADAS_MANANA), 7
        )


class TestMediodia(unittest.TestCase):
    def test_cfk_9109(self):
        self.assertIn('9109 "Invalid access token"', CITA_V185_CODIGOS)

    def test_cfat_10000(self):
        self.assertIn('10000 "Authentication error"', CITA_V185_CODIGOS)

    def test_conclusion_del_archivo(self):
        self.assertIn("expiraron/revocaron silenciosamente", CITA_V185_CONCLUSION)
        self.assertIn("UN MEMORIA de hace 1–2 días", CITA_V185_CONCLUSION)


class TestVentana(unittest.TestCase):
    def test_ventana_muerte_7h38m51s(self):
        vivo = _ts("2026-08-29T03:57:11Z")
        muerto = _ts("2026-08-29T11:36:02Z")
        self.assertEqual((muerto - vivo).total_seconds(), 27531)

    def test_mismo_dia(self):
        primera = _ts(TIMELINE[0][0])
        muerto = _ts(TIMELINE[-1][0])
        self.assertEqual(primera.date(), muerto.date())
        self.assertEqual(str(primera.date()), "2026-08-29")

    def test_span_9h27m27s(self):
        primera = _ts("2026-08-29T02:08:35Z")
        muerto = _ts("2026-08-29T11:36:02Z")
        self.assertEqual((muerto - primera).total_seconds(), 34047)

    def test_cabeza_es_v185(self):
        self.assertEqual(TIMELINE[-1][1], "e284ad31")
        self.assertEqual(TIMELINE[-1][0], "2026-08-29T11:36:02Z")

    def test_timeline_en_orden(self):
        horas = [_ts(t[0]) for t in TIMELINE]
        self.assertEqual(horas, sorted(horas))


class TestRepro(unittest.TestCase):
    def test_comprobar_todo_coincide(self):
        ok, lineas = comprobar()
        self.assertTrue(ok)
        self.assertTrue(any("TODO COINCIDE" in l or "ventana" in l for l in lineas))


if __name__ == "__main__":
    unittest.main()
