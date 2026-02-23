# My research trajectory

My work spans systems neuroscience and mechanistic interpretability. Unified by an interest in how structured representations emerge in complex systems, I've worked on a range of research projects from analyzing spatial and contextual encoding in hippocampal circuits in the brain to probing feature superposition and training dynamics in neural networks.

## [Applying SAEs to biological neurons](https://openreview.net/pdf?id=cPpMl7Y2y3)

NeurIPS 2025 – Data on the Brain & Mind Workshop

We introduced NLDisco, a sparse autoencoder-based pipeline to uncover interpretable latent structure in high-dimensional neural recordings. This approach encourages latent units to align with meaningful features in the data, making it easier to link neural activity to behavior or experimental variables. Across synthetic and real datasets, NLDisco recovers clearer, more interpretable latent features than many traditional embedding methods.

## [Compressed computation is not computation in superposition](https://openreview.net/pdf?id=iVeOIeHDP1)

NeurIPS 2025 - Mechanistic Interpretability Workshop

When we benchmark models, performance alone doesn’t guarantee we understand how they compute. We need mechanistic clarity so that interpretations reflect real internal structure, not artifacts. We analyzed a benchmark toy model of Compressed Computation previously thought to implement many functions via superposition, decomposing its training objective into computation and noise-induced mixing components. The model’s apparent advantage comes from a noise-driven mixing effect, not true superposition; when the mixing term is removed, performance drops and a simple baseline based on the mixing term reproduces the behavior.

## Place Cells Distinguish Visually Identical Rooms

During my PhD, I studied how hippocampal “place cells” (GPS neurons) represent space in a virtual environment composed of four rooms arranged A–B–B–C, where the two middle rooms were visually identical but located in different positions in the environment.

The central question was whether neurons encode only local visual information, or whether they also incorporate broader spatial context.

Using spatial correlation analyses and a Bayesian neural decoder, I found that while some neurons showed identical activity patterns in the two visually identical rooms, a substantial subset distinguished between them. These neurons were selectively active in only one of the two rooms, or shifted their active location across rooms, indicating sensitivity to global position rather than just visual input.

These results show that hippocampal spatial representations integrate both local sensory cues and broader environmental context.

![](assets/track_spikes.gif)
*Illustrative example of spiking activity in the A–B–B–C virtual track. Each row shows spikes from one example neuron as the mouse moves along the track. While some cells fire similarly in both visually identical B rooms, others differentiate between them, reflecting sensitivity to global position rather than purely local cues.*

## Biological neurons that "count" rooms

In the same multi-room virtual task, I identified neurons that were active at corresponding positions across all four rooms, despite differences in room identity. Rather than encoding the uniqueness of each room, these cells appeared to track structural regularities across repeated segments of the environment.

Interestingly, many of these neurons fired in similar positions across rooms but with different activity levels, suggesting that they simultaneously encoded local spatial features and global task structure.

This pattern resembles previously reported “lap-counting” cells in sequential navigation tasks, and supports the idea that hippocampal representations can reflect abstract environmental structure not just physical location.

## Attention modulates spatial representations

While analyzing place cell recordings, I encountered sessions in which spatial tuning appeared unusually unstable — contradicting decades of robust findings in rodent navigation research.

Further behavioral analysis revealed a key difference: in these sessions, mice were disengaged from the task. They ran more slowly and failed to lick in the reward zone, indicating reduced motivation. Unlike real-world navigation tasks, virtual environments allow animals to disengage without physical consequences (e.g., hitting walls), introducing a new source of variability.

I developed a machine learning classifier that used early-session behavioral features to predict disengagement, allowing us to detect low-quality sessions in real time and avoid collecting unusable data.

This work highlights how cognitive state — particularly attention and engagement — shapes the stability of neural representations, and introduced a practical solution for improving data quality in VR-based experiments.


[← Back to home](/)
