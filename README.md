# Cyber-Physical Risk and Resilience Analysis of National Water Infrastructure

**Analyzing how cyber intrusions and physical failures propagate across a 10-state water infrastructure network using cascade network modeling, directed flow analysis, and Model-Based Risk Assessment (MBRA), aligned with DHS NIPP and NIST SP 800-82 frameworks.**

This study models the American Water system spanning Illinois, Indiana, Kentucky, Maryland, Missouri, New Jersey, Pennsylvania, Tennessee, Virginia, and West Virginia. Two complementary network models evaluate how disruptions travel through cyber (lateral, undirected) and physical (downstream, directed) pathways, producing quantified risk rankings and investment recommendations for DHS.

---

## Key Findings

| Finding | Value |
|---|---|
| Critical infrastructure nodes | Pennsylvania, Illinois, New Jersey |
| Cascade (cyber) q-value at 20% vulnerability | 1.60 (stable) |
| Cascade (cyber) q-value at 80% vulnerability | 0.98 (near instability) |
| Cascade critical vulnerability threshold | 0.78 (resilient until 78%) |
| Flow (physical) q-value at 20% vulnerability | 0.81 (already unstable) |
| Flow (physical) q-value at 80% vulnerability | 0.75 (deeply unstable) |
| Flow critical vulnerability threshold | -1.44 (never reaches stability) |
| Risk reduction after targeted mitigation | Over 90% across both models |
| Cascade system risk (before → after controls) | 458 → 40 |
| Flow system risk (before → after controls) | 32 → 2 |
| Full threat elimination cost | $864M (exceeds available CAPEX) |
| Spectral radius (cascade network) | 2.27 |
| Node robustness | 55.95% |
| Link robustness | 0% (no redundant links) |

**Core insight:** The cyber cascade network remains resilient under stress because lateral connections distribute load across states. The physical flow network is inherently unstable at all vulnerability levels because strict downstream directionality forces every disruption to propagate without alternate routing. This asymmetry demands fundamentally different protection strategies for cyber vs physical infrastructure.

---

## Network Models

### Cascade Network (Cyber, Undirected)

Models lateral cyber and administrative connectivity: shared SCADA vendors, cloud managed operational technologies, corporate networks, and regional oversight structures. Cyber intrusions propagate nondirectionally across these pathways.

### Flow Network (Physical, Directed)

Models downstream physical water movement aligned with major river basins: Ohio, Tennessee, Mississippi, Susquehanna, Potomac, and Delaware systems. Physical contamination or supply loss travels strictly downstream with no option for rerouting.

Both models use the same 10-state adjacency matrix. The resilience differences arise entirely from how the topology is interpreted (undirected vs directed), not from changes in the underlying structure.

---

## Centrality Analysis

| State | Degree Centrality | Betweenness (Cascade) | Betweenness (Flow) | Eigenvector (Flow) |
|---|---|---|---|---|
| Pennsylvania | 0.444 | 0.306 | 0.569 | 0.439 |
| Kentucky | 0.333 | 0.639 | 0.639 | 0.296 |
| West Virginia | 0.333 | 0.556 | 0.569 | 0.371 |
| Virginia | 0.333 | 0.083 | 0.292 | 0.547 |
| New Jersey | 0.111 | 0.000 | 0.000 | 0.439 |

Pennsylvania dominates both models. Kentucky and West Virginia serve as internal cyber bridges. New Jersey gains outsized physical influence through downstream accumulation despite low direct connectivity.

---

## Attack Simulations

### Random Attacks
Cyber disruptions distribute according to lateral connectivity, concentrating at Kentucky, West Virginia, and Pennsylvania. Physical disruptions collapse into the same downstream bottlenecks regardless of where the random failure originates, because directional flow forces all consequences toward Pennsylvania and New Jersey.

### Targeted Attacks
Removing Pennsylvania fragments the physical network immediately because no bypass exists for downstream movement. In the cascade model, Kentucky and West Virginia absorb the redistributed cyber load but become structurally overloaded. The targeted removal of the highest degree node confirms that the network is cyber-resilient but physically brittle.

---

## Fault Tree Analysis

### Cyber Threats (Cascade Model: Pennsylvania + Illinois)

| Threat | Vulnerability | Elimination Cost |
|---|---|---|
| SCADA Malware | 15% | $78.6M / $83.4M |
| Ransomware | 12% | $62.9M / $66.8M |
| Phishing | 7% | $36.7M / $38.9M |
| Remote Access | 6% | $31.5M / $33.4M |
| **Total** | **40%** | **$432M** |

### Physical Threats (Flow Model: Pennsylvania + New Jersey)

| Threat | Vulnerability | Elimination Cost |
|---|---|---|
| Main Sabotage | 12% | $62.9M / $66.8M |
| Plant Contamination | 11% | $57.7M / $61.2M |
| Regional Flooding | 9% | $47.2M / $50.1M |
| Grid Outage | 8% | $41.9M / $44.5M |
| **Total** | **40%** | **$432M** |

Combined elimination cost of $864M exceeds available prevention budget, demonstrating the need for prioritized federal investment at structurally dominant nodes.

---

## MBRA Risk Reduction

| Model | Risk Before Controls | Risk After Controls | Reduction |
|---|---|---|---|
| Cascade (Cyber) | 458 | 40 | >90% |
| Flow (Physical) | 32 | 2 | >90% |

### Investment Priority Recommendation

1. **Pennsylvania** — dominates both cascade and flow networks, produces highest risk reduction when hardened
2. **Illinois** — strongest cyber conduit in cascade model
3. **New Jersey** — major downstream physical transfer point stabilizing the eastern corridor

---

## Frameworks and Alignment

| Framework | Application |
|---|---|
| DHS NIPP 2013 | Network structure, risk management approach, and critical infrastructure protection methodology |
| NIST SP 800-82 | Industrial control systems security guidance for SCADA and OT environments |
| CISA Water Sector Guidance | Cybersecurity best practices for water and wastewater systems |
| MBRA | Model-Based Risk Assessment for resilience evaluation, critical vulnerability estimation, and budget allocation |

---

## Technologies

| Tool | Purpose |
|---|---|
| Python | Network analysis, centrality calculations, spectral analysis |
| NumPy | Matrix operations and eigenvalue computation |
| NetworkX | Graph construction, centrality metrics, attack simulations |
| MBRA Software | Risk modeling, fault tree analysis, prevention budget optimization |

---

## Project Structure

```
CyberPhysical-Risk-Analysis/
├── code/           # Python scripts for network analysis and graph calculations
├── data/           # Datasets, simulation outputs, and analysis spreadsheets
├── docs/           # Research paper and supporting documentation
├── graphs/         # Network topology graphs and resilience visualizations
├── images/         # Figures and diagrams
├── mbra/           # MBRA models and resilience analysis files
└── README.md
```

---

## Data Sources

All consequence, prevention, and response cost values are grounded in publicly available data:

| Source | Data Used |
|---|---|
| American Water 2024 Annual Report | Capital expenditures ($2,856M), O&M costs ($152M), state-level investment data |
| Dunbar (Kanawha Valley) Incident | Physical consequence baseline (24.9M gallons/day), financial impact ($18M), litigation ($5M) |
| Regional River Basin Hydrology | Directional flow assignments for Ohio, Tennessee, Mississippi, Potomac, and Delaware systems |

---

## Disclaimer

This repository is intended for academic research, cybersecurity education, and critical infrastructure resilience analysis. No protected Sensitive Security Information (SSI) or facility-specific operational data is included.
