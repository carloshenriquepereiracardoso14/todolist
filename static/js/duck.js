  // Verifica se há uma mensagem na query string
  const urlParams = new URLSearchParams(window.location.search);
  const mensagem = urlParams.get("mensagem");

  if (mensagem) {
      alert(mensagem);
      // Remove a mensagem da URL sem recarregar
      window.history.replaceState(null, null, window.location.pathname);
  }

let botao = document.querySelector(".btn-menu")
let menu = document.querySelector(".menu")

botao.addEventListener('click', () => {
  menu.classList.toggle('ativo')
})