# ECAD open PRs and the bollard interposer

Read 2026-11-13T05:00Z with `gh pr list -R airgarage/tripwire-ecad --state open` and `git -C repos/tripwire-ecad fetch origin` (fetch only; no checkout). `tripwire-mcad` has no open PRs.

- https://github.com/airgarage/tripwire-ecad/pull/27, "[HW-892- Add side mount led to the sensor interposer pcb and fix", branch `monti/hw-892-add-side-mount-led-to-the-sensor-interposer-pcb`, open, updated 2026-10-27T16:38Z. Body: fixes an undervoltage lockout on the TI eFuse at 12 V by pulling the reference pin high, and adds a side-mount LED. Commits a9e4165 "Adds updated boards as produced and built for X4B" and merge a6baf8a. Changes only `bollard-interposer-board.kicad_pcb` and `.kicad_pro`, not the schematic. Every footprint's reference, value and footprint name on the branch PCB equals origin/main (20 footprints).
- https://github.com/airgarage/tripwire-ecad/pull/28, "[HW-975] compute stack bollard interface", branch `monti/hw-975-compute-stack-bollard-interface-1`, open, updated 2026-10-27T21:40Z. Adds a new project `compute-stack-bollard-interface` (schematic, PCB, project; commits 792c0cd, 88d20a6). No BOM extracted yet; not in Aligni or Notion.

## Interposer: KiCad vs Notion "X4A Sensor Interposer PCB"

By designator, ECAD origin/main (`data/ecad/bollard-interposer-board.csv`) against Notion (`data/notion/x4a-sensor-interposer-pcb.csv`, ref-des in Notes):

| Ref | KiCad main and PR #27 | Notion X4A |
|---|---|---|
| R1 | 2.0k RC0603FR-072KL | 6.8k RC0603FR-076K8L |
| R3 | 2.0k RC0603FR-072KL | 1M RC0603FR-071ML |
| R6 | not present | 10k RC0603FR-0710KL |
| D2 | SMAJ15A | SMAJ28A |
| C1 | value "C", no MPN | 10nF 1206 1kV CC1206KKX7RCBB103 |
| C3 | CL31B106KBHNNNE | C3216X7R1H106K160AC (both 10uF 1206) |
| C4 | CL10B103KB8NNNC (X7R) | GRM1885C1H103JA01D (C0G) |

C2, C5, D1, J2, J3, J4, R4, R5, U1, U2 agree. `git grep` for SMAJ28A, RC0603FR-076K8L and RC0603FR-071ML across all 14 remote branches of `tripwire-ecad`, and `git log --all -S SMAJ28A`, find nothing: Notion's X4A values are not committed anywhere.
