---
layout: default
title: Sara Molas Medina
---

**Computational Neuroscience * Mechanistic Interpretability * Deep Learning * Biology**

Currently based in London, UK · Email: <saramolas18@gmail.com>
[CV](assets/CV_MolasMedina.pdf) · [GitHub](https://github.com/saramolas) · [Google Scholar](https://scholar.google.com/citations?hl=ca&user=8JhisgsAAAAJ&view_op=list_works&gmla=APjjwuayMqVg0o4ixLqywd37WTufKmOKIQX4oJ8iAtIbjG07Zo0cgiCxXxcz_uvpMM-IfDPdx___iWWGx2I6lFlgySIEEJxv8PYQe4s#) · [LinkedIn](https://linkedin.com/in/saramolasmedina)

---

## One-liner
I’m a researcher focused on **mechanistic interpretability**: understanding how learned representations form and how sparse structure (e.g., SAEs) can make models more interpretable and controllable.

---

## Research snapshot
- **Sparse autoencoders / feature discovery** (structured + real data)
- **Training dynamics & SLT / LLC** (developmental interpretability: trajectories, not just endpoints)
- **Compositional generalization** (e.g., conditional diffusion / representation structure)
- Background: **computational neuroscience** (representation learning in biological systems)

---

## Selected work (3 highlights)

### 1) Developmental interpretability via Singular Learning Theory (SLT)
**TL;DR:** [1 sentence: what you found / what you’re testing / why it matters.]

<details>
<summary><strong>What I did</strong> (methods & engineering)</summary>

- Implemented **LLC estimation** pipeline using **SGLD** (multi-seed, reproducible runs)
- Designed training/eval protocol to track representation change over time
- Ran experiments on [model family], varying [key variables]
- Built analysis notebooks for: learning curves, LLC curves, ablations, failure cases

</details>

<details>
<summary><strong>Key results</strong> (include plots)</summary>

- **Finding 1:** [concrete statement]
- **Finding 2:** [concrete statement]
- **Interpretation:** [1–2 sentences]

**Plots:**  
![LLC during training](assets/llc_curve.png)  
![Generalization vs LLC](assets/gen_vs_llc.png)

</details>

<details>
<summary><strong>Open questions / next experiments</strong></summary>

- Does LLC change reliably under compositional generalization settings?
- Can developmental signals predict *when* features emerge (phase-transition-like behavior)?
- What’s the right “unit of analysis” (weights vs features vs circuits) for SLT-style signals?

</details>

---

### 2) Sparse Autoencoders on synthetic place-cell representations (NeurIPS workshop)
**TL;DR:** SAEs recover interpretable latent structure (global + local position variables) from synthetic neural codes.

<details>
<summary><strong>What I did</strong></summary>

- Generated synthetic place-cell-like datasets with controlled ground truth
- Trained SAEs; evaluated feature sparsity, reconstruction, and latent recovery
- Analyzed **global vs local encoding** and feature geometry

</details>

<details>
<summary><strong>Results</strong></summary>

- **Recovered latent position variables** aligned with ground truth structure  
- Identified feature sets corresponding to [global / local] components

**Paper:** [link] · **Code:** [link]  
**Figure:**  
![SAE features](assets/sae_features.png)

</details>

---

### 3) Mechanistic analysis of feature computation in small networks (superposition / ablations)
**TL;DR:** In small models, features can be computed in overlapping subspaces; targeted ablations reveal which weights carry which computations.

<details>
<summary><strong>What I did</strong></summary>

- Designed controlled toy task / model
- Ran ablations across layers/weights; measured performance + feature metrics
- Visualized learned weights and feature interference patterns

</details>

<details>
<summary><strong>Takeaways</strong></summary>

- [one concrete takeaway]
- [one concrete takeaway]

</details>

---

## Research direction (why Goodfire / what I want to push)
I’m excited about interpretability work that moves beyond static snapshots to **developmental interpretability**: how features form, stabilize, and interact during training.

In particular, I’m interested in:
- Connecting **feature learning** (SAEs, superposition, circuit structure) with **training-time signals** (SLT/LLC, phase transitions)
- Building mechanistic tools that scale to real models and give actionable interventions
- Bridging insights from **biological representation learning** and artificial systems

<details>
<summary><strong>Concrete questions I’m currently thinking about</strong></summary>

- Which training-time metrics reliably forecast feature emergence and generalization?
- When do sparse features become “modular” vs entangled—and can we encourage modularity?
- How should we evaluate interpretability methods on tasks requiring compositional structure?

</details>

---

## A bit more about me
PhD in **Systems & Computational Neuroscience**. Currently [role], previously [key research experiences]. I like projects with a tight loop: hypothesis → experiment → insight → iteration.

<details>
<summary><strong>Technical stack</strong></summary>

- **ML:** PyTorch, diffusion models, representation learning, SAEs
- **Interpretability:** feature analysis, probes, ablations, visualization
- **Research tooling:** experiment tracking, multi-seed runs, reproducibility, GPU workflows
- **Math:** statistics/probability, optimization, linear algebra, (SLT basics)

</details>

---

## Contact
Email: <youremail@domain.com>  
If helpful, I’m happy to share a short write-up of any project or walk through results live.
