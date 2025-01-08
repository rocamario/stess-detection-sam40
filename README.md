# EEG-Based Stress Detection with Visibility Graph Analysis

This repository contains code and resources for the research project:  
**EEG-Based Stress Detection: Identifying Interpretable Features with Visibility Graph Analysis.**

## Overview

The project explores stress detection using EEG signals and focuses on extracting interpretable features. The dataset used is **SAM40**, publicly available [here](https://doi.org/10.1016/j.dib.2021.107772).

### Key Objectives
- Identify interpretable features for stress discrimination.
- Investigate the utility of Visibility Graph features for EEG analysis.
- Validate findings against existing literature.

### Repository Structure
The project code is organized into four Jupyter Notebooks:
1. **Preprocessing**: Data cleaning, artifact removal (ICA), and filtering.
2. **Feature Extraction**: Computation of Visibility Graph, temporal, and frequency-based features.
3. **Feature Selection**: Identification of key features using ANOVA,  redundancy reduction and RFE.
4. **Modeling**: Training and evaluating stress detection models.

### Contact
For questions or contributions, contact **Mario Roca**: mario.roca@etu-upsaclay.fr
