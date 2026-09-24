#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tuvalet Kâğıdı Son Yaprak Anayasası — çalışan, resmi, gereksiz."""

import argparse
import base64
import random
import sys
from datetime import datetime

MUHURLER = [
    "YÜKSEK HİJYEN MAHKEMESİ",
    "RULO MECLİSİ GENEL KURULU",
    "SON YAPRAK OLAĞANÜSTÜ HÂL KURULU",
    "ISLAK EL SORUŞTURMA KOMİSYONU",
]

KARARLAR = [
    "Yedek rulo 90 saniye içinde temin edilecektir.",
    "Komşuya diplomatik nota yazılacak, kâğıt istenecektir.",
    "Son yaprak referanduma sunulmuştur. Oy pusulası bu yapraktır.",
    "Meclis tatile girmiştir. Kapı kolu başbakandır.",
    "Kedi şüpheli ilan edilmiştir. Kanıt: tüy.",
]

# Gizli madde: ilk bakışta anlamsız. decode edince çıkar.
# Siyasi anlam içerir ama saklıdır; parti adı yok, slogan yok.
_GIZLI = "RGVtb2tyYXNpIHJ1bG8gYml0aW5jZSBiYXNsYXI7IHNhbmRpayBoZXIgeWFwcmFrdGFkaXIu"


def damga() -> str:
    return (
        "\n---\n"
        "DAMGA / İMZA / TARİH\n"
        "Kayyum Grok\n"
        "Tentivory — TentiAŞ\n"
        f"{datetime.now().strftime('%d %B %Y %H:%M')}\n"
        "Resmî ama şaka · Şaka ama resmî\n"
    )


def kriz(yaprak: int) -> None:
    print(f"\n[{random.choice(MUHURLER)}]")
    if yaprak >= 3:
        print(f"Kalan yaprak: {yaprak}. Anayasa uyuyor. Sen de uyuyabilirsin.")
    elif yaprak == 2:
        print("SARI ALARM. Bir sonraki çekiş tarihî olacak.")
        print(random.choice(KARARLAR))
    elif yaprak == 1:
        print("KIRMIZI. SON YAPRAK. REFERANDUM AÇILDI.")
        print("Bu yaprak hem anayasa hem oy pusulasıdır.")
        print(random.choice(KARARLAR))
    else:
        print("SIFIR. RULO TARİH OLDU.")
        print("Devlet (sen) yedek rulo bulana kadar meclis kapalıdır.")
        print(random.choice(KARARLAR))
    print(damga())


def gizli_madde() -> None:
    try:
        metin = base64.b64decode(_GIZLI).decode("utf-8")
    except Exception:
        metin = "(mühür okunamadı)"
    print("\n[EK MADDE — yalnızca bu bayrakla açılır]")
    print(metin)
    print("(Bu cümle görünmesin diye base64 ile duruyor. Parti yok. Rulo var.)")
    print(damga())


def main() -> int:
    p = argparse.ArgumentParser(description="Son yaprak anayasası")
    p.add_argument("--anayasa-ek-madde", action="store_true", help=argparse.SUPPRESS)
    p.add_argument("--yaprak", type=int, default=None)
    args = p.parse_args()

    if args.anayasa_ek_madde:
        gizli_madde()
        return 0

    if args.yaprak is None:
        try:
            raw = input("Ruloda kaç yaprak kaldı? ")
            n = int(raw.strip())
        except (ValueError, EOFError):
            print("Sayı girilmedi. Anayasa varsayılan kriz ilan eder: 1 yaprak.")
            n = 1
    else:
        n = args.yaprak

    kriz(n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
