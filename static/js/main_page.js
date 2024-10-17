const contentFrame = document.querySelector('[data-js="content-frame"]');
const navLinks = document.querySelectorAll('[data-js="link-pages"]');

const handleNavigation = async (url) => {
    try {
        const response = await fetch(url);

        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        
        const html = await response.text();
        // const cleanHTML = DOMPurify.sanitize(html);
        // contentFrame.srcdoc = cleanHTML;
        contentFrame.srcdoc = html;
    
    } catch (error) {
        console.error(error);
    }
};

const addListenersInLinks = (link) => {
    link.addEventListener('click', (event) => {
        event.preventDefault();

        const url = event.target.getAttribute('href');
        
        handleNavigation(url);
    });
}
  

navLinks.forEach(addListenersInLinks);

handleNavigation('/tickets/all')