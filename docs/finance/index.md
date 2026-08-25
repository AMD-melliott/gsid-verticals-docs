# AMD Finance Toolkit

AMD Finance pulls the trajectory of tomorrow into today: an open toolkit on the [ROCm](https://rocm.docs.amd.com/) stack that
delivers GPU-native gradient-boosting stacks that the industry already trusts. XGBoost,
LightGBM, and ThunderGBM, tuned for [AMD Instinct](https://www.amd.com/en/products/accelerators/instinct.html)
accelerators, so training, scoring, and simulation work land closer to real time than the CPU-era
baselines could achieve.

AMD Finance collapses the distance between signal and decision. The same workloads that once
queued overnight now run in minutes. Risk, fraud detection, forecasting, and simulation pipelines step
into the high-bandwidth GPU computing ROCm was built to serve. AMD Finance provides production-oriented kernels, memory paths, and scaling behavior so your boosting jobs feel like
they arrived from the next generation, even on this week's cluster.

For more information on AMD Finance, including comparisons, prerequisites, installation, and deep API
reference, see the [AMD Finance documentation](https://rocm.docs.amd.com/projects/rocm-finance/en/latest/index.html).

<div class="id-deck">

<div class="id-grid">

<a class="id-card" href="xgboost.html">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/></svg></span>
  <span class="id-card-title">XGBoost</span>
  <span class="id-card-desc">General-purpose GPU gradient boosting. Start here for high-performance workloads for data-intensive applications.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="lightgbm.html">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z"/></svg></span>
  <span class="id-card-title">LightGBM</span>
  <span class="id-card-desc">Leaf-wise training. Strong fit when sparsity abounds and dataset size drives the bottleneck.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="thundergbm.html">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 3v18h18"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/></svg></span>
  <span class="id-card-title">ThunderGBM</span>
  <span class="id-card-desc">GPU-oriented boosting for highly parallel, GPU-intensive training and simulation-style runs on high-dimensional datasets.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="https://github.com/ROCm/ROCm-Finance">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="6" x2="6" y1="3" y2="15"/><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9a9 9 0 0 1-9 9"/></svg></span>
  <span class="id-card-title">GitHub</span>
  <span class="id-card-desc">Source for all AMD Finance libraries on GitHub.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="https://github.com/ROCm/rocm-finance/tree/release/26.01/examples">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="4 17 10 11 4 5"/><line x1="12" x2="20" y1="19" y2="19"/></svg></span>
  <span class="id-card-title">Examples</span>
  <span class="id-card-desc">Runnable examples on GitHub to explore the code.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="finance-blogs.html">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></span>
  <span class="id-card-title">AMD Finance Blogs</span>
  <span class="id-card-desc">Browse blogs detailing how to accelerate your finance workloads using gradient boosting on AMD Instinct GPUs.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

</div>
</div>
