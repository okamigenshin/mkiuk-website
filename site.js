const menuToggle = document.querySelector('.menu-toggle');
menuToggle?.addEventListener('click', () => {
  const open = menuToggle.getAttribute('aria-expanded') !== 'true';
  menuToggle.setAttribute('aria-expanded', String(open));
  menuToggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  document.querySelectorAll('.nav-group').forEach(navGroup => navGroup.classList.toggle('open', open));
});

// Prepare a draft locally; the visitor reviews and sends it in their email app.
const enquiryBrief = document.querySelector('#enquiry-brief');
if (enquiryBrief) {
  const emailLink = document.querySelector('#enquiry-email');
  const preview = document.querySelector('#enquiry-preview');
  const result = document.querySelector('#enquiry-result');
  const status = document.querySelector('#enquiry-status');
  enquiryBrief.hidden = false;

  const prepareEmail = () => {
    if (!enquiryBrief.reportValidity()) return;
    const service = enquiryBrief.elements.namedItem('service').value;
    const postcode = enquiryBrief.elements.namedItem('postcode').value.trim();
    const project = enquiryBrief.elements.namedItem('project').value.trim();
    if (!project) {
      enquiryBrief.elements.namedItem('project').setCustomValidity('Please tell us a little about your project.');
      enquiryBrief.reportValidity();
      return;
    }
    const body = ['Hello Martin Kaye Interiors,', '', `I would like to discuss ${service.toLowerCase()}.`,
      postcode ? `Project postcode: ${postcode}` : 'Project postcode: not supplied', '',
      'About my windows:', project, '', 'Please let me know the next steps.'].join('\n');
    emailLink.href = `mailto:info@mkiuk.com?subject=${encodeURIComponent(`${service} enquiry`)}&body=${encodeURIComponent(body)}`;
    preview.textContent = body;
    result.hidden = false;
    status.textContent = 'Your draft is ready. Open your email app to review and send it.';
    emailLink.focus();
  };
  enquiryBrief.addEventListener('submit', event => {
    event.preventDefault();
    prepareEmail();
  });
  document.querySelector('#prepare-enquiry').addEventListener('click', prepareEmail);
  enquiryBrief.addEventListener('input', () => {
    enquiryBrief.elements.namedItem('project').setCustomValidity('');
    result.hidden = true;
    emailLink.removeAttribute('href');
    status.textContent = '';
  });
}
