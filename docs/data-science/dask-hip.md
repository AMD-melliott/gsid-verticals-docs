# dask-hip

dask-hip extends [Dask.distributed](https://distributed.dask.org/) with one-worker-per-GPU scheduling for AMD
Instinct™ GPUs, ported from the RAPIDS® dask-cuda project. It handles automatic GPU device visibility and CPU
affinity, GPU memory spilling, and RMM pool integration, with UCX-based high-performance communication between
workers for scaling AMD Data Science workloads across multiple GPUs.

<div class="id-deck">

<div class="id-grid">

<a class="id-card" href="https://rocm.docs.amd.com/projects/dask-hip/en/latest/">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 7v14"/><path d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z"/></svg></span>
  <span class="id-card-title">Documentation</span>
  <span class="id-card-desc">Installation instructions, how-to guides, and API reference material are on the ROCm Documentation site.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="https://github.com/AMD-Ecosystem/dask-hip">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="6" x2="6" y1="3" y2="15"/><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9a9 9 0 0 1-9 9"/></svg></span>
  <span class="id-card-title">Github</span>
  <span class="id-card-desc">View the dask-hip source code on Github.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

</div>
</div>
