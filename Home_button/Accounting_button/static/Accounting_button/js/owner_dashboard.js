function toggleEditMode(constantId) {
  var checkbox = document.getElementById('edit_mode_' + constantId);
  var valueField = document.getElementById('value_' + constantId);
  var commentField = document.getElementById('comment_' + constantId);

  if (checkbox.checked) {
      valueField.removeAttribute('readonly');
      commentField.removeAttribute('readonly');
  } else {
      valueField.setAttribute('readonly', 'readonly');
      commentField.setAttribute('readonly', 'readonly');
  }
}
