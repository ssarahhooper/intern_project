const label = e.target.nextElementSibling;
if (checked) {
  label.textContent = 'Fully stocked';
  label.classList.remove('text-red-600');
  label.classList.add('text-green-700');
} else {
  label.textContent = 'Needs restock';
  label.classList.remove('text-green-700');
  label.classList.add('text-red-600');
}
