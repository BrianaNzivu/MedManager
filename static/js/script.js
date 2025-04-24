document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('themeToggle');
    const root = document.documentElement;
  
    const currentTheme = localStorage.getItem('theme') || 'light';
    root.setAttribute('data-bs-theme', currentTheme);
  
    themeToggle.addEventListener('click', () => {
      const newTheme = root.getAttribute('data-bs-theme') === 'light' ? 'dark' : 'light';
      root.setAttribute('data-bs-theme', newTheme);
      localStorage.setItem('theme', newTheme);
    });
  });
  