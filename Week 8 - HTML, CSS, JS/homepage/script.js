// Espera todo o conteúdo do HTML ser carregado antes de executar o script.
document.addEventListener('DOMContentLoaded', function() {

    /**
     * Recurso 1: Alternador de Tema (Dark/Light Mode)
     * Este código controla a funcionalidade do checkbox para mudar o tema.
     */
    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;

    // Adiciona um "ouvinte" que reage a mudanças no checkbox
    themeToggle.addEventListener('change', function() {
        // Se o checkbox estiver marcado, adiciona a classe 'dark-theme' ao body
        // Senão, a remove.
        if (this.checked) {
            body.classList.add('dark-theme');
        } else {
            body.classList.remove('dark-theme');
        }
    });


    /**
     * Recurso 2: Destaque do Link de Navegação Ativo
     * Este código identifica a página atual e adiciona uma classe 'active' ao link correspondente.
     */
    const currentPage = window.location.pathname.split('/').pop(); // Pega o nome do arquivo atual, ex: "index.html"
    const navLinks = document.querySelectorAll('#navegacao nav ul li a');

    navLinks.forEach(link => {
        const linkPage = link.getAttribute('href').split('/').pop();
        if (linkPage === currentPage) {
            link.classList.add('active'); // Adiciona a classe ao link ativo
        }
    });


    /**
     * Recurso 3: Ano do Copyright Dinâmico
     * Este código atualiza automaticamente o ano no rodapé.
     */
    const footer = document.querySelector('footer p');
    if (footer) {
        const currentYear = new Date().getFullYear(); // Pega o ano atual
        footer.textContent = `© ${currentYear} Tema Natureza. Todos os direitos reservados`;
    }

});
