/*
[ ] Acionar os routers(fecth) quando for clicado para editar ou deletar
*/

const ticketForm = document.querySelector('[data-js="ticket-form"]');
const ticketFields = document.querySelector('[data-js="ticket-fields"]');
const addTicketButton = document.querySelector('[data-js="add-ticket"]');

let ticketCount = 1;

const updateTicketLabels = () => {
  const ticketGroups = ticketFields.querySelectorAll('.ticket-group');
  ticketGroups.forEach((group, index) => {
    group.querySelector('h3').innerText = `Ticket ${index + 1}`;
  });
  ticketCount = ticketGroups.length;
}

const addRemoveBtn = event => {
  const ticketGroup = event.target.closest('.ticket-group');
  ticketGroup.remove();
  updateTicketLabels();
}

const addTicket = () => {
  ticketCount++;

  const newGroup = document.createElement('div');
  newGroup.className = 'ticket-group mb-4 border border-gray-300 p-4 rounded-md';

  newGroup.innerHTML = `
    <div class="flex justify-between">
      <h3 class="font-extrabold text-gray-700">Ticket ${ticketCount}</h3>
      <button type="button" class="removeTicket bg-inherit text-red-500 font-semibold py-1 px-3 rounded">
        Remover
      </button>
    </div>
    <div class="flex flex-col md:flex-row md:space-x-4">
      <div class="mt-2 w-full">
        <label class="block text-sm font-medium text-gray-700">Nome do Ticket</label>
        <input type="text" name="ticketName" required class="mt-1 block w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring focus:ring-green-500" placeholder="Ex: Concerto">
      </div>
      <div class="mt-2 w-full">
        <label class="block text-sm font-medium text-gray-700">Quantidade</label>
        <input type="number" name="quantity" required class="mt-1 block w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring focus:ring-green-500" placeholder="Ex: 2">
      </div>
      <div class="mt-2 w-full">
        <label class="block text-sm font-medium text-gray-700">Valor Pago</label>
        <input type="text" name="value" required class="mt-1 block w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring focus:ring-green-500" placeholder="Ex: R$ 100,00">
      </div>
    </div>
  `;

  ticketFields.appendChild(newGroup);
  newGroup.querySelector('.removeTicket').addEventListener('click', addRemoveBtn);
}

addTicketButton.addEventListener('click', addTicket);

// Form
ticketForm.addEventListener('submit', event => {
  event.preventDefault();
  // Lógica para lidar com o envio do formulário
});
