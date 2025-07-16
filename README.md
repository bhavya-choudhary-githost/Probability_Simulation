# ⭐ Genshin Impact 5★ Pull Simulator

This Python script simulates the probability of getting **5-star characters** in Genshin Impact, including banner vs standard 5★ logic, soft pity, and hard pity.

It tracks how many **banner 5★s** and **off-banner (standard) 5★s** you get over a fixed number of pulls.

---

## 💡 How It Works

The script replicates Genshin’s actual pity system:

- **Base 5★ chance**: 0.6% (0.006) per pull
- **Soft pity**: Starting at pull 74, the chance increases by 6% (0.06) per pull
- **Hard pity**: Pull 90 guarantees a 5★
- **50/50 rule**:
  - When you get a 5★, there's a 50% chance it is the featured banner unit
  - If not, the next 5★ is guaranteed to be banner

### Tracked Stats:
- `banner_5stars`: How many featured banner characters you pulled
- `standard_5stars`: How many off-banner 5★ characters you pulled

---

## 🛠️ How to Run

1. Make sure you have Python installed (v3.6 or higher).
2. Run the script in a terminal or Python IDE.

```bash
python genshin_simulator.py
