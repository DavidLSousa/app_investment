// Função para criar o elemento de popup com base no tipo (edição ou exclusão)
const createPopupElement = (type, message, currentValue = '') => {
  const isDelete = type === 'delete';
  const popupHTML = `
    <div class="bg-white p-6 rounded-lg shadow-xl max-w-sm w-full ${isDelete ? 'border-2 border-red-500' : ''}">
      <h3 class="text-lg font-bold mb-4 ${isDelete ? 'text-red-500' : ''}">${isDelete ? 'Confirmar Exclusão' : 'Editar Quantidade'}</h3>
      <p class="mb-4">${message}</p>
      ${type === 'edit' ? `<input type="number" class="w-full border rounded px-2 py-1 mb-4" value="${currentValue}">` : ''}
      <div class="flex justify-end space-x-2">
        <button class="cancel px-4 py-2 bg-gray-300 text-gray-800 rounded hover:bg-gray-400">Cancelar</button>
        <button class="confirm px-4 py-2 text-white rounded ${isDelete ? 'bg-red-500 hover:bg-red-600' : 'bg-blue-500 hover:bg-blue-600'}">${isDelete ? 'Excluir' : 'Salvar'}</button>
      </div>
    </div>
  `;

  const wrapper = document.createElement('div');
  wrapper.className = 'fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50';
  wrapper.innerHTML = popupHTML;
  return wrapper;
};

// Função para criar e gerenciar o popup
const createPopup = (type, message, currentValue = '') => {
  return new Promise((resolve) => {
    const popup = createPopupElement(type, message, currentValue);
    document.body.appendChild(popup);

    const closePopup = () => {
      document.body.removeChild(popup);
      resolve(null);
    };

    // Fecha o popup ao clicar fora dele
    popup.querySelector('.cancel').addEventListener('click', closePopup);
    popup.addEventListener('click', (e) => {
      if (e.target === popup) closePopup();
    });

    // Confirmação do popup
    popup.querySelector('.confirm').addEventListener('click', () => {
      const input = popup.querySelector('input');
      const result = type === 'edit' ? input?.value : true;
      resolve({ 
        result, 
        updatePopup: (message, success = true) => {
          const isEdit = type === 'edit'; // Verifica se a operação é de edição

          // Atualiza a mensagem e o estilo do popup após uma ação
          popup.innerHTML = `
            <div class="bg-${isEdit && success ? 'green-500' : !isEdit && success ? 'red-500' : 'red-500'} p-6 rounded-lg shadow-xl max-w-sm w-full flex items-center justify-center" style="min-height: 150px;">
              <p class="text-white text-xl font-bold">${message}</p>
            </div>
          `;

          // Mantém o tamanho e estilo do popup centralizado
          popup.className = 'fixed inset-0 flex items-center justify-center z-50';

          setTimeout(() => {
            closePopup();
            if (success) location.reload();
          }, 2000); // Tempo de exibição reduzido para 2 segundos
        }
      });
    });
  });
};

// Função para lidar com requisições da API
const handleApiRequest = async (apiCall, successMessage, errorMessage) => {
  try {
    const result = await apiCall();
    if (result.success) {
      return { success: true, message: successMessage };
    } else {
      throw new Error(result.error || errorMessage);
    }
  } catch (error) {
    console.error(errorMessage, error);
    return { success: false, message: `${errorMessage}.` };
  }
};

// Função para editar ticket
const editTicket = async (tickerSymbol, newQuantity) => {
  const response = await fetch(`/tickets/all/${tickerSymbol}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ number_of_tickets: newQuantity }),
  });

  if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
  const data = await response.json();
  return { success: true, data };
};

// Função para deletar ticket
const deleteTicket = async (tickerSymbol) => {
  const response = await fetch(`/tickets/all/${tickerSymbol}`, { method: 'DELETE' });
  if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
  const data = await response.json();
  return { success: true, data };
};

// Inicializa os listeners dos botões após carregar o DOM
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

    document.addEventListener('click', () => popup.classList.add('hidden'));
    popup.addEventListener('click', (e) => e.stopPropagation());

    editButton.addEventListener('click', async () => {
      const tickerSymbol = ticket.querySelector('[data-js="ticker"]').textContent;
      const currentQuantity = ticket.querySelector('[data-js="number_of_tickets"]').textContent;
      
      const response = await createPopup('edit', 'Digite a nova quantidade de tickets:', currentQuantity);
      
      if (response && response.result !== null && response.result !== currentQuantity) {
        const { success, message } = await handleApiRequest(
          () => editTicket(tickerSymbol, response.result),
          'Editado!',
          'Erro ao editar o ticket'
        );
        response.updatePopup(message, success);
      }
    });

    deleteButton.addEventListener('click', async () => {
      const tickerSymbol = ticket.querySelector('[data-js="ticker"]').textContent;
      const ticketName = ticket.querySelector('[data-js="ticket-name"]').textContent;
      
      const response = await createPopup('delete', `Tem certeza que deseja deletar o ticket ${ticketName}?`);
      
      if (response && response.result) {
        const { success, message } = await handleApiRequest(
          () => deleteTicket(tickerSymbol),
          'Excluído!',
          'Erro ao excluir o ticket'
        );
        response.updatePopup(message, success);
      }
    });
  });
});
