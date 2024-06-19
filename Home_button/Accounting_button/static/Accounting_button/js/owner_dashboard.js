function toggleEditMode(constantId) {
  var checkbox = document.getElementById('edit_mode_' + constantId);
  var valueField = document.querySelector('input[name="value"]');
  var commentField = document.querySelector('textarea[name="comment"]');

  if (checkbox.checked) {
      valueField.removeAttribute('readonly');
      commentField.removeAttribute('readonly');
  } else {
      valueField.setAttribute('readonly', 'readonly');
      commentField.setAttribute('readonly', 'readonly');
  }
}
