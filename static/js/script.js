document.addEventListener('DOMContentLoaded', () => {
  // Light/Dark Mode Switch
  const themeSwitch = document.getElementById('themeSwitch');
  const root = document.documentElement;
  const saved = localStorage.getItem('theme') || 'light';
  root.setAttribute('data-bs-theme', saved);
  themeSwitch.checked = (saved === 'dark');
  themeSwitch.addEventListener('change', () => {
    const mode = themeSwitch.checked ? 'dark' : 'light';
    root.setAttribute('data-bs-theme', mode);
    localStorage.setItem('theme', mode);
  });

  // Client Search Filter
  const searchInput = document.getElementById('clientSearch');
  if (searchInput) {
    searchInput.addEventListener('keyup', () => {
      const filter = searchInput.value.toLowerCase();
      document.querySelectorAll('#clientsTable tbody tr').forEach(row => {
        row.style.display = row.textContent.toLowerCase().includes(filter)
                          ? '' : 'none';
      });
    });
  }

  // Bar & Pie Charts
  const barCtx = document.getElementById('programChart');
  if (barCtx) {
    const labels = JSON.parse(barCtx.dataset.labels);
    const data   = JSON.parse(barCtx.dataset.counts);
    const colors = JSON.parse(barCtx.dataset.colors);
    new Chart(barCtx, {
      type: 'bar',
      data: { labels, datasets: [{ label:'Clients per Program', data, backgroundColor:colors }] },
      options: { scales: { y:{ beginAtZero:true } } }
    });
  }

  const pieCtx = document.getElementById('programPie');
  if (pieCtx) {
    const labels = JSON.parse(pieCtx.dataset.labels);
    const data   = JSON.parse(pieCtx.dataset.counts);
    const colors = JSON.parse(pieCtx.dataset.colors);
    new Chart(pieCtx, {
      type: 'pie',
      data: { labels, datasets: [{ data, backgroundColor:colors }] }
    });
  }

  document.querySelectorAll('.program-badge').forEach(el => {
    const c = el.getAttribute('data-color');
    if (c) el.style.backgroundColor = c;
  });
  
});
