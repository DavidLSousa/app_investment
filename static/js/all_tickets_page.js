document.addEventListener('DOMContentLoaded', () => {
  const tickets = document.querySelectorAll('.ticket-item');

  tickets.forEach(ticket => {
    const openButton = ticket.querySelector('[data-js="open-actions"]');
    const popup = ticket.querySelector('[data-js="actions-popup"]');

    openButton.addEventListener('click', (e) => {
      e.stopPropagation();
      popup.classList.toggle('hidden');
    });

    // Fechar o popup quando clicar fora dele
    document.addEventListener('click', () => {
      popup.classList.add('hidden');
    });

    popup.addEventListener('click', (e) => {
      e.stopPropagation();
    });
  });
});

/*
[ ] Implementar Buttons de deleção e edição
*/ 