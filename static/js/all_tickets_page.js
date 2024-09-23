const showPopupRes = data => {
  const createPopup = status => {
    const popup = document.createElement('div');
    popup.className = 'fixed top-4 right-4 p-4 rounded-lg shadow-lg';
    
    if (status === 200) {
      popup.classList.add('bg-green-500', 'text-white');
      popup.textContent = 'Feito!';
    } else {
      popup.classList.add('bg-red-500', 'text-white');
      popup.textContent = 'Erro!';
    }
  
    return popup
  }

  const popup = createPopup(data.status)

  document.body.appendChild(popup);

  setTimeout(() => { popup.remove(); }, 3000);
}

const editTicket = async (tickerSymbol, newQuantity) => {
  try {
    const res = await fetch(`/tickets/all/${tickerSymbol}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ number_of_tickets: newQuantity }),
    });

    if (!res.ok) {
      throw new Error(`HTTP error! status: ${res.status}`);
    }

    const data = await res.json();

    showPopupRes(data);

    if (data.status === 200) location.reload();

  } catch (error) {
    console.error('Erro edit:', error);
  }
}

const deleteTicket = async (tickerSymbol) => {
  try {
    const res = await fetch(`/tickets/all/${tickerSymbol}`, { method: 'DELETE' });

    if (!res.ok) {
      throw new Error(`HTTP error! status: ${res.status}`);
    }

    const data = await res.json();
    
    showPopupRes(data);

    if (data.status === 200) {
      setTimeout(() => { location.reload(); }, 3000);
    }
    
  } catch (error) {
    console.error('Erro delete:', error);
    showPopupRes({ status: 500 });
  }
}

// Listeners
document.addEventListener('DOMContentLoaded', () => {
  const tickets = document.querySelectorAll('.ticket-item');

  tickets.forEach(ticket => {
    const openButton = ticket.querySelector('[data-js="open-actions"]');
    const popup = ticket.querySelector('[data-js="actions-popup"]');
    const editButton = ticket.querySelector('[data-js="edit-ticket"]');
    const deleteButton = ticket.querySelector('[data-js="delete-ticket"]');

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

    editButton.addEventListener('click', () => {
      const tickerSymbol = ticket.querySelector('.font-semibold').textContent;
      const currentQuantity = ticket.querySelector('.w-1\\/4:nth-child(3) span').textContent;
      const newQuantity = prompt('Digite a nova quantidade de tickets:', currentQuantity);

      if (newQuantity !== null && newQuantity !== currentQuantity) {
        editTicket(tickerSymbol, newQuantity);
      }
    });

    deleteButton.addEventListener('click', () => {
      const tickerSymbol = ticket.querySelector('.font-semibold').textContent;
      const ticketName = ticket.querySelector('.text-sm.text-gray-600').textContent;
      
      if (confirm(`Tem certeza que deseja deletar o ticket ${ticketName}?`)) {
        deleteTicket(tickerSymbol);
      }
    });
  });
});
