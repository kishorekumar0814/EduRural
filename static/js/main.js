document.addEventListener("DOMContentLoaded", () => {
  const links = document.querySelectorAll("nav a");
  links.forEach(link => {
    link.addEventListener("click", (e) => {
      if(!link.href.includes(window.location.host)) return;
      e.preventDefault();
      const href = link.getAttribute("href");
      document.body.style.opacity = 0;
      setTimeout(() => {
        window.location.href = href;
      }, 300);
    });
  });
});
