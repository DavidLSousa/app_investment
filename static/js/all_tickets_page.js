const createPopupElement = (TicketName, currentValue = '') => {
    const popupHTML = `
        <div class="bg-white p-6 rounded-lg shadow-xl max-w-sm w-full">
            <h3 class="text-lg font-bold mb-4">Vender Ações da ${TicketName}</h3>
            <form id="saleForm">
                <input type="number" name="soldQuantity" class="w-full border rounded px-2 py-1 mb-4" placeholder="Número de ações vendidas" min="1" max="${currentValue}" required>
                <input type="number" name="totalSaleValue" class="w-full border rounded px-2 py-1 mb-4" placeholder="Valor total da venda" min="0.01" step="0.01" required>
                <div class="flex justify-between space-x-2 w-full">
                    <button type="button" class="cancel flex-1 px-4 py-2 bg-gray-300 text-gray-800 rounded hover:bg-gray-400">Cancelar</button>
                    <button type="submit" class="confirm flex-1 px-4 py-2 text-white rounded bg-blue-500 hover:bg-blue-600">Vender</button>
                </div>
            </form>
        </div>
    `;

    const wrapper = document.createElement('div');
    wrapper.className = 'fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50';
    wrapper.innerHTML = popupHTML;
    return wrapper;
};

const createPopup = (ticketName, currentValue = '') => {
    return new Promise((resolve) => {
        const popup = createPopupElement(ticketName, currentValue);
        document.body.appendChild(popup);

        const closePopup = () => {
            document.body.removeChild(popup);
            resolve(null);
        };

        popup.querySelector('.cancel').addEventListener('click', closePopup);
        popup.addEventListener('click', (e) => {
            if (e.target === popup) closePopup();
        });

        const form = popup.querySelector('#saleForm');
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const formData = new FormData(form);
            const result = {
                soldQuantity: parseInt(formData.get('soldQuantity')),
                totalSaleValue: parseFloat(formData.get('totalSaleValue'))
            };
            resolve({ 
                result, 
                updatePopup: (message, success = true) => {
                    popup.innerHTML = `
                        <div class="bg-${success ? 'green-500' : 'red-500'} p-6 rounded-lg shadow-xl max-w-sm w-full flex items-center justify-center" style="min-height: 150px;">
                            <p class="text-white text-xl font-bold text-center">${message}</p>
                        </div>
                    `;

                    popup.className = 'fixed inset-0 flex items-center justify-center z-50';

                    setTimeout(() => {
                        closePopup();
                        if (success) location.reload();
                    }, 2000);
                }
            });
        });
    });
};

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

const sellTicket = async (tickerSymbol, soldQuantity, totalSaleValue) => {
    const response = await fetch(`/tickets/all`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
            ticket: tickerSymbol,
            number_of_sale_tickets: soldQuantity, 
            total_sale_value: totalSaleValue 
        }),
    });

    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
    const data = await response.json();
    return { success: true, data };
};

document.addEventListener('DOMContentLoaded', () => {
    const tickets = document.querySelectorAll('.ticket-item');

    tickets.forEach(ticket => {
        const saleButton = ticket.querySelector('[data-js="sale-tickets"]');

        saleButton.addEventListener('click', async () => {
            const tickerSymbol = ticket.querySelector('[data-js="ticker"]').textContent;
            const currentQuantity = ticket.querySelector('[data-js="number_of_tickets"]').textContent;
            const ticketName = ticket.querySelector('[data-js="ticket-name"]').textContent;
            
            const response = await createPopup(ticketName, currentQuantity);
            
            if (response && response.result) {
                const { success, message } = await handleApiRequest(
                    () => sellTicket(tickerSymbol, response.result.soldQuantity, response.result.totalSaleValue),
                    'Venda realizada com sucesso!',
                    'Erro ao realizar a venda'
                );
                response.updatePopup(message, success);
            }
        });
    });
});
