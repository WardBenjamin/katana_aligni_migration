# /// script
# requires-python = ">=3.15"
# ///
"""Duty estimate for the 600-camera ELP order (PI ELPFP2026012704C). Rates: see docs/assembly-price/research/camera-tariffs.md."""
QTY, VALUE = 600, 74_160.00      # EXW goods value, proforma invoice
MPF_RATE, MPF_MIN, MPF_MAX = 0.003464, 33.58, 651.50  # FY2026 (Oct 2025 - Sep 2026)

def run(name, rates, value=VALUE):
    duty = value * sum(rates.values())
    mpf = min(max(value * MPF_RATE, MPF_MIN), MPF_MAX)
    print(f"{name:42s} rate {sum(rates.values()):6.1%}  duty ${duty:10,.2f}  per cam ${duty/QTY:6.2f}  +MPF ${mpf:6.2f} -> ${duty+mpf:10,.2f}")
    return duty

lo  = run("LOW  8525.89.40 (301 List 4A 7.5%) + S122", {"301": .075, "s122": .10})
lo2 = run("LOW2 8525.89.30 + S122 refunded/void",      {"301": .25})
mid = run("LIKELY 8525.89.30 (301 List 3) + S122",      {"301": .25, "s122": .10})
hi  = run("HIGH same stack, value incl. $2,095 freight", {"301": .25, "s122": .10}, value=VALUE + 2095)
assert round(mid, 2) == 25_956.00 and round(lo, 2) == 12_978.00 and round(lo2, 2) == 18_540.00
