const localTheme = localStorage.getItem("theme");
const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");

if (localTheme === "dark" || (!localTheme && prefersDarkScheme.matches)) {
  document.documentElement.classList.add("dark");
}
